#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c1=net.addController(name='c1',
                      controller=RemoteController,
                      ip='127.0.0.1',
                      protocol='tcp',
                      port=6634)

    c0=net.addController(name='c0',
                      controller=RemoteController,
                      ip='127.0.0.1',
                      protocol='tcp',
                      port=6633)

    c2=net.addController(name='c2',
                      controller=RemoteController,
                      ip='127.0.0.1',
                      protocol='tcp',
                      port=6635)

    info( '*** Add switches\n')
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch, dpid='0000000000000006')
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch, dpid='0000000000000004')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch, dpid='0000000000000001')
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch, dpid='0000000000000002')
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch, dpid='0000000000000003')
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch, dpid='0000000000000005')

    info( '*** Add hosts\n')
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2/24', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4/24', defaultRoute=None)
    h12 = net.addHost('h12', cls=Host, ip='10.0.2.12/24', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3/24', defaultRoute=None)
    h9 = net.addHost('h9', cls=Host, ip='10.0.2.9/24', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1/24', defaultRoute=None)
    h10 = net.addHost('h10', cls=Host, ip='10.0.2.10/24', defaultRoute=None)
    h11 = net.addHost('h11', cls=Host, ip='10.0.2.11/24', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.0.1.6/24', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.0.1.7/24', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.0.1.8/24', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.0.1.5/24', defaultRoute=None)

    info( '*** Add links\n')
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s2)
    net.addLink(h4, s2)
    net.addLink(h5, s3)
    net.addLink(h6, s3)
    net.addLink(h7, s4)
    net.addLink(h8, s4)
    net.addLink(s1, s2)
    net.addLink(s3, s4)
    net.addLink(s5, s6)
    net.addLink(h9, s5)
    net.addLink(h10, s5)
    net.addLink(h11, s6)
    net.addLink(h12, s6)
    net.addLink(s2, s3)
    net.addLink(s4, s5)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s6').start([c2])
    net.get('s4').start([c1])
    net.get('s1').start([c0])
    net.get('s2').start([c0])
    net.get('s3').start([c1])
    net.get('s5').start([c2])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()
