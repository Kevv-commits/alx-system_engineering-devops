#Sky is the limit, let's bring that limit higher task
exec { 'fix problem':
  command  => 'sed -i s/15/4096/g /etc/default/nginx; sudo service nginx restart',
  provider => 'shell'
}
