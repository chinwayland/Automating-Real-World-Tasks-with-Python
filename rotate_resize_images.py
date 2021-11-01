#!/usr/bin/env python3

import os
from PIL import Image

home = os.path.expanduser('~')
directory = "/images/"

for filename in os.listdir(home + directory):
	image = Image.open(home + directory + filename)
	image.convert('RGB').rotate(90).resize((128, 128)).save('/opt/icons/' + filename + '.jpg')
