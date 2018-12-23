from django.db import models
from django.contrib.auth.models import User
from generales.models import ClaseModelo
from decimal import Decimal
# Create your models here.


#++++++++++++++++++

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

    creadopor= models.ForeignKey(User, on_delete=models.CASCADE)

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
                                                    self.categoria.creadopor
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
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class OperacionDiaria(ClaseModelo):
    nombre=models.CharField(max_length=50,help_text='Funcionario') 
    hora=models.CharField(max_length=50, help_text='hora')
    caudal_entrada_LxS=models.IntegerField(null=False)
    caudal_entrada_m3=models.DecimalField(max_digits=11,decimal_places=2, blank=False, null=False)
    caudal_salida_LxS=models.IntegerField(null=False)
    caudal_salida_m3=models.DecimalField(max_digits=11,decimal_places=2, blank=False, null=False)
    sul_dial=models.DecimalField(max_digits=11,decimal_places=2, blank=False, null=False)
    sul_g_minut=models.DecimalField(max_digits=12,decimal_places=2, blank=False, null=False)
    sul_mg_l=models.DecimalField(max_digits=12,decimal_places=2, blank=False, null=False)
    precloracion_Lxdia=models.IntegerField(null=False)
    cloracion_Lxdia=models.IntegerField(null=False)
    cloracion_mg_l=models.DecimalField(max_digits=12,decimal_places=2, blank=False, null=False)
    tq_almacenam_altura_m=models.DecimalField(max_digits=5,decimal_places=2, blank=False, null=False)
    tq_almacenam_altura_m3=models.DecimalField(max_digits=11,decimal_places=2, blank=False, null=False)
    volumen_salida_acum=models.DecimalField(max_digits=12,decimal_places=2, blank=True, null=True)
    volumen_salida_real=models.DecimalField(max_digits=12,decimal_places=2, blank=False, null=False)
    #svolumen_salida_acum_anterior=models.DecimalField(max_digits=12,decimal_places=2, blank=False, null=False)


    def __str__(self):
        return '{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}:{}'.format(        self.OperacionDiaria.nombre,
                                                                                self.OperacionDiaria.hora,
                                                                                self.OperacionDiaria.caudal_entrada_LxS,
                                                                                self.OperacionDiaria.caudal_entrada_m3,
                                                                                self.OperacionDiaria.caudal_salida_LxS,
                                                                                self.OperacionDiaria.caudal_salida_m3,
                                                                                self.OperacionDiaria.sul_dial,
                                                                                self.OperacionDiaria.sul_g_minut,
                                                                                self.OperacionDiaria.sul_mg_l,
                                                                                self.OperacionDiaria.precloracion_Lxdia,
                                                                                self.OperacionDiaria.cloracion_Lxdia,
                                                                                self.OperacionDiaria.cloracion_mg_l,
                                                                                self.OperacionDiaria.tq_almacenam_altura_m,
                                                                                self.OperacionDiaria.tq_almacenam_altura_m3,
                                                                                #self.OperacionDiaria.volumen_salida_acum,
                                                                                self.OperacionDiaria.volumen_salida_real,
                                                                            )
    def save(self):
        self.nombre  = self.nombre.upper()
        self.caudal_entrada_m3 = ((Decimal(self.caudal_entrada_LxS) *3600)/1000)
        self.caudal_salida_m3 = (Decimal(self.caudal_salida_LxS)*3600)/1000
        self.sul_g_minut= Decimal((float(self.sul_dial)*10.72)+24.73)
        self.sul_mg_l= (Decimal((float(self.sul_dial)*10.72)+24.73)*1000)/Decimal((self.caudal_entrada_LxS)*60)
        self.cloracion_mg_l= Decimal(((self.cloracion_Lxdia + self.precloracion_Lxdia)*5.25)/(self.caudal_entrada_LxS))
        self.tq_almacenam_altura_m3 = (self.tq_almacenam_altura_m)*512
           
        self.volumen_salida_acum = Decimal(OperacionDiaria.objects.order_by('-id')[0].volumen_salida_acum) + Decimal(self.caudal_salida_m3) 
        self.volumen_salida_real = Decimal(self.volumen_salida_acum) - Decimal(OperacionDiaria.objects.order_by('-id')[0].volumen_salida_acum)
        super(OperacionDiaria,self).save()

class Meta:
    verbose_name_plural = "OperacionDiaria"

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class ControlSulfato(ClaseModelo):
    nombre=models.CharField(max_length=100,help_text='Funcionario') 
    turno=models.IntegerField(null=False)
    consumo_sulf=models.IntegerField(null=False)
    sedimentador_1=models.IntegerField(null=False)
    sedimentador_2=models.IntegerField(null=False)
    existencia_bultos_sulf=models.IntegerField(null=False)
    consumo_cal=models.IntegerField(null=False)
    observaciones=models.CharField(max_length=200,help_text='Observaciones')
    alimenta_existencias=models.IntegerField(null=True)
 

    def __str__(self):
        return '{}:{}:{}:{}:{}:{}:{}'.format(   self.ControlSulfato.nombre,
                                                self.ControlSulfato.turno,
                                                self.ControlSulfato.consumo_sulf,
                                                self.ControlSulfato.sedimentador_1,
                                                self.ControlSulfato.sedimentador_2,
                                                self.ControlSulfato.existencia_bultos_sulf,
                                                self.ControlSulfato.consumo_cal,
                                                self.ControlSulfato.observaciones,
                                                self.ControlSulfato.alimenta_existencias,

                       )
def save(self):
    self.nombre  = self.nombre.upper()        
    self.sedimentador_1= Decimal(ControlSulfato.objects.order_by('-id')[0].sedimentador_1) + self.consumo_sulf
    self.sedimentador_2= Decimal(ControlSulfato.objects.order_by('-id')[0].sedimentador_2) + self.consumo_sulf
    self.existencia_bultos_sulf= Decimal(ControlSulfato.objects.order_by('-id')[0].existencia_bultos_sulf) - Decimal(self.consumo_sulf)+ Decimal(self.alimenta_existencias)

class Meta:
    verbose_name_plural = "ControlSulfato"