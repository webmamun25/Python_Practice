"""_Create a text file named emails.txt containing multiple email addresses, some in uppercase and some repeated.
Write a Python program to clean the data by converting all emails to lowercase, removing duplicates, sorting them alphabetically, and saving the cleaned list to a new file named unique_emails.txt.

    """

with open('email.txt','r') as file:
    content=file.readlines()
    # remove /n and comma 
    preprocess=list(map(lambda x:x.strip().replace(',',''),content))
    # make email lowercase 
    lower_case=list(map(lambda x :x.lower(),preprocess))
    unique_emails = list(set(email.lower() for email in lower_case))
    sorted_emails=sorted(unique_emails)

with open('unique_emails.txt','w') as file:

    for email in sorted_emails:
        file.write(email + "\n")

print("✅ Cleaned and sorted emails saved to 'unique_emails.txt'")
  
    
