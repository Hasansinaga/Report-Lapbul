from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods

# Create your views here.
def index(request):
    return render(request, 'lapbul_app/index.html', {'title': 'Laporan Ekternal'})

def lapbul(request):
    return render(request, 'lapbul_app/lapbul.html', {'title': 'Lapbul OJK'})

def generate_report(request):
    if request.method == 'POST' and request.POST.get('action') == 'generate_report':
        try:
            with connection.cursor() as cursor:
                cursor.execute("EXEC reportlapbul_01_00 '2025', '07', '500949', '999', '0', '', 0")
            messages.success(request, 'Laporan berhasil dibuat.')
        except Exception as e:
            messages.error(request, f'Terjadi kesalahan: {str(e)}')
        
        return redirect('lapbul_app:lapbul')
    
    return redirect('lapbul_app:lapbul')

def form_0000(request):
    return render(request, 'lapbul_app/form_0000.html', {'title': 'Lapbul Ojk'})

def form_0001(request):
    return render(request, 'lapbul_app/form_0001.html', {'title': 'Lapbul Ojk'})

def form_0002(request):
    return render(request, 'lapbul_app/form_0002.html', {'title': 'Lapbul Ojk'})

def form_0003(request):
    return render(request, 'lapbul_app/form_0003.html', {'title': 'Lapbul Ojk'})

def form_0004(request):
    return render(request, 'lapbul_app/form_0004.html', {'title': 'Lapbul Ojk'})

def form_0005(request):
    return render(request, 'lapbul_app/form_0005.html', {'title': 'Lapbul Ojk'})

def form_0006(request):
    return render(request, 'lapbul_app/form_0006.html', {'title': 'Lapbul Ojk'})

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
            cursor.execute("EXEC sp_get_lap0007 '07', '2025', '500949'")
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

def form_0008(request):
    return render(request, 'lapbul_app/form_0008.html', {'title': 'Lapbul Ojk'})

def form_0009(request):
    return render(request, 'lapbul_app/form_0009.html', {'title': 'Lapbul Ojk'})

def form_0010(request):
    return render(request, 'lapbul_app/form_0010.html', {'title': 'Lapbul Ojk'})

def form_0011(request):
    return render(request, 'lapbul_app/form_0011.html', {'title': 'Lapbul Ojk'})

def form_0012(request):
    return render(request, 'lapbul_app/form_0012.html', {'title': 'Lapbul Ojk'})

def form_0013(request):
    return render(request, 'lapbul_app/form_0013.html', {'title': 'Lapbul Ojk'})

def form_0015(request):
    return render(request, 'lapbul_app/form_0015.html', {'title': 'Lapbul Ojk'})

def form_0016(request):
    return render(request, 'lapbul_app/form_0016.html', {'title': 'Lapbul Ojk'})

def form_0017(request):
    return render(request, 'lapbul_app/form_0017.html', {'title': 'Lapbul Ojk'})

def form_0018(request):
    return render(request, 'lapbul_app/form_0018.html', {'title': 'Lapbul Ojk'})

def form_0019(request):
    return render(request, 'lapbul_app/form_0019.html', {'title': 'Lapbul Ojk'})

def form_0020(request):
    return render(request, 'lapbul_app/form_0020.html', {'title': 'Lapbul Ojk'})

def form_0021(request):
    return render(request, 'lapbul_app/form_0021.html', {'title': 'Lapbul Ojk'})

def form_0100(request):
    return render(request, 'lapbul_app/form_0100.html', {'title': 'Lapbul Ojk'})

def form_0101(request):
    return render(request, 'lapbul_app/form_0101.html', {'title': 'Lapbul Ojk'})

def form_0200(request):
    return render(request, 'lapbul_app/form_0200.html', {'title': 'Lapbul Ojk'})

def form_0300(request):
    return render(request, 'lapbul_app/form_0300.html', {'title': 'Lapbul Ojk'})

def form_0400(request):
    return render(request, 'lapbul_app/form_0400.html', {'title': 'Lapbul Ojk'})

def form_0500(request):
    return render(request, 'lapbul_app/form_0500.html', {'title': 'Lapbul Ojk'})

def form_0600(request):
    return render(request, 'lapbul_app/form_0600.html', {'title': 'Lapbul Ojk'})

def form_0601(request):
    return render(request, 'lapbul_app/form_0601.html', {'title': 'Lapbul Ojk'})

def form_0602(request):
    return render(request, 'lapbul_app/form_0602.html', {'title': 'Lapbul Ojk'})

def form_0700(request):
    return render(request, 'lapbul_app/form_0700.html', {'title': 'Lapbul Ojk'})

def form_0800(request):
    return render(request, 'lapbul_app/form_0800.html', {'title': 'Lapbul Ojk'})

def form_0900(request):
    return render(request, 'lapbul_app/form_0900.html', {'title': 'Lapbul Ojk'})

def form_0901(request):
    return render(request, 'lapbul_app/form_0901.html', {'title': 'Lapbul Ojk'})

def form_1000(request):
    return render(request, 'lapbul_app/form_1000.html', {'title': 'Lapbul Ojk'})

def form_1100(request):
    return render(request, 'lapbul_app/form_1100.html', {'title': 'Lapbul Ojk'})

def form_1200(request):
    return render(request, 'lapbul_app/form_1200.html', {'title': 'Lapbul Ojk'})

def form_1300(request):
    return render(request, 'lapbul_app/form_1300.html', {'title': 'Lapbul Ojk'})

def form_1400(request):
    return render(request, 'lapbul_app/form_1400.html', {'title': 'Lapbul Ojk'})

def form_1401(request):
    return render(request, 'lapbul_app/form_1401.html', {'title': 'Lapbul Ojk'})

def form_1500(request):
    return render(request, 'lapbul_app/form_1500.html', {'title': 'Lapbul Ojk'})

def form_1600(request):
    return render(request, 'lapbul_app/form_1600.html', {'title': 'Lapbul Ojk'})

def form_1700(request):
    return render(request, 'lapbul_app/form_1700.html', {'title': 'Lapbul Ojk'})

def form_1800(request):
    return render(request, 'lapbul_app/form_1800.html', {'title': 'Lapbul Ojk'})

def form_1900(request):
    return render(request, 'lapbul_app/form_1900.html', {'title': 'Lapbul Ojk'})

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

def slik(request):
    return render(request, 'lapbul_app/slikindex.html', {'title': 'Slik OJK'})

def form_A01(request):
    return render(request, 'lapbul_app/form_A01.html', {'title': 'Slik Ojk'})

def form_D01(request):
    return render(request, 'lapbul_app/form_D01.html', {'title': 'Slik Ojk'})

def form_D02(request):
    return render(request, 'lapbul_app/form_D02.html', {'title': 'Slik Ojk'})

def form_F01(request):
    return render(request, 'lapbul_app/form_F01.html', {'title': 'Slik Ojk'})

def form_F02(request):
    return render(request, 'lapbul_app/form_F02.html', {'title': 'Slik Ojk'})

def form_F06(request):
    return render(request, 'lapbul_app/form_F06.html', {'title': 'Slik Ojk'})

def form_K01(request):
    return render(request, 'lapbul_app/form_K01.html', {'title': 'Slik Ojk'})

def form_M01(request):
    return render(request, 'lapbul_app/form_M01.html', {'title': 'Slik Ojk'})
