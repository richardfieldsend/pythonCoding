################################################################
#
# find primes from 2 to 1 million
#
################################################################
for testNumber in xrange(3,100,2):
    # print "testNumber is %d." % testNumber;
    # to check whether a number is a prime you should try dividing the
    # testNumber by every number from 2 to testNumber/2 looking for
    # any number that can be divided into the testNumber without
    # leaving a remainder.
    modCheck = 0;
    for primeTest in xrange(3,testNumber/2+1,2):
        print "testNumber is %d, and primeTest in %d." % (testNumber,primeTest);
