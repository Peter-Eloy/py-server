# Contributing to Mock API Server

Thank you for your interest in contributing! 🎉

## How to Contribute

1. **Fork** the repository
2. **Clone** your fork locally
   ```bash
   git clone https://github.com/YOUR-USERNAME/py-server.git
   cd py-server
   ```
3. **Create a branch** for your feature/fix
   ```bash
   git checkout -b feature/amazing-feature
   ```
4. **Make changes** and test thoroughly
5. **Commit** with clear messages
   ```bash
   git commit -m 'Add amazing feature'
   ```
6. **Push** to your fork
   ```bash
   git push origin feature/amazing-feature
   ```
7. **Open a Pull Request**

## Development Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Create a virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

2. **Install dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. **Run in development mode**
   ```bash
   # CLI mode (no GUI)
   python3 run.py
   
   # OR System tray mode
   python3 run_gui.py
   ```

4. **Access the admin panel**
   Open [http://localhost:5000/admin](http://localhost:5000/admin) in your browser

## Code Style

- Follow **PEP 8** for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions small and focused
- Use type hints where appropriate

### Example
```python
def create_endpoint(project_id: int, path: str, method: str) -> Endpoint:
    """
    Create a new API endpoint.
    
    Args:
        project_id: ID of the parent project
        path: URL path (e.g., '/users')
        method: HTTP method (GET, POST, etc.)
    
    Returns:
        The created Endpoint object
    """
    endpoint = Endpoint(
        project_id=project_id,
        path=path,
        method=method
    )
    db.session.add(endpoint)
    db.session.commit()
    return endpoint
```

## Project Structure

```
py-server/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── config.py            # Configuration
│   ├── models.py            # Database models
│   ├── routes/              # Route handlers
│   │   ├── admin.py         # Admin panel
│   │   ├── api.py           # Dynamic API
│   │   └── main.py          # Root routes
│   └── templates/           # HTML templates
├── run.py                   # Development server
├── run_gui.py               # System tray app
├── build.py                 # Build script
└── requirements.txt         # Dependencies
```

## Testing Checklist

Before submitting a Pull Request, please ensure:

- [ ] Code runs without errors: `python3 run.py`
- [ ] GUI works correctly: `python3 run_gui.py`
- [ ] Build succeeds: `python3 build.py`
- [ ] No console errors or warnings
- [ ] New features are documented
- [ ] Code follows PEP 8 style guide
- [ ] Database migrations work (if applicable)
- [ ] Existing functionality is not broken

## Building the Executable

Test that your changes work in the built version:

```bash
python3 build.py
```

The executable will be in `dist/MockAPIServer` (or `dist/MockAPIServer.exe` on Windows).

## Areas for Contribution

We welcome contributions in these areas:

### Features
- [ ] Authentication/API keys for endpoints
- [ ] Request logging and history
- [ ] Import/export projects (JSON format)
- [ ] Custom response headers
- [ ] Delay simulation for responses
- [ ] CORS configuration per endpoint
- [ ] Dark mode for admin panel

### Improvements
- [ ] Better error handling
- [ ] Unit tests
- [ ] Integration tests
- [ ] Documentation improvements
- [ ] UI/UX enhancements
- [ ] Performance optimizations

### Bug Fixes
- Check [Issues](https://github.com/peter-eloy/py-server/issues) for reported bugs

## Commit Message Guidelines

Write clear, descriptive commit messages:

- **Good**: `Add JSON validation for endpoint responses`
- **Good**: `Fix bug where DELETE endpoints weren't working`
- **Bad**: `update stuff`
- **Bad**: `fix`

Format:
```
<type>: <short summary>

<optional longer description>
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

## Pull Request Process

1. Update the README.md if you're adding new features
2. Ensure your code passes all checks
3. Request review from maintainers
4. Address any feedback
5. Once approved, your PR will be merged!

## Reporting Bugs

Found a bug? Please open an [Issue](https://github.com/peter-eloy/py-server/issues) with:

- **Clear title** describing the problem
- **Steps to reproduce** the issue
- **Expected behavior** vs. **actual behavior**
- **Screenshots** (if applicable)
- **Environment** (OS, Python version)

## Feature Requests

Have an idea? Open an [Issue](https://github.com/peter-eloy/py-server/issues) with:

- **Clear description** of the feature
- **Use case** - why is it needed?
- **Proposed solution** (optional)

## Questions?

- Open an [Issue](https://github.com/peter-eloy/py-server/issues) with the `question` label
- Reach out to [@peter-eloy](https://github.com/peter-eloy)

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Help others learn and grow

---

**Thank you for contributing to Mock API Server!** 🚀
