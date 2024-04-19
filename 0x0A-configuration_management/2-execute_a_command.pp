exec { 'kill a process':
command => 'pkill -9 -f killmenow',
path    => '/usr/bin',
}
