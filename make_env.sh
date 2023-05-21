python3 -m venv tmp
source tmp/bin/activate
pip install -r requirments.txt
./tmp/bin/pip install pipdeptree
./tmp/bin/pip install graphviz
./tmp/bin/python -m pipdeptree --graph-output png > dependencies.png
deactivate
rm -rf tmp