# Release Please Sample Repository

This repository demonstrates manifest-driven release automation using Google's release-please tool with a single Python package.

## 🏗️ Architecture Overview

```
release-please-sample/
├── .github/workflows/
│   └── release.yaml              # GitHub Actions workflow for releases
├── packages/a/                   # Sample Python package
│   ├── src/a/                   # Application source code
│   ├── tests/                   # Test suite
│   ├── pyproject.toml          # Poetry configuration
│   ├── Dockerfile              # Container definition
│   └── CHANGELOG.md            # Auto-generated changelog
├── release-please-config.json   # Release-please configuration
└── .release-please-manifest.json # Version tracking manifest
```

## 🚀 Features Demonstrated

### 1. **Manifest-Driven Release Automation**
- **Conventional Commits**: Automatic changelog generation from commit messages
- **Version Bumping**: Semantic versioning based on commit types
- **GitHub Releases**: Automated release creation with artifacts
- **Multi-format Support**: JSON and pretty-print outputs

### 2. **CI/CD Pipeline**
- **Automated Testing**: pytest with coverage reporting
- **Docker Building**: Multi-stage containerization
- **Artifact Publishing**: GitHub Packages integration
- **Conditional Workflows**: Only build/deploy on actual releases

### 3. **Python Package Structure**
- **Poetry Management**: Modern dependency and build management
- **CLI Interface**: Click-based command-line tool
- **Async Support**: HTTP client with asyncio
- **Type Safety**: Pydantic models and mypy checking

## 📋 Prerequisites

- Python 3.11+
- Poetry 1.7+
- Docker (optional)
- GitHub account with Actions enabled

## 🛠️ Setup Instructions

### Step 1: Clone and Initialize

```bash
# Clone the repository
git clone <your-repo-url>
cd release-please-sample

# Initialize git (if needed)
git init
git add .
git commit -m "feat: initial project setup

This commit sets up the basic project structure with:
- Release-please configuration for automated releases
- Python package with CLI interface
- GitHub Actions workflow for CI/CD
- Docker containerization support"
```

### Step 2: Configure GitHub Repository

1. **Enable GitHub Actions**:
   - Go to repository Settings → Actions → General
   - Allow all actions and reusable workflows

2. **Set Repository Permissions**:
   - Settings → Actions → General → Workflow permissions
   - Select "Read and write permissions"
   - Check "Allow GitHub Actions to create and approve pull requests"

3. **Configure Branch Protection** (optional):
   - Settings → Branches → Add rule for `main`
   - Require pull request reviews
   - Require status checks to pass

### Step 3: Install Dependencies

```bash
cd packages/a
poetry install
```

### Step 4: Test the Setup

```bash
# Run tests
poetry run pytest

# Try the CLI
poetry run sample-a --help
poetry run sample-a info
poetry run sample-a process -k name=test -k env=demo
```

## Release Process

### How It Works

1. **Make Changes**: Create commits following conventional format
2. **Push to Main**: GitHub Actions detects changes
3. **Release PR**: release-please creates/updates a release PR
4. **Merge PR**: Merging triggers actual release creation
5. **Automation**: Build, test, and publish happen automatically

### Conventional Commit Format

```bash
# Feature addition (minor version bump)
git commit -m "feat: add new data processing feature"

# Bug fix (patch version bump)  
git commit -m "fix: resolve async timeout issue"

# Breaking change (major version bump)
git commit -m "feat!: redesign API interface

BREAKING CHANGE: The process() method now returns ApiResponse instead of dict"

# Other types (no version bump)
git commit -m "docs: update installation instructions"
git commit -m "chore: update dependencies"
```

### Example Workflow

```bash
# 1. Make feature changes
echo "New feature code" >> packages/a/src/a/new_feature.py
git add .
git commit -m "feat: add advanced data transformation

- Implement new transformation algorithms
- Add configuration options for custom processing
- Include comprehensive test coverage"

# 2. Push to trigger release process
git push origin main

# 3. Wait for release-please to create PR
# 4. Review and merge the release PR
# 5. Automated build and publish will trigger
```

## Using the Sample Application

### CLI Commands

```bash
# Get your IP address
sample-a info

# Process data with custom key-value pairs
sample-a process -k name=john -k age=30 -k city=seattle

# Send data to external service
sample-a send -d '{"message": "Hello from sample-a!", "version": "1.0"}'

# Output in JSON format
sample-a info -f json
sample-a process -k test=value -f json
```

### Docker Usage

```bash
# Build image
docker build -t sample-a packages/a/

# Run commands
docker run --rm sample-a info
docker run --rm sample-a process -k env=docker -k test=container

# Interactive shell
docker run --rm -it --entrypoint bash sample-a
```

## 📊 Monitoring Releases

### GitHub Releases Page
- View: `https://github.com/your-username/repo-name/releases`
- Contains: Changelog, artifacts, Docker images

### Package Registry
- View: `https://github.com/your-username/repo-name/pkgs/container/package-a`
- Contains: Docker images with version tags

### Actions Logs
- View: Repository → Actions tab
- Monitor: Build status, test results, deployment progress

## 🔧 Configuration Details

### release-please-config.json
```json
{
  "packages": {
    "packages/a": {
      "changelog-path": "CHANGELOG.md",
      "release-type": "python",
      "component": "a",
      "package-name": "sample-package-a"
    }
  }
}
```

### Workflow Triggers
- **Push to main**: Triggers release-please analysis
- **Manual dispatch**: Allows manual workflow execution
- **PR merge**: Creates releases when release PR is merged

## 🐛 Troubleshooting

### Common Issues

1. **Release PR not created**:
   - Check commit message format
   - Verify conventional commits
   - Review workflow permissions

2. **Build failures**:
   - Check test results in Actions
   - Verify Python/Poetry versions
   - Review dependency conflicts

3. **Docker build issues**:
   - Verify Dockerfile syntax
   - Check base image compatibility
   - Review poetry.lock file

### Debug Commands

```bash
# Check release-please configuration
npx release-please release-pr --repo-url=. --dry-run

# Validate conventional commits
npx @commitlint/cli --from=HEAD~1

# Test workflow locally (with act)
act push -j release
```

## 📚 Additional Resources

- [Release Please Documentation](https://github.com/googleapis/release-please)
- [Conventional Commits Specification](https://www.conventionalcommits.org/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Poetry Documentation](https://python-poetry.org/docs/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes with conventional commits
4. Submit a pull request
5. Watch the automated release process!

---

**Happy Releasing! 🎉**