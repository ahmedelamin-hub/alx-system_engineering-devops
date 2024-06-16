# Adjust the maximum number of open files for Nginx and restart the service

exec { 'adjust_nginx_open_files_limit':
  # Modify the configuration file to set the max open files limit to 10000
  command => 'sed -i "s/15/10000/" /etc/default/nginx && sudo service nginx restart',
  # Define the search path for command execution
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games',
}

