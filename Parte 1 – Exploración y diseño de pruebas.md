# Contexto 
**Portal Público Seleccionado:** https://www.sisben.gov.co/Paginas/landing.html

# Parte 1 – Exploración y diseño de pruebas
**Funcionalidad Pública Seleccionada:** Consultar grupo Sisbén

## Descripción de la Funcionalidad
La opción “Consultar grupo Sisbén” es un servicio que le permite al ciudadano digitar sus datos (tipo y número de documento) y consultar su clasificación socioeconómica oficial según sus condiciones de vida e ingresos. Esta información es utilizada por el gobierno para determinar el acceso a subsidios y programas sociales.

## Casos de Prueba

1. Prueba Funcional:
   
    **ID:** PF001

    **Tipo de Prueba:** Funcional

    **Objetivo:** Validar que el sistema retorne correctamente la clasificación socioeconómica para un documento válido
   
    **Precondiciones:** Documento válido existente en la base de datos del Sisbén
   
    **Pasos:**
   
    1. Ir a la página del Sisbén
    2. Hacer clic en la opción “Consulta tu grupo Sisbén”
    3. Hacer clic en la opción “Tipo de documento” y seleccionar el tipo de documento correspondiente
    4. Ingresar el Número de Documento correctamente
    5. Hacer clic en el botón [Consultar]
       
    **Resultado Esperado:** El sistema debe mostrar en pantalla la información de Sisbén relacionada con el documento consultado:
      - Nombre del ciudadano
      - Grupo Sisbén
      - Estado del registro
      - Fecha de actualización (si aplica)
      - Además, la información debe visualizarse sin errores y con formato legible.

    **Resultado Obtenido:** Se evidencia que el sistema muestra la información de Sisbén relacionada con el documento consultado.
   
   <img width="1592" height="384" alt="image" src="https://github.com/user-attachments/assets/2f592ead-e9e8-4189-ac48-bc5aef1e8fef" />
   <img width="938" height="478" alt="image" src="https://github.com/user-attachments/assets/ef47b7d9-9831-4d53-81bd-53ef6858b33e" />
   <img width="968" height="217" alt="image" src="https://github.com/user-attachments/assets/49101230-0c5e-4764-ac85-d5e562e46d0e" />
   <img width="972" height="216" alt="image" src="https://github.com/user-attachments/assets/00b4457b-f34e-494e-90c5-3d7ec3a06eab" />
   <img width="1208" height="816" alt="image" src="https://github.com/user-attachments/assets/676581d2-63c1-48f8-85e7-db0596ac61c7" />

   **Resultado Final:** PASSED

2. Prueba Funcional:
   
    **ID:** PF002

    **Tipo de Prueba:** Funcional

    **Objetivo:** Validar que el sistema permita descargar la consulta socioeconómica realizada para un documento válido
   
    **Precondiciones:** Documento válido existente en la base de datos del Sisbén
   
    **Pasos:**
   
    1. Ir a la página del Sisbén
    2. Hacer clic en la opción “Consulta tu grupo Sisbén”
    3. Hacer clic en la opción “Tipo de documento” y seleccionar el tipo de documento correspondiente
    4. Ingresar el Número de Documento correctamente
    5. Hacer clic en el botón [Consultar]
    6. Hacer clic en el ícono de impresión
    7. Validar que se realice la descarga del archivo en formato PDF
    8. Abrir el archivo descargado y corroborar que la información descargada coincida con la información expuesta en pantalla para la consulta
       
    **Resultado Esperado:** El sistema debe permitir descargar la información en formato PDF, y la información consignada debe coincidir con la mostrada en pantalla, sin errores de contenido ni formato.

      - Nombre del ciudadano
      - Grupo Sisbén
      - Estado del registro
      - Fecha de actualización (si aplica)
      - Además, la información debe visualizarse sin errores y con formato legible.

    **Resultado Obtenido:** Se genera la descarga de la información en formato PDF, y la información consignada coincide con la mostrada en pantalla, sin errores de contenido ni formato.
   
   <img width="1592" height="384" alt="image" src="https://github.com/user-attachments/assets/2f592ead-e9e8-4189-ac48-bc5aef1e8fef" />
   <img width="938" height="478" alt="image" src="https://github.com/user-attachments/assets/ef47b7d9-9831-4d53-81bd-53ef6858b33e" />
   <img width="968" height="217" alt="image" src="https://github.com/user-attachments/assets/49101230-0c5e-4764-ac85-d5e562e46d0e" />
   <img width="972" height="216" alt="image" src="https://github.com/user-attachments/assets/00b4457b-f34e-494e-90c5-3d7ec3a06eab" />
   <img width="1208" height="816" alt="image" src="https://github.com/user-attachments/assets/676581d2-63c1-48f8-85e7-db0596ac61c7" />

   <img width="1120" height="409" alt="image" src="https://github.com/user-attachments/assets/32fe9994-6f4d-4f01-aa26-86179b618da6" />
   <img width="1218" height="805" alt="image" src="https://github.com/user-attachments/assets/933c6a45-9aa3-4773-8924-2835d02f076e" />

   **Resultado Final:** PASSED
    

