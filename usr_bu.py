#!/usr/bin/python

import os
import subprocess
import platform
import time

date = time.strftime("%Y-%m-%d")

operating_system = platform.platform()
computer_name = platform.node()

if computer_name.endswith('.local'):
    computer_name = computer_name.split('.')[0]
else:
    pass

osx_tar_path = '/usr/bin/tar'
linux_tar_path = '/bin/tar'
osx_destination = '/Volumes/FIN_SHARE/0-FINI_JOBS/0000_ENGINEERING/_BUs/'
linux_destination = '/mnt/FIN_SHARE/0-FINI_JOBS/0000_ENGINEERING/_BUs/'

if 'Darwin' in operating_system:
    tar_path = osx_tar_path
    destination = osx_destination
else:
    tar_path = linux_tar_path
    destination = linux_destination

rsync_path = '/usr/bin/rsync'

tar_options = '-zcvf'
tar_extension = '.tar.gz'



### paths to tar and backup
log = '/usr/discreet/log'
project = '/usr/discreet/project'
user = '/usr/discreet/user'
clip = '/usr/discreet/clip'
archive = '/usr/discreet/archive'
swdb = '/usr/discreet/sw/swdb'
network = '/usr/discreet/cfg/network.cfg'
stonewire = '/usr/discreet/sw/cfg'
### path to rsync
rsync_folder = '/usr/discreet'

archive_name = '{0}{1}_{2}{3}'.format(destination, date, computer_name, tar_extension)


### rsync server info
rsync_server_user = 'joint'
rsync_server_ip = '10.99.0.232'
rsync_destination_path = '/tank/backups'
rsync_ssh_string = '{0}@{1}:{2}/{3}'.format(rsync_server_user, rsync_server_ip, rsync_destination_path, computer_name)



print 'stopping wire'
subprocess.call(['/usr/discreet/sw/sw_stop'])
time.sleep(30)
print 'starting backup'
subprocess.call([tar_path, tar_options, archive_name, project, clip, archive, swdb, network, stonewire])
time.sleep(30)
subprocess.call([rsync_path, '-avP', '--delete', '-e', 'ssh', rsync_folder, rsync_ssh_string])
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
"""
