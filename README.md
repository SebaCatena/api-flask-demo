# API Flask Demo

Aplicación web hecha con **Flask** que consume la API pública de [JSONPlaceholder](https://jsonplaceholder.typicode.com/): lista publicaciones, permite buscarlas por título y ver el detalle de cada una.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1-000000?logo=flask&logoColor=white)
![Tests](https://github.com/SebaCatena/api-flask-demo/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-green)

## Demo

<!-- Cuando lo despliegues en Render/Railway, reemplazá esta línea por el link. -->
Próximamente: deploy en Render.

## Funcionalidades

- Listado de las primeras 5 publicaciones obtenidas desde una API externa.
- Búsqueda por título sin distinguir mayúsculas/minúsculas.
- Vista de detalle por ID.
- Manejo de errores de la API externa (timeout y respuesta inválida).
- Tests automatizados con `pytest` y linting con `ruff` en GitHub Actions.

## Stack

- **Python 3.10+**
- **Flask 3.1**
- **Requests** (cliente HTTP)
- **Pytest** + **Ruff** (calidad)
- **GitHub Actions** (CI)

## Cómo correrlo

```bash
git clone https://github.com/SebaCatena/api-flask-demo.git
cd api-flask-demo

python -m venv .venv

# Windows (PowerShell)
.\.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
flask --app app run --debug
```

Abrí <http://127.0.0.1:5000>.

> En Windows usá siempre `flask run`. `gunicorn` viene en `requirements.txt` para el deploy en Linux (Render/Railway), no para correrlo localmente.

Para probar los tests:

```bash
pip install -r requirements-dev.txt
pytest -q
ruff check .
```

## Deploy en Render (gratis)

1. Creá una cuenta en [render.com](https://render.com) y conectá tu GitHub.
2. **New → Web Service** → elegí el repo `api-flask-demo`.
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn app:app`
5. Deploy. Cuando termine, copiá la URL y pegala en la sección **Demo** de este README.

## Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| `GET` | `/` | Lista publicaciones. Acepta `?search=texto`. |
| `GET` | `/post/<id>` | Detalle de una publicación. |

## Estructura

```
api-flask-demo/
├─ app.py                  # rutas y lógica de la aplicación
├─ templates/
│  ├─ posts.html           # listado + búsqueda
│  └─ post_detail.html     # detalle
├─ tests/
│  └─ test_app.py          # tests de endpoints con la API mockeada
├─ .github/workflows/ci.yml
├─ requirements.txt
└─ requirements-dev.txt
```

## Decisiones técnicas

- **Timeout explícito** (`5 s`) en cada request saliente: evita que un worker quede colgado si la API externa falla.
- **Manejo de errores**: la vista muestra un mensaje amigable en lugar de un 500 cuando la API no responde.
- **Debug desactivado por defecto**: se habilita solo con `FLASK_DEBUG=1`, para no exponer el depurador de Werkzeug en producción.
- **Tests sin red**: los tests mockean `requests.get`, así que corren rápido y no dependen de un servicio externo.

## Seguridad

- No hay credenciales ni secretos en el código.
- En producción usá un servidor WSGI (`gunicorn app:app` o `waitress-serve app:app`), nunca el servidor de desarrollo.
- Jinja2 escapa las variables por defecto: no se usa `|safe`.

## Roadmap

- [ ] Cachear las publicaciones para reducir llamadas a la API.
- [ ] Paginación.
- [ ] Tests de integración con la API real (marcados como opcionales).
- [ ] Deploy público con URL en este README.

## Licencia

MIT © 2025 Sebastián Catena
