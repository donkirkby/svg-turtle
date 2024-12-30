from importlib import import_module
from .svg_turtle import SvgTurtle

class IPythonTurtle(SvgTurtle):
  ipy_disp = None

  def __init__(self, *args):
    if IPythonTurtle.ipy_disp is None:
      try:
        IPythonTurtle.ipy_disp = import_module('IPython.display')
      except ImportError as err:
        raise ImportError("Could not import required dependency IPython.display") from err
    super().__init__(*args)

  def _repr_svg_(self):
    return self.to_svg()
  
  def show(self):
    IPythonTurtle.ipy_disp.display(IPythonTurtle.ipy_disp.SVG(self.to_svg()))
