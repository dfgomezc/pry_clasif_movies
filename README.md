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
La Película de Mario 

http://20.62.126.193:5000/predict/?Plot=Italian-American%20brothers%20Mario%20and%20Luigi%20have%20recently%20started%20a%20plumbing%20business%20in%20Brooklyn%2C%20to%20the%20derision%20of%20their%20ex-employer%20Spike%20and%20the%20disapproval%20of%20their%20father.%20After%20seeing%20a%20significant%20water%20main%20leak%20on%20the%20news%2C%20Mario%20and%20Luigi%20go%20underground%20to%20fix%20it%20but%20are%20sucked%20into%20a%20Warp%20Pipe%20and%20separated.%20%20Mario%20lands%20in%20the%20Mushroom%20Kingdom%2C%20ruled%20by%20Princess%20Peach%2C%20while%20Luigi%20lands%20in%20the%20Dark%20Lands%2C%20ruled%20by%20the%20evil%20Koopa%20king%20Bowser.%20Bowser%20seeks%20to%20marry%20Peach%20and%20will%20destroy%20the%20Mushroom%20Kingdom%20using%20a%20Super%20Star%20if%20she%20refuses.%20He%20imprisons%20Luigi%20to%20threaten%20Mario%2C%20whom%20he%20sees%20as%20competition%20for%20Peach's%20love.%20Mario%20meets%20Toad%2C%20who%20takes%20him%20to%20Peach.%20Peach%20plans%20to%20ally%20with%20the%20primate%20Kongs%20to%20help%20repel%20Bowser%20and%20allows%20Mario%20and%20Toad%20to%20travel%20with%20her.%20She%20also%20tells%20Mario%20that%20she%20ended%20up%20in%20the%20Mushroom%20Kingdom%20as%20a%20baby%2C%20where%20the%20Toads%20took%20her%20in%20and%20eventually%20made%20her%20their%20leader.%20In%20the%20Jungle%20Kingdom%2C%20King%20Cranky%20Kong%20agrees%20to%20help%20on%20the%20condition%20that%20Mario%20defeats%20his%20son%2C%20Donkey%20Kong%2C%20in%20a%20fight.%20Despite%20Donkey%20Kong's%20immense%20strength%2C%20Mario%20is%20much%20faster%20and%20defeats%20him%20using%20a%20Cat%20Suit.%20%20Mario%2C%20Peach%2C%20Toad%2C%20and%20the%20Kongs%20use%20karts%20to%20drive%20back%20to%20the%20Mushroom%20Kingdom%2C%20but%20Bowser's%20army%20ambushes%20them%20on%20Rainbow%20Road.%20When%20a%20blue-shelled%20Koopa%20General%20destroys%20part%20of%20the%20road%20in%20a%20kamikaze%20attack%2C%20Mario%20and%20Donkey%20Kong%20plummet%20to%20the%20ocean%20while%20the%20other%20Kongs%20are%20captured.%20Peach%20and%20Toad%20return%20to%20the%20Mushroom%20Kingdom%20and%20urge%20the%20citizens%20to%20evacuate.%20Bowser%20arrives%20aboard%20his%20flying%20castle%20and%20proposes%20to%20Peach%2C%20who%20reluctantly%20accepts%20after%20Bowser's%20advisor%20Kamek%20tortures%20Toad.%20Mario%20and%20Donkey%20Kong%2C%20having%20been%20eaten%20by%20an%20eel-like%20Maw-Ray%2C%20learn%20they%20both%20want%20the%20respect%20of%20their%20fathers.%20They%20escape%20the%20Maw-Ray%20by%20riding%20a%20rocket%20from%20Donkey%20Kong's%20kart%20and%20hurry%20to%20Bowser%20and%20Peach's%20wedding.

Día de la Independencia

http://20.62.126.193:5000/predict/?Plot=U.S.%20Marine%20Captain%20Steven%20Hiller%20and%20his%20unit%2C%20the%20Black%20Knights%20fighter%20squadron%20out%20of%20MCAS%20El%20Toro%2C%20are%20called%20back%20from%20fourth%20of%20July%20leave%20to%20defend%20Los%20Angeles%3B%20his%20girlfriend%2C%20Jasmine%20Dubrow%2C%20decides%20to%20flee%20the%20city%20with%20her%20son%2C%20Dylan.%20Retired%20combat%20pilot%20Russell%20Casse%2C%20now%20an%20alcoholic%20single%20stepfather%20and%20crop%20duster%2C%20sees%20this%20as%20vindication%20of%20the%20alien%20abduction%20he%20has%20been%20claiming%20for%20years.%20In%20New%20York%20City%2C%20technician%20David%20Levinson%20decodes%20a%20signal%20embedded%20within%20global%20satellite%20transmissions%2C%20realizing%20it%20is%20the%20aliens%27%20countdown%20for%20a%20coordinated%20attack.%20With%20help%20from%20his%20ex-wife%2C%20White%20House%20Communications%20Director%20Constance%20Spano%2C%20David%20and%20his%20father%20Julius%20reach%20the%20Oval%20Office%20and%20alert%20President%20Thomas%20Whitmore.