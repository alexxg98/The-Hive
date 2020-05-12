tabooList = ["shit", "hell", "die"]

# def check(tabooWord):
#     with open('test.txt') as f:
#         datafile = f.readlines()
#     for line in datafile:
#         if tabooWord in line:
#             return True
#     f.close()
#     return False
#
# def replaceTaboo():
#     for value in tabooList:
#         isFournd = check(value)
#         if isFournd:
#             print("Taboo Word Found!")
#             fin = open("test.txt", "rt")
#             #read file contents to string
#             data = fin.read()
#             #replace taboo word with ***
#             data = data.replace(value, '***')
#             fin.close()
#
#             fin = open("test.txt", "wt")#open the input file in write mode
#             #overrite the input file with the resulting data
#             fin.write(data)
#             fin.close()
#
#     print("Done")

# fin=open("test.txt", "wt")
# fin.write(inputText)
# fin.close()
# replaceTaboo()
def check(input):
    inputText = input
    for value in tabooList:
        if (inputText.find(value) != -1):
            return True
    return false

def replaceTaboo(input):
    inputText = input
    for value in tabooList:
        if (inputText.find(value) != -1):
            # print ("Found Taboo Word ")
            inputText = inputText.replace(value, '***')
    return inputText
