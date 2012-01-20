#from django.db import models

# hier nur so tun als ob wir model wären - aber nicht von models.model erben weil kein DB zugriff

# DHCP/PXE satellite of pyequimon
# Used for controlling boot and autodeployment for PXE clients
# Tasks:
#   write dhcpd.conf & restart dhcpd
#   receive/manage kernel+initrd for autodepyloyment
#
#   needs to be able to manage more than 1 IP-net on 1 physical net
#   maybe can also work as offloading unit for pyequimon master (ping/alive check)