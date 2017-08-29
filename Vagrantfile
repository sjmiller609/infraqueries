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
     apt-get install -y build-essential libbz2-dev libssl-dev libreadline-dev \
                             libsqlite3-dev tk-dev virtualenv
     
     # optional scientific package headers (for Numpy, Matplotlib, SciPy, etc.)
     sudo apt-get install -y libpng-dev libfreetype6-dev 
     # install some coding utilities
     apt-get install -y tree nmap

     #stuff for node
     curl -sL https://deb.nodesource.com/setup_8.x > /tmp/setup_8.x.sh
     /bin/bash /tmp/setup_8.x.sh
     apt-get install -y nodejs
     npm install npm@latest -g
   SHELL

   config.vm.provision "shell", privileged: false, inline: <<-SHELL
     mkdir -p "/home/ubuntu/npm-packages"
     prefix=/home/ubuntu/.npm-packages
     echo 'prefix=/home/ubuntu/.npm-packages' >> "/home/ubuntu/.bashrc"
     export NPM_PACKAGES="/home/ubuntu/.npm-packages"
     echo 'export NPM_PACKAGES=/home/ubuntu/.npm-packages' >> "/home/ubuntu/.bashrc"
     export PATH="$NPM_PACKAGES/bin:$PATH"
     echo 'export PATH=$NPM_PACKAGES/bin:$PATH' >> "/home/ubuntu/.bashrc"
     export MANPATH=$NPM_PACKAGES/share/man:$(manpath)
     echo 'export MANPATH=$NPM_PACKAGES/share/man:$(manpath)' >> "/home/ubuntu/.bashrc"

     npm install -g roots
     cd /vagrant/src/frontend
     npm install acorn --no-bin-links
     npm install

     # installing python stuff
     curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
     export PATH="/home/ubuntu/.pyenv/bin:$PATH"
     eval "$(pyenv init -)"
     eval "$(pyenv virtualenv-init -)"
     pyenv install 2.7.13
     pyenv local 2.7.13
     cd /vagrant/src/infraqueries
     pip install virtualenv
     virtualenv 
     #pip install python-lambda
     
   SHELL

end
