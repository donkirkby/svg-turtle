from .svg_turtle import SvgTurtle
try:
  from IPython.display import display, SVG
except ImportError:
  display = SVG = None

class IPythonTurtle(SvgTurtle):
  ipy_disp = None

  def __init__(self, *args):
    if display is None:
      raise ImportError("Could not import required dependency IPython.display")
    super().__init__(*args)

  def _repr_svg_(self):
    return self.to_svg()
  
  def show(self):
    # noinspection PyCallingNonCallable
    display(SVG(self.to_svg()))
