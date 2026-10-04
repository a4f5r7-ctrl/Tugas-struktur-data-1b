import unittest
from src.antrean import QueueAntrean

class TestQueueAntrean(unittest.TestCase):

    def setUp(self) -> None:
        self.antrean = QueueAntrean()

    def test_is_empty_awal(self) -> None:
        """Uji kondisi antrean kosong di awal."""
        self.assertTrue(self.antrean.is_empty())

    def test_enqueue(self) -> None:
        """Uji penambahan data antrean."""
        data = self.antrean.enqueue("A001", "Ahmad Farhan Rantisi")
        self.assertFalse(self.antrean.is_empty())
        self.assertEqual(self.antrean.size(), 1)
        self.assertEqual(data["nama"], "Ahmad Farhan Rantisi")

    def test_peek(self) -> None:
        """Uji melihat data paling depan."""
        self.antrean.enqueue("A001", "Ahmad Farhan Rantisi")
        self.antrean.enqueue("A002", "Budi Santoso")
        terdepan = self.antrean.peek()
        self.assertIsNotNone(terdepan)
        self.assertEqual(terdepan["nomor_urut"], "A001")

    def test_dequeue(self) -> None:
        """Uji pengambilan/pelayanan antrean (FIFO)."""
        self.antrean.enqueue("A001", "Ahmad Farhan Rantisi")
        self.antrean.enqueue("A002", "Budi Santoso")
        
        dilayani = self.antrean.dequeue()
        self.assertEqual(dilayani["nomor_urut"], "A001")
        self.assertEqual(self.antrean.size(), 1)
        self.assertEqual(self.antrean.peek()["nomor_urut"], "A002")

    def test_dequeue_empty(self) -> None:
        """Uji dequeue pada antrean kosong."""
        self.assertIsNone(self.antrean.dequeue())

if __name__ == '__main__':
    unittest.main()