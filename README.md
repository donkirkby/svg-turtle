# SaVaGe Turtle
### Use the Python turtle to write SVG files
If you're using the Python turtle module to teach students, or you just like
using the turtle module yourself, this module can save the images from a turtle
script as SVG files. Experiment with your turtle code using the regular turtle
or the [Live Coding in Python] plugin for PyCharm, then pass an `SvgTurtle` to
the same code, and save it as an SVG file.

[Live Coding in Python]: https://donkirkby.github.io/live-py-plugin/

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
