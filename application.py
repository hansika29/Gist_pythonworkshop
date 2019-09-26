contact={}
def add_contact(name,ph_no):
    if(name in contact.keys()):
        print(name,"contact already exists.....!!!")
    else:
        contact[name]=ph_no
        print("contact added/saved successfully....!!!")
def display_contact():
    i=0
    for name,phone in contact.items():
        print(i+1,".name=",name,",phonenumber=",phone)
        if(i<len(contact)):
            break
        i=i+1
def delete_contact(name):
    if(name in contact.keys()):
        contact.pop(name)
        print("name,deleted successfully............!!!")
    else:
        print(name,"doesn't exits in contact list.....!!!")
def update_contact(name):
    if(name in contact.keys()):
        print("name=",name,"phonenumber=",contact[name])
    else:
        print(name,"doesn't exists.....!!!")
def search_contact(name):
    if(name in contact.keys()):
        print("name=",name,"phonenumber="contact[name])
else:
    print(name,"don't exists....!!!")