from input import input_process

def brain():
    print("Asistente Virtual activado. Escribe 'salir' para cerrar.")
    while True:
        entrada = input("Process: ")

        if entrada == "exit":
            print("adios")
            break
        input_process(entrada)

if __name__ == "__main__":
    brain()