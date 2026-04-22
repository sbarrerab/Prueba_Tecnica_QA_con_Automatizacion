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
    5. Dar clic en el botón [Consultar]
       
    **Resultado Esperado:** El sistema debe mostrar en pantalla la información de Sisbén relacionada con el documento consultado.

    **Resultado Obtenido:** El sistema muestra en pantalla la información de Sisbén relacionada con el documento consultado.
   
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
    5. Dar clic en el botón [Consultar]
    6. Dar clic en el ícono de impresión
    7. Validar que se realice la descarga
    8. Corroborar que la información descargada coincida con la información expuesta en la consulta
       
    **Resultado Esperado:** El sistema debe permitir descargar la información de Sisbén relacionada con el documento consultado.

    **Resultado Obtenido:** El sistema permite descargar la información de Sisbén relacionada con el documento consultado.
   
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
    4. Ingresar el Número de Documento incorrectamente (Letras/Campo Vacío/Caracteres Especiales)
    5. Dar clic en el botón [Consultar]
       
    **Resultado Esperado:** El sistema debe validar la existencia del documento de entrada y mostrar un mensaje de error indicando que los datos ingresados no se encuentran registrados en la base de datos.

    **Resultado Obtenido:** El sistema valida la existencia del documetno y expone un mensaje de error indicando que los datos ingresados no existen en la base de datos.
   
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
       
    **Resultado Esperado:** La información debe ser clara. Las opciones deben ser fáciles de encontrar. No debe haber campos adicionales que puedan generar confusión.

    **Resultado Obtenido:** La información es clara. Las opciones son fáciles de encontrar. Se identifica uso excesivo de espacio en blanco que puede generar percepción de carga incompleta o error en la interfaz.
   
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
    4. Dar clic en el botón [Consultar]
       
    **Resultado Esperado:** El sistema debe permitir realizar la consulta básica y mostrar resultados sin errores.
   
    **Resultado Obtenido:** El sistema permite realizar la consultas básicas y muestra resultados sin errores.
   
   <img width="1592" height="384" alt="image" src="https://github.com/user-attachments/assets/2f592ead-e9e8-4189-ac48-bc5aef1e8fef" />
   <img width="938" height="478" alt="image" src="https://github.com/user-attachments/assets/ef47b7d9-9831-4d53-81bd-53ef6858b33e" />
   <img width="968" height="217" alt="image" src="https://github.com/user-attachments/assets/49101230-0c5e-4764-ac85-d5e562e46d0e" />
   <img width="972" height="216" alt="image" src="https://github.com/user-attachments/assets/00b4457b-f34e-494e-90c5-3d7ec3a06eab" />
   <img width="1208" height="816" alt="image" src="https://github.com/user-attachments/assets/676581d2-63c1-48f8-85e7-db0596ac61c7" />
   <img width="1498" height="731" alt="image" src="https://github.com/user-attachments/assets/785003c6-d0de-4fef-9260-3448413b213b" />


   **Resultado Final:** PASSED



# Parte 2 – Documentación de bugs reales

**Título:** Falla en la primera consulta

**Descripción:** Al realizar la primera consulta de la clasificación socioeconómica la página oculta los campos "Tipo de documento" y "Número de documento", y el botón [Consultar], pero no expone la información consultada. Se debe recargar la página y proceder a repetir la consulta para que la información le sea mostrada al usuario.

**Pasos:** 
    1. Ir a la página del Sisbén
    2. Hacer clic en la opción “Consulta tu grupo Sisbén”
    3. Hacer clic en la opción “Tipo de documento” y seleccionar el tipo de documento correspondiente
    4. Ingresar el Número de Documento correctamente
    5. Dar clic en el botón [Consultar]
    6. Recarga la página
    7. Hacer clic en la opción “Tipo de documento” y seleccionar el tipo de documento correspondiente
    8. Ingresar el Número de Documento correctamente
    9. Dar clic en el botón [Consultar]
    
**Resultado Esperado:** El sistema debe mostrar en pantalla la información de Sisbén relacionada con el documento consultado

**Resultado Obtenido:** El sistema al realizar la primera consulta oculta los campos "Tipo de documento" y "Número de documento", y el botón [Consultar], pero no expone la información consultada. Se debe recargar la página y proceder a repetir la consulta para que la información le sea mostrada al usuario.

**Severidad:** Alta

**Impacto:** Aunque el problema es de forma intermitente, puede causar que se duplique el número de peticiones en un lapso de tiempo, lo cual consume recursos adicionales innecesariamente.

**Tipo de Bug:** Funcional / UI / Estado inconsistente

**Frecuencia:** Intermitente

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

**¿Qué riesgos ves en depender completamente de IA para QA?**
Depender completamente de IA en QA implica varios riesgos. Aunque es muy útil para automatizar pruebas repetitivas y acelerar procesos, la IA no comprende completamente la experiencia de usuario ni el contexto real de las personas. Puede validar que algo funcione, pero no necesariamente que sea usable o adecuado. Además, puede pasar por alto escenarios no previstos o comportamientos atípicos. Por eso, el criterio humano sigue siendo clave para asegurar calidad real, no solo técnica sino también funcional y de experiencia.
