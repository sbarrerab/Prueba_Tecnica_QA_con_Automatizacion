# Contexto 
**Portal Público Seleccionado:** [https://www.colpensiones.gov.co](https://www.sisben.gov.co/Paginas/landing.html)

# Parte 1 – Exploración y diseño de pruebas
**Funcionalidad Pública Seleccionada:** Consultar grupo Sisbén

## Descripción de la Funcionalidad
La opción “Consultar grupo Sisbén” es un servicio que le permite al ciudadano digitar sus datos (tipo y número de documento) y consultar su clasificación socioeconómica oficial según sus condiciones de vida e ingresos. Esta información es utilizada por el gobierno para determinar el acceso a subsidios y programas sociales.

## Casos de Prueba

1. Prueba Funcional:
   
    **Objetivo:** Validar que el sistema redirija al apartado de PQRSD
   
    **Precondiciones:** Ninguna
   
    **Pasos:**
   
    1. Ir a la página del Sisbén
    2. Desplegar la opción de "Atención al Ciudadano"
    3. Hacer clic en la opción “Peticiones, quejas, reclamos, solicitudes y denuncias”
    4. Hacer clic en la opción “aquí” del titulo *Registra tu PQRSD*
   
    **Resultado Esperado:** El sistema redirije al formulario de radicación de PQRSD.

    **Resultado Obtenido:** El sistema redirije al formulario de radicación de PQRSD.

   <img width="1788" height="551" alt="image" src="https://github.com/user-attachments/assets/0f4ba79c-b439-4902-aaff-16ddb129ad10" />
   
   <img width="845" height="618" alt="image" src="https://github.com/user-attachments/assets/4ea5ab67-786b-4595-a87a-0b1f28e479a3" />
   
   <img width="1693" height="1392" alt="image" src="https://github.com/user-attachments/assets/d97d9407-bad2-4894-ab08-b18624d04a42" />

3. Prueba Funcional:
4. Prueba Negativa:
   
    **Objetivo:** Validar que el sistema detecte inconsistencias en el correo al radicar PQRSD
   
    **Precondiciones:** Ninguna
   
    **Pasos:**
   
    1. Ir a la página del Sisbén
    2. Desplegar la opción de "Atención al Ciudadano"
    3. Hacer clic en la opción “Peticiones, quejas, reclamos, solicitudes y denuncias”
    4. Hacer clic en la opción “aquí” del titulo *Registra tu PQRSD*
    5. Ingresar Correo Electrónico correctamente
    6. Ingresar la Confirmación del Correo Electrónico incorrectamente
       
    **Resultado Esperado:** El sistema notifica inconsistencia entre el Correo Electrónico y la Confirmación del Correo Electrónico.

    **Resultado Obtenido:** El sistema notifica inconsistencia entre el Correo Electrónico y la Confirmación del Correo Electrónico.
   
   <img width="1788" height="551" alt="image" src="https://github.com/user-attachments/assets/0f4ba79c-b439-4902-aaff-16ddb129ad10" />
   
   <img width="845" height="618" alt="image" src="https://github.com/user-attachments/assets/4ea5ab67-786b-4595-a87a-0b1f28e479a3" />
   
   <img width="1691" height="506" alt="image" src="https://github.com/user-attachments/assets/bfb6e8e7-d4a3-4fff-b2a2-c6611fa96b10" />
   
   <img width="1714" height="575" alt="image" src="https://github.com/user-attachments/assets/24d4bc35-1433-4922-9ee4-4b2f40fdb2bb" />

6. Prueba de Usabilidad o Validación Visual:
7. Prueba Smoke:


# Parte 2 – Documentación de bugs reales
