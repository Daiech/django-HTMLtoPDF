from django.conf.urls import url, patterns
urlpatterns = patterns('django_htmlToPDF.views',
    url(r'^htmltopdf$', 'html_to_pdf', name='html_to_pdf'),
)
