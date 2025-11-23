import os
from pathlib import Path
from django.conf import settings
from django.shortcuts import render
from django.http import Http404, FileResponse
from PyPDF2 import PdfReader


def form_list(request):
    """List all PDFs and show if they are fillable + how many fields"""
    forms_dir = Path(settings.BASE_DIR) / "applications" / "static" / "forms"

    if not forms_dir.exists():
        pdf_files = []
    else:
        pdf_files = []
        for pdf_path in sorted(forms_dir.glob("*.pdf")):
            try:
                reader = PdfReader(pdf_path)
                fields = reader.get_fields()
                num_fields = len(fields) if fields else 0
                field_names = list(fields.keys()) if fields else []
                is_fillable = num_fields > 0
            except Exception as e:
                num_fields = 0
                field_names = []
                is_fillable = False
                error = str(e)

            pdf_files.append({
                'path': pdf_path,
                'name': pdf_path.name,
                'size_mb': round(pdf_path.stat().st_size / (1024*1024), 2),
                'is_fillable': is_fillable,
                'num_fields': num_fields,
                'field_sample': field_names[:5],  # show first 5 field names
            })

    context = {'pdf_files': pdf_files}
    return render(request, 'forms/list.html', context)


def open_form(request, filename='i-129f.pdf'):
    """Open PDF form using PyPDF2 and extract form fields, or serve PDF if view_pdf parameter is set"""
    if '..' in filename or filename.startswith('/'):
        raise Http404

    file_path = Path(settings.BASE_DIR) / "applications" / "static" / "forms" / filename
    if not file_path.exists():
        raise Http404("Form not found")

    # If view_pdf parameter is set, serve the PDF directly
    if request.GET.get('view_pdf') == 'true':
        response = FileResponse(open(file_path, 'rb'), content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{filename}"'
        return response

    try:
        reader = PdfReader(file_path)
        fields = reader.get_fields()
        
        # Extract form field information
        form_fields = []
        if fields:
            for field_name, field_obj in fields.items():
                field_info = {
                    'name': field_name,
                    'type': field_obj.get('/FT', 'Unknown'),
                    'value': field_obj.get('/V', ''),
                    'default_value': field_obj.get('/DV', ''),
                }
                # Get field type as string
                if field_info['type'] == '/Tx':
                    field_info['type'] = 'text'
                elif field_info['type'] == '/Btn':
                    field_info['type'] = 'button'
                elif field_info['type'] == '/Ch':
                    field_info['type'] = 'choice'
                elif field_info['type'] == '/Sig':
                    field_info['type'] = 'signature'
                else:
                    field_info['type'] = str(field_info['type'])
                
                form_fields.append(field_info)
        
        context = {
            'filename': filename,
            'form_fields': form_fields,
            'num_fields': len(form_fields),
            'is_fillable': len(form_fields) > 0,
        }
        
        return render(request, 'forms/open_form.html', context)
        
    except Exception as e:
        context = {
            'filename': filename,
            'error': str(e),
            'form_fields': [],
            'num_fields': 0,
            'is_fillable': False,
        }
        return render(request, 'forms/open_form.html', context)