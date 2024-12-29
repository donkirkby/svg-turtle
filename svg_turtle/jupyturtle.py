from importlib import import_module
from .svg_turtle import SvgTurtle

class JupyTurtle(SvgTurtle):
  ipy_disp = None

  def __init__(self, *args):
    if JupyTurtle.ipy_disp is None:
      try:
        JupyTurtle.ipy_disp = import_module('IPython.display')
      except ImportError as err:
        raise ImportError("Could not import required dependency IPython.display") from err
    super().__init__(*args)

  def _repr_svg_(self):
    return self.to_svg()
  
  def show(self):
    JupyTurtle.ipy_disp.display(JupyTurtle.ipy_disp.SVG(self.to_svg()))
