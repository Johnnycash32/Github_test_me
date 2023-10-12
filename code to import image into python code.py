

#python
from PIL import Image

def image_to_py_code(image_path, output_path):
    image = Image.open(image_path)
    width, height = image.size

    with open(output_path, 'w') as f:
        f.write('from PIL import Image\n\n')
        f.write(f'image = Image.new("RGB", ({width}, {height}))\n\n')

        for y in range(height):
            for x in range(width):
                r, g, b = image.getpixel((x, y))
                f.write(f'image.putpixel(({x}, {y}), ({r}, {g}, {b})))\n')

image_path = 'path/to/your/image.png'
output_path = 'image_to_py_code.py'
image_to_py_code(image_path, output_path)