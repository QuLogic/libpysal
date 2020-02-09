import unittest
import libpysal
import tempfile, os





class TestWIO(unittest.TestCase):
    def setUp(self):
        self.swmFile1 = libpysal.examples.get_path('ohio.swm')
        self.swmFile2 = libpysal.examples.get_path('us48_CONTIGUITY_EDGES_ONLY.swm')
        self.swmFile3 = libpysal.examples.get_path('us48_INVERSE_DISTANCE.swm')
        self.files = [self.swmFile1, self.swmFile2, self.swmFile3]


    def test_SWMIO(self):
        for file in self.files:
            f1 = libpysal.io.open(file)
            w1 = f1.read()

            f = tempfile.NamedTemporaryFile(suffix='.swm')
            fname = f.name
            f.close()

            with libpysal.io.open(fname, 'w') as f2:
                f2.varName = f1.varName
                f2.srs = f1.srs

                f2.write(w1)

            with libpysal.io.open(fname, 'r') as f:
                w2 = f.read()

            assert w1.pct_nonzero == w2.pct_nonzero
            os.remove(fname)


if __name__ == '__main__':
    unittest.main()
