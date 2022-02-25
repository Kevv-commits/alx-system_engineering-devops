# User limit
exec { 'change limit_1':
  command  => 'sudo sed -i 's/holberton hard nofile 5/holberton hard nofile 88888/g'  /etc/security/limits.conf',
  provider => 'shell'
}
exec { 'change limit_2':
  command  => 'sudo sed -i 's/holberton soft nofile 4/holberton soft nofile 88888/g'  /etc/security/limits.conf',
  provider => 'shell'
}
