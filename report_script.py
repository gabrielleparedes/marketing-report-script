"""
Marketing Performance Report Script

This script simulates 4 weeks of campaign performance across various marketing channels.
It calculates:
- Total sessions
- Total conversions
- Average CPA
- Conversion rate

It also generates:
- A CSV summary
- A bar chart of average CPA by channel
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create mock data
np.random.seed(42)
channels = ['Organic Search', 'Paid Search', 'Email', 'Social Media', 'Referral']
weeks = [f'Week {i}' for i in range(1, 5)]

data = []

for week in weeks:
    for channel in channels:
        sessions = np.random.randint(500, 2000)
        conversions = np.random.randint(20, 100)
        cpa = round(np.random.uniform(5.0, 50.0), 2)
        data.append([week, channel, sessions, conversions, cpa])

df = pd.DataFrame(data, columns=['Week', 'Channel', 'Sessions', 'Conversions', 'CPA'])

# Summarize data by channel
summary = df.groupby('Channel').agg({
    'Sessions': 'sum',
    'Conversions': 'sum',
    'CPA': 'mean'
}).reset_index()

summary['Conversion Rate (%)'] = round((summary['Conversions'] / summary['Sessions']) * 100, 2)

# Save summary to CSV
summary.to_csv("marketing_channel_summary.csv", index=False)
print("✅ Summary saved to marketing_channel_summary.csv")

# Plot CPA by channel
plt.figure(figsize=(10, 6))
plt.bar(summary['Channel'], summary['CPA'], color='skyblue')
plt.title('Average CPA by Channel')
plt.xlabel('Marketing Channel')
plt.ylabel('CPA ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("average_cpa_by_channel.png")
print("✅ Chart saved to average_cpa_by_channel.png")
