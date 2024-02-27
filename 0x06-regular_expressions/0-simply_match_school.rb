#!/usr/bin/env
input_string = ARGV[0]
matches = input_string.scan(/School/)
matches.each { |match| print "#{match}$" }
puts
