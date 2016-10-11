import pg

db = pg.DB(dbname='phonebook_v2')


# if exists('phonebook_v2.sql'):
#     print "Loading phonebook"
#
# else:
#     phonebook_dict = {}

while True:
    #Looks up an entry
    def look_up():
        name = raw_input("Name? ")
        if name in phonebook_dict:
            info_dict = phonebook_dict[name]
            print "Found entry for %s: " % (name)
            print "Cell Phone Number: %s" % (info_dict["Cell"])
            print "Home Phone Number: %s" % (info_dict["Home"])
            print "Work Phone Number: %s" % (info_dict["Work"])

        else:
            print "Entry for %s not found." % name

    #Sets an entry
    def set_entry():
        print "Please add the name and number to create a new entry:"
        name = raw_input("Name: ")
        phone = raw_input("Phone Number: ")
        email = raw_input("Email: ")

        db.query("""
        update phonebook set
            name = %s,
            phone = %s,
            email = %s
        """, (name, phone, email))
        print "Entry stored for %s" % name


    #Deletes an entry
    def delete_entry():
        print "Please enter a name to delete from the phonebook."
        name = raw_input("Name: ").lower()
        if name in phonebook_dict:
            del phonebook_dict[name]
            print "Deleted entry for %s" % name
        else:
            print "%s not found." % name

    #Lists all entries
    def list_entries():
        query = db.query('select name as "Name", phone_number as "Phone", email as "Email" from phonebook')
        print query



    print """
    Electronic Phone Book
    =====================

    1\. Look up an entry
    2\. Set an entry
    3\. Delete an entry
    4\. List all entries
    5\. Quit
    """

    menu_number = int(raw_input("What do you want to do (1-5)? "))

    if menu_number == 1:
        look_up()
    elif menu_number == 2:
        set_entry()
    elif menu_number == 3:
        delete_entry()
    elif menu_number == 4:
        list_entries()
    elif menu_number == 5:
        print "Goodbye!"
        break
    elif menu_number > 5:
        print "Invalid option. Please enter a valid option (1-6)."