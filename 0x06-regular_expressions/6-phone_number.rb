#!/usr/bin/env ruby
input_string = ARGV[0]
puts input_string.scan(/^\d{10}$/).join
