# Environment Setup

## Intro

We used enp4s0f1 and enp130s0f1 NICs.

Basic usage for ip/ifconfig

```bash
# To see the configuration via ifconfig
ifconfig -a
ifconfig enp4s0f1
ifconfig enp130s0f1

# show NIC
ip link show enp4s0f1
ip link show enp130s0f1

# Show addr
ip addr show enp4s0f1
ip addr show enp130s0f1

# Show stat
ip -s link show enp4s0f

# Configure IP addr
sudo ip addr add 192.168.10.2/24 dev enp4s0f1
sudo ip addr add 192.168.10.3/24 dev enp130s0f1

# Setup
sudo ip link set enp4s0f1 up
sudo ip link set enp130s0f1 up

sudo 

```

## Create separated network namespace

```bash
# Create netns

sudo ip netns add ns1
sudo ip netns add ns2

# NIC 0
sudo ip link set enp4s0f1 netns ns1
sudo ip netns exec ns1 ip addr add 192.168.10.1/24 dev enp4s0f1
sudo ip netns exec ns1 ip link set enp4s0f1 up

# NIC 1
sudo ip link set enp130s0f1 netns ns2
sudo ip netns exec ns2 ip addr add 192.168.10.2/24 dev enp130s0f1
sudo ip netns exec ns2 ip link set enp130s0f1 up

# Test it 
sudo ip netns exec ns2 ip -s link show enp130s0f1 
sudo ip netns exec ns1 ping 192.168.10.2 -c 10
sudo ip netns exec ns2 ip -s link show enp130s0f1 


# Remove netns
sudo ip netns del ns1
sudo ip netns del ns2

sudo ip netns exec ns1 bash
sudo ip netns exec ns2 bash

```
