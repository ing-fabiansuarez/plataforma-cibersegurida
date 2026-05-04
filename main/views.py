from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'main/index.html'

class NarrativasListView(TemplateView):
    template_name = 'main/narrativas_list.html'

class NarrativaUnoView(TemplateView):
    template_name = 'main/narrativa_1.html'

class NarrativaDosView(TemplateView):
    template_name = 'main/narrativa_2.html'

class NarrativaTresView(TemplateView):
    template_name = 'main/narrativa_3.html'

class NarrativaCuatroView(TemplateView):
    template_name = 'main/narrativa_4.html'
