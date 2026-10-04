from collections import deque
from typing import Optional, Dict, Any

class QueueAntrean:
    """
    Kelas untuk mengelola antrean layanan mahasiswa menggunakan konsep Queue (FIFO).
    """
    def __init__(self) -> None:
        self._queue: deque = deque()

    def enqueue(self, nomor_urut: str, nama: str) -> Dict[str, str]:
        """Menambahkan mahasiswa baru ke barisan antrean terbelakang."""
        mahasiswa = {"nomor_urut": nomor_urut, "nama": nama}
        self._queue.append(mahasiswa)
        return mahasiswa

    def dequeue(self) -> Optional[Dict[str, str]]:
        """Melayani dan menghapus mahasiswa di posisi paling depan."""
        if not self.is_empty():
            return self._queue.popleft()
        return None

    def peek(self) -> Optional[Dict[str, str]]:
        """Melihat mahasiswa yang berada di posisi paling depan tanpa menghapusnya."""
        if not self.is_empty():
            return self._queue[0]
        return None

    def is_empty(self) -> bool:
        """Memeriksa apakah antrean dalam keadaan kosong."""
        return len(self._queue) == 0

    def size(self) -> int:
        """Mengembalikan jumlah mahasiswa dalam antrean."""
        return len(self._queue)

    def get_all(self) -> list:
        """Mengembalikan daftar seluruh elemen antrean saat ini."""
        return list(self._queue)