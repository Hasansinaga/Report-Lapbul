from django.shortcuts import render, redirect
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from django.contrib import messages
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

def form_0006(request):
    """Main view untuk form 0006"""
    data = []
    jenis_setoran_options = []
    jenis_modal_options = []
    columns = []
    total_cbs = 0

    try:
        with connection.cursor() as cursor:
            # Ambil data utama menggunakan SELECT langsung dari tabel
            cursor.execute("""
                SELECT bulan, tahun, kodeljk, flagdetail, jenissetoran, 
                       tglojkoke, jenismodal, jumlahmodal, id_lap0006
                FROM lap0006 
                WHERE bulan = '07' AND tahun = '2025' AND kodeljk = '500949'
                ORDER BY id_lap0006
            """)
            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            
            for row in rows:
                row_dict = dict(zip(columns, row))
                # Format tanggal jika diperlukan
                if 'tglojkoke' in row_dict and row_dict['tglojkoke']:
                    if hasattr(row_dict['tglojkoke'], 'strftime'):
                        row_dict['tglojkoke'] = row_dict['tglojkoke'].strftime('%Y-%m-%d')
                    else:
                    # jika sudah string, bisa coba parse dulu
                      try:
                          dt = datetime.strptime(row_dict['tglojkoke'], '%Y-%m-%d')
                          row_dict['tglojkoke'] = dt.strftime('%-d/%-m/%Y')
                      except:
                          pass
                
                # Pastikan jumlahmodal adalah number
                if 'jumlahmodal' in row_dict and row_dict['jumlahmodal']:
                    try:
                        row_dict['jumlahmodal'] = float(row_dict['jumlahmodal'])
                    except (ValueError, TypeError):
                        row_dict['jumlahmodal'] = 0
                
                data.append(row_dict)

            # Dropdown Jenis Setoran
            try:
                cursor.execute("EXEC sandi_jnssetoran '500949'")
                rows = cursor.fetchall()
                for row in rows:
                    jenis_setoran_options.append({'value': row[0], 'label': row[1]})
            except Exception as e:
                logger.warning(f"Error getting jenis setoran options: {str(e)}")

            # Dropdown Jenis Modal  
            try:
                cursor.execute("EXEC sandi_jnsmodal '500949'")
                rows = cursor.fetchall()
                for row in rows:
                    jenis_modal_options.append({'value': row[0], 'label': row[1]})
            except Exception as e:
                logger.warning(f"Error getting jenis modal options: {str(e)}")

            # Ambil total CBS (jika ada stored procedure untuk ini)
            try:
                # Sesuaikan query ini dengan tabel CBS yang sebenarnya
                cursor.execute("""
                    SELECT ISNULL(SUM(jumlah_cbs), 0) as total_cbs
                    FROM cbs_modal_disetor 
                    WHERE bulan = '07' AND tahun = '2025' AND kodeljk = '500949'
                """)
                cbs_result = cursor.fetchone()
                if cbs_result:
                    total_cbs = cbs_result[0] or 0
            except Exception as cbs_error:
                logger.warning(f"Error getting CBS total: {str(cbs_error)}")
                total_cbs = 0

    except Exception as e:
        logger.error(f"Database error in form_0006: {str(e)}")
        messages.error(request, f"Terjadi kesalahan saat memuat data: {str(e)}")
        data = []

    context = {
        'title': 'Form 0006 - Data Modal Disetor',
        'data': data,
        'columns': columns,
        'jenis_setoran_options': jenis_setoran_options,
        'jenis_modal_options': jenis_modal_options,
        'total_cbs': total_cbs,
    }
    return render(request, 'lapbul_app/form_0006.html', context)


@csrf_protect
@require_http_methods(["POST"])
def insert_form_0006(request):
    """Insert new data for form 0006"""
    try:
        # Validasi input
        jenissetoran = request.POST.get('jenissetoran', '').strip()
        tglojkoke = request.POST.get('tglojkoke', '').strip()
        jenismodal = request.POST.get('jenismodal', '').strip()
        jumlahmodal = request.POST.get('jumlahmodal', '').strip()

        # Validasi required fields
        if not all([jenissetoran, tglojkoke, jenismodal, jumlahmodal]):
            return JsonResponse({
                'success': False, 
                'message': 'Semua field harus diisi.'
            })

        # Validasi format jumlah
        try:
            jumlahmodal_float = float(jumlahmodal)
            if jumlahmodal_float < 0:
                return JsonResponse({
                    'success': False, 
                    'message': 'Jumlah modal tidak boleh negatif.'
                })
        except ValueError:
            return JsonResponse({
                'success': False, 
                'message': 'Format jumlah modal tidak valid.'
            })

        with connection.cursor() as cursor:
            cursor.execute(
                "EXEC sp_insert_lap0006 '07', '2025', '500949', %s, %s, %s, %s",
                [jenissetoran, tglojkoke, jenismodal, jumlahmodal_float]
            )
            
            # Check if procedure execution was successful
            # Beberapa stored procedure mengembalikan result set
            try:
                result = cursor.fetchall()
                logger.info(f"Insert result: {result}")
            except:
                pass  # No result set returned

        return JsonResponse({
            'success': True, 
            'message': 'Data berhasil ditambahkan.'
        })
        
    except Exception as e:
        logger.error(f"Error in insert_form_0006: {str(e)}")
        return JsonResponse({
            'success': False, 
            'message': f'Terjadi kesalahan saat menambah data: {str(e)}'
        })


