Vagrant.configure("2") do |config|
	config.vm.define "linux1" do |linux1|
		linux1.vm.box = "generic/alpine318"
		linux1.vm.network "private_network", ip: "192.168.56.42", auto_config: true
		linux1.vm.synced_folder ".", "/vagrant", disabled: true
		linux1.vm.provider "virtualbox" do |vb|
			vb.name = 'Alpine1'
			vb.cpus = 1
			vb.memory = 1024
		end
	end
	config.vm.define "linux2" do |linux2|
		linux2.vm.box = "generic/alpine318"
		linux2.vm.network "private_network", ip: "192.168.56.43", auto_config: true
		linux2.vm.synced_folder ".", "/vagrant", disabled: true
		linux2.vm.provider "virtualbox" do |vb|
			vb.name = 'Alpine2'
			vb.cpus = 1
			vb.memory = 1024
			linux2.vm.provision "shell", inline: <<-SHELL
			apk update
			apk add docker
			rc-update add docker boot
			service docker start
		SHELL
		end
	end
end