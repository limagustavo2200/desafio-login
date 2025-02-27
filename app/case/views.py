
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from django.http import HttpResponse
import pandas as pd
from .forms import UploadFileForm
from .conversor.conversor_boleto import transformar_planilha, gerar_arquivo


def home(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        try:
            if form.is_valid():
                file_path = gerar_arquivo(request.FILES['file'])
                planilha_original = pd.read_csv(file_path, delimiter=',')
                planilha_final = transformar_planilha(planilha_original)

                output_file_path = '/tmp/planilha_final.csv'
                planilha_final.to_csv(output_file_path, index=False, sep='\t')

                response = HttpResponse(open(output_file_path, 'rb').read(), content_type='text/csv')
                response['Content-Disposition'] = f'attachment; filename="planilha_final.csv"'
                return response
        except Exception as e:
            response = HttpResponse(f'Erro: {e}')
            return response
    else:
        form = UploadFileForm()
    return render(request, 'home.html', {'form': form,
                                         'user': request.user})
