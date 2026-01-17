# Mock API Server

**Build and test APIs without backend code.**

A free desktop application that runs in your system tray, letting you create mock REST APIs with a visual admin panel. Perfect for frontend developers, QA testers, and rapid prototyping.

## 🌐 Website
**[Download the latest release →](https://peter-eloy.github.io/Landing-py-server/)**

---

## ✨ Features

- 🖥️ **System Tray App** - Runs quietly in your system tray, always ready
- 🚫 **No Coding Required** - Visual admin panel for creating endpoints
- 📄 **JSON & File Responses** - Return JSON data or serve static files (PDFs, images, etc.)
- 🗂️ **Multiple Projects** - Organize endpoints into separate projects
- 🔧 **Local Development** - Runs on `localhost:5000` by default
- ⚡ **Instant Setup** - Download, install, and start mocking APIs in seconds

---

## 📥 Download Pre-Built App

Get the ready-to-use application for your platform:

- **Windows**: [MockAPIServer.exe](https://github.com/peter-eloy/py-server/releases/latest/download/MockAPIServer.exe)
- **macOS**: [MockAPIServer.dmg](https://github.com/peter-eloy/py-server/releases/latest/download/MockAPIServer.dmg)

Or visit the [**landing page**](https://peter-eloy.github.io/Landing-py-server/) for auto-detection.

---

## 🛠️ Development Setup

Want to contribute or build from source? Follow these steps:

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/peter-eloy/py-server.git
   cd py-server
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

### Running in Development Mode

**Option 1: Command-line server (no tray icon)**
```bash
python3 run.py
```
Then open [http://localhost:5000/admin](http://localhost:5000/admin) in your browser.

**Option 2: System tray app**
```bash
python3 run_gui.py
```
The tray icon will appear, and the admin panel will open automatically.

---

## 🏗️ Building the Executable

To create a standalone executable for distribution:

```bash
python3 build.py
```

The compiled binary will be in the `dist/` folder:
- **Windows**: `dist/MockAPIServer.exe`
- **macOS**: `dist/MockAPIServer` (single-file app)

### Build Configuration

The build process uses PyInstaller and is configured in [`build.py`](build.py):
- Bundles all templates and dependencies
- Creates a single-file executable
- Includes Flask, SQLAlchemy, and pystray

---

## 📂 Project Structure

```
py-server/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── config.py            # App configuration
│   ├── models.py            # Database models (Project, Endpoint)
│   ├── routes/
│   │   ├── admin.py         # Admin panel routes
│   │   ├── api.py           # Dynamic API endpoints
│   │   └── main.py          # Root routes
│   └── templates/           # HTML templates
│       ├── base.html
│       └── admin/
│           ├── projects.html
│           ├── endpoints.html
│           └── ...
├── run.py                   # Development server (CLI)
├── run_gui.py               # System tray app
├── build.py                 # PyInstaller build script
├── requirements.txt         # Python dependencies
└── README.md
```

---

## 🚀 Usage

1. **Launch the app** (system tray icon will appear)
2. **Open the admin panel** at [http://localhost:5000/admin](http://localhost:5000/admin)
3. **Create a project** (e.g., "UserAPI")
4. **Add endpoints**:
   - Method: `GET`, `POST`, `PUT`, `DELETE`, `PATCH`
   - Path: `/users`, `/products`, etc.
   - Response: JSON or file (PDF, images)
5. **Test your API** at `http://localhost:5000/api/{ProjectName}/{endpoint}`

### Example

Create a `GET /users` endpoint under project `MyAPI`:
```
URL: http://localhost:5000/api/MyAPI/users
Response: {"users": [{"id": 1, "name": "John"}]}
```

---

## 🧪 Tech Stack

- **Backend**: Python, Flask, Flask-SQLAlchemy
- **Database**: SQLite
- **GUI**: pystray (system tray), Pillow (icons)
- **Build**: PyInstaller

---

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guide for Python code
- Test your changes with both `run.py` and `run_gui.py`
- Ensure the build succeeds with `python3 build.py`
- Update documentation if adding new features

---

## 🐛 Troubleshooting

### macOS: "App can't be opened because it is from an unidentified developer"
Right-click the app → Open → Confirm to bypass Gatekeeper (first run only).

### Windows: Antivirus flags the .exe
PyInstaller executables may trigger false positives. Add an exception or build from source.

### Port 5000 already in use
Change the port in [`run.py`](run.py) or [`run_gui.py`](run_gui.py):
```python
app.run(host='0.0.0.0', port=5001)
```

---

## 📧 Contact

**Developer**: [@peter-eloy](https://github.com/peter-eloy)  
**Website**: [Landing Page](https://peter-eloy.github.io/Landing-py-server/)

---

## ⭐ Support

If you find this project helpful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs or requesting features via [Issues](https://github.com/peter-eloy/py-server/issues)
- 📢 Sharing with other developers

---

**Made with ❤️ by developers, for developers.**
