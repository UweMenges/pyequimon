from django.db import models
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext as _

class Vendor(models.Model):
    name = models.CharField # TODO: vendor -> logo file/url mapping?

class Architecture(models.Model):
    name = models.CharField

class Location(models.Model):
    name = models.CharField # TODO: split this into roomlist/freetext fields: "Room" + "Row/Rack#Unit"
    
# A host/machine entry. Legacy DB fields:
# CREATE TABLE machines(
#   id INTEGER PRIMARY KEY NOT NULL,
#   hostname VARCHAR( 20 ) UNIQUE,
#   groupname VARCHAR( 20 ),
#   lastupdate INTEGER, updateby INTEGER,
#   vendor VARCHAR( 20 ), model VARCHAR( 40 ),
#   state INTEGER,
#   arch VARCHAR( 8 ),
#   assettag VARCHAR( 40 ),
#   expiredate DATE, expirestate INTEGER,
#   ip VARCHAR( 20 ), mac VARCHAR( 20 ),
#   monfiles_data TEXT,
#   room VARCHAR( 20 ),
#   cpu VARCHAR( 20 ), os VARCHAR( 20 ), mem VARCHAR( 20 ),
#   disk VARCHAR( 20 ), kernel VARCHAR( 20 ), libc VARCHAR( 20 ), compiler VARCHAR( 20 ),
#   usedby VARCHAR( 40 ), usedby_id1 INTEGER, usedby_id2 INTEGER,
#   notes TEXT, rack INTEGER, hostsystem VARCHAR( 20 ), lastping INTEGER,
#   mailtarget VARCHAR( 40 ), mailopts INTEGER,
#   wbem_info VARCHAR( 20 ), wbem_lastupdate INTEGER,
#   remoteadm INTEGER , groupid integer not null default 1, owner integer,
#   equipment_nr VARCHAR (40), serial_nr VARCHAR(40),
#   costcenter VARCHAR(40), tech_c varchar(40));

USED_CHOICES = (('0', _("Free")),
                ('1', _("In use")))

MAIL_CHOICES = (('0', _("Don't mail on connectivity changes")),
                ('1', _("Send mail on connectivity changes")))

def getIP:
""" gethostbyname() replacement - get IP from DNS (OS). """ 
#pprint.PrettyPrinter(indent=2).pprint(socket.getaddrinfo('timehost', None, socket.AF_INET, 0, socket.SOL_TCP, socket.AI_CANONNAME))
#socket.getaddrinfo('timehost', None, socket.AF_INET, 0, socket.SOL_TCP, socket.AI_CANONNAME)
# TODO: return a default value for use in GenericIPAddressField(default=...), with warning check (rDNS doesn't match, multiple IPs returned) 
    return None


class Host(models.Model):
    # host data, invariant
    vendor = models.ForeignKey('Vendor')
    model = models.CharField
    arch = models.ForeignKey('Architecture')
    assettag = models.CharField
    serial_nr = models.CharField
    mac = models.CharField(max_lenght=18, unique=True)
    cpu = models.CharField
    mem = models.IntegerField

    # host data, variable
    hostname = models.CharField(max_length=255, help_text=_("The DNS host name as per RFC1123")) # RFC1123/2.1: SHOULD handle up to 255 chars
    ip = models.GenericIPAddressField(default=help_text=_("IP address, automatically set from DNS"))
    location = models.ForeignKey('Location')
    equipment_nr = models.CharField
    notes = models.CharField(help_text=_("Task/usage of this host. This string will also be included in the host's motd."))
    #sysinfo - maybe use an extra object/table for extended information

    # host organizational metadata, admin/management layer
    owner = models.ForeignKey(User)
    group = models.ForeignKey(Group)
    used = models.PositiveSmallIntegerField(choices=USED_CHOICES)
    usedby = models.ForeignKey(User) # TODO: make this a list of Users
    costcenter = models.CharField
    tech_c = models.ForeignKey(User, help_text=_("Technical responsible person"))
    expiredate = models.DateTimeField
    #expired = models.BooleanField(editable=False) # This is basically a cache; premature optimization omitted
    lastupdate = models.DateTimeField(auto_now=True)
    lastupdateby = models.ForeignKey(User, editable=False) # TODO: automatically set this 
    mailtarget = models.EmailField
    mail_notify = models.PositiveSmallIntegerField(choices=MAIL_CHOICES)
    remoteadm = models.CharField(help_text=_("URL, or a short hint on how to access remote management"))
    
    # TODO: related_hosts = { list of hosts } - eg. hypervisor/virtualmachine, or cluster nodes 
