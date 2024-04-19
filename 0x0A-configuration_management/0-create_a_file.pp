# create a file named school
file { '/tmp/school':
content => 'I love Puppet',
owner   => 'www-data',
group   => 'www-data',
mode    => '0744',
}
