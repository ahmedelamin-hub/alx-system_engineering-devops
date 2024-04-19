# This manifest creates a file at /tmp/school with specified properties and content

file { '/tmp/school':
  ensure  => file,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => "I love Puppet\n", # Ensure the file ends with a new line
}
