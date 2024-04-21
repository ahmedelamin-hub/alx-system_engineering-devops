# Puppet manifest to kill a process named 'killmenow'

exec { 'killmenow':
  command   => '/usr/bin/pkill -f killmenow',
  path      => ['/bin', '/usr/bin'],
  provider  => shell,
  onlyif    => "/usr/bin/pgrep -f killmenow",
}
