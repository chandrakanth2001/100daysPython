#Averge height

heights = input("Enter the heights with spaces")

heights_list = heights.split()

print(f"Split method returns this list : {heights_list}")

#without using length function to find length, Im using counting

count = 0

for i in heights_list:
    count+=1
print(f"Count is : {count}")


#converting the string list to integer for calculating sum and average


for toint in range(count):
    heights_list[toint] = int(heights_list[toint])
print(f"Int List : {heights_list}")

#finding the total/sum

total = 0

for tot in heights_list:
    total +=tot
print(f"Total is : {total}")

#average

avg = total/count

#rounding

print(round(avg))