@csrf_protect
@require_http_methods(["POST"])
def update_form_0006(request):
    """Update existing data for form 0006"""
    try:
        # Validasi input - menggunakan id_lap0006 sebagai identifier
        id_lap0006 = request.POST.get('noidentitas', '').strip()  # frontend masih kirim sebagai noidentitas
        jenissetoran = request.POST.get('jenissetoran', '').strip()
        tglojkoke = request.POST.get('tglojkoke', '').strip()
        jenismodal = request.POST.get('jenismodal', '').strip()
        jumlahmodal = request.POST.get('jumlahmodal', '').strip()

        # Validasi required fields
        if not all([id_lap0006, jenissetoran, tglojkoke, jenismodal, jumlahmodal]):
            return JsonResponse({
                'success': False, 
                'message': 'Semua field harus diisi.'
            })

        # Validasi format jumlah
        try:
            jumlahmodal_float = float(jumlahmodal)
            if jumlahmodal_float < 0:
                return JsonResponse({
                    'success': False, 
                    'message': 'Jumlah modal tidak boleh negatif.'
                })
        except ValueError:
            return JsonResponse({
                'success': False, 
                'message': 'Format jumlah modal tidak valid.'
            })

        with connection.cursor() as cursor:
            try:
                # Coba menggunakan stored procedure terlebih dahulu
                cursor.execute(
                    "EXEC sp_update_lap0006 '07', '2025', '500949', %s, %s, %s, %s, %s",
                    [id_lap0006, jenissetoran, tglojkoke, jenismodal, jumlahmodal_float]
                )
            except Exception as sp_error:
                logger.warning(f"Stored procedure failed, using direct UPDATE: {str(sp_error)}")
                # Fallback ke UPDATE langsung
                cursor.execute("""
                    UPDATE lap0006 
                    SET jenissetoran = %s, tglojkoke = %s, jenismodal = %s, jumlahmodal = %s
                    WHERE id_lap0006 = %s AND bulan = '07' AND tahun = '2025' AND kodeljk = '500949'
                """, [jenissetoran, tglojkoke, jenismodal, jumlahmodal_float, id_lap0006])
            
            # Check if procedure execution was successful
            try:
                result = cursor.fetchall()
                logger.info(f"Update result: {result}")
            except:
                pass  # No result set returned

        return JsonResponse({
            'success': True, 
            'message': 'Data berhasil diperbarui.'
        })
        
    except Exception as e:
        logger.error(f"Error in update_form_0006: {str(e)}")
        return JsonResponse({
            'success': False, 
            'message': f'Terjadi kesalahan saat memperbarui data: {str(e)}'
        })


@csrf_protect
@require_http_methods(["POST"])
def delete_form_0006(request):
    """Delete data for form 0006"""
    try:
        # Menggunakan id_lap0006 sebagai identifier
        id_lap0006 = request.POST.get('noidentitas', '').strip()  # frontend masih kirim sebagai noidentitas
        
        if not id_lap0006:
            return JsonResponse({
                'success': False, 
                'message': 'ID laporan diperlukan untuk menghapus data.'
            })

        with connection.cursor() as cursor:
            # Check if data exists before deletion
            cursor.execute(
                "SELECT COUNT(*) FROM lap0006 WHERE id_lap0006 = %s AND bulan = '07' AND tahun = '2025' AND kodeljk = '500949'",
                [id_lap0006]
            )
            count = cursor.fetchone()[0]
            
            if count == 0:
                return JsonResponse({
                    'success': False, 
                    'message': 'Data tidak ditemukan.'
                })

            try:
                # Proceed with deletion using stored procedure
                cursor.execute(
                    "EXEC sp_delete_lap0006 '07', '2025', '500949', %s",
                    [id_lap0006]
                )
            except Exception as sp_error:
                logger.warning(f"Stored procedure failed, using direct DELETE: {str(sp_error)}")
                # Fallback ke DELETE langsung
                cursor.execute(
                    "DELETE FROM lap0006 WHERE id_lap0006 = %s AND bulan = '07' AND tahun = '2025' AND kodeljk = '500949'",
                    [id_lap0006]
                )
            
            # Check if procedure execution was successful
            try:
                result = cursor.fetchall()
                logger.info(f"Delete result: {result}")
            except:
                pass  # No result set returned

        return JsonResponse({
            'success': True, 
            'message': 'Data berhasil dihapus.'
        })
        
    except Exception as e:
        logger.error(f"Error in delete_form_0006: {str(e)}")
        return JsonResponse({
            'success': False, 
            'message': f'Terjadi kesalahan saat menghapus data: {str(e)}'
        })


# Helper function untuk get single record (untuk AJAX edit jika diperlukan)
@csrf_protect
@require_http_methods(["GET"])
def get_form_0006_detail(request, noidentitas):
    """Get detail data for editing"""
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM lap0006 WHERE noidentitas = %s AND bulan = '07' AND tahun = '2025' AND kodekantor = '500949'",
                [noidentitas]
            )
            columns = [col[0] for col in cursor.description]
            row = cursor.fetchone()
            
            if row:
                data = dict(zip(columns, row))
                # Format tanggal jika diperlukan
                if 'tglojkoke' in data and data['tglojkoke']:
                    if hasattr(data['tglojkoke'], 'strftime'):
                        data['tglojkoke'] = data['tglojkoke'].strftime('%Y-%m-%d')
                
                return JsonResponse({
                    'success': True, 
                    'data': data
                })
            else:
                return JsonResponse({
                    'success': False, 
                    'message': 'Data tidak ditemukan.'
                })
                
    except Exception as e:
        logger.error(f"Error in get_form_0006_detail: {str(e)}")
        return JsonResponse({
            'success': False, 
            'message': f'Terjadi kesalahan: {str(e)}'
        })