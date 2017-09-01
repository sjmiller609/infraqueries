# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

   config.vm.box = "ubuntu/xenial64"
   config.vm.provider "virtualbox" do |vb|
  #   # Customize the amount of memory on the VM:
     vb.memory = "4096"
     vb.cpus = "4"
   end

   config.vm.network "forwarded_port", guest: 1111, host_ip: "127.0.0.1", host: 1111

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.

   config.vm.provision "shell", run: "always", inline: <<-SHELL
     apt-get update
     # install build essential
     apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev

     # install some coding utilities
     apt-get install -y tree nmap git

     #stuff for node
     #curl -sL https://deb.nodesource.com/setup_8.x > /tmp/setup_8.x.sh
     #/bin/bash /tmp/setup_8.x.sh
     #apt-get install -y nodejs

     #mkdir -p "/home/ubuntu/npm-packages"

     #echo 'prefix=/home/ubuntu/.npm-packages' 		      >> /home/ubuntu/.bashrc
     #echo 'export NPM_PACKAGES=/home/ubuntu/.npm-packages'    >> /home/ubuntu/.bashrc
     #echo 'export PATH=$NPM_PACKAGES/bin:$PATH'               >> /home/ubuntu/.bashrc
     #echo 'export MANPATH=$NPM_PACKAGES/share/man:$(manpath)' >> /home/ubuntu/.bashrc

     #source /home/ubuntu/.bashrc

     #npm install npm@latest -g
     #npm install --no-bin-links acorn
     #npm install -g roots

     #chown -R ubuntu:ubuntu /home/ubuntu/

   SHELL

   config.vm.provision "shell", privileged: false, inline: <<-SHELL

     cd /vagrant/src/frontend

     ## installing python stuff
     curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
     export PATH="/home/ubuntu/.pyenv/bin:$PATH"
     eval "$(pyenv init -)"
     eval "$(pyenv virtualenv-init -)"
     pyenv install 2.7.13
     pyenv local 2.7.13
     pip install virtualenv
     cd /vagrant/src/infraqueries/vmstatus
     virtualenv env --always-copy
     source env/bin/activate
     pip install python-lambda
     
   SHELL

end
