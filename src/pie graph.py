import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/Spotify_Youtube.csv')

#counts how many album types are listed in the data set
df_album_type_count = df['Album_type'].value_counts()

# Create a pie chart
labels = df_album_type_count.index.tolist()
sizes = df_album_type_count.values.tolist()

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=30)
plt.axis('equal')
plt.title('Album Types')
plt.legend(labels, loc='best')

plt.show()
