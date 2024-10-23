# Instrucciones de Instalación

1. Tenga en cuenta que este módulo fue desarrollado en la versión 17 de Odoo comunitario.
2. Al crear la base de datos, recuerde cargar los datos demo. **(Muy importante)**
3. Proceda a instalar el módulo llamado `unam_test`.
4. Al finalizar el proceso, se instalará todo lo necesario para que pueda probar el funcionamiento del módulo.

# Explicación de los Modelos

Se crearon los siguientes modelos:

- **student.inscription**: Registro de las inscripciones de los alumnos con su respectivo curso y fecha de inicio.
- **subject**: Registro de las materias (subjects).

Para los cursos, estudiantes y profesores, se crearon adicionalmente dos modelos más bajo el paradigma de herencia, usando los campos booleanos `is_student` o `is_professor` para diferenciarlos y aplicar la lógica de negocio con grupos y reglas de registro.

En el caso de los cursos, se procedió de igual manera, creando un campo adicional `is_course` para diferenciarlos de los productos corrientes que se instalan de manera nativa en Odoo cuando se usa el demo.

La estructura de la App es la siguiente:

1. **product.template**: Para registrar en la base de datos los cursos.
2. **res.partner**: Para el registro de estudiantes, profesores y terceros.
3. **student.inscription**: Para registrar el curso, el estudiante y la fecha de inicio.
4. **subject**: Para registrar todas las materias con sus unidades de crédito y descripción.

# Instrucciones de Administración y Mantenimiento del Sistema

Odoo es un sistema muy flexible que permite crear diversos grupos de usuarios, a los cuales se les pueden aplicar diferentes tipos de permisos bajo el modelo CRUD (Crear, Leer, Actualizar, Eliminar).

En el contexto de nuestra App, se crearon tres grupos de usuarios:

1. **Profesores**: Tienen permisos de lectura dentro del sistema.
2. **Asistentes y Administrativos**: Cualquier tercero que necesite colaborar dentro del sistema, como coordinadores.
3. **Coordinador Académico**: Tienen mayores permisos que los grupos anteriores.

Además, se otorgaron permisos al grupo **Administrador de Sistema**, que tiene los más altos permisos.

### Otras Consideraciones

Al crear estudiantes, profesores y cursos, es necesario marcar el campo `is_professor`/`is_student` o `is_course` para diferenciarlos correctamente en el sistema.

### Mantenimiento:

1. Se recomienda hacer un respaldo regular de la base de datos (preferiblemente diario).
2. Realizar un respaldo antes de aplicar actualizaciones.
3. Revisar regularmente los permisos de los usuarios para verificar que no haya accesos indebidos.
4. Consultar el log periódicamente en busca de errores o advertencias.
5. Mantener actualizado el servidor que ejecuta Odoo.
6. Limpiar los archivos temporales regularmente.
7. Reiniciar el servidor de manera periódica para liberar la memoria caché.
