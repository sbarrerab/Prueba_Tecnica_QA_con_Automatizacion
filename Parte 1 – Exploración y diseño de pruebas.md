# Contexto 
**Portal Público Seleccionado:** https://www.sisben.gov.co/Paginas/landing.html

# Parte 1 – Exploración y diseño de pruebas
**Funcionalidad Pública Seleccionada:** Consultar grupo Sisbén

## Descripción de la Funcionalidad
La opción “Consultar grupo Sisbén” es un servicio que le permite al ciudadano digitar sus datos (tipo y número de documento) y consultar su clasificación socioeconómica oficial según sus condiciones de vida e ingresos. Esta información es utilizada por el gobierno para determinar el acceso a subsidios y programas sociales.

## Casos de Prueba

1. Prueba Funcional:
   
    **ID:** PF001

    **Objetivo:** Validar que el sistema permita realizar la consulta socioeconómica en el apartado "Consulta tu grupo Sisbén"
   
    **Precondiciones:** Ninguna
   
    **Pasos:**
   
    1. Ir a la página del Sisbén
    2. Hacer clic en la opción “Consulta tu grupo Sisbén”
    3. Hacer clic en la opción “Tipo de documento” y seleccionar el tipo de documento correspondiente
    4. Ingresar el Número de Documento correctamente
    5. Dar clic en el botón [Consultar]
    
   
    **Resultado Esperado:** El sistema debe mostrar en pantalla la información de Sisbén relaciona con el documento consultado.

    **Resultado Obtenido:** El sistema muestra en pantalla la información de Sisbén relaciona con el documento consultado.
   
   <img width="1592" height="384" alt="image" src="https://github.com/user-attachments/assets/2f592ead-e9e8-4189-ac48-bc5aef1e8fef" />
   <img width="938" height="478" alt="image" src="https://github.com/user-attachments/assets/ef47b7d9-9831-4d53-81bd-53ef6858b33e" />
   <img width="968" height="217" alt="image" src="https://github.com/user-attachments/assets/49101230-0c5e-4764-ac85-d5e562e46d0e" />
   <img width="972" height="216" alt="image" src="https://github.com/user-attachments/assets/00b4457b-f34e-494e-90c5-3d7ec3a06eab" />
   <img width="1208" height="816" alt="image" src="https://github.com/user-attachments/assets/676581d2-63c1-48f8-85e7-db0596ac61c7" />

   **Resultado Final:** EXITOSO

2. Prueba Funcional:
   
    **ID:** PF002

    **Objetivo:** Validar que el sistema permita descargar la consulta socioeconómica realizada en el apartado "Consulta tu grupo Sisbén"
   
    **Precondiciones:** Ninguna
   
    **Pasos:**
   
    1. Ir a la página del Sisbén
    2. Hacer clic en la opción “Consulta tu grupo Sisbén”
    3. Hacer clic en la opción “Tipo de documento” y seleccionar el tipo de documento correspondiente
    4. Ingresar el Número de Documento correctamente
    5. Dar clic en el botón [Consultar]
    6. Dar clic en el ícono de impresión
    7. Valiar que se realice la descarga
    8. Corroborar que la información descargada coincida con la información expuesta en la consulta
    
   
    **Resultado Esperado:** El sistema debe permitir descargar la información de Sisbén relaciona con el documento consultado.

    **Resultado Obtenido:** El sistema permite descargar la información de Sisbén relaciona con el documento consultado.
   
   <img width="1592" height="384" alt="image" src="https://github.com/user-attachments/assets/2f592ead-e9e8-4189-ac48-bc5aef1e8fef" />
   <img width="938" height="478" alt="image" src="https://github.com/user-attachments/assets/ef47b7d9-9831-4d53-81bd-53ef6858b33e" />
   <img width="968" height="217" alt="image" src="https://github.com/user-attachments/assets/49101230-0c5e-4764-ac85-d5e562e46d0e" />
   <img width="972" height="216" alt="image" src="https://github.com/user-attachments/assets/00b4457b-f34e-494e-90c5-3d7ec3a06eab" />
   <img width="1208" height="816" alt="image" src="https://github.com/user-attachments/assets/676581d2-63c1-48f8-85e7-db0596ac61c7" />

   <img width="1120" height="409" alt="image" src="https://github.com/user-attachments/assets/32fe9994-6f4d-4f01-aa26-86179b618da6" />
   <img width="1218" height="805" alt="image" src="https://github.com/user-attachments/assets/933c6a45-9aa3-4773-8924-2835d02f076e" />


   **Resultado Final:** EXITOSO
    

3. Prueba Negativa:

    **ID:** PN001

    **Objetivo:** Validar que el sistema detecte inconsistencias en el correo al radicar PQRSD
   
    **Precondiciones:** Ninguna
   
    **Pasos:**
   
    1. Ir a la página del Sisbén
    2. Desplegar la opción de "Atención al Ciudadano"
    3. Hacer clic en la opción “Peticiones, quejas, reclamos, solicitudes y denuncias”
    4. Hacer clic en la opción “aquí” del titulo *Registra tu PQRSD*
    5. Ingresar Correo Electrónico correctamente
    6. Ingresar la Confirmación del Correo Electrónico incorrectamente
       
    **Resultado Esperado:** El sistema debe notificar al usuario inconsistencia entre el Correo Electrónico y la Confirmación del Correo Electrónico.

    **Resultado Obtenido:** El sistema notifica inconsistencia entre el Correo Electrónico y la Confirmación del Correo Electrónico.
   
   <img width="1788" height="551" alt="image" src="https://github.com/user-attachments/assets/0f4ba79c-b439-4902-aaff-16ddb129ad10" />
   <img width="845" height="618" alt="image" src="https://github.com/user-attachments/assets/4ea5ab67-786b-4595-a87a-0b1f28e479a3" />
   <img width="1691" height="506" alt="image" src="https://github.com/user-attachments/assets/bfb6e8e7-d4a3-4fff-b2a2-c6611fa96b10" />
   <img width="1714" height="575" alt="image" src="https://github.com/user-attachments/assets/24d4bc35-1433-4922-9ee4-4b2f40fdb2bb" />

   **Resultado Final:** EXITOSO
   
4. Prueba de Usabilidad o Validación Visual:
5. Prueba Smoke:


# Parte 2 – Documentación de bugs reales
