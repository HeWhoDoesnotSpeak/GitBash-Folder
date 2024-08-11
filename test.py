from PIL import Image

def test_image_open():
    try:
        # Replace the path with the correct path to your image
        image = Image.open(r"C:\\Users\\64223\\CPS\\GitBash Folder\\DDT logo.png")
        image.show()  # This will open the image using the default image viewer
    except Exception as e:
        print(f"Error: {e}")

test_image_open()