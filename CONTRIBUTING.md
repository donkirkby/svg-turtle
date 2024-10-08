# Contributing to the SVG Turtle Project
If you like this project and want to make it better, please help out. It could
be as simple as sending [@donkirkby] a nice note on Twitter, you could report a
bug, or pitch in with some development work.

[@donkirkby]: https://twitter.com/donkirkby

## Bug Reports and Enhancement Requests
Please create issue descriptions [on GitHub][issues]. Be as specific as possible.
Which version are you using? What did you do? What did you expect to happen? Are
you planning to submit your own fix in a pull request? Please include an SVG
file or a code sample if it helps explain the problem.

[issues]: https://github.com/donkirkby/svg-turtle/issues?state=open

## Building a Release
Releasing a new version means publishing it on the [Python package index] where
pip can find it. The details are at [packaging.python.org], but the main steps
are:

1. Update the version number in `svg_turtle/about.py` and development status
   in `setup.py`.
2. Activate the project's Python virtual environment.

        . .tox/py39/bin/activate

3. Temporarily install the build tools using pip.

        python -m pip install --upgrade setuptools wheel twine

4. Build the release files.

        python setup.py sdist bdist_wheel

5. Upload the release to PyPI. You'll need a user name and password.

        ls dist/*
        twine upload dist/*

6. Check that the new version is on the [package page], and try installing it.

        pip install --no-cache svg_turtle

7. Remove the uploaded files, deactivate the virtual environment, and remove the
   extra packages.

        rm dist/*
        deactivate
        tox -re py39

8. Commit the version number changes, push, and create a release on GitHub.

[packaging.python.org]: https://packaging.python.org/tutorials/packaging-projects/
[package page]: https://pypi.org/project/svg_turtle/


[Python package index]: https://pypi.org/

## Testing GitHub Pages locally
The web site uses the [Bulma Clean theme], which is based on [Bulma]. The
[Bulma colours] can be particularly helpful to learn about.

GitHub generates all the web pages from markdown files, but it can be useful to
test out that process before you commit changes. See the detailed instructions
for setting up [Jekyll], but the main command is this:

    cd docs
    bundle exec jekyll serve

[Bulma Clean theme]: https://github.com/chrisrhymes/bulma-clean-theme
[Bulma]: https://bulma.io/documentation/
[Bulma colours]: https://bulma.io/documentation/overview/colors/
[Jekyll]: https://help.github.com/en/github/working-with-github-pages/testing-your-github-pages-site-locally-with-jekyll
