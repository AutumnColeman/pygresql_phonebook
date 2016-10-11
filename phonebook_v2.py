# You will write a command line program to manage a phone book. Only this time, using a PostgreSQL database to store the information instead of a dictionary and then persisting to files. You will use the PyGreSQL module to connect to a PostgresSQL database.

import pg

db = pg.DB(dbname='phonebook_v2')


while True:
    #Looks up an entry
    def look_up():
        name = raw_input("Name? ").lower().title()
        result_list = db.query("select * from phonebook where name ilike '%s'" % name).namedresult()
        if len(result_list) > 0:
            for result in result_list:
                print "%s's phone number: %s and email: %s" % (result.name, result.phone_number, result.email)
        else:
            print "%s is not found." % name

    #Sets an entry
    def set_entry():
        name = raw_input('Name? ').lower()
        number = raw_input('Number? ')
        email = raw_input('Email? ')
        result_list = db.query("select id from phonebook where name ilike '%s'" % name).namedresult()
        if len(result_list) > 0:
            id = result_list[0].id
            db.update('phonebook', {
                'id': id,
                'name': name,
                'phone_number': number,
                'email': email
            })
            print 'Updated entry for %s' % name
        else:
            db.insert('phonebook', name=name, phone_number=number, email=email)
            print 'Added entry for %s' % name


    #Deletes an entry
    def delete_entry():
        print "Please enter a name to delete from the phonebook."
        name = raw_input("Name: ").lower().title()
        query = db.query('select id, name from phonebook')
        result_list = query.namedresult()
        for result in result_list:
            if name == result.name:
                db.delete('phonebook', {'id': result.id})
                print "Entry for %s deleted." % name
            else:
                print "%s is not found." % name


    #Lists all entries
    def list_entries():
        query = db.query('select name as "Name", phone_number as "Phone", email as "Email" from phonebook')
        print query



    print """
    Electronic Phone Book
    =====================

    1. Look up an entry
    2. Set an entry
    3. Delete an entry
    4. List all entries
    5. Quit
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
        print "Invalid option. Please enter a valid option (1-5)."
