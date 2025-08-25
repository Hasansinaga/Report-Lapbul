from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods

def form_0008(request):
    data = {}
        
    try:
        with connection.cursor() as cursor:
            # Get main form data
            cursor.execute("EXEC sp_get_lap0008 '06', '2025', '500949'")
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            
            # Convert rows to dictionary with sandi as key
            for row in rows:
                row_dict = dict(zip(columns, row))
                # Use sandipos as key for easy template access
                if 'sandipos' in row_dict and 'persenrasio' in row_dict:
                    data[row_dict['sandipos']] = row_dict['persenrasio']
             
    except Exception as e:
        print(f"Database error: {str(e)}")
        data = {}
    
    context = {
        'title': 'Lapbul Ojk',
        'data': data,
    }
    return render(request, 'lapbul_app/form_0008.html', context)


@csrf_protect
@require_http_methods(["POST"])
def update_form_0008(request):
    """Handle form 0008 data updates"""
    try:
        # Get form data
        sandipos = request.POST.get('sandipos', '')
        persenrasio = request.POST.get('persenrasio', '')

        # Execute the update stored procedure
        with connection.cursor() as cursor:
            cursor.execute(
                "EXEC sp_update_lap0008 '06', '2025', '500949', %s, %s",
                [sandipos, persenrasio]
            )
        
        return JsonResponse({
            'success': True,
            'message': 'Data berhasil diperbarui.'
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Terjadi kesalahan: {str(e)}'
        })
