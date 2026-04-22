# Contexto 
**Portal Público Seleccionado:** https://www.sisben.gov.co/Paginas/landing.html

# Parte 1 – Exploración y diseño de pruebas
**Funcionalidad Pública Seleccionada:** Consultar grupo Sisbén

## Descripción de la Funcionalidad
La opción “Consultar grupo Sisbén” es un servicio que le permite al ciudadano digitar sus datos (tipo y número de documento) y consultar su clasificación socioeconómica oficial según sus condiciones de vida e ingresos. Esta información es utilizada por el gobierno para determinar el acceso a subsidios y programas sociales.

## Casos de Prueba

1. Prueba Funcional:
   
    **ID:** PF001

    **Objetivo:** Validar que el sistema permita realizar la consulta socioeconómica
   
    **Precondiciones:** Ninguna
   
    **Pasos:**
   
    1. Ir a la página del Sisbén
    2. Hacer clic en la opción “Consulta tu grupo Sisbén”
    3. Hacer clic en la opción “Tipo de documento” y seleccionar el tipo de documento correspondiente
    4. Ingresar el Número de Documento correctamente
    5. Dar clic en el botón [Consultar]
    
   
    **Resultado Esperado:** El sistema debe mostrar en pantalla la información de Sisbén relacionada con el documento consultado.

    **Resultado Obtenido:** El sistema muestra en pantalla la información de Sisbén relacionada con el documento consultado.
   
   <img width="1592" height="384" alt="image" src="https://github.com/user-attachments/assets/2f592ead-e9e8-4189-ac48-bc5aef1e8fef" />
   <img width="938" height="478" alt="image" src="https://github.com/user-attachments/assets/ef47b7d9-9831-4d53-81bd-53ef6858b33e" />
   <img width="968" height="217" alt="image" src="https://github.com/user-attachments/assets/49101230-0c5e-4764-ac85-d5e562e46d0e" />
   <img width="972" height="216" alt="image" src="https://github.com/user-attachments/assets/00b4457b-f34e-494e-90c5-3d7ec3a06eab" />
   <img width="1208" height="816" alt="image" src="https://github.com/user-attachments/assets/676581d2-63c1-48f8-85e7-db0596ac61c7" />

   **Resultado Final:** EXITOSO

2. Prueba Funcional:
   
    **ID:** PF002

    **Objetivo:** Validar que el sistema permita descargar la consulta socioeconómica
   
    **Precondiciones:** Ninguna
   
    **Pasos:**
   
    1. Ir a la página del Sisbén
    2. Hacer clic en la opción “Consulta tu grupo Sisbén”
    3. Hacer clic en la opción “Tipo de documento” y seleccionar el tipo de documento correspondiente
    4. Ingresar el Número de Documento correctamente
    5. Dar clic en el botón [Consultar]
    6. Dar clic en el ícono de impresión
    7. Validar que se realice la descarga
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

    **Objetivo:** Validar que el sistema informe que el documento consultado no existe en la base de datos
   
    **Precondiciones:** Ninguna
   
    **Pasos:**
   
    1. Ir a la página del Sisbén
    2. Hacer clic en la opción “Consulta tu grupo Sisbén”
    3. Hacer clic en la opción “Tipo de documento” y seleccionar el tipo de documento correspondiente
    4. Ingresar el Número de Documento incorrectamente
    5. Dar clic en el botón [Consultar]
    
   
    **Resultado Esperado:** El sistema debe generar una notificación indicando que no existe información en la base de datos del Sisbén.

    **Resultado Obtenido:** El sistema genera una alerta en pantalla indicando que no existe información en la base de datos del Sisbén.
   
   <img width="1592" height="384" alt="image" src="https://github.com/user-attachments/assets/2f592ead-e9e8-4189-ac48-bc5aef1e8fef" />
   <img width="938" height="478" alt="image" src="https://github.com/user-attachments/assets/ef47b7d9-9831-4d53-81bd-53ef6858b33e" />
   <img width="968" height="217" alt="image" src="https://github.com/user-attachments/assets/49101230-0c5e-4764-ac85-d5e562e46d0e" />
   <img width="972" height="216" alt="image" src="https://github.com/user-attachments/assets/00b4457b-f34e-494e-90c5-3d7ec3a06eab" />
   <img width="713" height="431" alt="image" src="https://github.com/user-attachments/assets/2256026a-e2b1-4f63-a797-8269c2aad3da" />

   **Resultado Final:** EXITOSO
   
4. Prueba de Usabilidad o Validación Visual:

    **ID:** PU001

    **Objetivo:** Validar claridad visual y experiencia de usuario al realizar la consulta
   
    **Precondiciones:** Ninguna
   
    **Pasos:**
   
    1. Ir a la página del Sisbén
    2. Hacer clic en la opción “Consulta tu grupo Sisbén”
    3. Revisar que la información y los campos presentados sean claros y no generen confusión al usuario
    
   
    **Resultado Esperado:** La información deber ser clara. Las opciones deben ser fáciles de encontrar. No debe haber campos adicionales que puedan generar confusión.

    **Resultado Obtenido:** La información es clara. Las opciones son fáciles de encontrar. Hay demasiado espacio adicional que puede generar confusión en el usuario al pensar que falta información por cargar.
   
   <img width="1592" height="384" alt="image" src="https://github.com/user-attachments/assets/2f592ead-e9e8-4189-ac48-bc5aef1e8fef" />
   <img width="1030" height="894" alt="image" src="https://github.com/user-attachments/assets/71b00c30-a7d2-4a0a-b03b-1d7fb33cb7db" />
   <img width="1018" height="702" alt="image" src="https://github.com/user-attachments/assets/c4c9df48-4010-4fa7-902d-55d1fe3661b5" />
   <img width="473" height="902" alt="image" src="https://github.com/user-attachments/assets/b0f3105c-d791-4573-8cb5-6d9c2316f0c9" />

   **Resultado Final:** FALLIDO
   
5. Prueba Smoke:

    **ID:** PS001

    **Objetivo:** Validar la operatividad del sistema
   
    **Precondiciones:** Ninguna
   
    **Pasos:**
   
    1. Ir a la página del Sisbén
    2. Hacer clic en la opción “Consulta tu grupo Sisbén”
    3. Hacer clic en la opción “Tipo de documento” y seleccionar el tipo de documento correspondiente
    4. Ingresar el Número de Documento correctamente
    5. Dar clic en el botón [Consultar]
    
   
    **Resultado Esperado:** La página debe cargar sin errores. La navegación debe ser fluida. La operación realizada debe estar operativa.

    **Resultado Obtenido:** La página cargar sin errores de conexión. La navegación es fluida y no presenta demoras. La operación realizada es operativa y funcional.

   
   <img width="1592" height="384" alt="image" src="https://github.com/user-attachments/assets/2f592ead-e9e8-4189-ac48-bc5aef1e8fef" />
   <img width="938" height="478" alt="image" src="https://github.com/user-attachments/assets/ef47b7d9-9831-4d53-81bd-53ef6858b33e" />
   <img width="968" height="217" alt="image" src="https://github.com/user-attachments/assets/49101230-0c5e-4764-ac85-d5e562e46d0e" />
   <img width="972" height="216" alt="image" src="https://github.com/user-attachments/assets/00b4457b-f34e-494e-90c5-3d7ec3a06eab" />
   <img width="1208" height="816" alt="image" src="https://github.com/user-attachments/assets/676581d2-63c1-48f8-85e7-db0596ac61c7" />

   **Resultado Final:** EXITOSO

# Parte 2 – Documentación de bugs reales
