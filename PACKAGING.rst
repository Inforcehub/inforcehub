.. :packaging:

Packaging
---------

Manual preparation of packages to upload to PYPI.


Preparing packages::

    python setup.py sdist bdist_wheel


Uploading to PYPI.org::

    twine upload --skip-existing dist/*
