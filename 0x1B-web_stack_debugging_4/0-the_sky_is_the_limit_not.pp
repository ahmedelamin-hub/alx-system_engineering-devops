```puppet
# This Puppet manifest configures Nginx
exec { 'fix-nginx':
  command => '/usr/sbin/nginx -s reload',
  refreshonly => true,
}

file { '/etc/nginx/nginx.conf':
  ensure  => file,
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  content => template('nginx/nginx.conf.erb'),
  notify  => Exec['fix-nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  content => template('nginx/default.erb'),
  notify  => Exec['fix-nginx'],
}

file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  notify => Exec['fix-nginx'],
}
