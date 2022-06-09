import psycopg2
conn = psycopg2.connect(
   host="localhost",
   database="postgres",
   user="postgres",
   password="password"
)

def read_dict(C):
    cur = C.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows
def add_word(C, word, translation):
    cur = C.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
def delete_word(C, ID):
    cur = C.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
def save_dict(C):
    cur = C.cursor()
    cur.execute("COMMIT;")
    cur.close()
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
