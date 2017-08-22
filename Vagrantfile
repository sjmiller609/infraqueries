# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

   config.vm.box = "ubuntu/trusty64"
   config.vm.provider "virtualbox" do |vb|
  #   # Customize the amount of memory on the VM:
     vb.memory = "4096"
     vb.cpus = "4"
   end

   config.vm.synced_folder "./src/", "/home/vagrant/src"
   config.vm.network "forwarded_port", guest: 5000, host_ip: "127.0.0.1", host: 5000

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
   config.vm.provision "shell", inline: <<-SHELL
     apt-get update
     apt-get install -y build-essential
     apt-get install -y nmap git python-pip python-virtualenv
     pip install --upgrade virtualenv
   SHELL

   config.vm.provision "shell", privileged: false, inline: <<-SHELL
     pip install --upgrade --user awsebcli
     virtualenv ~/eb-virt
     source ~/eb-virt/bin/activate
     pip install flask flask-cors
   SHELL

end
