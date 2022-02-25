# User limit
 taskexec { 'change limit_1':
  command  => 'sed -i "s/holberton file 5/holberton hard nofile 55000/g" /etc/security/limits.conf',
  provider => 'shell'
}

exec { 'change limit_2':
  command  => 'sed -i "s/holberton file 4/holberton soft nofile 55000/g" /etc/security/limits.conf',
  provider => 'shell'
}