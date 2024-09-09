# Prueba Técnica Ecommerce - Fullstack

Aplicación web Full Stack de Ecommerce que permite a los usuarios registrarse, iniciar sesión, ver una lista de productos, agregar productos al carrito y realizar pedidos.

## Tabla de Contenidos

- [Tecnologías](#tecnologías)
- [Instalación](#instalación)
- [Endpoints](#endpoints)
    - [Usuarios](#usuarios)
    - [Productos](#productos)
- [Pruebas](#pruebas)

## Tecnologías

- **Frontend:**

    [![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/es/docs/Web/HTML)[![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/es/docs/Web/CSS)[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/es/docs/Web/JavaScript)[![Vue.js](https://img.shields.io/badge/Vue.js-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white)](https://vuejs.org/)

- **Backend:**

    [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://docs.djangoproject.com/en/5.0/)[![Django REST Framework](https://img.shields.io/badge/Django%20REST%20Framework-0082C9?style=for-the-badge&logo=django&logoColor=white)](https://www.django-rest-framework.org/)

- **Base de Datos:**

    [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/docs/)

- **Autenticación:**

    [![JSON Web Token](https://img.shields.io/badge/JSON%20Web%20Token-000000?style=for-the-badge&logo=json-web-tokens&logoColor=white)](https://jwt.io/)

## Instalación

### Prerrequisitos

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu sistema:

- Python (versión 3.12.2)
- PostgreSQL (versión 16)
- pip (administrador de paquetes de Python)
- Node.js (versión 20.11.1)

### Pasos de Instalación

1. **Clona este repositorio:**

    ```bash
    git clone https://github.com/JohannGaviria/PruebaTecnicaEcommerce.git
    ```

2. **Crear el entorno virtual para el backend:**

    Utiliza `virtualenv` o otro gestor de entornos virtuales

    ```bash
    cd backend
    pip install virtualenv
    python -m virtualenv venv
    ```

3. **Instalar las dependencias del backend:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configurar la base de datos:**

    - Crea una base de datos PostgreSQL en tu entorno.
    - Crea un archivo `.env` en el directorio `backend` de tu proyecto y define las variables de entorno correspondientes:
        - `ENGINE` -> Tipo de base de datos
        - `NAME` -> Nombre de la base de datos
        - `USER` -> Usuario de la base de datos
        - `PASSWORD` -> Contraseña de la base de datos
        - `HOST` -> Host de la base de datos
        - `PORT` -> Puerto de la base de datos

5. **Crear las migraciones y aplicarlas:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Iniciar el servidor frontend:**

    ```bash
    cd ../frontend
    npm install
    npm run serve
    ```

7. **Iniciar el servidor backend:**

    ```bash
    cd ../backend
    python manage.py runserver
    ```

¡Listo! El proyecto debería estar en funcionamiento en tu entorno local. Puedes acceder a la interfaz de usuario desde tu navegador web visitando `http://localhost:8080` y la API backend desde `http://localhost:8000`.

## Endpoints

### Usuarios

| Nombre | Método | Url |
|:------ | :----- | :-- |
| [Registro de Usuarios](#registro-de-usuario) | `POST` | `/api/users/register` |
| [Inicio de Sesión de Usuarios](#inicio-de-sesión-de-usuario) | `POST` | `/api/users/login` |

#### registro de usuario

```http
POST /api/users/register
```

##### Parámetros

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Requerido**. Nombre del usuario |
| `email` | `string` | **Requerido**.  Correo electrónico del usuario |
| `password` | `string` | **Requerido**. Contraseña del usuario |

#### Inicio de sesión de usuario

##### Método HTTP

```http
POST /api/users/login
```

##### Parámetros

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `email` | `string` | **Requerido**.  Correo electrónico del usuario |
| `password` | `string` | **Requerido**. Contraseña del usuario |

### Productos

| Nombre | Método | Url |
|:------ | :----- | :-- |
| [Obtener lista de productos](#obtener-productos) | `GET` | `/api/products/` |

#### Obtener lista de productos

##### Método HTTP

```http
GET /api/products/

GET /api/products/?page=<number_page>
```

##### Parámetros

| Parámetro | Tipo     | Descripción                |
| :-------- | :------- | :------------------------- |
| `?page=<number_page>` | `int` | Numero de la paginacion |

**Nota:** Utiliza el siguiente comando para llenar la base de datos con productos de muestra

```bash
cd backend
python manage.py populate_products
```

## Pruebas

### Backend

Para garantizar que el backend funcione correctamente, realiza las siguientes pruebas:

- **Ejecutar Todas las Pruebas del Backend**

    Ejecuta todas las pruebas del backend para verificar el funcionamiento general de la aplicación:

    ```bash
    python manage.py test
    ```

- **Ejecutar Pruebas Específicas de la Aplicación de Usuarios**

    Si deseas ejecutar solo las pruebas relacionadas con la aplicación de usuarios, utiliza el siguiente comando:

    ```bash
    python manage.py test users.tests
    ```

    Estas pruebas se encargan de verificar que los endpoints de register y login funcionen correctamente.

- **Ejecutar Pruebas Especificas de la Aplicación de Productos**

    Si deseas ejecutar solo las pruebas relacionadas con la aplicación de productos, utiliza el siguiente comando:

    ```bash
    python manage.py test products.tests
    ```

    Estas pruebas se encargan de verificar que el endpoint de product_list funcione correctamente.
