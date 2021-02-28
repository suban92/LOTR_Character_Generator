# Run ansible playbook.yaml and install docker onto the swarm plus nginx and set up the swarm
cd ansible
ansible-playbook playbook.yaml -i inventory.yaml
cd .. 