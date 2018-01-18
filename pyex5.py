# -*- coding:utf-8 -*-
my_name = 'Lily'
my_age = 30 # Turning 31.
my_height = 156.00 # CM
cm_to_inch = 0.39
my_weight = 49 # Kg
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "She's %f inches tall." % (my_height * cm_to_inch)
print "She's %d Kg heavy." % my_weight
print "Actually that's very light."
print "She's got %s eyes and %s hair." % (my_eyes, my_hair)
print "Her teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right.
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
