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

	# run `cd /home/` on each host to navigate to private dirs on startup
        for host in net.hosts:
		host.cmd('cd /home/')
	
	print "**********\nFinished setting up and testing.\n**********\n"
	app = consoles.ConsoleApp(net, width=4)
	app.mainloop()

	# CLI(net)        #start CLI after user quits consoles

	net.stop()

if __name__ == '__main__':
	setLogLevel('info')
	startNet()
