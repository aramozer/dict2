import psycopg2
conn = psycopg2.connect(
   host="localhost",
   database="postgres",
   user="postgres",
   password="password"
)

# read_dict: returns the list of all dictionary entries:
# argument: C - the database connection.
def read_dict(C):
    cur = C.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows
# add_word: INSERTS new words in the dictionary:
# arguments: word and translation are each column in the database
def add_word(C, word, translation):
    cur = C.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
# delete_word: DELETS a row in the dictionary:
# argumant: ID is the value of id.
def delete_word(C, ID):
    cur = C.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
# save_dict: makes a commit to database.
def save_dict(C):
    cur = C.cursor()
    cur.execute("COMMIT;")
    cur.close()
# help_list
def help_list():
    print(list_of_inst)

list_of_inst = ('''Hello and welcome to the dictionary, available commands:
    add - New word
    delete - delete a word
    list - list all words
    save - save the list
    help - for list of commands
    quit - quit the program''')

print(list_of_inst)

while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ")
    if cmd == "list":
        print(read_dict(conn))
    elif cmd == "add":
        name = input("  Word: ")
        phone = input("  Translation: ")
        add_word(conn, name, phone)
    elif cmd == "delete":
        ID = input("  ID: ")
        delete_word(conn, ID)
    elif cmd == "help":
        help_list()
    elif cmd == "quit":
        save_dict(conn)
        exit()
