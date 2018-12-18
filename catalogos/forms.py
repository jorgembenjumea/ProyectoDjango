#35
from django import forms

from catalogos.models import Categoria, ProcesosPlanta


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