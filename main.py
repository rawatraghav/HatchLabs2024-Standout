# main.py
from dotenv import load_dotenv
from crewai import Crew
from agents.research_agent import ResearchAgent
from agents.scoring_agent import ScoringAgent

class CandidateScreeningSystem:
    def __init__(self):
        load_dotenv()
        self.research_agent = ResearchAgent()
        self.scoring_agent = ScoringAgent()
        
    def process_candidate(self, job_url, resume_path, linkedin_url=None, github_url=None):
        # 1. Collect data
        job_data = self.job_scraper.extract_job_details(job_url)
        resume_data = self.resume_parser.parse_resume(resume_path)
        
        # 2. Research phase
        profile_analysis = self.research_agent.analyze_profile({
            'resume': resume_data,
            'linkedin': linkedin_url,
            'github': github_url
        })
        
        # 3. Scoring phase
        scores = self.scoring_agent.calculate_scores(job_data, profile_analysis)
        
        return self.generate_report(profile_analysis, scores)