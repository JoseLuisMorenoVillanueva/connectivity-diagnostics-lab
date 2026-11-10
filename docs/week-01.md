# Semana 1 — entorno y Git

## Primera sesión (60–90 minutos)

1. Ejecuta `src/first_event.py` con el intérprete de tu entorno, siguiendo el README.
2. Explica qué es el diccionario `event` y cómo `json.dumps` lo convierte en texto.
3. Comprueba que el timestamp incluye zona horaria UTC.
4. Crea tu rama con `git switch -c exercise/week-01`.
5. Cambia device_id a device-002, result a failure y añade error_code con LAB_TIMEOUT.
6. Ejecuta de nuevo. Los valores son ficticios; no se ha producido un timeout real.
7. Inspecciona `git diff`, guarda con commit y sube la rama:
   `git push -u origin exercise/week-01`.
8. Escribe en `docs/learning-log.md` qué cambiaste y qué puedes explicar sin ayuda.

## Resto de la semana

- Realiza tres commits pequeños y comprueba `git log --oneline`.
- En una rama de práctica, crea un cambio temporal, haz commit y después
  `git revert HEAD`. Esto añade un commit que deshace el anterior.
- Clona el repositorio en otra carpeta o equipo y reproduce el ejemplo desde el README.
- Para continuar una rama publicada en una copia nueva: `git fetch origin` y
  `git switch --track origin/exercise/week-01`.
- No marques esta semana completada solo porque el ejemplo esté preparado.

## Criterio de salida

- [ ] Ejecuto desde una copia limpia.
- [ ] Entiendo diccionario frente a JSON.
- [ ] Puedo explicar commit, rama, push y pull.
- [ ] He probado revert en una rama de práctica.
- [ ] Sé alternar equipos sin perder cambios.

## Lecturas enfocadas

- [Entornos virtuales Python](https://docs.python.org/3.12/tutorial/venv.html)
- [Pro Git](https://git-scm.com/book/en/v2): Getting Started y Git Basics.

El script inicial y la configuración están preparados como punto de partida; los ejercicios anteriores siguen pendientes.
