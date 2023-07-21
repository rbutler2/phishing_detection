import csv
import tensorflow as tf
from sklearn.model_selection import train_test_split

csv.field_size_limit(20 * 1024 * 1024)

def import_csv_as_dictionary(file_path):
    data_dict = {}
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Assuming 'Email Text' and 'Email Type' are the relevant columns
            email_text = row['Email Text']
            email_type = row['Email Type']
            data_dict[email_text] = {
                'Email Type': email_type
            }
    return data_dict

# Replace 'file_path' with the actual path to your CSV file
csv_file_path = 'resources\data\Phishing_Email.csv'
data_dict = import_csv_as_dictionary(csv_file_path)

# Print the first 5 rows of the dictionary
# count = 0
# for email_text, email_data in data_dict.items():
#     print(f"Email Text: {email_text}, Email Type: {email_data['Email Type']}")
#     count += 1
#     if count == 5:
#         break

#put dictionary into list to train test split
def split_dictionary(data_dict, test_size=0.2, random_state=None):
    keys = list(data_dict.keys())
    values = list(data_dict.values())

    keys_train, keys_test, values_train, values_test = train_test_split(
        keys, values, test_size=test_size, random_state=random_state
    )

    train_dict = {k: v for k, v in zip(keys_train, values_train)}
    test_dict = {k: v for k, v in zip(keys_test, values_test)}

    return train_dict, test_dict

train_dict, test_dict = split_dictionary(data_dict, random_state = 10)

#Print the first 5 rows of the dictionary
# count = 0
# for email_text, email_data in train_dict.items():
#     print(f"Email Text: {email_text}, Email Type: {email_data['Email Type']}")
#     count += 1
#     if count == 5:
#         break













