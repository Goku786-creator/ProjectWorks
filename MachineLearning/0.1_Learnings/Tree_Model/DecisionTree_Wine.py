import pandas as pd
import numpy as np




wine_data = pd.read_csv("wine.csv",
    names=["Fixed Acidity","Volatile Acidity","Citric Acid","Residual Sugar",
    "Chlorides","Free Sulfur Dioxide","Total Sulfur Dioxide","Density","pH",
    "Sulphates","Alcohol","Quality"],
    sep=r'\s*, \s*',na_values='?',skiprows=1)

wine_data.head()




import matplotlib.pyplot as plt
import seaborn as sns
corrmat = wine_data.corr()
f, ax = plt.subplots (figsize=(7, 7))
sns.heatmap(corrmat, vmax=.8, square=True, annot=True, fmt='.2f')
plt.show ()




from sklearn.model_selection import train_test_split
X=wine_data.drop('Quality',axis=1)
y=wine_data['Quality']

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)




from sklearn.tree import DecisionTreeClassifier
classifier= DecisionTreeClassifier(max_depth=5, max_features=5,criterion='entropy')
#Adding a limit tends to decrease the Accuracy of the Model
classifier

classifier.fit(x_train, y_train)

score = classifier.score(x_test, y_test)
print(score)

classifier.n_features_

classifier.feature_importances_




import sklearn.tree as tree
tree.export_graphviz(classifier,out_file='tree.dot', feature_names=X.columns)


#Creating a Tree png file of the Decision Tree
from subprocess import call
call(['dot', '-T', 'png', 'tree.dot', '-o', 'tree.png'])



