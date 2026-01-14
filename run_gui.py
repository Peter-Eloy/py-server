import threading
import webbrowser
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw
import sys
from app import create_app

app = None
server_thread = None

def create_image():
    """Create a simple icon"""
    width = 64
    height = 64
    image = Image.new('RGB', (width, height), 'blue')
    dc = ImageDraw.Draw(image)
    dc.rectangle([width // 4, height // 4, width * 3 // 4, height * 3 // 4], fill='white')
    return image

def run_server():
    global app
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)

def start_server(icon, item):
    global server_thread
    if server_thread is None or not server_thread.is_alive():
        server_thread = threading.Thread(target=run_server, daemon=True)
        server_thread.start()
        webbrowser.open('http://localhost:5000/admin')

def quit_app(icon, item):
    icon.stop()
    sys.exit()

def setup_tray():
    icon = Icon(
        "MockAPIServer",
        create_image(),
        "Mock API Server",
        Menu(
            MenuItem('Open Admin Panel', start_server, default=True),
            MenuItem('Quit', quit_app)
        )
    )
    
    # Auto-start server
    start_server(icon, None)
    
    icon.run()

if __name__ == '__main__':
    setup_tray()