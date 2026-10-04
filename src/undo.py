from typing import Optional, Dict, Any

class StackUndo:
    """
    Kelas untuk mengelola riwayat aktivitas petugas menggunakan konsep Stack (LIFO).
    """
    def __init__(self) -> None:
        self._stack: list = []

    def push(self, timestamp: str, aktivitas: str) -> Dict[str, str]:
        """Menambahkan aktivitas baru ke bagian teratas tumpukan (Stack)."""
        data_aktivitas = {"timestamp": timestamp, "aktivitas": aktivitas}
        self._stack.append(data_aktivitas)
        return data_aktivitas

    def pop(self) -> Optional[Dict[str, str]]:
        """Membatalkan (Undo) dan mengambil aktivitas terakhir dari tumpukan."""
        if not self.is_empty():
            return self._stack.pop()
        return None

    def peek(self) -> Optional[Dict[str, str]]:
        """Melihat aktivitas terakhir yang tersimpan tanpa membatalkannya."""
        if not self.is_empty():
            return self._stack[-1]
        return None

    def is_empty(self) -> bool:
        """Memeriksa apakah tumpukan aktivitas kosong."""
        return len(self._stack) == 0

    def size(self) -> int:
        """Mengembalikan jumlah riwayat aktivitas yang tersimpan."""
        return len(self._stack)

    def get_all(self) -> list:
        """Mengembalikan daftar seluruh elemen stack dari bawah ke atas."""
        return list(self._stack)