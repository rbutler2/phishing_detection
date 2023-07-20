import csv


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
count = 0
for email_text, email_data in data_dict.items():
    print(f"Email Text: {email_text}, Email Type: {email_data['Email Type']}")
    count += 1
    if count == 5:
        break















csv_file_path = 'resources\data\Phishing_Email.csv'