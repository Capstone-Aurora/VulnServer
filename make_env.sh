rm -rf finish
rm -rf ../../../var/www/html/dependencies.png
python3 -m venv tmp
#source tmp/bin/activate
./tmp/bin/pip install -r requirments.txt
./tmp/bin/pip install pipdeptree
./tmp/bin/pip install graphviz
./tmp/bin/python -m pipdeptree --exclude pipdeptree,graphviz --graph-output png > ../../../var/www/html/dependencies.png
echo "done" >> finish
rm -rf tmp