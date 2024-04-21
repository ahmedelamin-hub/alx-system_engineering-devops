# This manifest uses pip3 to install Flask version 2.1.0

class flask_install {
    package { 'python3-pip':
        ensure => installed,
    }

    # Ensure pip3 is present before installing Flask
    package { 'Flask':
        ensure   => '2.1.0',  # Specify the Flask version to install
        provider => 'pip3',   # Specify the package provider
        require  => Package['python3-pip'],  # Ensures pip3 is installed first
    }
}

include flask_install
