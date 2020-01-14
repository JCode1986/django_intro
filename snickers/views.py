from django.views.generic import TemplateView

#extend TemplateView
class HomePageView(TemplateView):
    #create top level folder for templates; for htmls
    #add to setting.py in DIR list with --> os.path.join(BASE_DIR, 'templates')
    template_name='home.html'

class AboutPageView(TemplateView):
    template_name='about.html'