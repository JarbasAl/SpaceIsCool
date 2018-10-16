#!/usr/bin/env bash
mkdir docs
python py2md.py --sourcedir space --docfile docs/space.md
python py2md.py --sourcedir space/research --docfile docs/research.md
python py2md.py --sourcedir space/bodies --docfile docs/bodies.md
python py2md.py --sourcedir space/satellites --docfile docs/satellites.md
python py2md.py --sourcedir space/imagery --docfile docs/imagery.md

