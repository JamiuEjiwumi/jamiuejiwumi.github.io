# Jamiu Ejiwumi — Engineering Portfolio

A dependency-light, responsive, accessible static portfolio with seven sanitised engineering case studies, a full experience timeline, verified professional credentials and a Codex engineering workflow page.

## Publishing

1. Create a **public** repository named `jamiu-portfolio` in personal GitHub account `JamiuEjiwumi`.
2. Upload **all files**, including `.github/workflows/pages.yml`, to `main`.
3. Go to **Settings → Pages → Build and deployment → Source: GitHub Actions**.
4. Push to `main` to run the workflow. Your site will be served at `https://jamiuejiwumi.github.io/jamiu-portfolio/` once GitHub Pages is configured and deployment succeeds.

## Editing

- `index.html`: homepage and featured projects.
- `work.html`: seven sanitised case studies.
- `experience.html`: role history, education and credentials.
- `method.html`: Codex-assisted engineering and verification process.
- `profile.html`: compact print-to-PDF profile (not a full ATS CV).
- `styles.css`: design system and responsive behaviour.

## Accuracy and privacy

- Master’s Degree in Digital Transformation at Nexford University is **awarded**, confirmed by the degree holder; public statement of result is intentionally not embedded.
- Microsoft credential links are included for third-party verification; check credential expiry at issuer site.
- Some employment periods overlap. Verify all exact months and contract/concurrent arrangements before repurposing as a formal CV.
- Employer projects are described only at high level. Do not publish proprietary source code, architectural secrets, real cloud identifiers, or internal screenshots without authorisation.
- Codex workflow describes engineering approach; does not claim unreviewed AI deployments.

## Local preview

```bash
python3 -m http.server 8080
```

Open http://localhost:8080 . No build step or node dependencies required.
