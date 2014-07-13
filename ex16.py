
print "this is about file writing..."

fname = raw_input("enter file name > ")

f1 = open(fname, "w")

l1 = raw_input("enter the line1\n")
l2 = raw_input("enter the line2\n")
l3 = raw_input("enter the line3\n")


f1.write(l1 + "\n" + l2 + "\n" + l3)

f1.close()


