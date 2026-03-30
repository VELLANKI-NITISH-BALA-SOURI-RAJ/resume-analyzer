from typing import List, Dict

SKILL_SUGGESTIONS = {
    # Programming
    "python": {
        "resources": ["Python.org official tutorial", "Automate the Boring Stuff (free book)"],
        "certifications": ["PCEP – Certified Entry-Level Python Programmer"],
        "tools": ["PyCharm", "Jupyter Notebook"]
    },
    "java": {
        "resources": ["Oracle Java Tutorials", "Effective Java by Joshua Bloch"],
        "certifications": ["Oracle Certified Professional Java SE"],
        "tools": ["IntelliJ IDEA", "Maven", "Gradle"]
    },
    "javascript": {
        "resources": ["javascript.info", "MDN Web Docs"],
        "certifications": ["freeCodeCamp JavaScript Algorithms"],
        "tools": ["VS Code", "Node.js", "npm"]
    },
    "typescript": {
        "resources": ["TypeScript Handbook (official)", "Total TypeScript by Matt Pocock"],
        "certifications": [],
        "tools": ["VS Code", "ts-node"]
    },
    # Frontend
    "react": {
        "resources": ["React official docs (react.dev)", "Full Stack Open (Helsinki)"],
        "certifications": ["Meta Front-End Developer Certificate (Coursera)"],
        "tools": ["Vite", "Redux Toolkit", "React DevTools"]
    },
    "vue": {
        "resources": ["Vue.js official guide", "Vue Mastery"],
        "certifications": [],
        "tools": ["Vite", "Pinia", "Vue DevTools"]
    },
    "angular": {
        "resources": ["Angular official docs", "Angular University"],
        "certifications": [],
        "tools": ["Angular CLI", "RxJS", "NgRx"]
    },
    # Backend
    "fastapi": {
        "resources": ["FastAPI official docs", "TestDriven.io FastAPI course"],
        "certifications": [],
        "tools": ["Uvicorn", "Pydantic", "SQLAlchemy"]
    },
    "django": {
        "resources": ["Django official tutorial", "Django for Beginners (book)"],
        "certifications": [],
        "tools": ["Django REST Framework", "Celery", "PostgreSQL"]
    },
    "node.js": {
        "resources": ["Node.js official docs", "The Odin Project"],
        "certifications": ["OpenJS Node.js Application Developer"],
        "tools": ["Express", "npm", "PM2"]
    },
    # Databases
    "postgresql": {
        "resources": ["PostgreSQL official tutorial", "pgexercises.com"],
        "certifications": ["EDB PostgreSQL Associate"],
        "tools": ["pgAdmin", "DBeaver", "Prisma"]
    },
    "mongodb": {
        "resources": ["MongoDB University (free)", "MongoDB docs"],
        "certifications": ["MongoDB Associate Developer"],
        "tools": ["MongoDB Compass", "Mongoose", "Atlas"]
    },
    "redis": {
        "resources": ["Redis University", "Redis docs"],
        "certifications": ["Redis Certified Developer"],
        "tools": ["RedisInsight", "ioredis"]
    },
    # Cloud & DevOps
    "aws": {
        "resources": ["AWS Skill Builder (free)", "A Cloud Guru"],
        "certifications": ["AWS Certified Cloud Practitioner", "AWS Solutions Architect Associate"],
        "tools": ["AWS CLI", "CloudFormation", "CDK"]
    },
    "docker": {
        "resources": ["Docker official get-started guide", "Play with Docker"],
        "certifications": ["Docker Certified Associate"],
        "tools": ["Docker Desktop", "Docker Compose", "Portainer"]
    },
    "kubernetes": {
        "resources": ["Kubernetes official tutorials", "KodeKloud"],
        "certifications": ["CKA – Certified Kubernetes Administrator", "CKAD"],
        "tools": ["kubectl", "Helm", "k9s", "Minikube"]
    },
    "terraform": {
        "resources": ["HashiCorp Learn (free)", "Terraform: Up & Running (book)"],
        "certifications": ["HashiCorp Certified Terraform Associate"],
        "tools": ["Terraform Cloud", "Terragrunt", "tfsec"]
    },
    # ML / AI
    "machine learning": {
        "resources": ["Andrew Ng ML Specialization (Coursera)", "fast.ai"],
        "certifications": ["Google Professional ML Engineer", "AWS ML Specialty"],
        "tools": ["scikit-learn", "MLflow", "Weights & Biases"]
    },
    "deep learning": {
        "resources": ["Deep Learning Specialization (Coursera)", "fast.ai Part 2"],
        "certifications": ["TensorFlow Developer Certificate"],
        "tools": ["PyTorch", "TensorFlow", "CUDA"]
    },
    "pytorch": {
        "resources": ["PyTorch official tutorials", "Zero to Mastery PyTorch"],
        "certifications": [],
        "tools": ["torchvision", "Lightning", "Hugging Face"]
    },
    "tensorflow": {
        "resources": ["TensorFlow official tutorials", "DeepLearning.AI TF course"],
        "certifications": ["TensorFlow Developer Certificate"],
        "tools": ["Keras", "TensorBoard", "TFX"]
    },
    "nlp": {
        "resources": ["Hugging Face NLP Course (free)", "Speech and Language Processing (Jurafsky)"],
        "certifications": [],
        "tools": ["Hugging Face Transformers", "spaCy", "NLTK"]
    },
    "data science": {
        "resources": ["Kaggle Learn (free)", "Python for Data Analysis (book)"],
        "certifications": ["IBM Data Science Professional Certificate", "Google Data Analytics"],
        "tools": ["Jupyter", "Pandas", "Matplotlib", "Seaborn"]
    },
    # Tools
    "git": {
        "resources": ["Pro Git book (free)", "Learn Git Branching (interactive)"],
        "certifications": [],
        "tools": ["GitHub", "GitLab", "SourceTree"]
    },
    "linux": {
        "resources": ["Linux Journey (free)", "The Linux Command Line (book)"],
        "certifications": ["LPIC-1", "CompTIA Linux+"],
        "tools": ["Ubuntu", "bash", "vim", "tmux"]
    },
    "graphql": {
        "resources": ["GraphQL official docs", "How to GraphQL"],
        "certifications": [],
        "tools": ["Apollo", "Hasura", "GraphQL Playground"]
    },
    "kafka": {
        "resources": ["Confluent Kafka tutorials", "Kafka: The Definitive Guide (free)"],
        "certifications": ["Confluent Certified Developer for Apache Kafka"],
        "tools": ["Confluent Platform", "Kafka UI", "ksqlDB"]
    },
}

