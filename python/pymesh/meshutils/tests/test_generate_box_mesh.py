from pymesh.meshutils import generate_box_mesh
from pymesh.TestCase import TestCase

import numpy as np

class GenerateBoxMeshTest(TestCase):
    def test_3D(self):
        bbox_min = np.zeros(3);
        bbox_max = np.ones(3);
        vertices, voxels, info = generate_box_mesh(
                bbox_min, bbox_max);

        self.assertEqual(8, len(vertices));
        self.assertEqual(6, len(voxels));

        self.assert_array_equal(bbox_min, np.amin(vertices, axis=0));
        self.assert_array_equal(bbox_max, np.amax(vertices, axis=0));

    def test_2D(self):
        bbox_min = np.zeros(2);
        bbox_max = np.ones(2) * 100.5;

        vertices, voxels, info = generate_box_mesh(
                bbox_min, bbox_max);

        vertices, faces, info = generate_box_mesh(
                bbox_min, bbox_max);

        self.assertEqual(4, len(vertices));
        self.assertEqual(2, len(faces));

        self.assert_array_equal(bbox_min, np.amin(vertices, axis=0));
        self.assert_array_equal(bbox_max, np.amax(vertices, axis=0));

    def test_samples(self):
        bbox_min = np.zeros(3);
        bbox_max = np.ones(3);
        vertices, voxels, info = generate_box_mesh(
                bbox_min, bbox_max, num_samples=2);

        self.assertEqual(27, len(vertices));
        self.assertEqual(48, len(voxels));

        # There is a total of 8 cells.
        self.assertEqual(0, np.amin(info["cell_index"]));
        self.assertEqual(7, np.amax(info["cell_index"]));

        self.assert_array_equal(bbox_min, np.amin(vertices, axis=0));
        self.assert_array_equal(bbox_max, np.amax(vertices, axis=0));

    def test_symmetric_connectivity(self):
        bbox_min = np.zeros(3);
        bbox_max = np.ones(3);
        vertices, voxels, info = generate_box_mesh(
                bbox_min, bbox_max, keep_symmetry=True);

        self.assertEqual(15, len(vertices));
        self.assertEqual(24, len(voxels));

        self.assert_array_equal(bbox_min, np.amin(vertices, axis=0));
        self.assert_array_equal(bbox_max, np.amax(vertices, axis=0));

    def test_subdiv(self):
        bbox_min = np.zeros(3);
        bbox_max = np.ones(3);
        vertices, voxels, info = generate_box_mesh(
                bbox_min, bbox_max, subdiv_order=1);

        self.assertEqual(27, len(vertices));
        self.assertEqual(48, len(voxels));

        # All tets belongs to the same cell.
        self.assertEqual(0, np.amax(info["cell_index"]));
        self.assertEqual(0, np.amin(info["cell_index"]));

        self.assert_array_equal(bbox_min, np.amin(vertices, axis=0));
        self.assert_array_equal(bbox_max, np.amax(vertices, axis=0));
