################################################################
#
# Magic Square solving code.
#
# Another homework problem which I am trying to solve in Python.
#
# The problem is to populate a magic 3x3 square with the values
# 15,25,35,45,55,65,75,85,95 such that each column and each row totals
# to 165.  There is one square pre-populated, the lower left square
# which is 25.
#
# I am planning to use an approach similar to the one I used for the 4
# cell square where the numbers totalled to 200.
#
################################################################


# The plan is to have a series of nested for loop iterating over the
# list which is used repeatedly. This is a really bad program!

# create list for box1 - box8
box1 = [15,35,45,55,65,75,85,95]
box2 = [15,35,45,55,65,75,85,95]
box3 = [15,35,45,55,65,75,85,95]
box4 = [15,35,45,55,65,75,85,95]
box5 = [15,35,45,55,65,75,85,95]
box6 = [15,35,45,55,65,75,85,95]
box7 = [15,35,45,55,65,75,85,95]
box8 = [15,35,45,55,65,75,85,95]


# The following brute forces the values for each of the boxes.  For
# information the box looks like this:
#
#
# |box1|box2|box3|
# |box4|box5|box6|
# |25  |box7|box8|
#
# As this is the case, you can add in more filtering of the results.
for n1 in box1:
    for n2 in box2:
        if n2 == n1:
            continue
        for n3 in box3:
            if n3 == n1 or n3 == n2:
                continue
            for n4 in box4:
                if n4 == n1 or n4 == n2 or n4 == n3:
                    continue
                for n5 in box5:
                    if n5 == n1 or n5 == n2 or n5 == n3 or n5 == n4:
                        continue
                    for n6 in box6:
                        if n6 == n1 or n6 == n2 or n6 == n3 or n6 == n4 or n6 == n5:
                            continue
                        for n7 in box7:
                            if n7 == n1 or n7 == n2 or n7 == n3 or n7 == n4 or n7 == n5 or n7 == n6:
                                continue
                            for n8 in box8:
                                if n8 == n1 or n8 == n2 or n8 == n3 or n8 == n4 or n8 == n5 or n8 == n6 or n8 == n7:
                                    continue
                                if (n1 + n2 + n3) == 165 and (n4 + n5 + n6) == 165 and (25 + n7 + n8) == 165 and (n1 + n4 + 25) == 165 and (n2 + n5 + n7) == 165 and (n3 + n6 + n8) == 165:
                                    print "result square:";
                                    print "|%d|%d|%d|" % (n1,n2,n3);
                                    print "|%d|%d|%d|" % (n4,n5,n6);
                                    print "|25|%d|%d|" % (n7,n8);
