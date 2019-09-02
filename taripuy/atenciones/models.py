from django.db import models


class TipoAtencion(models.Model):
    """ Cada uno de los tipos de atencion """
    nombre = models.CharField(max_length=30, help_text='Tipo de atención')
    
    TIPO_CONSULTA = 100
    TIPO_PRACTICA = 200
    TIPO_INTERNACION = 300
    # el Anexo II al parecer solo permite estos tipos reales de atención.
    # https://github.com/cluster311/Anexo2
    tipos = ((TIPO_CONSULTA, 'Consulta'),
             (TIPO_PRACTICA, 'Práctica'),
             (TIPO_INTERNACION, 'Internación')
             )
    tipo = models.PositiveIntegerField(choices=tipos, default=TIPO_CONSULTA)

    # TODO generar los tipos básicos y si no es indispensable prohibir la edicion de esta tabla
    # https://github.com/cluster311/taripuy/issues/3
    # Consultas medicas
    # Enfermería
    # Guardia
    # Imagenes - Rayos X
    # Imagenes - Ecografía
    # Imagenes - Mamografía
    # Imagenes - Otros
    # Internacion breve
    # Internacion prolongada
    # Atencion de urgencias, emergencias y traslados
    # Odontología 
    # Kinesiología


class Atencion(models.Model):
    """ Cada una de las atenciones a un paciente/beneficiario 
        cubiertos por algun programa, obra social o prepaga 

        Referencia de atencion en Anexo II (interpretando el formulario)
        atencion = {'tipo': 'consulta',  # | practica | internacion
                    'especialidad': 'Va un texto al parecer largo, quizas sea del nomenclador',
                    'codigos_N_HPGD': ['AA01', 'AA02', 'AA06', 'AA07'],  # no se de donde son estos códigos
                    'fecha': {'dia': 3, 'mes': 9, 'anio': 2019},
                    'diagnostico_ingreso_cie10': {'principal': 'W020', 'otros': ['w021', 'A189']}}
        """

    tipo = models.ForeignKey(TipoAtencion, on_delete=models.PROTECT)
    servicios_incluidos = models.ManyToManyField('nomenclador.Nomenclador', 
                                                  blank=True,
                                                  help_text='Lista de atenciones o servicios arancelados recibidos')
    # especialidad: será el tipo? preguntar
    # ver la imagen: https://github.com/cluster311/Anexo2/blob/master/originales/Anexo-II-RESOLUCION-487-2002.gif
    fecha = models.DateField(null=True, blank=True, help_text='Fecha de la atencion')
    