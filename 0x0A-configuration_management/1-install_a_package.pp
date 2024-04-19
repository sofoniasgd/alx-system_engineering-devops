# install flask using pip
package { 'flask':
ensure   => 'installed',
provider => 'pip3',
version  => '2.1.0',
}
