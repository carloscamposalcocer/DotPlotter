import DotPlotter
import unittest


class TestDotPlotter(unittest.TestCase):
    _csvPath = "./testdots.csv"


    def setUp(self):
        self.Plotter = DotPlotter.Plotter()

    def test_LoadCSV_BadFile_ReturnsFalse(self):
        bad_path = "kdjfaa.csv"
        self.assertEqual(self.Plotter.LoadCSV(bad_path),False)

    def test_LoadCSV_GoodFile_AssertPoint0(self):
        self.Plotter.LoadCSV(_csv_path)
        self.assertEqual(self.Plotter.Points[0].x,0)
        self.assertEqual(self.Plotter.Points[0].y,1)
        self.assertEqual(self.Plotter.Points[0].z,2)

if __name__ == "__main__":
    unittest.main()
    input("Press any  key to exit...")


