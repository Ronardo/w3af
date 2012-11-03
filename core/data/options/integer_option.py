'''
integer_option.py

Copyright 2008 Andres Riancho

This file is part of w3af, w3af.sourceforge.net .

w3af is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 2 of the License.

w3af is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with w3af; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

'''
from core.controllers.w3afException import w3afException
from core.data.options.baseoption import BaseOption
from core.data.options.option_types import INT


class IntegerOption(BaseOption):
    
    _type = INT
    
    def set_value(self, value):
        '''
        @parameter value: The value parameter is set by the user interface, which
        for example sends 'True' or 'a,b,c'

        Based on the value parameter and the option type, I have to create a nice
        looking object like True or ['a','b','c'].
        '''
        self._value = self.validate(value)
        
    def validate(self, value):
        try:
            return int(value)
        except:
            msg = 'Invalid integer option value "%s".' % value
            raise w3afException(msg)
