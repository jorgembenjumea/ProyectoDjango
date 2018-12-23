#35
from django import forms

from catalogos.models import Categoria, ProcesosPlanta, OperacionDiaria, ControlSulfato


class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields = ['descripcion','cruda','tratada','hr_servidas',
                'hr_sin_servicio', 'ag_cruda_recibida','ag_tratada_despachada',
                'consumo_sulfato','consumo_cloro', 'activo']
        labels= {'descripcion': "Descripción de la Categoría",
                "activo:":"Estado"}
        widget={'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class ProcesosPlantaForm(forms.ModelForm):
    class Meta:
        model=ProcesosPlanta
        fields =['nombre',
                'hora',
                'temperatura_ag_cruda',
                'ph_ag_cruda',
                'color_ag_cruda',
                'turbiedad_ag_cruda',
                'color_sal_sedimentadores',
                'turbiedad_sal_sedimentadores',
                'cloro_res_sal_sedimentadores',
                'ph_sal_tq_desinfeccion',
                'turbiedad_sal_tq_desinfeccion',
                'temperatura_sal_tq_distribucion',
                'ph_sal_tq_distribucion',
                'color_sal_tq_distribucion',
                'turbiedad_sal_tq_distribucion',
                'alcalinidad_sal_tq_distribucion',
                'cloro_res_sal_tq_distribucion']

        labels= {'nombre': "Nombre funcionario",
                "activo:":"Estado"}

        widget={'nombre': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

#+++ OPERACIONES DIARIAS ++++++
class OperacionDiariaForm(forms.ModelForm):
    class Meta:
        model=OperacionDiaria
        fields =['nombre',
                'hora',
                'caudal_entrada_LxS',
                #'caudal_entrada_m3',
                'caudal_salida_LxS',
                #'caudal_salida_m3',
                'sul_dial',
               # 'sul_g_minut',
               # 'sul_mg_l',
                'precloracion_Lxdia',
                'cloracion_Lxdia',
               # 'cloracion_mg_l',
                'tq_almacenam_altura_m',
               # 'tq_almacenam_altura_m3',
                #'volumen_salida_acum',
                #'volumen_salida_real'
                ]
   

        labels= {'nombre': "Nombre funcionario",
                "activo:":"Estado"}

        widget={'nombre': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

#+++++++++++++++++++++++++++++++++++++++++++++++++++
class ControlSulfatoForm(forms.ModelForm):
    class Meta:
        model=ControlSulfato
        fields =[   'nombre',
                    'turno',
                    'consumo_sulf',
                    'sedimentador_1',
                    'sedimentador_2',
                    'existencia_bultos_sulf',
                    'consumo_cal',
                    'observaciones',
                    'alimenta_existencias',
]
        labels= {'nombre': "Nombre funcionario",
                        "activo:":"Estado"}


        widget={'nombre': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })