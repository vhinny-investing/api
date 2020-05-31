echo "Removing old distribution"
rm -r dist;
echo "Creating new distribution"
python setup.py sdist bdist_wheel;
echo "Updateing PyPI..."
python -m twine upload dist/*

