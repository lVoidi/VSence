import pypresence
import psutil
import random
import time
import os

start = time.time()
pid = os.getpid()

philosophy = {
    "Maquiavelo": [
        "La naturaleza de los pueblos es muy poco constante", 
        "Pocos ven lo que somos, pero todos ven lo que aparentamos",
        "Los hombres olvidan con mayor rapidez la muerte de su padre que la pérdida de su patrimonio",
        "El que no detecta los males cuando nacen, no es verdaderamente prudente", 
        "Puede combinarse perfectamente el ser temido y el no ser odiado",
        "El que engaña con arte halla siempre gente que se deja engañar",
        "Uno debe de ser un zorro con el fin de reconocer las trampas y un león para ahuyentar a los lobos",
        "Vale más hacer y arrepentirse, que no hacer y arrepentirse"
    ], 
    "Robert Greene": [
        "No permita que el éxito se le suba a la cabeza", 
        "A veces cualquier emoción es mejor que el aburrimiento de la seguridad",
        "Aumenta tu poder y tu imagen ganará en fiabilidad",
        "Cada ser humano es una creación completamente única",
        "Conoce a quién te enfrentas"
    ],
    "Nietszche": [
        "Dios ha muerto",
        "Lo que no me mata, me hará más fuerte",
        "El hombre, en su orgullo, creó a Dios a su imagen y semejanza",
        "Olvidar nuestro propósito es la forma más común de estupidez",
        "Todo lo que se hace por amor está más allá del bien y del mal"
    ]
}

def get_philosophy_status() -> dict:
    images = {
        "Nietszche": "https://hips.hearstapps.com/hmg-prod/images/gettyimages-515350818jpg-.jpg",
        "Robert Greene": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Robert_Greene_B%26W.jpg/1200px-Robert_Greene_B%26W.jpg",
        "Maquiavelo": "https://www.elviejotopo.com/wp-content/uploads/2018/06/nicolas-maquiavelo-realmente-pensaba-justifica.jpg"
    }
    random_philosopher = random.choice(list(philosophy.keys()))
    return {
        "img": images[random_philosopher],
        "name": random_philosopher,
        "phrase": random.choice(philosophy[random_philosopher])
    }

def is_discord_opened() -> bool:
    process_list = (process.name() for process in psutil.process_iter())
    return "Discord.exe" in process_list

def update_uptime() -> str:
    uptime = int(time.time() - start)
    return f"{uptime//(60**2)}:{uptime//60}:{uptime%60}"

def main():
    presence = pypresence.Presence(client_id="1115295203423690833")
    presence.connect()
    print("Succesfully connected to the client")
    philosophy_status = get_philosophy_status()
    while True:
        try:
            if int(time.time() - start)%30 == 0:
                philosophy_status = get_philosophy_status()
            # These are the default values for this rich presence. Modify them 
            # here
            presence.update(
                pid=pid,
                state=philosophy_status["name"], 
                details=philosophy_status["phrase"], 
                large_image=philosophy_status["img"],
                large_text=f"U p t i m e  => {update_uptime()}", 
                small_text="Philosophy",
                buttons=[{"label": "lVoidi github", "url": "https://github.com/lvoidi"}]
            )
        except KeyboardInterrupt:
            print("Closing program...")
            presence.close()
            presence.clear(os.getpid())

if __name__ == "__main__":
    while not is_discord_opened():
        print("Discord is not opened. Waiting some time.")
        time.sleep(10)
    
    try:
        main()
    except KeyboardInterrupt:
        print("Saliendo del programa...")