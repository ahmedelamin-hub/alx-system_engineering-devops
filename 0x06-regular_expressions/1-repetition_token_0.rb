#!/usr/bin/env ruby

input_string = ARGV[0]
matches = input_string.scan(/h+/)
matches.each { |match| print "#{match}\n" }
