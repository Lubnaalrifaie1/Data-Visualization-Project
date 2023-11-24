import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

df = pd.read_csv('data/Spotify_Youtube.csv')

# Calculate mean value
df_mean_Loudness = np.mean(df['Loudness'])

fig = px.histogram(df, x = 'Loudness',)
fig.update_layout(title ='Distribution of Loudness', title_x=0.5, title_xanchor= 'center',width = 1000, height = 600)
fig.add_annotation(x=0,y=1.05, text=f"Mean: {df_mean_Loudness:.2f}", showarrow=False, xref="paper", yref="paper", font=dict(size=15))
fig.update_xaxes(title_text='Loudness')
fig.update_yaxes(title_text='Tracks')
