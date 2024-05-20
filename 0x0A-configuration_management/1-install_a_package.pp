#!/usr/bin/pup
# install flask using puppet
package {'flask':
  ensure   =>'2.1.0',
  provider =>'pip3'
}
package { 'Werkzeug':
  ensure   => '2.1.1',  # Specify the version required by Flask 2.1.0
  provider => 'pip3',
}