DEFAULT_SUGGESTION = {
    "resources": ["Search on Coursera, Udemy, or YouTube for beginner tutorials"],
    "certifications": ["Look for vendor-specific certifications on the official website"],
    "tools": ["Explore the official documentation and community tools"]
}


def generate_suggestions(missing_skills: List[str]) -> List[Dict]:
    suggestions = []
    for skill in missing_skills:
        skill_lower = skill.lower()
        info = SKILL_SUGGESTIONS.get(skill_lower, DEFAULT_SUGGESTION)
        suggestions.append({
            "skill": skill,
            "resources": info.get("resources", []),
            "certifications": info.get("certifications", []),
            "tools": info.get("tools", []),
            "priority": _get_priority(skill_lower)
        })
    # Sort by priority: high → medium → low
    priority_order = {"high": 0, "medium": 1, "low": 2}
    suggestions.sort(key=lambda x: priority_order.get(x["priority"], 1))
    return suggestions


def _get_priority(skill: str) -> str:
    high_priority = [
        "python", "javascript", "java", "aws", "docker", "kubernetes",
        "machine learning", "react", "sql", "postgresql", "git"
    ]
    medium_priority = [
        "typescript", "node.js", "django", "fastapi", "mongodb", "redis",
        "terraform", "deep learning", "pytorch", "tensorflow", "linux"
    ]
    if skill in high_priority:
        return "high"
    elif skill in medium_priority:
        return "medium"
    return "low"
