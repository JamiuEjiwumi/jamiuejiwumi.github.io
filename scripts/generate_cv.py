from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from pathlib import Path
p=Path("assets/Jamiu_Ejiwumi_Senior_DevOps_CV.pdf")
p.parent.mkdir(parents=True,exist_ok=True)
c=canvas.Canvas(str(p),pagesize=A4)
c.setTitle("Jamiu Ejiwumi | Senior DevOps & Platform Engineer")
w,h=A4
x,y=44,h-49
def line(s,size=9,bold=False,space=14,color="#27374B"):
    global y
    c.setFillColor(HexColor(color))
    c.setFont("Helvetica-Bold" if bold else "Helvetica",size)
    c.drawString(x,y,s)
    y-=space
def heading(s):
    global y
    y-=8
    line(s,10,True,18,"#0B7667")
line("JAMIU EJIWUMI",20,True,27,"#12283A")
line("Senior DevOps & Platform Engineer | AWS | Azure | Terraform | Kubernetes",10,False,16)
line("Coventry, UK | jamiu.ejiwumi@gmail.com | linkedin.com/in/jamiuejiwumi",8,False,13)
line("github.com/JamiuEjiwumi | jamiuejiwumi.github.io",8,False,18)
heading("PROFESSIONAL PROFILE")
for s in ["Senior DevOps and Platform Engineer with 8+ years of cloud and software-delivery experience.","Builds reusable infrastructure, secure CI/CD and reliable production operations across AWS and Azure.","Recognised by engineering leadership for delivery ownership and accelerating stalled initiatives."]:line(s)
heading("EXPERIENCE")
line("iamproperty | DevOps / Senior DevOps Engineer | Jun 2026 - Present",10,True,16)
for s in ["- Modernised AWS and Azure deployment processes with reusable Terraform and CI/CD workflows.","- Advanced CRM application and database deployment automation and ephemeral environments.","- Delivered secure AI-powered CRM integration using Entra ID, AWS STS, Lambda and API Gateway.","- Established immutable container releases, GitHub OIDC and controlled release/rollback patterns.","- Manager review: significantly exceeded first-three-month expectations."]:line(s,8.6,False,13)
line("Agriculture and Horticulture Development Board | Senior DevOps Engineer | Jul 2024 - Jun 2026",9.5,True,16)
for s in ["- Standardised Azure DevOps pipelines; reported a 50% reduction in release cycle time.","- Engineered Azure infrastructure, AKS deployments, Terraform modules and DevSecOps scanning."]:line(s,8.6,False,13)
line("Polaris Bank | Lead DevOps Engineer | Apr 2023 - Jan 2025",9.5,True,16)
for s in ["- Led AKS, CI/CD, Terraform, monitoring and secure deployments for banking workloads.","- Mentored engineers and strengthened delivery quality gates."]:line(s,8.6,False,13)
line("ParallelScore | Senior DevOps Engineer | Apr 2022 - May 2023",9.5,True,16)
line("- AWS EKS migration, GitHub Actions, Terraform and Prometheus/Grafana observability.",8.6,False,13)
line("E-Settlement | Senior DevOps Engineer | Jan - May 2022",9.5,True,16)
line("- Kubernetes, DigitalOcean, Terraform and Bitbucket Pipelines.",8.6,False,13)
line("Terragon Group | DevOps Engineer | Jan 2021 - Jan 2022",9.5,True,16)
line("- AWS/Azure infrastructure, Jenkins, Rancher and Kubernetes.",8.6,False,13)
heading("SELECTED ENGINEERING WORK")
for s in ["AWS platform delivery templates; Pack Manager immutable releases; CRM deployment modernisation;","Azure-to-AWS identity federation; AI CRM connector; Azure Virtual WAN automation."]:line(s,8.6,False,13)
heading("EDUCATION AND CREDENTIALS")
for s in ["MSc Digital Transformation | Nexford University | Awarded October 2026","Bachelor's degree | Federal University of Technology, Minna | 2010-2015","Microsoft Certified: DevOps Engineer Expert (AZ-400) | January 2026","Microsoft Certified: Azure Administrator Associate (AZ-104) | December 2025"]:line(s,8.7,False,14)
heading("TECHNOLOGY")
line("AWS, Azure, AKS, EKS, Kubernetes, Docker, Terraform, GitHub Actions, Azure DevOps,",8.6,False,13)
line("PowerShell, Python, IAM/OIDC, SQL deployment governance, Linux, Windows/IIS, observability.",8.6,False,13)
line("Career periods may overlap; exact engagements and credential validity available on request.",7.5,False,12,"#56677A")
c.save()
print(p)
