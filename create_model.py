import pandas as pd
import strcount
from sklearn import preprocessing
from sklearn import tree
from joblib import dump, load

df = pd.read_csv('train.csv')

le = preprocessing.LabelEncoder()

df['label'] = le.fit_transform(df['label'])


enList=[]
digList=[]
puncList=[]
spaceList=[]
lowerList=[]

for cont in df["content"]:
    enList.append(strcount.str_count(cont).en)
    digList.append(strcount.str_count(cont).digit)
    puncList.append(strcount.str_count(cont).punc)
    spaceList.append(strcount.str_count(cont).space)
    lowerList.append(strcount.str_count(cont).lower)


print("en")
print(enList)
df['en']=enList

print("dig")
print(digList)
df['digit']=digList

print("punc")
print(puncList)
df['punc']=puncList

print("space")
print(spaceList)
df['space']=spaceList

print("lower")
print(lowerList)
df['lower']=lowerList

X = df.iloc[:, 2:7]
y = df.iloc[:, 1]

print(X)
print(y)

decision_tree = tree.DecisionTreeClassifier(criterion='gini')

decision_tree.fit(X, y)

dump(decision_tree, 'tree.joblib')

print(le.inverse_transform(decision_tree.predict([(10,0,5,3,0)])))

 