# noinspection PyUnresolvedReferences
from .about import __title__, __version__, __url__

# Importing TurtleGraphicsError directly from turtle will fail without tkinter.
# noinspection PyUnresolvedReferences
from .svg_turtle import SvgTurtle, TurtleGraphicsError
