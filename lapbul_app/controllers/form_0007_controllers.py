from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods

def form_0007(request):
    data = []
    gol_kreditur_options = []
    ljk_options = []
    dati2_options = []
    jnspyd_options = []
    terkait_options = []
    cara_hitung_options = []
    jnsagunan_options = []
    
    try:
        with connection.cursor() as cursor:
            # Get main form data
            cursor.execute("EXEC sp_get_lap0007 '08', '2025', '000001'")
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            
            # Convert rows to list of dictionaries
            for row in rows:
                data.append(dict(zip(columns, row)))
                
            # Get dropdown options for gol kreditur
            cursor.execute("EXEC sandi_gol_kreditur '500949'")
            gol_kreditur_rows = cursor.fetchall()
            for row in gol_kreditur_rows:
                gol_kreditur_options.append({'value': row[0], 'label': row[1]})
                
            # Get dropdown options for ljk
            cursor.execute("EXEC sandi_ljk '500949'")
            ljk_rows = cursor.fetchall()
            for row in ljk_rows:
                ljk_options.append({'value': row[0], 'label': row[1]})
                
            # Get dropdown options for dati2
            cursor.execute("EXEC sandi_dati2 '500949'")
            dati2_rows = cursor.fetchall()
            for row in dati2_rows:
                dati2_options.append({'value': row[0], 'label': row[1]})
                
            # Get dropdown options for jnspyd
            cursor.execute("EXEC sandi_jnspyd '500949'")
            jnspyd_rows = cursor.fetchall()
            for row in jnspyd_rows:
                jnspyd_options.append({'value': row[0], 'label': row[1]})
                
            # Get dropdown options for terkait
            cursor.execute("EXEC sandi_terkait '500949'")
            terkait_rows = cursor.fetchall()
            for row in terkait_rows:
                terkait_options.append({'value': row[0], 'label': row[1]})
                
            # Get dropdown options for cara hitung
            cursor.execute("EXEC sandi_cara_hitung '500949'")
            cara_hitung_rows = cursor.fetchall()
            for row in cara_hitung_rows:
                cara_hitung_options.append({'value': row[0], 'label': row[1]})
                
            # Get dropdown options for jnsagunan
            cursor.execute("EXEC sandi_jnsagunan '500949'")
            jnsagunan_rows = cursor.fetchall()
            for row in jnsagunan_rows:
                jnsagunan_options.append({'value': row[0], 'label': row[1]})
                
    except Exception as e:
        print(f"Database error: {str(e)}")
        data = []
    
    context = {
        'title': 'Lapbul Ojk',
        'data': data,
        'columns': columns if data else [],
        'gol_kreditur_options': gol_kreditur_options,
        'ljk_options': ljk_options,
        'dati2_options': dati2_options,
        'jnspyd_options': jnspyd_options,
        'terkait_options': terkait_options,
        'cara_hitung_options': cara_hitung_options,
        'jnsagunan_options': jnsagunan_options,
    }
    return render(request, 'lapbul_app/form_0007.html', context)


@csrf_protect
@require_http_methods(["POST"])
def update_form_0007(request):
    """Handle form 0007 data updates"""
    try:
        # Get form data
        nopyd = request.POST.get('nopyd', '')
        cif = request.POST.get('cif', '')
        kodegolkreditur = request.POST.get('kodegolkreditur', '')
        sandibank = request.POST.get('sandibank', '')
        kodedati2 = request.POST.get('kodedati2', '')
        kodejenispyd = request.POST.get('kodejenispyd', '')
        sandihubbank = request.POST.get('sandihubbank', '')
        jwmulai = request.POST.get('jwmulai', '')
        jwtempo = request.POST.get('jwtempo', '')
        sukubunga = request.POST.get('sukubunga', '')
        carahitbunga = request.POST.get('carahitbunga', '')
        plafon = request.POST.get('plafon', '')
        kodejnsagunan = request.POST.get('kodejnsagunan', '')
        nominalagunan = request.POST.get('nominalagunan', '')
        bakidebet = request.POST.get('bakidebet', '')
        bytranbelumamor = request.POST.get('bytranbelumamor', '')
        diskontobelumamor = request.POST.get('diskontobelumamor', '')
        bakidebetneto = request.POST.get('bakidebetneto', '')
        
        # Execute the update stored procedure
        with connection.cursor() as cursor:
            cursor.execute(
                "EXEC sp_update_lap0007 '07', '2025', '500949', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s",
                [nopyd, cif, kodegolkreditur, sandibank, kodedati2, kodejenispyd, sandihubbank,
                 jwmulai, jwtempo, sukubunga, carahitbunga, plafon, kodejnsagunan,
                 nominalagunan, bakidebet, bytranbelumamor, diskontobelumamor, bakidebetneto]
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
def insert_form_0007(request):
    """Handle form 0007 data insertion"""
    try:
        # Get form data
        nopyd = request.POST.get('nopyd', '')
        cif = request.POST.get('cif', '')
        kodegolkreditur = request.POST.get('kodegolkreditur', '')
        sandibank = request.POST.get('sandibank', '')
        kodedati2 = request.POST.get('kodedati2', '')
        kodejenispyd = request.POST.get('kodejenispyd', '')
        sandihubbank = request.POST.get('sandihubbank', '')
        jwmulai = request.POST.get('jwmulai', '')
        jwtempo = request.POST.get('jwtempo', '')
        sukubunga = request.POST.get('sukubunga', '')
        carahitbunga = request.POST.get('carahitbunga', '')
        plafon = request.POST.get('plafon', '')
        kodejnsagunan = request.POST.get('kodejnsagunan', '')
        nominalagunan = request.POST.get('nominalagunan', '')
        bakidebet = request.POST.get('bakidebet', '')
        bytranbelumamor = request.POST.get('bytranbelumamor', '')
        diskontobelumamor = request.POST.get('diskontobelumamor', '')
        bakidebetneto = request.POST.get('bakidebetneto', '')
        
        # Execute the insert stored procedure
        with connection.cursor() as cursor:
            cursor.execute(
                "EXEC sp_insert_lap0007 '07', '2025', '500949', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s",
                [nopyd, cif, kodegolkreditur, sandibank, kodedati2, kodejenispyd, sandihubbank,
                 jwmulai, jwtempo, sukubunga, carahitbunga, plafon, kodejnsagunan,
                 nominalagunan, bakidebet, bytranbelumamor, diskontobelumamor, bakidebetneto]
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
def delete_form_0007(request):
    """Handle form 0007 data deletion"""
    try:
        cif = request.POST.get('cif', '')
        if not cif:
            return JsonResponse({
                'success': False, 
                'message': 'CIF diperlukan untuk menghapus data.'
            })
        
        # Execute the delete stored procedure
        with connection.cursor() as cursor:
            cursor.execute(
                "EXEC sp_delete_lap0007 '07', '2025', '500949', %s",
                [cif]
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


