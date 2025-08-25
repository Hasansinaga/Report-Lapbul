from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods


def form_0007(request):
    # Fetch data for form 0007
    data = []
    try:
        with connection.cursor() as cursor:
            cursor.execute("EXEC sp_get_lap0007 '07', '2025', '500949'")
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            for row in rows:
                data.append(dict(zip(columns, row)))
            print(f"[form_0007] fetched rows: {len(data)}; columns: {columns}")
            if data:
                sample_keys = list(data[0].keys())
                print(f"[form_0007] first row keys: {sample_keys}")

            # Extra diagnostics: compare against raw table counts with same filters
            try:
                cursor.execute("SELECT COUNT(*) FROM lap0007 WHERE tahun=%s AND bulan=%s AND kodeljk=%s", ['2025','07','500949'])
                raw_count = cursor.fetchone()[0]
                print(f"[form_0007][diag] lap0007 raw count (2025/07/500949): {raw_count}")
                cursor.execute("SELECT TOP 10 nopyd FROM lap0007 WHERE tahun=%s AND bulan=%s AND kodeljk=%s ORDER BY nopyd", ['2025','07','500949'])
                ids = [r[0] for r in cursor.fetchall()]
                print(f"[form_0007][diag] sample nopyd list: {ids}")
            except Exception as diag_err:
                print(f"[form_0007][diag] raw table check failed: {diag_err}")
    except Exception as e:
        print(f"Database error (form_0007): {str(e)}")
        data = []

    context = {
        'title': 'Lapbul Ojk',
        'data': data,
        'columns': columns if data else [],
    }
    return render(request, 'lapbul_app/form_0007.html', context)


@csrf_protect
@require_http_methods(["POST"])
def update_form_0007(request):
    """Handle updates for form 0007"""
    try:
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

        with connection.cursor() as cursor:
            cursor.execute(
                "EXEC sp_update_lap0007 '07', '2025', '500949', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s",
                [
                    nopyd, cif, kodegolkreditur, sandibank, kodedati2, kodejenispyd, sandihubbank,
                    jwmulai, jwtempo, sukubunga, carahitbunga, plafon, kodejnsagunan,
                    nominalagunan, bakidebet, bytranbelumamor, diskontobelumamor, bakidebetneto
                ]
            )

        return JsonResponse({'success': True, 'message': 'Data berhasil diperbarui.'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Terjadi kesalahan: {str(e)}'})


@csrf_protect
@require_http_methods(["POST"])
def insert_form_0007(request):
    """Handle insert for form 0007"""
    try:
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

        with connection.cursor() as cursor:
            cursor.execute(
                "EXEC sp_insert_lap0007 '07', '2025', '500949', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s",
                [
                    nopyd, cif, kodegolkreditur, sandibank, kodedati2, kodejenispyd, sandihubbank,
                    jwmulai, jwtempo, sukubunga, carahitbunga, plafon, kodejnsagunan,
                    nominalagunan, bakidebet, bytranbelumamor, diskontobelumamor, bakidebetneto
                ]
            )

        return JsonResponse({'success': True, 'message': 'Data berhasil ditambahkan.'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Terjadi kesalahan: {str(e)}'})


@csrf_protect
@require_http_methods(["POST"])
def delete_form_0007(request):
    """Handle delete for form 0007"""
    try:
        cif = request.POST.get('cif', '')
        if not cif:
            return JsonResponse({'success': False, 'message': 'CIF diperlukan untuk menghapus data.'})

        with connection.cursor() as cursor:
            cursor.execute(
                "EXEC sp_delete_lap0007 '07', '2025', '500949', %s",
                [cif]
            )

        return JsonResponse({'success': True, 'message': 'Data berhasil dihapus.'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': f'Terjadi kesalahan: {str(e)}'})


