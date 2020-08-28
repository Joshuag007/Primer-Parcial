
import pandas as pd
df = pd.read_csv('winequality-red.csv', sep=';')
df.head()

alcoholmediana = df.alcohol.median()
for i, propiedad_alcohol in enumerate(df.alcohol):
    if propiedad_alcohol >= alcoholmediana:
        df.loc[i, 'alcohol'] = 'alto'
    else:
        df.loc[i, 'alcohol'] = 'bajo'
print (df.groupby('alcohol').quality.mean())

pH_Mediana = df.pH.median()
for i, propiedad_pH in enumerate(df.pH):
    if propiedad_pH >= pH_Mediana:
        df.loc[i, 'pH'] = 'alto'
    else:
        df.loc[i, 'pH'] = 'bajo'
print (df.groupby('pH').quality.mean())

azucar_residual_mediana = df.residual_sugar.median()
for i, propiedad_sugar in enumerate(df.residual_sugar):
    if propiedad_sugar >= azucar_residual_mediana:
        df.loc[i, 'residual_sugar'] = 'alto'
    else:
        df.loc[i, 'residual_sugar'] = 'bajo'
print (df.groupby('residual_sugar').quality.mean())

acido_citrico_mediana = df.citric_acid.median()
for i, Propiedad_citric_acid in enumerate(df.citric_acid):
    if Propiedad_citric_acid >= acido_citrico_mediana:
        df.loc[i, 'citric_acid'] = 'alto'
    else:
        df.loc[i, 'citric_acid'] = 'bajo'
print (df.groupby('citric_acid').quality.mean())