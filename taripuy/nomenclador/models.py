from django.db import models


class Nomenclador(models.Model):
    """ cada uno de los códigos del nomenclador del Anexo II
        https://github.com/cluster311/Anexo2
        """
    codigo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=190)
    arancel = models.DecimalField(max_digits=11, decimal_places=2, default=0.0)
    observaciones = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.codigo} {self.descripcion}'
