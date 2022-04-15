import os
print("How many folders named 'CON' do you want to create?")
a = input()
i = 0
while i < int(a):
    f = "‎"
    if i < 1:
        folder = f + "CON" + f
    else:
        folder = f + folder + f
    os.mkdir(folder)
    i = i + 1
    
