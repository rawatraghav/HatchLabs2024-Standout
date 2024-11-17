# test_screening.py
import unittest

class TestScreeningSystem(unittest.TestCase):
    def setUp(self):
        self.system = CandidateScreeningSystem()
    
    def test_end_to_end_screening(self):
        result = self.system.process_candidate(
            job_url="sample_job_url",
            resume_path="sample_resume.pdf",
            linkedin_url="sample_linkedin_url",
            github_url="sample_github_url"
        )
        self.assertIsNotNone(result)