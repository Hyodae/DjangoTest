from django.shortcuts import render
from django.http import HttpResponse

from matplotlib import pylab
from pylab import *
from PIL import Image
import PIL.Image

import io

import numpy as np


# Create your views here.

def showimage(request):
    # Construct the graph
    t = arange(0.0, 2.0, 0.01)
    s = sin(2*pi*t)
    plot(t, s, linewidth=1.0)

    xlabel('time (s)')
    ylabel('voltage (mV)')
    title('Simple Sine Graph')
    grid(True)

    # Store image in a string buffer
    buffer = io.BytesIO()
    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    pylab.close()

    # Send buffer in a http response the the browser with the mime type image/png set
    return HttpResponse(buffer.getvalue(), content_type="image/png")

def mplimage(request):
	# Construct the graph
	x = np.arange(-2,1.5,.01)
	y = np.sin(np.exp(2*x))
	plot(x, y)

	# Store image in a buffer
	buffer = io.BytesIO()
	canvas = pylab.get_current_fig_manager().canvas
	canvas.draw()
	pilImage = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
	pilImage.save(buffer, "PNG")
	pylab.close()

	return HttpResponse(buffer.getvalue(), content_type="image/png")
