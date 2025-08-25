from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods

def form_0001(request):
    # Execute the SQL query to get form data
    data = []
    jenis_pemilik_options = []
    stsps_options = []
    status_perubahan_options = []
    
    try:
        with connection.cursor() as cursor:
            # Get main form data
            cursor.execute("EXEC sp_get_lap0001 '07', '2025', '500949'")
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            
            # Convert rows to list of dictionaries
            for row in rows:
                data.append(dict(zip(columns, row)))
                
            # Get dropdown options for jenis pemilik
            cursor.execute("EXEC sandi_jnspemilik '500949'")
            jenis_pemilik_rows = cursor.fetchall()
            for row in jenis_pemilik_rows:
                jenis_pemilik_options.append({'value': row[0], 'label': row[1]})
                
            # Get dropdown options for STSPS
            cursor.execute("EXEC sandi_stspsp '500949'")
            stsps_rows = cursor.fetchall()
            for row in stsps_rows:
                stsps_options.append({'value': row[0], 'label': row[1]})
                
            # Get dropdown options for status perubahan
            cursor.execute("EXEC sandi_stsperubahan '500949'")
            status_perubahan_rows = cursor.fetchall()
            for row in status_perubahan_rows:
                status_perubahan_options.append({'value': row[0], 'label': row[1]})
                
    except Exception as e:
        print(f"Database error: {str(e)}")
        data = []
    
    context = {
        'title': 'Lapbul Ojk',
        'data': data,
        'columns': columns if data else [],
        'jenis_pemilik_options': jenis_pemilik_options,
        'stsps_options': stsps_options,
        'status_perubahan_options': status_perubahan_options
    }
    return render(request, 'lapbul_app/form_0001.html', context)

@csrf_protect
@require_http_methods(["POST"])
def update_form_0001(request):
    """Handle form 0001 data updates"""
    try:
        # Get form data
        nama = request.POST.get('nama', '')
        alamat = request.POST.get('alamat', '')
        jnspemilik = request.POST.get('jenispemilik', '')
        noidentitas = request.POST.get('noidentitas', '')
        stsps = request.POST.get('kodestsps', '')
        nominal = request.POST.get('nominalsaham', '')
        persentase = request.POST.get('persensaham', '')
        statusperubahan = request.POST.get('statusperubahan', '')
        
        # Execute the update stored procedure
        with connection.cursor() as cursor:
            cursor.execute(
                "EXEC sp_update_lap0001 '07', '2025', '500949', %s, %s, %s, %s, %s, %s, %s, %s",
                [nama, alamat, jnspemilik, noidentitas, stsps, nominal, persentase, statusperubahan]
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

@csrf_protect
@require_http_methods(["POST"])
def insert_form_0001(request):
    """Handle form 0001 data insertion"""
    try:
        # Get form data
        nama = request.POST.get('nama', '')
        alamat = request.POST.get('alamat', '')
        jnspemilik = request.POST.get('jenispemilik', '')
        noidentitas = request.POST.get('noidentitas', '')
        stsps = request.POST.get('kodestsps', '')
        nominal = request.POST.get('nominalsaham', '')
        persentase = request.POST.get('persensaham', '')
        statusperubahan = request.POST.get('statusperubahan', '')
        
        # Execute the insert stored procedure
        with connection.cursor() as cursor:
            cursor.execute(
                "EXEC sp_insert_lap0001 '07', '2025', '500949', %s, %s, %s, %s, %s, %s, %s, %s",
                [nama, alamat, jnspemilik, noidentitas, stsps, nominal, persentase, statusperubahan]
            )
        
        return JsonResponse({
            'success': True,
            'message': 'Data berhasil ditambahkan.'
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Terjadi kesalahan: {str(e)}'
        })

@csrf_protect
@require_http_methods(["POST"])
def delete_form_0001(request):
    """Handle form 0001 data deletion"""
    try:
        # Get the noidentitas from the request
        noidentitas = request.POST.get('noidentitas', '')
        
        if not noidentitas:
            return JsonResponse({
                'success': False,
                'message': 'No identitas diperlukan untuk menghapus data.'
            })
        
        # Execute the delete stored procedure
        with connection.cursor() as cursor:
            cursor.execute(
                "EXEC sp_delete_lap0001 '07', '2025', '500949', %s",
                [noidentitas]
            )
        
        return JsonResponse({
            'success': True,
            'message': 'Data berhasil dihapus.'
        })
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'Terjadi kesalahan: {str(e)}'
        })