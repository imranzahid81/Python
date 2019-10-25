import os

# paste link of folder below in commas to edit file name
# os.chdir('/home/underworld/Desktop/vdo')

# To check whether i am in a directory or not
# print(os.getcwd())

for f in os.listdir():
    # Just to check list of directory :
    # text = "List of directory"
    # print(f"{text} {f}")

    # now for Real code
    # Now for splicing and converting to tuple for ease:
    fileName, fileExt = os.path.splitext(f)
    text2 = "Printing only file name without extension : "
    print(f"{text2} {fileName}")

    # Now to split title name by spaces to turn them into a list
    f_num = fileName.split(" ")
    print(f_num)

    # Now
    finalNumber = f_num[3].zfill(2)
    finalName = ' '.join(f_num[:3])
    completeName = f"{finalNumber} {finalName}"

    print(completeName)

    # Finally Rename the files
    os.rename(f, completeName)
