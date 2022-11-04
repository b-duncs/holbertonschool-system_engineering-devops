#!/usr/bin/puppet
# set up your client SSH configuration file so that you can connect to a server without typing a password

file_line { 'indentity_file':
  ensure => present,
  line   => 'IdentityFile ~/.ssh/school',
  path   => '/etc/ssh/ssh_config',
}

file_line { 'pwd_aut':
  ensure => present,
  line   => 'PasswordAuthentication no',
  path   => '/etc/ssh/ssh_config',
}
