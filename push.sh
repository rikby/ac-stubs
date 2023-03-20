# @see https://www.freecodecamp.org/news/build-your-first-python-package/
python setup.py sdist bdist_wheel
while true; do
    read -p "Do you wish to push built package to PyPi? [y/n] " yn
    case $yn in
        [Yy]* )
          twine upload --repository ac-stubs dist/*
          break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done