3. Prueba Negativa:

    **ID:** PN001

    **Tipo de Prueba:** Negativa

    **Objetivo:** Validar que el sistema maneje correctamente documentos no registrados en la base de datos
   
    **Precondiciones:** Campo de número de documento habilitado para ingreso de datos
   
    **Pasos:**
   
    1. Ir a la página del Sisbén
    2. Hacer clic en la opción “Consulta tu grupo Sisbén”
    3. Hacer clic en la opción “Tipo de documento” y seleccionar el tipo de documento correspondiente
    4. Ingresar un número de documento que no se encuentre registrado en la base de datos
    5. Hacer clic en el botón [Consultar]
       
    **Resultado Esperado:** El sistema debe indicar que el documento no se encuentra registrado mediante un mensaje claro al usuario, sin mostrar información de consulta.

    **Resultado Obtenido:** Se evidencia que el sistema muestra un mensaje indicando que la información ingresada no existe en la base de datos.
   
   <img width="1592" height="384" alt="image" src="https://github.com/user-attachments/assets/2f592ead-e9e8-4189-ac48-bc5aef1e8fef" />
   <img width="938" height="478" alt="image" src="https://github.com/user-attachments/assets/ef47b7d9-9831-4d53-81bd-53ef6858b33e" />
   <img width="968" height="217" alt="image" src="https://github.com/user-attachments/assets/49101230-0c5e-4764-ac85-d5e562e46d0e" />
   <img width="972" height="216" alt="image" src="https://github.com/user-attachments/assets/00b4457b-f34e-494e-90c5-3d7ec3a06eab" />
   <img width="1137" height="275" alt="image" src="https://github.com/user-attachments/assets/8b33340d-bfca-4223-945f-bc6c519737a9" />
   <img width="713" height="431" alt="image" src="https://github.com/user-attachments/assets/2256026a-e2b1-4f63-a797-8269c2aad3da" />

   **Resultado Final:** PASSED
   
4. Prueba de Usabilidad o Validación Visual:

    **ID:** PU001

    **Tipo de Prueba:** UX

    **Objetivo:** Validar claridad visual y experiencia de usuario al realizar la consulta socioeconómica para un documento válido
   
    **Precondiciones:** Equipo con acceso a internet
   
    **Pasos:**
   
    1. Ir a la página del Sisbén
    2. Hacer clic en la opción “Consulta tu grupo Sisbén”
    3. Revisar que la información y los campos presentados sean claros y no generen confusión al usuario
       
    **Resultado Esperado:**
    - Los campos deben estar claramente identificados
    - El botón de acción debe ser fácilmente visible
    - La interfaz debe evitar espacios en blanco excesivos que generen confusión
    - La información debe mostrarse de forma inmediata tras la consulta

    **Resultado Obtenido:** Se identifica uso excesivo de espacio en blanco después de la consulta, lo que puede generar percepción de error o carga incompleta.
   
   <img width="1592" height="384" alt="image" src="https://github.com/user-attachments/assets/2f592ead-e9e8-4189-ac48-bc5aef1e8fef" />
   <img width="1030" height="894" alt="image" src="https://github.com/user-attachments/assets/71b00c30-a7d2-4a0a-b03b-1d7fb33cb7db" />
   <img width="1018" height="702" alt="image" src="https://github.com/user-attachments/assets/c4c9df48-4010-4fa7-902d-55d1fe3661b5" />
   <img width="473" height="902" alt="image" src="https://github.com/user-attachments/assets/b0f3105c-d791-4573-8cb5-6d9c2316f0c9" />

   **Severidad:** Baja

   **Mejora:** Reducir el espacio y que se amplíe automáticamente al exponer la información de la consulta
   
   **Resultado Final:** FAILED
   
5. Prueba Smoke:

    **ID:** PS001

    **Tipo de Prueba:** Smoke

    **Objetivo:** Validar que la funcionalidad principal de consulta está operativa
   
    **Precondiciones:** Documento existente en la base de datos del Sisbén
   
    **Pasos:**
   
    1. Ir a la página del Sisbén
    2. Acceder a “Consulta tu grupo Sisbén”
    3. Ingresar datos válidos
    4. Hacer clic en el botón [Consultar]
       
    **Resultado Esperado:** El sistema debe permitir realizar la consulta básica y mostrar los datos del ciudadano sin errores funcionales ni visuales.
   
    **Resultado Obtenido:** Permite realizar la consulta básica y muestra los datos del ciudadano sin errores funcionales ni visuales.
   
   <img width="1592" height="384" alt="image" src="https://github.com/user-attachments/assets/2f592ead-e9e8-4189-ac48-bc5aef1e8fef" />
   <img width="938" height="478" alt="image" src="https://github.com/user-attachments/assets/ef47b7d9-9831-4d53-81bd-53ef6858b33e" />
   <img width="968" height="217" alt="image" src="https://github.com/user-attachments/assets/49101230-0c5e-4764-ac85-d5e562e46d0e" />
   <img width="972" height="216" alt="image" src="https://github.com/user-attachments/assets/00b4457b-f34e-494e-90c5-3d7ec3a06eab" />
   <img width="1208" height="816" alt="image" src="https://github.com/user-attachments/assets/676581d2-63c1-48f8-85e7-db0596ac61c7" />
   <img width="1498" height="731" alt="image" src="https://github.com/user-attachments/assets/785003c6-d0de-4fef-9260-3448413b213b" />


   **Resultado Final:** PASSED



