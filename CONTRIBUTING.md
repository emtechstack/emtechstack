
# Contributing to EmTechStack

Thank you for considering contributing to our project! Here are the guidelines for contributing:

## Fork and Clone

1. Fork the repository by clicking the "Fork" button at the top right of the repository page.
2. Clone the forked repository to your local machine:
   ```sh
   git clone https://github.com/emtechstack/emtechstack.git
   cd repo-name
   ```

## Create a Branch

1. Create a new branch for your feature or bugfix:
   ```sh
   git checkout -b feat/feature-name
   ```

## Make Changes

1. Make your changes to the code.
2. Commit your changes with a meaningful commit message:
   ```sh
   git add .
   git commit -m "Description of the changes"
   ```

## Push Changes

1. Push your changes to your forked repository:
   ```sh
   git push origin feature-branch-name
   ```

## Submit a Pull Request

1. Go to the original repository on GitHub.
2. Click on the "Pull Requests" tab and then the "New Pull Request" button.
3. Select the branch you made changes on, and click "Create Pull Request".
4. Add a descriptive title and detailed description of your changes.
5. Submit the pull request.

## Code Review

Your pull request will be reviewed by one of the project maintainers. Please make any requested changes promptly.

## Status Checks

All pull requests must pass the following status checks before merging:
- **Linting**: Code must pass linting rules using Flake8.
- **Testing**: Code must pass all tests using pytest.

Thank you for your contribution!
