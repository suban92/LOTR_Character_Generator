# Run ansible playbook.yaml and install docker onto the swarm plus nginx and set up the swarm
cd ansible
ansible-playbook -i inventory playbook.yaml