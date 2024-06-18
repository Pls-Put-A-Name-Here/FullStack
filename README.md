# FullStack repository

Welcome to the `FullStack` repository under the organization `pls-put-a-name-here`. This repository is dedicated to the development of the EcommerceX project. Here's a guide on how to contribute effectively using a feature branch workflow.

## Getting Started

Follow these steps to set up your development environment and contribute to the project:

### 1. Fork the Repository

Visit the main repository on GitHub: `https://github.com/pls-put-a-name-here/FullStack`

Click on the "Fork" button in the top-right corner.

Choose the destination for the fork (personal account or organization).

### 2. Clone Your Fork Locally

Open a terminal on your local machine.

Clone your forked repository using the following command:

```bash
git clone https://github.com/your-username/FullStack.git
```

### 3. Add Upstream Remote

Navigate to the cloned directory:

```bash
cd FullStack
```

Add a remote to track the main repository:

```bash
git remote add upstream https://github.com/pls-put-a-name-here/FullStack.git
```

### 4. Create a Feature Branch

Create and switch to a new branch for your feature:

```bash
git checkout -b feature-branch
```

### 5. Make Changes and Commit

Make your changes in the code.

Stage and commit your changes:

```bash
git add .
git commit -m "Implemented feature X"
```

### 6. Push Changes to Your Fork

Push your changes to your fork on GitHub:

```bash
git push origin feature-branch
```

### 7. Open a Pull Request

Visit your fork on GitHub.

Switch to the `feature-branch` and click on "New Pull Request."

Select `dev` as the base branch and your `feature-branch` as the compare branch.

### 8. Review and Merge

Team members review the pull request.

Address any feedback and make additional commits if necessary.

Once approved, merge the changes into the `dev` branch.

### 9. Sync Fork with Upstream (Optional)

Periodically, sync your fork with the upstream to get the latest changes:

```bash
git fetch upstream
git merge upstream/dev
git push origin dev
```

## Contribution Guidelines

- All contributions should be made through feature branches.
- All pull requests should be made on the dev branch
- Follow the outlined steps for creating feature branches and making pull requests.
- Ensure that your changes pass automated tests in the CI/CD pipeline.
- Collaborate through code reviews and address feedback promptly.

## Additional Information

For additional information, project setup details, coding standards, and guidelines, please refer to the documentation in the [`docs`](./project_docs) directory.

Thank you for contributing to the `FullStack` project under `pls-put-a-name-here`! Let's build something amazing together.

---

<div style="display:flex;justify-content:center">©Pls-Put-A-Name-Here 2024<div>
