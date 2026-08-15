import joblib
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,classification_report

iris=load_iris()
X=pd.DataFrame(iris.data,columns=iris.feature_names)
y=iris.target

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=RandomForestClassifier(random_state=42)
model.fit(X_train,y_train)

y_pred=model.predict(X_test)

accuracy=accuracy_score(y_test,y_pred)
print(f"Model Accuracy:{accuracy*100:.2f}%\n")
print("Classification Report:")
print(classification_report(y_test,y_pred,target_names=iris.target_names))


#dump model

joblib.dump(model,"iris_model.pkl")
print("Model saved Successfully as iris_model.pkl")