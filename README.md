# Centro Cultural Amadeus
Página web sobre un instituto ficticio de música hecha en Django

## Instrucciones de instalación

### **1- Descarga**

Descargar el repositorio utilizando la pestaña **<> Code**, y descargar el archivo en formato zip. Descomprimirlo y extraerlo en el directorio deseado. Alternativamente, puede descargarse mediante **git clone** dentro de esa misma pestaña (Requiere previa instalación de git. Luego de instalarlo, abrir una ventana de git bash y colocarse en el directorio deseado con el comando `cd <ruta de trabajo>` , o alternativamente ejecutar la ventana en dicho directorio pulsando click derecho, **Open git Bash here**)

### **2- Creación y ejecución de entorno virtual**

Con el comando `python -m venv "nombre_deseado"` se puede crear un entorno virtual. Luego de posicionarse con cd en el directorio de trabajo, se puede activarlo copiando su ruta de acceso relativa (`nombre_deseado\Scripts\activate`).

### **3- Instalación de requerimentos**

Una vez activado el entorno virtual, instalar django y demás requerimentos con el comando `pip install -r requirements.txt`


### **4- Ejecución de servidor**

Ahora podemos ejecutar el comando: 
`python manage.py runserver` lo que ejecutará nuestro servidor. Podemos acceder al mismo desde cualquier navegador escribiendo `localhost:8000` en la barra de direcciones y presionando enter.
