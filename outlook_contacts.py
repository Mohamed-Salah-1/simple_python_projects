import win32com.client

def add_outlook_contacts():
    outlook = win32com.client.Dispatch('Outlook.Application')
    namespace = outlook.GetNamespace('MAPI')

    contacts_folder = namespace.GetDefaultFolder(10)  # 10 represents the Contacts folder

    # Get all received emails
    inbox = namespace.GetDefaultFolder(6)  # 6 represents the Inbox folder
    received_items = inbox.Items

    # Iterate over each received email
    for email in received_items:
        if email.Class == 43:  # 43 represents an email
            sender_email = email.SenderEmailAddress
            sender_name = email.SenderName

            # Check if the contact already exists in the Contacts folder
            contact = contacts_folder.Items.Find("[Email1Address]='{}'".format(sender_email))

            if not contact:
                # Create a new contact item
                contact = contacts_folder.Items.Add()
                contact.Email1Address = sender_email
                contact.FullName = sender_name
                contact.Save()
                print("Added contact: {} ({})".format(sender_name, sender_email))

    print("Contacts added successfully.")

# Call the function to add Outlook contacts
add_outlook_contacts()