count = 0

while (count <= 10):
    print (f"Counter is currently at {count}")
    if (count%2 == 0):
        print(f"{count} is even")
    else:
        print(f"{count} is odd")
    count += 1
print ("Loop complete")
