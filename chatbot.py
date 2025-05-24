class ChatBot:
    def __init__(self):
        # Main dataset with detailed responses
        self.dataset = {
            "greetings": {
                "keywords": ["hi", "hello", "hey", "greetings", "good morning"],
                "response": "Hello! Welcome to CMRIT. How can I help you today?"
            },
            "college_info": {
                "keywords": ["college", "about", "information", "details", "cmrit"],
                "response": """CMR Institute of Technology:
- Established: 2000
- Affiliation: VTU
- Location: AECS Layout, Bengaluru
- Accredited: NAAC 'A' Grade"""
            },
            "courses": {
                "keywords": ["courses", "programs", "branches", "degrees", "study"],
                "response": """We offer these engineering programs:
1. Computer Science (CSE)
2. Information Science (ISE)
3. Electronics (ECE)
4. Mechanical (ME)
5. Artificial Intelligence (AI/ML)
6. Civil Engineering (CE)"""
            },
            "admissions": {
                "keywords": ["admission", "apply", "join", "enroll", "process"],
                "response": "Admissions are based on KCET/COMEDK scores. Visit our website www.cmrit.ac.in for application details."
            },
            "default": {
                "response": "I'm sorry, I didn't understand. Could you rephrase your question? You can ask about admissions, courses, or college information."
            }
        }

    def get_response(self, user_input):
        user_input = user_input.lower().strip()
        
        # Check for matches in dataset
        for category in self.dataset:
            if category == "default":
                continue
                
            if any(keyword in user_input for keyword in self.dataset[category]["keywords"]):
                return self.dataset[category]["response"]
        
        # Check direct questions
        direct_answers = {
            "location": "We're located in AECS Layout, Bengaluru",
            "principal": "Our principal is Dr. Sanjay Jain",
            "website": "Visit us at www.cmrit.ac.in"
        }
        
        if user_input in direct_answers:
            return direct_answers[user_input]
            
        return self.dataset["default"]["response"]