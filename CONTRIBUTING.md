# Contributing

Thanks for your interest in contributing! The following guidelines are a minimal set of best-practices to help keep the project tidy and ensure your change can be reviewed quickly.

1. Fork the repository and create a feature branch:

```bash
git clone <repo-url>
git checkout -b feature/my-feature
```

2. Follow the coding style and add tests for all new functionality. Run the test suite before submitting a PR:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m pytest -q
```

3. When opening a PR, include a clear description of the problem you're solving and what changes you made. Reference any related issues with `#`.

4. Keep PRs scoped to a single purpose when possible — small focused PRs are easier to review.

5. Be responsive to review feedback and iterate quickly; tests and CI should pass before requesting a merge.

6. If your PR contains potentially breaking changes, please include a short migration guide in the PR description or documentation.

We welcome contributions of all sizes. If you need help deciding what to work on, open an issue and describe your idea.
