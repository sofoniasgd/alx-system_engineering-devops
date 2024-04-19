exec { 'kill a process':
command => 'pkill killmenow',
path    => '/usr/bin'
}
