import pandas as pd
import numpy as np




original_data = pd.read_csv("adult.csv",
    names=[
    "Age", "Workclass", "fnlwgt", "Education", "Education-Num", "Marital Status",
    "Occupation", "Relationship", "Race", "Gender", "Capital Gain", "Capital Loss",
    "Hours per week", "Country", "Target"],
    sep=r'\s*, \s*',na_values='?')




import matplotlib.pyplot as plt
import math
%matplotlib inline
fig = plt.figure (figsize=(20,20))
cols=3
rows = math.ceil(float(original_data.shape[1]) / cols)
for i, column in enumerate(['Age', 'Workclass', 'Education', 'Occupation', 'Race', 'Gender']):
    ax = fig.add_subplot (rows, cols, i + 1)
    ax.set_title(column)
    if original_data.dtypes[column] == np.object:
        original_data[column].value_counts ().plot (kind="bar", axes=ax)
    else:
        original_data[column].hist(axes=ax)
        plt.xticks (rotation="vertical")
plt.subplots_adjust(hspace=0.7, wspace=0.2)
plt.show ()




import sklearn.preprocessing as preprocessing
le = preprocessing.LabelEncoder ()
original_data['Occupation'] = le.fit_transform(original_data[ 'Occupation'].astype (str))
original_data.head()


original_data['Target'] = le.fit_transform(original_data[ 'Target'].astype(str))
original_data.tail()


original_data.Target.unique()


original_data.groupby ('Education-Num').Target.mean().plot (kind= 'bar')
plt.show()




from sklearn.model_selection import train_test_split
# Taking only the features that is important for now
X = original_data[['Education-Num', 'Occupation']]
y = original_data[ 'Target']


# Spliting into 808 for training set and 208 for testing set so we can see our accuracy
x_train, x_test, y_train, y_test = train_test_split (X, y, test_size=0.2, random_state=0)


from sklearn.svm import SVC
# Declaring the svc with no tuning
classifier= SVC()


# Fitting the data. This is where the sVM will learn
classifier.fit(x_train , y_train)


# Predicting the result and giving the accuracy
score = classifier.score(x_test, y_test)
print (score)




# Correlation matrix
import seaborn as sns
corrmat = original_data.corr()
f, ax = plt.subplots (figsize=(7, 7))
sns.heatmap(corrmat, vmax=.8, square=True);
plt.show ()




# Convert potential relevant fields to have numeric values
original_data['Race'] = le.fit_transform(original_data[ 'Race'].astype (str))
original_data[ 'Gender'] = le.fit_transform(original_data[ 'Gender'].astype (str))
original_data[ 'Marital Status'] - le.fit_transform (original_data[ 'Marital Status'].astype (str))
original_data['Education'] = le.fit_transform (original_data[ 'Education'].astype(str))




# To get the actual correlation values, annotate the heatmap
f, ax = plt.subplots (figsize=(7, 7))
sns.heatmap(corrmat, vmax=.8, square=True, annot=True, fmt='.2f')
plt.show ()




# Resetting features
x = original_data[['Education-Num', 'Occupation', 'Age', 'Gender']]
y = original_data[ 'Target']


#Splitting training and test data
x_train, x_test, y_train, y_test = train_test_split (X, y, test_size=0.2, random_state=0)
classifier = SVC()

classifier.fit(x_train, y_train)

score = classifier.score(x_test, y_test)
print (score)




# Setting our kernel to Radial Basis Function with penalty parameter C=1.0
classifier= SVC(kernel=' rbf', C=1.0)  # default values
classifier.fit(x_train, y_train)

score = classifier.score(x_test, y_test)
print (score)




# Adjust the penalty parameter C
classifier = SVC(kernel='rbf', C=10.0)
classifier.fit(x_train, y_train)

score = classifier.score(x_test, y_test)
print(score)




# Let us now try a linear kernel
classifier = SVC(kernel='linear', C=10.0)
classifier.fit(x_train, y_train)

score = classifier.score(x_test, y_test)
print(score)