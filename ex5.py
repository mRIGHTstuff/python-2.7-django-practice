name = 'Michael J. Chotikul'
age = 30 # not a lie
height = 69.0 # inches
height_met = height * 2.54
weight = 172.0 # lbs
weight_met = weight * 0.45359
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall.  That's %d in centimeters." % (height, height_met)
print "He's %d pounds.  That's %d in kilograms." % (weight, weight_met)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d. And if I add %d, %d, and %d I get %d!" % (age, height, weight, age + height + weight, age, height_met, weight_met, age + height_met + weight_met)