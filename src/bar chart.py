import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/Spotify_Youtube.csv')

# Group the songs by artist and views from youtube and streams from spotify
df_artist_group = df.groupby('Artist')[['Views', 'Stream']].sum()

# Sort the artists descending order by the sum of views and streams
df_artist_sort = df_artist_group.sort_values(['Views', 'Stream'], ascending=False)

# Store the top 10 artists with the most number of views on YouTube and streams on Spotify
top_10 = df_artist_sort.head(10)

# Create two separate DataFrames for views and streams
df_views = df.groupby('Artist')['Views'].sum().sort_values(ascending=False)[:10]
df_streams = df.groupby('Artist')['Stream'].sum().sort_values(ascending=False)[:10]

# Set the width of the bars
barWidth = 0.35

# Set the position of the bars on the x-axis
r1 = np.arange(len(df_views))
r2 = [x + barWidth for x in r1]

# Create the figure and axes objects
fig, ax = plt.subplots(figsize=(20,10))

# Create the first set of bars
ax.bar(r1, df_views, color='#EE3224', width=barWidth, label='Views')

# Create the second set of bars
ax.bar(r2, df_streams, color='#F78F1E', width=barWidth, label='Streams')

# Set the x-axis tick marks to be the artist names
ax.set_xticks([r + barWidth / 2 for r in range(len(df_views))])
ax.set_xticklabels(top_10.index)

# Set the title and labels
ax.set_title('Top 10 Artists on YouTube and Spotify')
ax.set_xlabel('Artist')
ax.set_ylabel('Number of Views/Streams')

# Add the legend
ax.legend()

plt.show()
