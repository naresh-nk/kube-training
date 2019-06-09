# Install Kubernetes Cluster
Ansible playbooks to install multinode Kubernetes cluster in below environment 

* Behind proxy server
* Without proxy server

## Getting Started

Clone git repository
```
git clone https://github.com/bishnoink/kube-training.git .
```

## Update hosts inventory file with node details in your setup
```
vi ansible/hosts


[master]
master01 ansible_host=192.168.20.51 ansible_user=root

[workers]
worker01 ansible_host=192.168.20.52 ansible_user=root
worker02 ansible_host=192.168.20.53 ansible_user=root
```

## Update 'ansible/group_vars/all.yml' variable file with proxy details.
**If there is no proxy in your environment then skip this step.**
```
vi ansible/group_vars/all.yml

# Reset exisintg cluster
## If below variable is set to true then entire exiting cluster config will be deleted
reset_cluster: true

#Proxy server
proxy_setup: False

#Configure below proxy configs      when: {{ proxy_setup }} is set to True

#proxy_server: "http://web-proxy.server.net:8080"
#proxy_env:
#  http_proxy: http://web-proxy.server.net:8080
#  https_proxy: http://web-proxy.server.net:8080
#  no_proxy: <localnet_IP>,localhost


# Kubernetes
reset_cluster: true
kube_version: v1.14.2
token: yd6643.0xuwzrquyhh6cjj1
pod_network_cidr: 10.244.0.0/16

master_ip: "{{ hostvars[groups['master'][0]]['ansible_default_ipv4'].address | default(groups['master'][0]) }}"

```
## Prepare all nodes for installation
```
cd ansible/
ansible-playbook -i hosts prepare-cluster.yml

```
## Initialize cluster and join worker nodes into cluster
```
ansible-playbook -i hosts init-cluster.yml

```
## Validate play-recap output it should look similar to:

```

PLAY RECAP ********************************************************************************************************************
master01                   : ok=11   changed=6    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0   
worker01                   : ok=4    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
worker02                   : ok=4    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

## Check cluster status
Login to master node

```
ssh root@master01
su - kube

[kube@master01 ~]$ kubectl get nodes
NAME       STATUS   ROLES    AGE     VERSION
master01   Ready    master   3m45s   v1.14.3
worker01   Ready    <none>   3m25s   v1.14.3
worker02   Ready    <none>   3m24s   v1.14.3

```
## Copy kube config from master node to local machine/laptop to manage k8 cluster remotely
```
mkdir ~/.kube
scp root@master01:/home/kube/.kube/config ~/.kube/
```

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE](LICENSE) file for details

## Acknowledgments