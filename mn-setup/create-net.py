#!/usr/bin/python
# import consoles.py to interact with hosts
import sys
sys.path.insert(0, '/home/mininet/mininet/examples')
import consoles

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from functools import partial
from mininet.node import RemoteController
from mininet.util import dumpNodeConnections, pmonitor
from mininet.log import setLogLevel, info
from mininet.node import Host

class MTDNetwork(Topo):
	# Single switch connected to 10 hosts (as default)
	def build(self, n=10):
		hosts = []
		for i in range(0,n):
			# create private persistent dirs for each host at ./proj/<hostname>
			# also create temporary dir at /var/mn on host
			privateDirs = [ ('/var/log', './hostfiles/%(name)s/var/log'),
					('/var/run', './hostfiles/%(name)s/var/run'),
					('/home/', './hostfiles/%(name)s/'),
					 '/var/mn' ]
			hosts.append(self.addHost('h%d' % (i+1), privateDirs=privateDirs))
			
		s1 = self.addSwitch('s1')
		for h in hosts:
			self.addLink(h,s1)
		
def startNet():
	info("Creating and testing network...\n")
	topo = MTDNetwork()
	info("Creating network...\n")
	net = Mininet(topo=topo, controller=None)
	ctlIP = sys.argv[1]
	ctlPort = int(sys.argv[2])
	info("Adding external controller with IP %s on port %d...\n" % (ctlIP, ctlPort))
	c0 = net.addController('c0', controller=RemoteController, ip=ctlIP, port=ctlPort)
	net.start()
	info("Dumping host connections...\n")
	dumpNodeConnections(net.hosts)
	info("Testing network connectivity...\n")
	net.pingAll()

	# run `cd /home/` on each host
        for host in net.hosts:
		host.cmd('cd /home/')

	# create dict to fill with hostnames and respective PIDs
	#popens = {}
	# run timer.sh process on first four hosts
	#numActiveHosts = 4
	#activeHosts = []
	#for i in range(0,numActiveHosts):
	#	activeHosts.append(net.get('h%d' % (i+1)))
	#for host in activeHosts:
	#	print "Starting timer.sh"
	#	popens[host] = host.popen('/home/timer.sh')

	# monitor hosts and print respective outputs
	#for host, line in pmonitor(popens):
	#	if host:
	#		info("<%s>: %s" % (host.name, line))
	
	print "**********\nFinished setting up and testing.\n**********\n"
	# CLI(net)
	app = consoles.ConsoleApp(net, width=4)
	app.mainloop()
	net.stop()

if __name__ == '__main__':
	setLogLevel('info')
	startNet()
