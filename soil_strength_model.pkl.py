from sklearn.tree import DecisionTreeRegressor
import joblib

model = DecisionTreeRegressor()
model.fit(X_train, y_train)  # Your data here
joblib.dump(model, 'soil_strength_model.pkl')
