# Cookiecutter Python Project Template

A versatile Python project template designed to streamline development with best practices for various project types, including CLI tools, web applications, and machine learning pipelines.

## Features

- **Domain-Specific Scaffolding**:
  - Support for CLI tools (`click`).
  - Web applications (`FastAPI`).
  - Machine learning pipelines (`scikit-learn`).
- **Pre-Configured Tools**:
  - Testing with `pytest` and `tox`.
  - Code quality with `black`, `flake8`, `isort`, and `mypy`.
  - Logging with `loguru`.
- **Advanced Configuration Management**:
  - Environment-based settings with `.env` files and `pydantic`.
- **Security Tools**:
  - Dependency checks with `safety`.
  - Code analysis with `bandit`.
  - Secret detection with `detect-secrets`.
- **Integrated CI/CD Workflows**:
  - Testing and security checks.
  - Deployment with Docker and GitHub Actions.

## Getting Started

### Requirements
- Python 3.10+
- [Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/installation.html)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/versapy.git
   cd versapy
   ```

2. Install `cookiecutter`:
   ```bash
   pip install cookiecutter
   ```

3. Scaffold a new project:
   ```bash
   cookiecutter ./cookiecutter-template
   ```

### Usage
When you run the `cookiecutter` command, you'll be prompted to enter:
- `project_name`: The name of your new project.
- `author_name`, `email`, and more based on the `cookiecutter.json` configuration.

Once complete, your new project will be created in a directory named after your `project_name`.

### Example
Scaffold a CLI project:
```bash
cookiecutter ./cookiecutter-template
```
Select `project_type=cli` when prompted.

Run the example:
```bash
python src/cli.py
```

## Directory Structure
This template creates a project with the following structure:
```
project_name/
├── src/
│   ├── __init__.py
│   ├── app.py
│   └── logging_config.py
├── tests/
│   ├── __init__.py
│   └── test_example.py
├── docs/
│   ├── index.md
│   └── guide.md
├── examples/
│   └── example_usage.py
├── scripts/
│   └── utility_script.py
├── requirements/
│   ├── base.txt
│   ├── dev.txt
│   └── test.txt
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── deploy.yml
├── .gitignore
├── LICENSE
├── README.md
```

## CI/CD Workflows
This template includes GitHub Actions workflows for:
1. **Testing and Security Checks**:
   - Ensures high-quality code with automated tests.
2. **Deployment**:
   - Builds Docker images and optionally deploys to AWS ECS.

Refer to `.github/workflows/` for more details.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to your branch and open a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

