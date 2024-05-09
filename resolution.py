import glfw 
from OpenGL.GL import *
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np

# Initialize GLFW
if not glfw.init():
    raise Exception("GLFW initialization failed")

# Get the primary monitor
primary_monitor = glfw.get_primary_monitor()
if primary_monitor is None:
    raise Exception("Primary monitor not found")

# Get the video mode for the primary monitor
video_modes = glfw.get_video_modes(primary_monitor)
if not video_modes:
    raise Exception("Video modes not found")

screen_width = video_modes[0][0]  # Access width using index 0
screen_height = video_modes[0][1]  # Access height using index 1
resolution_str = f"Display Resolution: {screen_width}x{screen_height}"

# Initialize OpenGL
def initialize():
    window = glfw.create_window(600, 100, "The resolution of my Display", None, None)
    if not window:
        glfw.terminate()
        raise Exception("Window creation failed")
    glfw.make_context_current(window)
    
    while not glfw.window_should_close(window):
        display()
        glfw.swap_buffers(window)
        glfw.poll_events()
    
    glfw.terminate()

# Display function
def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)
    draw_text(10, 40, resolution_str)

# Function to draw text on the screen
def draw_text(x, y, text):
    font = ImageFont.load_default()
    image = Image.new("RGB", (600, 100), color=(0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.text((x, y), text, font=font, fill=(255, 255, 255, 0))
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    data = np.array(image)
    glDrawPixels(600, 100, GL_RGB, GL_UNSIGNED_BYTE, data)

if __name__ == "__main__":
    initialize()
