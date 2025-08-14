# Sample Package A

A demonstration Python package showcasing manifest-driven release automation with release-please.

## 🎯 Purpose

This package demonstrates:
- **Modern Python packaging** with Poetry
- **CLI development** with Click and asyncio
- **HTTP client integration** with httpx and Pydantic
- **Comprehensive testing** with pytest and coverage
- **Container deployment** with Docker
- **Automated releases** with release-please

## 📦 Installation

### From Source
```bash
# Install with Poetry
cd packages/a
poetry install

# Or with pip (after building)
poetry build
pip install dist/sample_package_a-*.whl
```

### From Docker
```bash
docker run --rm ghcr.io/your-username/repo-name/package-a:latest --help
```

## 🚀 Usage

### Command Line Interface

```bash
# Get help
sample-a --help

# Check your IP address
sample-a info

# Process data with key-value pairs
sample-a process -k name=alice -k role=developer -k location=remote

# Send custom data to external service
sample-a send -d '{"project": "sample-a", "status": "active"}'

# Use JSON output format
sample-a info -f json
sample-a process -k env=production -f json
```

### Python API

```python
import asyncio
from a.main import SampleService

# Initialize service
service = SampleService()

# Process data synchronously
result = service.process_data({"key": "value"})
print(result.status)  # "success"
print(result.data)    # {"input_keys": ["key"], "input_count": 1, "processed": True}

# Use async methods
async def main():
    ip_info = await service.get_ip_info()
    print(f"Your IP: {ip_info['origin']}")
    
    response = await service.post_data({"message": "Hello!"})
    print(response)

asyncio.run(main())
```

## 🧪 Development

### Setup Development Environment

```bash
# Install dependencies including dev tools
poetry install

# Install pre-commit hooks (optional)
pre-commit install
```

### Running Tests

```bash
# Run all tests with coverage
poetry run pytest

# Run with detailed output
poetry run pytest -v --cov-report=html

# Run specific test file
poetry run pytest tests/test_dummy.py -v
```

### Code Quality

```bash
# Format code
poetry run black .
poetry run isort .

# Lint code
poetry run flake8
poetry run mypy src/

# All quality checks
poetry run black . && poetry run isort . && poetry run flake8 && poetry run mypy src/
```

### Docker Development

```bash
# Build development image
docker build -t sample-a:dev .

# Run tests in container
docker run --rm sample-a:dev -c "poetry run pytest"

# Interactive development
docker run --rm -it -v $(pwd):/app sample-a:dev bash
```

## 📖 API Reference

### SampleService

Main service class providing core functionality.

#### Methods

- **`process_data(input_data: Dict[str, Any]) -> ApiResponse`**
  - Synchronously processes input data
  - Returns structured response with metadata

- **`async get_ip_info() -> Dict[str, Any]`**
  - Fetches IP information from external service
  - Returns JSON response from httpbin.org

- **`async post_data(data: Dict[str, Any]) -> Dict[str, Any]`**
  - Posts data to external service
  - Returns server response with echo data

### ApiResponse

Pydantic model for structured responses.

#### Fields

- **`status: str`** - Response status ("success", "error", etc.)
- **`message: str`** - Human-readable message
- **`data: Dict[str, Any]`** - Response payload data
- **`timestamp: str`** - Processing timestamp

## 🏗️ Architecture

```
src/a/
├── __init__.py          # Package initialization and metadata
└── main.py             # CLI application and service logic

tests/
└── test_dummy.py       # Comprehensive test suite

Configuration:
├── pyproject.toml      # Poetry package configuration
├── Dockerfile         # Multi-stage container build
└── .dockerignore      # Docker build exclusions
```

## 🔄 Release Process

This package uses automated releases via release-please:

1. **Commit Changes**: Use conventional commit format
   ```bash
   git commit -m "feat: add new transformation algorithm"
   git commit -m "fix: resolve timeout in async operations"
   ```

2. **Release PR**: release-please creates PR with changelog
3. **Merge PR**: Triggers automated build and deployment
4. **Artifacts**: Package and Docker image published automatically

### Version History

See [CHANGELOG.md](./CHANGELOG.md) for detailed version history.

## Contributing

1. **Fork & Clone**: Create your own copy
2. **Branch**: Create feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit**: Use conventional commit format
4. **Test**: Ensure all tests pass (`poetry run pytest`)
5. **Submit**: Create pull request with clear description

### Conventional Commits

- `feat:` - New features (minor version bump)
- `fix:` - Bug fixes (patch version bump)  
- `feat!:` - Breaking changes (major version bump)
- `docs:` - Documentation only changes
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

##  License

This project is licensed under the MIT License - see the main repository LICENSE file for details.

## Support

- **Issues**: Report bugs via GitHub Issues
- **Discussions**: Ask questions in GitHub Discussions
- **Documentation**: Full docs in main repository README

---

Built with for demonstrating modern Python release automation!