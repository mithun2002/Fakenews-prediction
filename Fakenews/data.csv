import pandas as pd

# Sample data
data = {
    'text': [
        "COVID-19 vaccine rollout begins worldwide.",
        "Study shows eating broccoli cures cancer.",
        "Breaking: Bigfoot found in the Himalayas.",
        "Aliens land in New York City!",
        "New research on climate change published.",
        "Elvis Presley spotted at a grocery store."
    ],
    'label': [1, 1, 0, 0, 1, 0]  # 1 for real news, 0 for fake news
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('fake_news_dataset.csv', index=False)

print("CSV file 'fake_news_dataset.csv' created.")
