from PIL import Image, ImageFilter

from django.core.files.base import ContentFile

from io import BytesIO
import os

def blur_image(image, blur_radius=25):
    
    img = Image.open(image)
    img = img.filter(ImageFilter.GaussianBlur(blur_radius))
    img_io = BytesIO()

    file_extension = os.path.splitext(image.name)[1].lower()
    format = 'JPEG'
    if file_extension in ['.jpeg', '.jpg']:
        format = 'JPEG'
    elif file_extension == '.png':
        format = 'PNG'
    elif file_extension == '.gif':
        format = 'GIF'
                
    img.save(img_io, format=format)
    img_content = ContentFile(img_io.getvalue(), name=image.name)
    return img_content


