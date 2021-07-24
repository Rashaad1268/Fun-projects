from PIL import Image


ASCII_CHARS = ["@", "#", "&", "%", "?", "*", "+", ";", ":", ",", "."]
WIDTH = 150

def resize_image(image, new_width=WIDTH):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    return image.resize((new_width, new_height))


def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return characters

image_path = input("Image path >>> ")
image = Image.open(image_path).convert("L")
image = resize_image(image)
new_image_data = pixels_to_ascii(image)
pixel_count = len(new_image_data)

ascii_image = "\n".join(new_image_data[i:(i+WIDTH)] for i in range(0, pixel_count, WIDTH))
print(ascii_image)
