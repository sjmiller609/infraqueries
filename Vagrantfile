# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

   config.vm.box = "ubuntu/trusty64"
   config.vm.provider "virtualbox" do |vb|
  #   # Customize the amount of memory on the VM:
     vb.memory = "4096"
     vb.cpus = "4"
   end

   config.vm.network "forwarded_port", guest: 1111, host_ip: "127.0.0.1", host: 1111

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
   config.vm.provision "shell", inline: <<-SHELL

     apt-get update
     # install build essential
     apt-get install -y build-essential
     # install some coding utilities
     apt-get install -y tree nmap

     # install python stuff
     apt-get install -y python-pip python-virtualenv
     pip install --upgrade virtualenv

     #deployment modules
     pip install s3-deploy-website

   SHELL

   # set up roots, a static site generator available on node
   config.vm.provision "shell", privileged: false, inline: <<-SHELL
     curl -sL https://deb.nodesource.com/setup_8.x > /tmp/setup_8.x.sh
   SHELL

   config.vm.provision "shell", inline: <<-SHELL
     /bin/bash /tmp/setup_8.x.sh
     apt-get install -y nodejs
     npm install npm@latest -g
   SHELL

   config.vm.provision "shell", privileged: false, inline: <<-SHELL
     mkdir "/home/vagrant/npm-packages"
     echo "prefix=/home/vagrant/.npm-packages" >> "/home/vagrant/.npmrc"
     echo 'NPM_PACKAGES="/home/vagrant/.npm-packages"' >> "/home/vagrant/.bashrc"
     echo 'PATH="$NPM_PACKAGES/bin:$PATH"' >> "/home/vagrant/.bashrc"
     echo '# Unset manpath so we can inherit from /etc/manpath via the `manpath` command' >> "/home/vagrant/.bashrc"
     echo 'unset MANPATH # delete if you already modified MANPATH elsewhere in your config' >> "/home/vagrant/.bashrc"
     echo 'export MANPATH="$NPM_PACKAGES/share/man:$(manpath)"' >> "/home/vagrant/.bashrc"
     source /home/vagrant/.bashrc
     npm install -g roots
     cd /vagrant/src/frontend
     npm install acorn --no-bin-links
     npm install
   SHELL
   # done setting up roots

end
