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

4. Explore y preprocese los datos:
