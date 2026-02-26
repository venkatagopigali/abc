import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
data=pd.read_excel(r"C:\Users\hp\Desktop\LAND.xlsx")
st.title("HOUSE PRICE PREDICTION....")
# print(data)
data['location']=data['location'].map({"KPHB":0,"MADHAPUR":1,"AMEERPET":2,"UPPAL":3,"HI-TECH":4,"DILSUKNAGAR":5})
print(data)
X=data[['sqrt','location']]
y=data['prices']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
model=LinearRegression()
model.fit(X,y)
tx1=st.number_input("enter sqft")
tx2=st.number_input("entre city code")
new=model.predict([[tx1,tx2]])
bt=st.button("submit")
if bt:
    st.write("predicted price is",new)