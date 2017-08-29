if [ $# -eq 0 ]
then
echo -n "enter name for service: "
read servicename
else
export servicename=$1
fi
mkdir $servicename
cd $servicename

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

lambda init

echo 'region: us-west-2' > config.yaml
echo "function_name: $servicename" >> config.yaml
echo 'handler: service.handler' >> config.yaml
echo 'description: no description' >> config.yaml
echo 'runtime: python2.7' >> config.yaml

echo 'rm -rf venv' >> activate.sh
echo 'virtualenv venv --always-copy' >> activate.sh
echo 'source venv/bin/activate' >> activate.sh
echo 'pip install python-lambda' >> activate.sh

echo 'venv/*' >> .gitignore
echo '__pycache__' >> .gitignore
echo '*.pyc' >> .gitignore
echo 'dist' >> .gitignore
