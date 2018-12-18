from django.db import models
from django.contrib.auth.models import User
from generales.models import ClaseModelo

# Create your models here.

class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripción de la categoría',        
    ) 
    cruda = models.IntegerField(null=False)
    tratada = models.IntegerField(null=False)
    hr_servidas = models.IntegerField(null=False)
    hr_sin_servicio = models.IntegerField(null=False)
    ag_cruda_recibida = models.IntegerField(null=False)
    ag_tratada_despachada = models.IntegerField(null=False)
    consumo_sulfato = models.IntegerField(null=False)
    consumo_cloro = models.IntegerField(null=False)

  #  creadopor= models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}:{}:{}:{}:{}:{}:{}:{}:{}' .format(
                                                    self.categoria.descripcion,
                                                    self.categoria.cruda,
                                                    self.categoria.tratada,
                                                    self.categoria.hr_servidas,
                                                    self.categoria.hr_sin_servicio,
                                                    self.categoria.ag_cruda_recibida,
                                                    self.categoria.ag_tratada_despachada,
                                                    self.categoria.consumo_sulfato,
                                                    self.categoria.consumo_cloro,
                                                    #self.categoria.creadopor
                                                    )

    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()
    
    class Meta:
        verbose_name_plural = "Categorias"
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class ProcesosPlanta(ClaseModelo):
    nombre = models.CharField(max_length=100,help_text='Descripción de la categoría') 
    hora=models.IntegerField(null=False, blank=False)
    temperatura_ag_cruda=models.IntegerField(null=False, blank=False)
    ph_ag_cruda=models.DecimalField(max_digits=5,decimal_places=2, blank=False, null=False)
    color_ag_cruda=models.IntegerField(null=False)
    turbiedad_ag_cruda=models.DecimalField(max_digits=5,decimal_places=2, blank=False, null=False)
    color_sal_sedimentadores=models.IntegerField(null=False, blank=False)
    turbiedad_sal_sedimentadores=models.DecimalField(max_digits=5,decimal_places=2, blank=False, null=False)
    cloro_res_sal_sedimentadores=models.DecimalField(max_digits=5,decimal_places=2, blank=False, null=False)
    ph_sal_tq_desinfeccion=models.DecimalField(max_digits=5,decimal_places=2, blank=False, null=True)
    turbiedad_sal_tq_desinfeccion=models.DecimalField(max_digits=5,decimal_places=2, blank=False, null=False)
    temperatura_sal_tq_distribucion=models.IntegerField(null=False, blank=False)
    ph_sal_tq_distribucion=models.DecimalField(max_digits=5,decimal_places=2, blank=False, null=False)
    color_sal_tq_distribucion=models.IntegerField(null=False, blank=False)
    turbiedad_sal_tq_distribucion=models.DecimalField(max_digits=5,decimal_places=2, blank=False, null=False)
    alcalinidad_sal_tq_distribucion=models.IntegerField(null=False, blank=False)
    cloro_res_sal_tq_distribucion=models.DecimalField(max_digits=5,decimal_places=2, blank=False, null=False)

  

    def __str__(self):
        return '{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}'.format(
                                                                            self.ProcesosPlanta.nombre,
                                                                            self.ProcesosPlanta.hora,
                                                                            self.ProcesosPlanta.temperatura_ag_cruda,
                                                                            self.ProcesosPlanta.ph_ag_cruda,
                                                                            self.ProcesosPlanta.color_ag_cruda,
                                                                            self.ProcesosPlanta.turbiedad_ag_cruda,
                                                                            self.ProcesosPlanta.color_sal_sedimentadores,
                                                                            self.ProcesosPlanta.turbiedad_sal_sedimentadores,
                                                                            self.ProcesosPlanta.cloro_res_sal_sedimentadores,
                                                                            self.ProcesosPlanta.ph_sal_tq_desinfeccion,
                                                                            self.ProcesosPlanta.turbiedad_sal_tq_desinfeccion,
                                                                            self.ProcesosPlanta.temperatura_sal_tq_distribucion,
                                                                            self.ProcesosPlanta.ph_sal_tq_distribucion,
                                                                            self.ProcesosPlanta.color_sal_tq_distribucion,
                                                                            self.ProcesosPlanta.turbiedad_sal_tq_distribucion,
                                                                            self.ProcesosPlanta.alcalinidad_sal_tq_distribucion,
                                                                            self.ProcesosPlanta.cloro_res_sal_tq_distribucion,

                                                    )

    
    def save(self):
        self.nombre  = self.nombre.upper()
        super(ProcesosPlanta, self).save()
    
    class Meta:
        verbose_name_plural = "ProcesosPlantas"