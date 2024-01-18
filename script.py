from DatabaseManager import DatabaseManager
from Question import Question
import random

def shuffle_questions(question_list):
    shuffled_array = question_list.copy()  # Se crea una copia para no modificar el array original
    random.shuffle(shuffled_array)
    return shuffled_array    

def game_questions(question_list, accumulated, profit, helpP, help5050):
    total = accumulated
    for q in question_list:
        question = Question(q)
        question.show_question()  
        print("¡Ayudas!\n")
        if not helpP:
            print("1. Ayuda del público\n")
        if not help5050:
            print("2. 50 / 50 \n")
        user_response = input("Ingresa la opción correcta o 'R' para retirarte: \n").lower()
        if user_response == '1':
            if helpP:
                print(print(f"\n Ya hizo uso de esta ayuda \n"))
                user_response = input("Ingresa la opción correcta o 'R' para retirarte: \n").lower()
            else:
                print(f"\n Opción sugerida por el público: {random.choice(['A', 'B', 'C', 'D'])}")
                helpP = True
                user_response = input("Ingresa la opción correcta o 'R' para retirarte: \n").lower()
        if user_response == '2':
            if help5050:
                print(print(f"\n Ya hizo uso de esta ayuda \n"))
                user_response = input("Ingresa la opción correcta o 'R' para retirarte: \n").lower()
            else:
                question.show_question50()
                help5050 = True
                user_response = input("Ingresa la opción correcta o 'R' para retirarte: \n").lower()
        if user_response == 'r':
            print(f"\nTe retiras con ${total}. ¡Gracias por jugar!")
            return accumulated, True, helpP, help5050
        if question.check_answer(user_response):
            print("\n¡Respuesta correcta!\n")
            accumulated += profit 
            print(f"Tu acumulado actual es de ${accumulated}\n")
        else:
            print("Respuesta incorrecta. Fin del juego.\n")
            print(f"Tu acumulado actual es de ${total}\n")
            return accumulated, True, helpP, help5050 
    return accumulated, False, helpP, help5050



def main():
    db_manager = DatabaseManager(
        host="localhost",
        user="root",
        password="root",
        database="database"
    )
    try:
        question_list_shuffled1 = shuffle_questions(db_manager.get_questions(1))
        question_list_shuffled2 = shuffle_questions(db_manager.get_questions(2))
        question_list_shuffled3 = shuffle_questions(db_manager.get_questions(3))
        question_list_shuffled4 = shuffle_questions(db_manager.get_questions(4))
        list_question = [question_list_shuffled1, question_list_shuffled2, question_list_shuffled3, question_list_shuffled4]
    finally:
        # Cierra la conexión al finalizar
        db_manager.close_connection()

    print("###############################################\n")
    print("¡Bienvenido a ¿Quién Quiere Ser Millonario?!\n")
    print("###############################################\n")
    
    total_accumulated = 0
    current_profit = 100
    public_help = False
    help50 = False
    for questions in list_question:
        total_accumulated, finish, public_help, help50 = game_questions(questions, total_accumulated, current_profit, public_help, help50)
        if finish:
            break
        else:
            if current_profit!=100000:
                print("##############################################################################################\n")
                print(f"\n¡Felicidades! Has pasado al siguiente nivel\n")    
                print(f"Tu acumulado seguro hasta el momento es de ${total_accumulated}\n")
                print("##############################################################################################\n")
                current_profit *= 10
    if finish==False:
        print("##############################################################################################\n")
        print(f"\n¡Felicidades! Has respondido todas las preguntas correctamente y has ganado ${total_accumulated}.\n")
        print("##############################################################################################\n")
        
if __name__ == "__main__":
    main()