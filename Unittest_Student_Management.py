import unittest
from student_management import add_student, view_students, update_student, delete_student

class testStudentManagement(unittest.TestCase):
    def setUp(self):
        self.sample_student = ("John Doe", 16, "G", "S123", "Mathes, Science")


    def test_add_student(self):
        result = add_student(*self.sample_student)
        self.assertTrue(result) 
        
    def test_view_students_empty(self):
        # Ensure viewing students returns an empty list initially
        self.assertEqual(view_students(), [])

    def test_view_students_after_add(self):
        # Ensure added student is visible in the list
        add_student(*self.sample_student)
        self.assertIn(self.sample_student, view_students())
    
    def test_update_student(self):
        # Test updating an existing student
        add_student(*self.sample_student)
        updated_info = (1, "Jane Doe", 21, "Junior", ["Physics", "Chemistry"])
        self.assertTrue(update_student(*updated_info))
        self.assertIn(updated_info, view_students())

    def test_delete_student(self):
        # Test deleting an existing student
        add_student(*self.sample_student)
        self.assertTrue(delete_student(1))
        self.assertNotIn(self.sample_student, view_students())

if __name__ == "__main__":
    unittest.main()
