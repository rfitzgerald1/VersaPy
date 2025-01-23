# Cookiecutter Python Project Template

🎉 **Welcome to the Cookiecutter Python Project Template!** 🎉  
A versatile Python project template designed to streamline development with best practices for CLI tools, web applications, and machine learning pipelines.

---

## 🚀 Quickstart

Get up and running in just a few steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/versapy.git
   cd versapy
   ```

2. **Install `cookiecutter`**:
   ```bash
   pip install cookiecutter
   ```

3. **Scaffold a new project**:
   ```bash
   cookiecutter ./cookiecutter-template
   ```

4. **Start your project**:
   ```bash
   cd your_project_name
   python src/app.py
   ```

---

## ✨ Highlights

✔️ **Pre-configured testing**: Comes with `pytest`, `tox`, and coverage tools.  
✔️ **CI/CD workflows**: Automated pipelines using GitHub Actions.  
✔️ **Security tools**: Integrated with `bandit`, `safety`, and `detect-secrets`.  
✔️ **Domain-specific scaffolding**: Supports CLI (`click`), web (`FastAPI`), and ML (`scikit-learn`) projects.  
✔️ **Advanced logging**: Built-in logging with `loguru`.  
✔️ **Environment-based configuration**: Easy management with `.env` files and `pydantic`.  

---

## 👥 Who Is This For?

This template is ideal for:

- **Developers** who want a head start on Python projects with best practices built-in.
- **Teams** seeking a unified structure and tooling for their projects.
- **Beginners** aiming to learn professional Python development setups.

---

## Features

- **Domain-Specific Scaffolding**:
  - 🛠️ Support for CLI tools (`click`).
  - 🌐 Web applications (`FastAPI`).
  - 📊 Machine learning pipelines (`scikit-learn`).
  - Easily switch between project types or customize scaffolding by selecting the appropriate `project_type` during initialization.
- **Pre-Configured Tools**:
  - 🧪 Testing with `pytest` and `tox`.
  - 🛡️ Code quality with `black`, `flake8`, `isort`, and `mypy`.
  - 🔍 Logging with `loguru`.
- **Advanced Configuration Management**:
  - 🌍 Environment-based settings with `.env` files and `pydantic`.
- **Security Tools**:
  - 🛡️ Dependency checks with `safety`.
  - 🔍 Code analysis with `bandit`.
  - 🔑 Secret detection with `detect-secrets`.
- **Integrated CI/CD Workflows**:
  - ✅ Testing and security checks.
  - 🚀 Deployment with Docker and GitHub Actions.

---

## 📂 Directory Structure

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

---

## 🔄 CI/CD Workflows

This template includes GitHub Actions workflows for:

1. **Testing and Security Checks**:
   - Ensures high-quality code with automated tests.
2. **Deployment**:
   - Builds Docker images and optionally deploys to AWS ECS.

Refer to `.github/workflows/` for more details.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. [Fork the repository](https://github.com/your-username/versapy).
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to your branch and open a pull request.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

