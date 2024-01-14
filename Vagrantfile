Vagrant.configure("2") do |config|
	config.vm.box = "generic/alpine318"
	config.vm.network "public_network", ip: "192.168.1.31", auto_config: true
	config.vm.synced_folder ".", "/vagrant", disabled: true
	config.vm.provider "virtualbox" do |vb|
	  vb.name = 'Alpine1'
	  vb.cpus = 1
	  vb.memory = 1024
	  # vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
	  # Display the VirtualBox GUI when booting the machine
	  # vb.gui = true
	end
	config.vm.provision "shell", inline: <<-SHELL
		echo http://dl-3.alpinelinux.org/alpine/edge/main >> /etc/apk/repositories
		echo http://dl-3.alpinelinux.org/alpine/edge/community >> /etc/apk/repositories
		apk update
		apk add docker
		rc-update add docker boot
		service docker start
	SHELL
end