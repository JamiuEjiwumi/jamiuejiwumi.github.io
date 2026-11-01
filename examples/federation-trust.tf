# Reference only. Adapt issuer, subject, audience and permissions after validating actual claims.
variable "oidc_provider_arn" { type = string }
variable "oidc_provider_host" { type = string }
variable "expected_audience" { type = string }
variable "approved_subject" { type = string }

data "aws_iam_policy_document" "assume_from_azure" {
  statement {
    sid     = "ApprovedAzureWorkloadOnly"
    effect  = "Allow"
    actions = ["sts:AssumeRoleWithWebIdentity"]
    principals {
      type        = "Federated"
      identifiers = [var.oidc_provider_arn]
    }
    condition {
      test     = "StringEquals"
      variable = "${var.oidc_provider_host}:aud"
      values   = [var.expected_audience]
    }
    condition {
      test     = "StringEquals"
      variable = "${var.oidc_provider_host}:sub"
      values   = [var.approved_subject]
    }
  }
}
# Resource permissions intentionally omitted; restrict execute-api:Invoke to exact API/stage/method/path.
