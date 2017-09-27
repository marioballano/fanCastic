#!/bin/bash 
rm -rf build dist
pyinstaller fancastic-osx.spec
pushd ./dist/
zip -r fancastic-osx.zip fancastic.app/ 
popd
