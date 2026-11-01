# Platform delivery reference patterns

These are original, deliberately non-deployable reference examples for public demonstration. They are **not** employer implementations and must not be applied without adapting trust policies, role scopes, verification, and deployment controls.

## Immutable promotion

The workflow sketch in `immutable-promotion.yml` separates building an immutable image from promoting its digest. It intentionally omits production credentials and infrastructure wiring. Real consumers should use pinned actions, OIDC, environment approvals, tests, rollout checks and verified rollback.

## Cross-cloud federation

`federation-trust.tf` demonstrates an exact OIDC provider, audience and subject claim trust boundary. Actual implementation must validate the Azure managed-identity token issuer, audience and subject formats, configure the AWS identity provider and IAM execution permissions and use request signing. Do not copy placeholder values into live infrastructure.

## Validation

Review `terraform fmt`, `terraform validate` with proper providers, `actionlint`, IAM policy simulation, access-token expiry and negative authorisation tests. All secret material stays outside repository history.
