#/bin/bash

# regenerate .whl
echo "re-build .whl file ....................................."
echo

rm -rf build dist TLUtils.egg-info
python setup.py bdist_egg --universal


echo
echo "re-build .whl file complete."
echo

# git update
if [ "$1" == "git" ]
then
echo "github update .........................................."
echo

git add -A
git commit -m "normal update"
git push

echo 
echo "github update complete."
echo
fi

#
echo "re-install TLUtils ....................................."
echo
# cd ..
which pip
pip uninstall TLUtils
# cd TLUtils
pip install --user dist/TLUtils-0.1.0-py2.py3-none-any.whl

echo
echo "re-install TLUtils complete."
echo

echo "all done."
