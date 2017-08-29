export PATH="/home/ubuntu/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
pyenv install 2.7.13
pyenv local 2.7.13
pip install virtualenv
rm -rf venv
virtualenv venv --always-copy
source venv/bin/activate
pip install python-lambda
