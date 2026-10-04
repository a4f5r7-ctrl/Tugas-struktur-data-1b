from src.antrean import QueueAntrean
from src.undo import StackUndo

def main():
    print("="*60)
    print(" SIMULASI SISTEM ANTREAN DAN FITUR UNDO LAYANAN MAHASISWA")
    print("="*60)

    # 1. SIMULASI FITUR ANTREAN
    print("\n--- 1. SIMULASI FITUR ANTREAN (QUEUE - FIFO) ---")
    antrean = QueueAntrean()
    
    # Menambahkan 5 Data Mahasiswa
    data_mahasiswa = [
        ("A001", "Ahmad Farhan Rantisi"),
        ("A002", "Budi Santoso"),
        ("A003", "Citra Dewi"),
        ("A004", "Doni Pratama"),
        ("A005", "Eka Putri")
    ]
    
    print("\n[Operasi Enqueue - Penambahan 5 Mahasiswa]")
    for no, nama in data_mahasiswa:
        antrean.enqueue(no, nama)
        print(f"-> Enqueue: {no} - {nama} | Antrean: {antrean.get_all()}")

    print(f"\n[Operasi Peek]: Mahasiswa terdepan = {antrean.peek()}")
    
    print("\n[Operasi Dequeue - Pelayanan 2 Mahasiswa Terdepan]")
    print(f"<- Dequeue (Dilayani): {antrean.dequeue()}")
    print(f"<- Dequeue (Dilayani): {antrean.dequeue()}")
    print(f"Kondisi Antrean Akhir: {antrean.get_all()}")

    # 2. SIMULASI FITUR UNDO
    print("\n" + "="*60)
    print("--- 2. SIMULASI FITUR UNDO (STACK - LIFO) ---")
    undo = StackUndo()

    aktivitas_list = [
        ("2026-10-02 08:00", "Melayani A001 (Ahmad Farhan Rantisi)"),
        ("2026-10-02 08:10", "Melayani A002 (Budi Santoso)"),
        ("2026-10-02 08:20", "Melayani A003 (Citra Dewi)"),
        ("2026-10-02 08:30", "Cetak Transkrip Nilai"),
        ("2026-10-02 08:40", "Update Status Pembayaran")
    ]

    print("\n[Operasi Push - Pencatatan 5 Aktivitas]")
    for waktu, akt in aktivitas_list:
        undo.push(waktu, akt)
        print(f"-> Push: {akt}")

    print(f"\n[Operasi Peek]: Aktivitas Terakhir = {undo.peek()}")

    print("\n[Operasi Pop - Pembatalan/Undo 2 Aktivitas Terakhir]")
    print(f"<- Undo (Pop): {undo.pop()}")
    print(f"<- Undo (Pop): {undo.pop()}")
    print(f"Kondisi Stack Akhir: {undo.get_all()}")

if __name__ == "__main__":
    main()