import gzip
import json
from sklearn import svm
from sklearn.preprocessing import MultiLabelBinarizer

file = "Caucasus"
a_file = gzip.open(f"Transformed_data/{file}.json.gz", "rb")
contents = json.loads(a_file.read())

input = []
test = []
print(len(contents))
for row in contents:
    input.append([row["input"]["x"], row["input"]["y"]])
    test.append([row["test"]["x"], row["test"]["y"]])

test_transformed = MultiLabelBinarizer().fit_transform(test)
input_transformed = MultiLabelBinarizer().fit_transform(input)

clf = svm.SVC(gamma=0.001, C=100.)
model = clf.fit(input_transformed[:-1], test_transformed[:-1])

output = clf.predict(input[-1:])
print(output, test[-1:])
