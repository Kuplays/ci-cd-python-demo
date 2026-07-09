# CI/CD Sample

Sample learning CI/CD with Python, pytest, GitHub Actions, Docker, reports, and deployment basics.

## Run tests locally

```bash
pip install -r requirements-dev.txt
pytest

## CI report

The CI pipeline runs pytest with JUnit XML report generation.

Reports are saved as GitHub Actions artifacts:

- `pytest-report`
- `reports/junit.xml`