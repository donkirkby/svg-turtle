# SaVaGe Turtle [![Build Badge]][build] [![Coverage Badge]][codecov] [![Downloads Badge]][downloads] [![PyPI Badge]][pypi] [![Supported Python versions]][pypi]
[Supported Python versions]: https://img.shields.io/pypi/pyversions/svg-turtle.svg

### Use the Python turtle to write SVG files

[Build Badge]: https://github.com/donkirkby/svg-turtle/actions/workflows/build.yml/badge.svg?branch=main
[build]: https://github.com/donkirkby/svg-turtle/actions
[Coverage Badge]: https://codecov.io/github/donkirkby/svg-turtle/coverage.svg?branch=main
[codecov]: https://codecov.io/github/donkirkby/svg-turtle?branch=main
[PyPI Badge]: https://badge.fury.io/py/svg-turtle.svg
[pypi]: https://pypi.org/project/svg-turtle/
[Downloads Badge]: https://static.pepy.tech/badge/svg-turtle/month
[downloads]: https://pepy.tech/project/svg-turtle

If you're using the Python turtle module to teach students, or you just like
using the turtle module yourself, this library can save the images from a turtle
script as SVG files. Experiment with your turtle code using the regular turtle
or the [Live Coding in Python] plugin for PyCharm, then pass an `SvgTurtle` to
the same code, and save it as an SVG file. If you want to produce other file
formats, use [svglib] to convert the SVG to PDF, PNG, GIF, JPG, TIFF, and PCT,
among others.

[Live Coding in Python]: https://donkirkby.github.io/live-py-plugin/
[svglib]: https://pypi.org/project/svglib/#examples

## Installing
Install it with `pip install svg_turtle`. If you haven't installed Python
packages before, read Brett Cannon's [quick-and-dirty guide].

[quick-and-dirty guide]: https://snarky.ca/a-quick-and-dirty-guide-on-how-to-install-packages-for-python/

## Drawing
Once it's installed, create an `SvgTurtle`, telling it how big to make the SVG
file. Then give it some turtle commands, and save the file.

    from svg_turtle import SvgTurtle
    
    t = SvgTurtle(500, 500)
    t.forward(200)
    t.dot(10)
    t.save_as('example.svg')

## More Information
If you'd like to help out with the project, see the `CONTRIBUTING.md` file in
the source code.
