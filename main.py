import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
import os

# Sujet: Employee Attrition Prediction
# Source: https://www.kaggle.com/datasets/patelprashant/employee-attrition

## Chargement des données
df = pd.read_csv('./data/employee_attrition.csv')

## Affichage des 5 premières lignes du DataFrame
print(df.head(5))

## Nombre total d'employés dans le dataset
print(df.shape[0])

## Supprimer les lignes avec des valeurs manquantes
df = df.dropna()

## Afficher la fiabilité des données
print(df.isnull().sum())

## Transformer Attrition en variable numérique
df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})

## Transformer Gender en variable numérique
df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})

## Transformer OverTime en variable numérique
df['OverTime'] = df['OverTime'].map({'Yes': 1, 'No': 0})

# Vérifier la transformation
print(df['OverTime'].unique())

# Créer le dossier "img" si nécessaire
if not os.path.exists('img'):
    os.makedirs('img')

# Arbres de décisions
## Prédire si l'employé va quitter l'entreprise (Attrition)
### Features = Age, DistanceFromHome, JobSatisfaction, JobInvolvement, EnvironmentSatisfaction, MonthlyIncome, OverTime, YearsAtCompany

### Sélection des features
features = ['Age', 'DistanceFromHome', 'JobSatisfaction', 'JobInvolvement', 'EnvironmentSatisfaction', 'MonthlyIncome', 'OverTime', 'YearsAtCompany']
X = df[features]
y = df['Attrition']

### Transformation des variables catégorielles en variables numériques
X = pd.get_dummies(X)

### Création du modèle
model = DecisionTreeClassifier(max_depth=5)
model = model.fit(X, y)

### Affichage de l'arbre de décision
plt.figure(figsize=(60, 30))
plot_tree(model, feature_names=X.columns, filled=True)
plt.show()

# Sauvegarder l'image dans le dossier "img"
plt.figure(figsize=(60, 30))
plot_tree(model, feature_names=X.columns, filled=True)
plt.savefig('img/attrition_tree.png')

## Prédiction pour savoir si le salaire est important pour l'attrition de l'employée
### Sélection des features
features = ['MonthlyIncome']
X = df[features]
y = df['Attrition']

### Transformation des variables catégorielles en variables numériques
X = pd.get_dummies(X)

### Création du modèle
model = DecisionTreeClassifier(max_depth=5)
model = model.fit(X, y)

### Affichage de l'arbre de décision
plt.figure(figsize=(60, 30))
plot_tree(model, feature_names=X.columns, filled=True)
plt.show()

# Sauvegarder l'image dans le dossier "img"
plt.figure(figsize=(60, 30))
plot_tree(model, feature_names=X.columns, filled=True)
plt.savefig('img/salary_tree.png')

## Prédiction pour savoir si on fait des heures supplémentaires selon le job level
### Features = JobLevel

### Sélection des features
features = ['JobLevel']
X = df[features]
y = df['OverTime']

### Transformation des variables catégorielles en variables numériques
X = pd.get_dummies(X)

### Création du modèle
model = DecisionTreeClassifier()
model = model.fit(X, y)

### Affichage de l'arbre de décision
plt.figure(figsize=(60, 30))
plot_tree(model, feature_names=X.columns, filled=True)
plt.show()

# Sauvegarder l'image dans le dossier "img"
plt.figure(figsize=(60, 30))
plot_tree(model, feature_names=X.columns, filled=True)
plt.savefig('img/overtime_tree.png')
