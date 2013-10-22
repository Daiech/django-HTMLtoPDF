==================
Django Html to PDF
==================

Django PDF is a simple Django app to create PDF files from Html using xhtml2pdf.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "django_htmlToPDF" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'django_htmlToPDF',
      )

2. Include the polls URLconf in your project urls.py like this::

      url(r'^pdf/', include('django_htmlToPDF.urls')),

3. django_htmlToPDF needs HTTP POST method to run, be sure to send a POST method with two params:
	pdf_name	: The name for your PDF file (optional)
	html_data 	: The html you want to convert to pdf