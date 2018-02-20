## Synopsis

This repository contains networking code and other files involved in researching moving-target defenses in Software-Defined Network spaces.

The **mn-setup** directory contains code to set up a small SDN in a Mininet instance.

The **net-sim** directory contains code to simulate a 5-node network that processes 100 packets, encountering 1 intrusion for every 12 normal packets. Upon intrusion, it switches the IP address of one of the network nodes at random.
