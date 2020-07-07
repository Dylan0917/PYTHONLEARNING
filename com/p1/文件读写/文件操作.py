import pickle

myList = [1,2,3,4,5,"good man"]

f = open("/Users/ywh/CODESRC/pwb","wb")
pickle.dump(myList,f)
f.close()

f1 = open("/Users/ywh/CODESRC/pwb","rb")
temList = pickle.load(f1)
print(temList)
f1.close()