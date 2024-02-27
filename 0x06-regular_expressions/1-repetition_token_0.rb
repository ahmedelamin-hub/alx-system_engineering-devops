#!/usr/bin/env

input_string = ARGV[0]
matches = input_string.scan(/h+/)
matches.each { |match| print "#{match}\n" }
