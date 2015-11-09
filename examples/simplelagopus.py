#!/usr/bin/python

"""
Simple example of using Lagopus

This creates a following network:

+-----------+      +-----------+
|           |      |           |
|    s1     +------+    s2     |
| (Lagopus) |      | (Lagopus) |
|           |      |           |
+-----+-----+      +-----+-----+
      |                  |
   +--+-+             +--+-+
   | h1 |             | h2 |
   +----+             +----+

NOTE:
OpenFlow 1.3 controller performing as
Layer 2 switch (e.g: Ryu's simple_switch_13.py) should be
running before starting this.

"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.node import RemoteController
from mininet.node import Lagopus

class SimpleLagopusTopo(Topo):

    def __init__(self):
        "Set Lagopus as a default switch class"
        Topo.__init__(self, sopts={ "cls" : Lagopus })

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')

        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        self.addLink(h1, s1)
        self.addLink(s1, s2)
        self.addLink(s2, h2)

def lagopusTest():
    "Create network with Lagopus and check connections"
    topo = SimpleLagopusTopo()

    """ Set contoroller class in order to
        use external OpenFlow 1.3 controller """
    net = Mininet( topo=topo,
                   controller=RemoteController )

    net.start()

    print "Checking that switches class is Lagopus"
    for s in net.switches:
        print repr(s)

    print "Testing connections"
    net.pingAll()

    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    lagopusTest()



