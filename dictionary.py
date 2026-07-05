def myDictionary():
    Dict = {0:23, 1:45, 2:56}
    data = {'awantika':27, 'jayesh':26, 'chitra':25}
    Dict1 = {'name':'Awantika', 'age':28, 'city':'Bangalore'}

    print(Dict[2])  # this is for dealing with integers
    print(Dict[1])
    print(data.get('jayes', 'not found'))  # not found is alternate print option if key is not found
    print(data.get('awantika'))  # this is for dealing with string
    print(Dict1.get('name'))
    print(Dict1.get('age'))


    keys = {'riya', 'shreya', 'priya'}
    values = [20,22,23]
    myDict = dict(zip(keys,values))
    print(myDict)

    print(myDict.pop('riya')) # print is to just print the value of key but eventually removing it (stack function)
    print(myDict)

    del myDict['shreya']
    print(myDict)

    languagesList = {'js':'vscode', 'python':['pycharm','vscode'], 'java':{'corejava': 'vscode', 'spring': 'intelliJ'}}
    print(languagesList)
    print(languagesList['python'])
    print(languagesList['python'][1])
    print(languagesList['java'])
    print(languagesList['java']['spring'])


myDictionary()


# keys are collection of set (need to be unique); values are collection of list (no need of unique values)