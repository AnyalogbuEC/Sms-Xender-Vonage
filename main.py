# This application was written by Anyalogbu, Ernest Chinualum on wednesday, April 20, 2022.
# Developer's contact: AnyalogbuEC or Anyalogbu_EC on any platform, phone: +234(0)8149390948.
# It was written for the sole aim of sending sms using vonage API.

# importing the vonage library
import vonage

print("\n\n|||||||||||  ||\\\\      //||  |||||||||||            //\\\\        ||||||||||  ||||||||||")
print("||           || \\\\    // ||  ||		           //  \\\\       ||	||  ||      ||")
print("||           ||  \\\\  //  ||  ||		          //    \\\\      ||	||  ||	    ||")
print("|||||||||||  ||   \\\\//   ||  |||||||||||         //||||||\\\\     ||||||||||  ||||||||||")
print("         ||  ||          ||           ||        //        \\\\    ||          ||")
print("         ||  ||          ||           ||       //          \\\\   ||          ||")
print("|||||||||||  ||          ||  |||||||||||      //            \\\\  ||          ||")
print("~~~~~~~~~~~~~AnyalogbuEC~~~~~~~~~~~~~~~~         ~~~~~~~~~~~~Vonage API~~~~~~~~~~~~\n\n")

key = "d22b8f62"  # input("Enter key: ")  # setting key

secret = "g0z3HlDpnQe8NPEG"  # input("Enter secret: ")  # setting secret

sender = "Vonage"  # input("Enter Sender's name: ")  # setting sender's name

successful = []  # list of phone numbers of the successfully sent sms

unsuccessful = []  # list of phone numbers of the unsuccessfully sent sms

client = vonage.Client(key=key, secret=secret)
sms = vonage.Sms(client)


# the function responsible for sending the sms
def message_sender(message, to):
    # data to be sent to the api
    response_data = sms.send_message(
        {
            "from": sender,
            "to": to,
            "text": message,
        }
    )

    if response_data["messages"][0]["status"] == "0":
        print("Message sent successfully.")
        successful.append(to)
    else:
        print(f"Message failed with error: {response_data['messages'][0]['error-text']}")
        unsuccessful.append(to)


# taking the file that contains the contacts details
contacts_details_file = "ContactsData.csv"  # input("Filename or Filepath for contact details:  ")

if not contacts_details_file.endswith(".csv"):
    print("File type must be .csv")
    quit()

contactsDetails = ""  # initializing contactsDetails

# trying to open the contacts_details_file file
try:
    contactsDetails = open(contacts_details_file, "r")
except:
    print("file not found")
    quit()

# taking the file that contains the message
message_file = "Message.txt"  # input("Filename or Filepath for the message:  ")

if not message_file.endswith(".txt"):
    print("File type must be .txt")
    quit()

messageDetails = ""  # initializing messageDetails

# trying to open the message_file file
try:
    messageDetails = open(message_file, "r")
except:
    print("file not found")
    quit()

messageData = ""  # initializing messageData

for message_body in messageDetails:
    messageData = messageData + message_body

x = 0

for contactDetails in contactsDetails:

    if x > 0:
        wordList = contactDetails.split(',')
        first_name = wordList[0].strip()
        last_name = wordList[1].strip()
        phoneNumber = wordList[2].strip()
        Message = "Hi " + last_name + " " + first_name + ",  " + messageData
        print("Sending\n" + Message + "\nto " + phoneNumber)
        message_sender(Message, phoneNumber)

    x = x + 1

print("The successfully sent message(s) are:")
print(successful)
print("The unsuccessfully sent message(s) are:")
print(unsuccessful)
