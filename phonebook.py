phone_book={}
def add_contact():
    name=input("enter the name:").strip().lower()
    phone_num=int(input("enter the phone number:").strip())
    phone_book[name]=phone_num
    print()
    print()
    print("------contact saved successfully----")
def read_contact():
    search_name=input("enter the searching number:").strip().lower()
    if search_name in phone_book.keys():
        print()
        print('--------')
        print("the number for{search_name}is:{phone_book[serach_name]}")
    else:
        print("contact is available...!")
def update_contact():
    update_name=input("enter the name").strip().lower()
    update_num=int(input("enter the new number to update:"))
    phone_book['name']=update_num
    print()
    print()
    print("---contact updated----")
update_contact()
    
def delete_contact():
    delete_name=input("enter the name").strip().lower()
    delete_number=int(input("enter the delete number:"))
    #phone_book[name]=phone_num
    print()
    print("---contact deleted")
delete_contact()

def main():
    while(True):
        print("choose the task from the below options")
        print("""
              1.add contact
              2.read contact
              3.update contact
              4.delete contact""") 
        choice=int(input()) 
        if choice==1:
            add_contact()
        elif choice==2:
            read_contact()
        elif choice==3:
            update_contact()
        elif choice==4:
            delete_contact()
        else:
            break  
        
if __name__=='__main__':
    main()
    