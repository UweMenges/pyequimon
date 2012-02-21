from django.db import models

# Create your models here.

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

class Host(models.Model):
    name = models.CharField(max_length=255) # RFC1123/2.1: SHOULD handle up to 255 chars
    
    