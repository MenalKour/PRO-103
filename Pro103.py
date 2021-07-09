import pandas as pd
import plotly.express as px

df=pd.read_csv("data.csv")
fig=px.scatter(df,x="date",y="cases",color="country",title="COVID CASES IN VARIOUS COUNTRIES ON BASIS OF DATES")
fig.show()