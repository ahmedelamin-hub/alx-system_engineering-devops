#!/usr/bin/env ruby

input_string = ARGV[0]

matches = input_string.scan(/b*/)

matches.each { |match| print "#{match}\n" unless match.empty? }
