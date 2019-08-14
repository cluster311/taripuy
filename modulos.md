# Módulos y planificación pendiente

Historia clínica:
 - Core: Django + Postgres + APIs seguras + **cifrado**.
   + Se conecta al bus de interoperabilidad nacional respetando los estándares requeridos
   + Recibe datos de atenciones y diagnósticos de otros módulos
 - Sin UI

Turnero & backend general gobierno:
 - Core: Django + psql: Centros de salud, médicos, especialidad que se atienden, etc.
 - UI: Login con vecinos comunes (incluye creación de usuarios). 

Recupero:
 - Core: Django + psql: Recibe atenciones médicas de otros módulos y emite documentos a firmar. Almacena y contabiliza facturas para obras sociales. Administra cobranzas y deudas con obras sociales. 
 - Si este módulo va por separado **podrá adaptarse desde otros sistema de atención médica que ya existen**.

Obras sociales:
 - Lista con pocos cambios de las obras sociales vigentes a nivel nacional. Tienen un código único (RNOS).  

Conexión a SISA/PUCO:
 - Sistema de información que dado un DNI entrega la obra social y datos de ReNaPer de una persona. Requiere credenciales.
 - Esto podría ser una librería python simple
 
Otros:
 - Calendario de vacunación nacional: Una vez al año o en sitiaciones excepcionales se actualiza. 
 - Lista de ARTs oficiales (opcional pero util para el sistema).  
 - ANSES: conexión al sistema para obtener las negativas directamente
 - Conexión al sistema Plan sumar para notificar atenciones y no cargar más a mano
 - Firma digital. Ver si madura la firma nacional
