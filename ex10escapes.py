# These are escape strings python supports. You may not use many of these, but memorize their format and what they do anyway.  Try them out in some strings to see if you can make them work.

# Escape = What it does.

# \\ = Backslash (\)
# \' = Single-quote (')
# \" = Double-quote (")
# \a = ASCII bell (BEL)
# \b = ASCII backspace (BS)
# \f = ASCII formfeed (FF)
# \n = ASCII linefeed (LF)
# \N{name} = Character named name in the Unicode database (Unicode only)
# \r = carriage Return (CR)
# \t = Horizontal Tab (TAB)
# \uxxxx = Character with 16-bit hex value xxxx (Unicode only)
# \Uxxxxxxxx = Character with 32-bit hex value xxxxxxxx (Unicode only)
# \v = ASCII vertical tab (VT)
# \ooo = Character with octal value ooo
# \xhh = Character with hex value hh

# Fun escape code, produces a spinning line
'''while True:
	for i in ["/", "-", "|", "\\", "|"]:
		print "%s\r" % i,
'''

# differemce between %r and %s.  Notice how using %r will show it as you typed it (with quotes) while %s shows it as you might want to see it without the necessary formatting (w/o quotes). Remember %r is for debugging and %s is for displaying
'''print "this is r %r" % "double-quote"
print 'this is r %r' % 'single-quote'
print "this is s %s" % "double-quote"
print 'this is s %s' % 'single-quote'
'''

# example of a format string combined with an escape string
'''print "I hope you %s" % "\n\"understand\""
'''