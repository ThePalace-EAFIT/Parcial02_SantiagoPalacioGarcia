## Pregunta de Analisis

Para integrar con un servicio que persiste el historial, haría el cálculo independiente y comounicaria el resultado por un sistema asincrónico con mensajes: publico un evento "calculo.realizado" y un worker guarda en la BD externa. Esto reduce acoplamiento, mejora resiliencia/escala y permite reintentos automáticos, usaria idempotencia (request_id), variables de entorno para configuración y trazabilidad (correlation-id).

## Correr el codigo 

 - Instalar Flask

Ejecutar en consola:

 - export FLASK_APP=app.py

 - flask run --host=0.0.0.0 --port=8000

Probar en el navegador con la URL:

  - http://127.0.0.1:8000/api/v1/factorial/5
