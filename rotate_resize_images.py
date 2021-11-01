#!/usr/bin/env python3

import os
from PIL import Image

home = os.path.expanduser('~')
directory = "/images/"

for file in os.listdir(home + directory):
	image = Image(file)
	image.rotate(90)
	image.resize((128, 128))
	image.save()
