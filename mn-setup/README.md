## Synopsis

This directory contains the files to set up and test a small SDN running in a Mininet instance.

## Installation

### Pre-requisites

Running this test bed assumes you have the following items installed on your local machine.

  * [Mininet](http://mininet.org/download)

  * [Floodlight](https://floodlight.atlassian.net/wiki/spaces/floodlightcontroller/pages/1343544/Installation+Guide)

### Test-bed Setup

1. Log into the Mininet VM either from SSH or in the VM itself.  I find it easier to SSH, as I usually have a few terminals into the Mininet VM open at a time.  I set up my VM to enable port forwarding with the instructions given [here](https://github.com/mininet/openflow-tutorial/wiki/VirtualBox-specific-Instructions).  Then, I use the command below to SSH into the VM.
  * `ssh -Y -l mininet -p2222 localhost`

2. Navigate into the `mininet` directory from the home directory (the home directory is also `mininet`).  Type `git clone https://github.com/mgottsacker34/mtd-research.git` to copy these files to your VM.

3. From the `mn-setup` directory, type `hostfiles/setup.sh` to run the setup script.  This script creates the private directories for each host that are used when the virtual network runs.  Additionally, it copies the simple timer.sh script into each VM's working /home/ directory.

4. Run Floodlight from the command line using `ant` in your Floodlight directory and then `java -jar target/floodlight`.  Alternatively, run it from your IDE's built-in tools.

5. In the Mininet VM, run `sudo route -n`.  Note the IP address listed under the `Gateway` field for the entry with the `UG` flags shown.  This address is the one with which your VM communicates to your local computer and thus, the Floodlight controller.

## Running the Test-bed
1. Type `sudo python create-net.py` from the `mn-setup` directory in the VM.  This script creates the network test-bed with 10 hosts and spawns virtual terminals to interact with every virtualized network device.

2. That's it!  You can run commands in different terminals just by clicking in each of them.  Type `/timer.sh` on a few hosts to run the basic timer script.  It should print out its process ID and the current date and time every 3 seconds.
  * Note: Each host has its own private directories, but they still have access to the same underlying VM.  For illustration, type `ps -a` on a host after starting `timer.sh` on a few others.  You will see every process running.

To tear down the network, click the "Exit" button from the terminal app's top menu bar.
