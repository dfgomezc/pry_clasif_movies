# **Proyecto de clasificación de películas**

Este es un proyecto de clasificación de películas que utiliza técnicas de aprendizaje automático para determinar las etiquetas o categorías adecuadas para cada película. El objetivo es proporcionar una herramienta que ayude a organizar y categorizar películas en función de sus características y contenido.

## **Estructura del proyecto**
El proyecto está organizado de la siguiente manera:

- **.gitignore:** archivo que indica qué archivos y carpetas no se deben incluir en el repositorio.
- **requirements.txt:** archivo que contiene las librerías necesarias para ejecutar el proyecto y sus respectivas versiones.
- **DATA/:** carpeta que contiene los conjuntos de datos utilizados para entrenar y evaluar los modelos de clasificación.
- **SCRIPTS/:** carpeta que contiene los scripts y notebooks utilizados para explorar y preprocesar los datos, entrenar los modelos y evaluar su rendimiento.
- **MODELS/:** carpeta que contiene los modelos de clasificación entrenados y guardados en formato compatible con la biblioteca utilizada.
- **OUTPUT/:** carpeta que contiene los resultados de la clasificación, como etiquetas asignadas a películas y métricas de rendimiento.

## **Funcionamiento**
Para utilizar este proyecto de clasificación de películas, se deben seguir los siguientes pasos:

1. Explorar y preprocesar los datos: utilizando los scripts y notebooks proporcionados en la carpeta `SCRIPTS`, se pueden realizar tareas como carga de datos, limpieza, transformación y extracción de características relevantes.

2. Entrenar el modelo de clasificación: utilizando los datos preprocesados, se pueden entrenar diferentes modelos de clasificación, como clasificadores basados en árboles de decisión, clasificadores de vectores de soporte (SVM) o modelos de clasificación basados en redes neuronales. Los scripts y notebooks en la carpeta `SCRIPTS` proporcionan ejemplos de cómo entrenar modelos utilizando diferentes algoritmos y técnicas.

3. Evaluar el rendimiento del modelo: una vez que se entrena el modelo, es importante evaluar su rendimiento utilizando métricas adecuadas, como precisión, recall y F1-score. Los scripts y notebooks en la carpeta `SCRIPTS` también proporcionan ejemplos de cómo evaluar el rendimiento de los modelos.

4. Aplicar el modelo a nuevas películas: una vez que el modelo está entrenado y se ha evaluado su rendimiento, se puede utilizar para clasificar nuevas películas. Esto implica aplicar el modelo a características relevantes de la película y asignarle las etiquetas o categorías correspondientes.

## **Requerimientos**
Es necesario tener instalado Python 3 y las librerías que se encuentran en el archivo `requirements.txt`. Para instalar las librerías necesarias, se puede utilizar el siguiente comando en la terminal:

```cmd
pip install -r requirements.txt
```

## **Instrucciones de uso**
Para utilizar este proyecto de clasificación de películas, siga los siguientes pasos:

1. Clone este repositorio en su máquina local:

```cmd
git clone https://github.com/tu_usuario/tu_repositorio.git
```

2. Navegue hasta la carpeta donde se encuentra el proyecto:

```cmd
cd tu_repositorio
```

3. Instale las librerías necesarias:

```cmd
pip install -r requirements.txt
```

4. Cambiar el directorio a la carpeta SCRPITS:

```cmd
cd SCRIPTS
```

5. Correr la aplicacón api.py

```cmd
python api.py
```

6. Si el SO es Windows, para poder acceder a la aplicación remotamente es necesario apagar el firewall público y privado. De lo contrario no se permiten conexiones externas a la máquina. Se puede hacer manualmente o a través de la ventan de comandos:

```cmd
netsh advfirewall set allprofiles state off
```

7. Explore y preprocese los datos:

Pruebe la aplicación haciendo requests con la trama de las películas que desee. Recuerde usar la dirección IP provista y el puerto 5000. 

```cmd
IP: 20.62.126.193
Port: 5000
```

8. Enlaces de prueba:

```
http://20.62.126.193:5000/predict/?Plot=john%20singleton%20'%20s%20portrayal%20of%20social%20problems%20in%20inner%20-%20city%20los%20angeles%20takes%20the%20form%20of%20a%20tale%20of%20three%20friends%20growing%20up%20together%20%20'%20in%20the%20%20'%20hood%20.%20%20'%20%20half%20-%20brothers%20doughboy%20and%20ricky%20baker%20are%20foils%20for%20each%20other%20'%20s%20personality%20%2C%20%20presenting%20very%20different%20approaches%20to%20the%20tough%20lives%20they%20face%20.%20%20ricky%20is%20the%20%20'%20all%20-%20american%20'%20%20athlete%20%2C%20%20looking%20to%20win%20a%20football%20scholarship%20to%20usc%20and%20seeks%20salvation%20through%20sports%20%2C%20%20while%20%20'%20dough%20'%20%20succumbs%20to%20the%20violence%20%2C%20%20alcohol%20%2C%20%20and%20crime%20surrounding%20him%20in%20his%20environment%20%2C%20%20but%20maintains%20a%20strong%20sense%20of%20pride%20and%20code%20of%20honor%20.%20%20between%20these%20two%20is%20their%20friend%20tre%20%2C%20%20who%20is%20lucky%20to%20have%20a%20father%20%2C%20%20%20'%20furious%20'%20%20styles%20%2C%20%20to%20teach%20him%20to%20have%20the%20strength%20of%20character%20to%20do%20what%20is%20right%20and%20to%20always%20take%20responsibility%20for%20his%20actions%20.
```
```
http://20.62.126.193:5000/predict/?Plot='when%20we%20go%20to%20sleep%20%2C%20%20two%20forces%20battle%20for%20our%20dreams%20%3A%20%20the%20storytellers%20%2C%20%20who%20give%20us%20good%20dreams%20%3B%20%20and%20the%20incubi%20%2C%20%20who%20give%20us%20nightmares%20.%20%20widower%20john%20sullivan%20is%20estranged%20from%20his%20young%20daughter%20emma%20%2C%20%20having%20been%20deemed%20unable%20to%20care%20for%20her%20.%20%20now%20on%20the%20edge%20of%20a%20huge%20investment%20deal%20with%20a%20major%20corporation%20%2C%20%20he%20is%20unaware%20that%20he%20is%20being%20stalked%20by%20an%20incubus%20.%20%20and%20on%20the%20city%20outskirts%20%2C%20%20a%20mysterious%20stranger%20named%20ink%20snatches%20little%20emma%20from%20her%20bed%20and%20escapes%20into%20the%20dream%20world%20%2C%20%20intent%20on%20selling%20her%20soul%20to%20the%20assembly%20of%20the%20incubi%20so%20that%20he%20may%20be%20allowed%20entry%20into%20their%20ranks%20.%20%20a%20small%20band%20of%20storytellers%20realizes%20that%20the%20only%20way%20to%20save%20emma%20is%20to%20reunite%20her%20with%20her%20father%20in%20the%20physical%20world%20%2C%20%20and%20they%20will%20do%20anything%20to%20make%20sure%20that%20this%20comes%20to%20pass%20.'
```