#!/usr/bin/python

import os
import subprocess
import platform
import time

date = time.strftime("%Y-%m-%d")

computer_name = platform.node()
platform = platform.platform()

osx_tar_path = '/usr/bin/tar'


tar_options = '-zcvf'

tar_extension = '.tar.gz'

tar_path = '/usr/bin/tar'

### paths to backup
log = '/usr/discreet/log'
project = '/usr/discreet/project'
user = '/usr/discreet/user'
clip = '/usr/discreet/clip'
archive = '/usr/discreet/archive'
swdb = '/usr/discreet/sw/swdb'
network = '/usr/discreet/cfg/network.cfg'
stonewire = '/usr/discreet/sw/cfg'

### osx destination
destination = '/Volumes/FIN_SHARE/0-FINI_JOBS/0000_ENGINEERING/_BUs/'

### linux destination
# destination = '/mnt/FIN_SHARE/0-FINI_JOBS/0000_ENGINEERING/_BUs/'

archive_name = '{}{}_{}{}'.format(destination, date, computer_name, tar_extension)
print archive_name


print 'stopping wire'
subprocess.call(['/usr/discreet/sw/sw_stop'])
time.sleep(30)
print 'starting backup'
subprocess.call([tar_path, tar_options, archive_name, project, clip, archive, swdb, network, stonewire])
time.sleep(30)
print 'starting wire'
subprocess.call(['/usr/discreet/sw/sw_start'])

"""
def check_if_fin_share_is_mounted():
    if os.path.isdir(destination):
        print "FIN_SHARE is mounted"
    else:
        print "FIN_SHARE is not mounted"


check_if_fin_share_is_mounted()


if 'Darwin' in platform:
    print "this is a mac"
    tar_path = osx_tar_path
else:
    print "this is linux"
    tar_path = linux_tar_path
    print tar_path
"""
