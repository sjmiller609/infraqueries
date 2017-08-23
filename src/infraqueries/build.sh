source ~/eb-virt/bin/activate
pip freeze > requirements.txt
echo "=========="
cat requirements.txt
echo "=========="
~/.local/bin/eb use flask-env
~/.local/bin/eb deploy
