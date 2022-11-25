import gzip
import json
import random
import numpy as np
from sklearn.linear_model import LinearRegression


file = "Caucasus"
a_file = gzip.open(f"Transformed_data/{file}.json.gz", "rb")
contents = json.loads(a_file.read())

training = {
    'input': [],
    'target': []
}
test = {
    'input': [],
    'target': []
}

for row in contents:
    if bool(random.getrandbits(1)):
        training['input'].append([row["input"]["x"], row["input"]["y"]])
        training['target'].append([row["test"]["x"], row["test"]["y"]])
    else:
        test['input'].append([row["input"]["x"], row["input"]["y"]])
        test['target'].append([row["test"]["x"], row["test"]["y"]])



gps_to_dcs_model = LinearRegression()
gps_to_dcs_model.fit(training['input'], training['target'])

print("GPS_TO_DCS Training set score: {:.2f}".format(gps_to_dcs_model.score(training['input'], training['target'])))
print("GPS_TO_DCS Test set score: {:.2f}".format(gps_to_dcs_model.score(test['input'], test['target'])))

index = random.randint(0, len(training['input']) -1)
input = test['input'][index]
expected = test['target'][index]
output = gps_to_dcs_model.predict([input])
output_value =  output.tolist()[0]
print("GPS_TO_DCS input:",input,"expected:", expected, "actual:", output_value, "X diff:", expected[0] - output_value[0], "Y diff: ", expected[1] - output_value[1])

# This model is inverse to the previous model allowing backward transformation
dcs_to_gps_model = LinearRegression()
dcs_to_gps_model.fit(training['target'], training['input'])

print("DCS_TO_GPS Training set score: {:.2f}".format(dcs_to_gps_model.score(training['target'], training['input'])))
print("DCS_TO_GPS Test set score: {:.2f}".format(dcs_to_gps_model.score(test['target'], test['input'])))

index = random.randint(0, len(training['input']) -1)
input = test['target'][index]
expected = test['input'][index]
output = dcs_to_gps_model.predict([input])
output_value =  output.tolist()[0]
print("DCS_TO_GPS input:",input,"expected:", expected, "actual:", output_value, "X diff:", expected[0] - output_value[0], "Y diff: ", expected[1] - output_value[1])