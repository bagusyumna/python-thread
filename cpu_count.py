import multiprocessing

""" 
Jumlah CPU yang tersedia
"""
cpu_count = multiprocessing.cpu_count()

""" 
Max CPU utilization, 
Seberapa berat utilisasi CPU yang ingin di dapatkan. 
Rangenya dari 0-100% atau 0-1
"""
cpu_max_util = 1

""" 
(Wait Time / Compute time) (millisecond).
Wait time    --> Total waktu yang diperlukan untuk sebuah proses termasuk waktu untuk request ke service eksternal seperti database, API lain dll.
Compute time --> Total waktu yang diperlukan untuk sebuah proses tidak termasuk waktu untuk proses ke service eksternal. Dalam artian proses yang 
                 menggunakan resource CPU secara intensif sepeti kalkulasi berat.
"""
wait_time = 1000
compute_time = 200

total_thread = cpu_count * cpu_max_util * (1 + wait_time / compute_time)

print(total_thread)
