# include library
import random

# create variable RGB444 list
RGB444_ls = []
pixel_width = int(input("Enter monitor width: "))
pixel_high = int(input("Enter monitor high: "))
total_pixel = pixel_width * pixel_high
file_name = str(input("Enter file name: "))

print ("Number input = ", total_pixel)
print ("Number input = ", file_name)

for i in range(total_pixel):
    R = hex(random.randint(0, 15))[2:]
    G = hex(random.randint(0, 15))[2:]
    B = hex(random.randint(0, 15))[2:]
    # print("R = " + str(R))
    # print("G = " + str(G))
    # print("B = " + str(B))
    pixel_RGB = str(R) + str(G) + str(B)
    RGB444_ls.append(pixel_RGB)
    # print(pixel_RGB.upper())

for i in range(total_pixel):
    print(RGB444_ls[i])

with open(file_name, "w") as file:

    for i in range(0, len(RGB444_ls), pixel_width):

        # RGB444_ls[x : y] x is start, y is end
        line_elements = RGB444_ls[i : i+pixel_width] 
        # hex_values = [hex(x)[2:] for x in line_elements]
        line = ",".join(line_elements)
        file.write(line.upper() + "\n")

print("Done")