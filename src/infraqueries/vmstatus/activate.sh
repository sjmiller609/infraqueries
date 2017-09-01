
export PATH="/home/ubuntu/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
pyenv local 2.7.13
cd /vagrant/src/infraqueries/vmstatus
if [ ! -d ./env ]; then
    virtualenv env --always-copy
    env/bin/pip install python-lambda
fi
source env/bin/activate
