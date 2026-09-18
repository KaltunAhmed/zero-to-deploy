# 🚀 Zero-to-deploy 🚀

A hands-on repo for learning CI/CD, containers, and cloud deployment from
first principles — starting with what a server even is, and building up to a
real deployment on AWS.

## What's in this repo

- **`docs/`** — the actual course content, written as numbered markdown files
  organized by part. Read these in order.
- **`app/`** — a small Python app that grows through the course. You'll run
  it locally, test it, containerize it, and eventually deploy it.
- **`tests/`** — automated tests for the app, introduced in Part 3.
- **`.github/workflows/`** — the CI/CD pipeline configuration, introduced in
  Part 3 and expanded in later parts.
- **`infra/`** — Terraform code describing the AWS infrastructure, introduced
  in Part 9.

Each doc that has a hands-on step tells you exactly what to run and where —
you're not just reading, you're doing.

## How to use this repo

Start at the top of the contents below and work down. Each section builds on
concepts from the one before it, so it's not really designed to be skipped
around — even if you already know a piece, skimming it first will keep the
mental model consistent for later sections.

## Contents

### Part 1 — Foundations
1. [Components of a computer](docs/01-foundations/01-computers-and-os.md)
2. [What a server is & run your first local server ](docs/01-foundations/02-what-is-a-server.md)


### Part 2 — Version Control
4. [What Git is vs what GitHub is](docs/02-version-control/01-git-vs-github.md)
5. [Repositories](docs/02-verison-control/01-git-vs-github.md#repositories) 
6. [Branches](docs/02-verison-control/01-git-vs-github.md#stagingandcommitting)
7. [Staging and committing](docs/02-verison-control/01-git-vs-github.md#staging-and-committing)
8. [Pull Requests](docs/02-verison-control/01-git-vs-github.md#pull-requests)
9. [Common git commands](docs/02-verison-control/01-git-vs-github.md#common-git-commands)
10. [Exersise: make a branch, commit a change, push it](docs/02-verison-control/01-git-vs-github.md#exercise)


## COMING SOON: 
### Part 3 — Testing & CI 
10. What is testing and why we test code 
11. Writing your first test (pytest)
12. What CI actually is — automated checks on every change
13. Setting up CI to run tests automatically (GitHub Actions)
14. Branch protection — blocking merges until CI passes


### Part 4 — Environments & Deployment
15. What "deployment" means
16. What an environment is 
17. Dev, staging, and prod — purpose of each
18. Other environments you may see (ext test / sandbox / UAT)
19. What manual deployment used to look like and risks
20. What CD is — automating deployment


### Part 5 — Containers
21. What are containers and the problem they solve 
23. Docker basics — building an image, running a container
24. Dockerizing the example app (hands-on)


### Part 6 — AWS Fundamentals
25. What "the cloud" actually means
26. What AWS is, and renting vs owning infrastructure
27. Setting up your own AWS account safely (budgets, root vs IAM user)
28. IAM basics — users, roles, permissions

### Part 7 — Running Containers in AWS
29. ECR — storing your container images
30. ECS — running your containers
31. Pushing and running your first container manually (hands-on)
32. Mapping dev/stg/prod onto ECS

### Part 8 — Automating Deployment (CD)
33. Automating the build → ECR → ECS flow with CI/CD
34. Deploying to dev automatically, promoting to stg/prod

### Part 9 — Infrastructure as Code
35. What is Infrastructure as Code
36. What Terraform is and how it works
37. Writing your first Terraform file (hands-on)
38. Representing environments in Terraform (workspaces / tfvars)

### Part 10 — Automating Infrastructure
39. Why applying Terraform manually is risky
40. What Spacelift is — CI/CD for infrastructure
41. Reviewing and applying infrastructure changes safely

### Part 11 — Putting It All Together
42. Full picture: from `git push` to a live user request
43. Glossary of terms