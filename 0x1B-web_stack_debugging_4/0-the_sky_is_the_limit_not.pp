# This Puppet manifest configures Nginx to handle high load by optimizing worker processes and connections.

file { '/etc/nginx/nginx.conf':
  ensure  => file,
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  content => template('nginx/nginx.conf.erb'),
  notify  => Exec['reload-nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  content => template('nginx/default.erb'),
  notify  => Exec['reload-nginx'],
}

exec { 'reload-nginx':
  command     => '/usr/sbin/nginx -s reload',
  refreshonly => true,
}
