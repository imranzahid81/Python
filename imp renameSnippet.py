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

    # Now to first add zero with  numers index and make 2 no display for easy sorting
    finalNumber = f_num[3].zfill(2)

    #  Then to turn list into text again
    finalName = ' '.join(f_num[:3])

    # Now saving to variable with f string formating
    completeName = f"{finalNumber} {finalName}"

    # Test the output
    print(completeName)

    # Finally Rename the files
    os.rename(f, completeName)
