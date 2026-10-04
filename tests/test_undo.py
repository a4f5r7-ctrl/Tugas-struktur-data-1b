import os
import sys

# Menambahkan direktori utama (Tugas 1b) ke Python Path agar folder 'src' ditemukan
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

# Baru panggil modul dari src
from src.undo import StackUndo
import unittest

import unittest
from src.undo import StackUndo

class TestStackUndo(unittest.TestCase):

    def setUp(self) -> None:
        self.undo_stack = StackUndo()

    def test_is_empty_awal(self) -> None:
        """Uji kondisi stack kosong di awal."""
        self.assertTrue(self.undo_stack.is_empty())

    def test_push(self) -> None:
        """Uji penambahan riwayat aktivitas baru."""
        self.undo_stack.push("2026-10-02 08:00", "Melayani A001")
        self.assertFalse(self.undo_stack.is_empty())
        self.assertEqual(self.undo_stack.size(), 1)

    def test_peek(self) -> None:
        """Uji melihat aktivitas terakhir."""
        self.undo_stack.push("2026-10-02 08:00", "Melayani A001")
        self.undo_stack.push("2026-10-02 08:10", "Melayani A002")
        terakhir = self.undo_stack.peek()
        self.assertEqual(terakhir["aktivitas"], "Melayani A002")

    def test_pop_undo(self) -> None:
        """Uji pembatalan aktivitas terakhir (LIFO)."""
        self.undo_stack.push("2026-10-02 08:00", "Melayani A001")
        self.undo_stack.push("2026-10-02 08:10", "Melayani A002")
        
        dibatalkan = self.undo_stack.pop()
        self.assertEqual(dibatalkan["aktivitas"], "Melayani A002")
        self.assertEqual(self.undo_stack.size(), 1)
        self.assertEqual(self.undo_stack.peek()["aktivitas"], "Melayani A001")

    def test_pop_empty(self) -> None:
        """Uji pop pada stack kosong."""
        self.assertIsNone(self.undo_stack.pop())

if __name__ == '__main__':
    unittest.main()