from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Lista de 30 búsquedas
busquedas = [
"cómo mejorar la productividad personal",
    "mejores libros de desarrollo personal",
    "qué es el metaverso",
    "cómo funciona la computación cuántica",
    "trucos para dormir mejor",
    "cómo crear un canal de YouTube exitoso",
    "alimentos ricos en proteína vegetal",
    "diferencias entre frontend y backend",
    "cuánto gana un desarrollador web",
    "cómo protegerse de ciberataques",
    "aplicaciones para meditar gratis",
    "mejores documentales de naturaleza",
    "cómo aprender a programar desde cero",
    "qué es el diseño UX/UI",
    "cómo usar Notion para organizarse",
    "ventajas del trabajo remoto",
    "qué es una API y cómo funciona",
    "mejores herramientas de IA para estudiantes",
    "cómo estudiar mejor para un examen",
    "ejercicios para fortalecer rodillas",
    "cómo crear una tienda en línea",
    "qué es el marketing digital",
    "consejos para entrevistas de trabajo",
    "diferencia entre HTTP y HTTPS",
    "cómo empezar un podcast",
    "mejores lenguajes de programación en 2025",
    "cómo hacer presupuesto personal",
    "qué es DevOps y para qué sirve",
    "cómo ser freelancer en tecnología",
    "mejores hábitos para la salud mental"
]

# Configura el servicio de EdgeDriver con la ruta correcta
service = Service(executable_path=r"C:\Users\Dante\OneDrive\Documentos\Backup\Cursos\Bing\V138\msedgedriver.exe")
options = webdriver.EdgeOptions()

# Inicializa el driver con Service y Options
driver = webdriver.Edge(service=service, options=options)

# Ciclo de búsquedas
for termino in busquedas:
    driver.get("https://www.bing.com")
    time.sleep(2)

    search_box = driver.find_element("name", "q")
    search_box.clear()
    search_box.send_keys(termino)
    search_box.send_keys(Keys.RETURN)

    print(f"Búsqueda realizada: {termino}")
    time.sleep(5)


driver.quit()
print("Todas las búsquedas fueron realizadas.")