# Parte 2 – Documentación de bugs reales

**Título:** Falla en la primera consulta

**Descripción:** Al realizar la primera consulta, la página oculta los campos de entrada y el botón [Consultar], pero no muestra la información del ciudadano. Es necesario recargar la página y repetir la consulta para visualizar los resultados.

**Pasos:** 
    1. Ir a la página del Sisbén
    2. Hacer clic en la opción “Consulta tu grupo Sisbén”
    3. Realizar una consulta por primera vez
    4. Observar que los campos desaparecen tras hacer clic en [Consultar]
    5. Verificar que no se muestra la información del ciudadano
    6. Recarga la página
    7. Repetir la consulta con los mismos datos
    8. Observar que en el segundo intento sí se muestra la información
    
**Resultado Esperado:** El sistema debe mostrar la información del ciudadano correspondiente al documento consultado de forma inmediata, sin ocultar los campos de entrada ni requerir recarga de la página.

**Resultado Obtenido:** Al realizar la primera consulta oculta los campos "Tipo de documento" y "Número de documento", y el botón [Consultar], pero no expone la información consultada. Se debe recargar la página y proceder a repetir la consulta para que la información le sea mostrada al usuario.

**Severidad:** Alta

**Impacto:** 
   - Puede provocar múltiples intentos de consulta, incrementando carga innecesaria en el sistema.
   - El usuario puede interpretar que no está registrado en el sistema
   - Genera desconfianza en la plataforma

**Tipo de Bug:** Funcional / UI / Estado inconsistente

**Frecuencia:** Intermitente - Ocurre en el primer intento tras cargar la página (observado en múltiples ocasiones)

**Posible Causa:** Problema de manejo de estado en la interfaz, donde los campos se ocultan antes de recibir una respuesta válida del backend.

**Navegador:** Edge 147 – Windows 11

**Evidencia:** 
   <img width="1592" height="384" alt="image" src="https://github.com/user-attachments/assets/2f592ead-e9e8-4189-ac48-bc5aef1e8fef" />
   <img width="938" height="478" alt="image" src="https://github.com/user-attachments/assets/ef47b7d9-9831-4d53-81bd-53ef6858b33e" />
   <img width="968" height="217" alt="image" src="https://github.com/user-attachments/assets/49101230-0c5e-4764-ac85-d5e562e46d0e" />
   <img width="972" height="216" alt="image" src="https://github.com/user-attachments/assets/00b4457b-f34e-494e-90c5-3d7ec3a06eab" />
   <img width="1161" height="1298" alt="image" src="https://github.com/user-attachments/assets/c2c22e4e-8edd-4eb1-bb7f-0d44174cb05d" />


   **Recargar página**

   <img width="938" height="478" alt="image" src="https://github.com/user-attachments/assets/ef47b7d9-9831-4d53-81bd-53ef6858b33e" />
   <img width="968" height="217" alt="image" src="https://github.com/user-attachments/assets/49101230-0c5e-4764-ac85-d5e562e46d0e" />
   <img width="972" height="216" alt="image" src="https://github.com/user-attachments/assets/00b4457b-f34e-494e-90c5-3d7ec3a06eab" />
   <img width="1208" height="816" alt="image" src="https://github.com/user-attachments/assets/676581d2-63c1-48f8-85e7-db0596ac61c7" />



# Parte 4 – Uso de IA

**¿En qué parte de la prueba usaste inteligencia artificial?**
Se utilizó inteligencia artificial como apoyo en la elaboración del documento, principalmente para mejorar la redacción y asegurar una estructura alineada con estándares profesionales de QA. Adicionalmente, se empleó como herramienta de aprendizaje para reforzar conocimientos en el uso de Playwright, dado que es un framework con el cual no se cuenta aún con amplia experiencia.

**¿Qué hiciste tú directamente (criterio humano)?**
1. Definición y diseño de los casos de prueba, basados en el análisis funcional del sistema.
2. Ejecución manual de las pruebas, validando el comportamiento real de la aplicación.
3. Elaboración de la documentación inicial de pruebas, incluyendo resultados y evidencias.
4. Implementación del proceso de automatización de pruebas.
5. Se validó manualmente que los resultados documentados correspondieran con el comportamiento real del sistema.

**¿Qué riesgos ves en depender completamente de IA para QA?**
Depender completamente de IA en QA implica varios riesgos. Aunque es muy útil para automatizar pruebas repetitivas y acelerar procesos, la IA no comprende completamente la experiencia de usuario ni el contexto real de las personas. Puede Validar que algo funcione, pero no necesariamente que sea usable o adecuado. Además, puede pasar por alto escenarios no previstos o comportamientos atípicos. Por eso, el criterio humano sigue siendo clave para asegurar calidad real, no solo técnica sino también funcional y de experiencia.
