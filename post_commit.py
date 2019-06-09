#!/usr/bin/env python3
from os.path import isfile

from semantic_versioning import Version

try:
    if isfile('VERSION'):
        with open('VERSION', 'r+') as f:
            content = f.read()
            version = Version(content)
            version.patch += 1
            f.seek(0)
            f.truncate()
            f.write(str(version))
    else:
        with open('VERSION', 'w') as f:
            f.write('1.0.1')
except TypeError:
    print('{} is not a valid version'.format(content))
