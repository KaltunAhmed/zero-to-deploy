# zero-to-deploy

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
2. [What a server is && Run your first local server ](docs/01-foundations/02-what-is-a-server.md)


