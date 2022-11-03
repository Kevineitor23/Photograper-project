from django.shortcuts import  render
from igles.forms import UsuariosForm, ContactoForm

""" API PEXELS """
from pexels_api import API
PEXELS_API_KEY = '563492ad6f91700001000001b52ff90768744b9089f32109f67d6503'


def casa(request):
    """FUNCION HOME API PEXELS"""
    form = UsuariosForm
    api = API(PEXELS_API_KEY)
    api.search( 'peleas', page=1, results_per_page=6)
    photos = api.get_entries()
    context = {
        'photos': photos,
        'form':form,
        }

    if request.method == 'POST':
        form = UsuariosForm(request.POST)
        form.is_valid()
        name = form.cleaned_data['name']
        api = API(PEXELS_API_KEY)
        api.search( name, page=1, results_per_page=6)
        photos = api.get_entries()
        context = {
        'photos': photos,
        'form':form,
        }
        return render(request, 'home/home.html', context)

    return render(request, 'home/home.html', context)


    
def contactoform(request):
    """ FORMULARIO DE CONTACTO REVISION  E.164"""
    formcontacto  = ContactoForm()

    if request.method == 'POST':
       formcontacto = ContactoForm(request.POST)
       formcontacto.is_valid()
       name = formcontacto.cleaned_data['name']

       context = {
        'formcontacto':formcontacto,
        'name' : name,
       }
       return render(request, 'level/formulario.html', context)
    
    
    context ={
        'formcontacto': formcontacto
    }
    return render(request, 'level/formulario.html', context)

    

        
