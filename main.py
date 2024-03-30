import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def main():
    dataset = pd.read_csv("dataset.csv")
    data_sev = pd.read_csv("Symptom-severity.csv")
    for cols in dataset.columns:
        for i in range(len(dataset[cols])):
            if type(dataset[cols][i]) == str:
                dataset[cols][i] = dataset[cols][i].strip()
                dataset[cols][i] = dataset[cols][i].replace(" ", "_")
    data_sev_dic = data_sev.to_dict()
    data_dict = data_sev.set_index('Symptom').T.to_dict() 
    cols = dataset.columns
    for col in cols:
        for i in range(len(dataset[col])):
            try:
            #print(data_dict[data2[columnName][i]]["weight"])
                dataset[col][i] = data_dict[dataset[col][i]]["weight"]
            except:
                pass
    dataset = dataset.fillna(0) # put empty cell to 0
    dataset = dataset.replace("foul_smell_of_urine" , 5)
    dataset = dataset.replace("dischromic__patches" , 6)
    dataset = dataset.replace("spotting__urination" , 6)
    x = dataset.iloc[:, 1:]
    y = dataset.iloc[:, 0]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    dtc = DecisionTreeClassifier(criterion='entropy', random_state=42)
    dtc.fit(x_train, y_train)
    return dtc

def start(dtc,user_input):
    input_symptoms = [symptom.strip().lower() for symptom in user_input.split(',')]
    data_sev = pd.read_csv("Symptom-severity.csv")
# Create a new DataFrame with all zeros
    new_df1 = pd.DataFrame(0, index=range(1), columns=['Symptom_' + str(i+1) for i in range(17)])
    # Set weights for the input symptoms
    for i, symptom in enumerate(input_symptoms):
        if symptom in data_sev['Symptom'].values:
            weight = data_sev.loc[data_sev['Symptom'] == symptom, 'weight'].values[0]
            new_df1.iloc[0, i] = weight

    print("New DataFrame with input symptoms:")
    print(new_df1)
    pred = dtc.predict(new_df1)
    print("predicted :"+pred[0])
    return pred[0]

def desc(name):
    df = pd.read_csv("symptom_Description.csv")
    name = name.replace("_", " ")
    df['Disease'] = df['Disease'].str.lower()

    # Search for the disease name
    matching_row = df[df['Disease'] == name.lower()]

    # If no match found, return an error message
    # if matching_row.empty:
    #     return "Symptom not found."

    # Extract and return the description
    return matching_row['Description'].iloc[0]

    # Extract and return the description
    # return matching_row['Description'].iloc[0]

def precaution(name):
    
    df = pd.read_csv("symptom_precaution.csv")
    name =  name.lower()
    name = name.replace("_"," ")
    # name=name.split()
    print(name)

    # df['Disease'] = df['Disease'].str.replace(" ","_")
    # df['Disease'] = df['Disease'].str.split()
    df['Disease'] = df['Disease'].str.lower()
    df['Disease'] = df['Disease'].str.strip()
    print(df['Disease'])
    # Search for the disease name
    matching_row = df[df['Disease'] == name.lower()]
    try:
        precaution1 = matching_row['Precaution_1'].iloc[0]
    except:
        precaution1 = 'not-found'
    try:
        precaution2 = matching_row['Precaution_2'].iloc[0]
    except:
        precaution2 = 'not-found'
    try:
        precaution3 = matching_row['Precaution_3'].iloc[0]
    except:
        precaution3 = 'not-found'
    return precaution1,precaution2,precaution3
    
