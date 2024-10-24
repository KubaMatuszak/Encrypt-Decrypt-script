from Utils.encdec_handler import EncDec
from Utils.file_management import FileMan
from Utils.Sql_handler import SqlHandler
file_dialog = FileMan()
cesar = EncDec()

print("Chcesz zakodować czy odkodować plik?")
action = input()
if action=='zakodować':

    print('Wybierz plik do zakodowania...')
    file = file_dialog.file_load()

    print('O ile przesunąć litery w pliku?')
    num = int(input())
    coded_file = cesar.cesar_encrypt(file,num)

    print('Gdzie zapisać plik: SQL/Dysk')
    save_action = input()
    if save_action == 'SQL':
        sql = SqlHandler('DB_SERVER_NAME','DB_NAME')
        sql.write(coded_file)

    elif save_action == 'Dysk':
        print('Wybierz miejsce zapisu')
        file_dialog.file_save(coded_file)
    else:
        print("Błąd składni :/")

elif action == 'odkodować':

    print('Wybierz plik do odkodowania...')
    file = file_dialog.file_load()

    print('O ile przesunąłeś litery w pliku?')
    num = int(input())
    coded_file = cesar.cesar_decrypt(file, num)

    print('Gdzie zapisać odkodowany plik?')
    file_dialog.file_save(coded_file)
else:
    print('Błąd składni :/ ')