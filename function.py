def countwords():
    filename = input('Enter the filename.')
    numberofwords = 0
    file = open(filename,'r')
    for line in file:
        words = line.split()
        numberofwords = numberofwords+len(words)
    print('Number of words=')
    print(numberofwords)
countwords()
