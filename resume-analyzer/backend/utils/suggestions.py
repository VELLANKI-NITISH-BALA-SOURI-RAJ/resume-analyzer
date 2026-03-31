from typing import List, Dict

SKILL_SUGGESTIONS = {
    # Programming
    "python": {
        "resources": ["Python.org official tutorial", "Automate the Boring Stuff (free book)"],
        "course_url": "https://docs.python.org/3/tutorial/",
        "certifications": ["PCEP – Certified Entry-Level Python Programmer"],
        "tools": ["PyCharm", "Jupyter Notebook"]
    },
    "java": {
        "resources": ["Oracle Java Tutorials", "Effective Java by Joshua Bloch"],
        "course_url": "https://dev.java/learn/",
        "certifications": ["Oracle Certified Professional Java SE"],
        "tools": ["IntelliJ IDEA", "Maven", "Gradle"]
    },
    "javascript": {
        "resources": ["javascript.info", "MDN Web Docs"],
        "course_url": "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide",
        "certifications": ["freeCodeCamp JavaScript Algorithms"],
        "tools": ["VS Code", "Node.js", "npm"]
    },
    "typescript": {
        "resources": ["TypeScript Handbook (official)", "Total TypeScript by Matt Pocock"],
        "course_url": "https://www.typescriptlang.org/docs/handbook/intro.html",
        "certifications": [],
        "tools": ["VS Code", "ts-node"]
    },
    # Frontend
    "react": {
        "resources": ["React official docs (react.dev)", "Full Stack Open (Helsinki)"],
        "course_url": "https://react.dev/learn",
        "certifications": ["Meta Front-End Developer Certificate (Coursera)"],
        "tools": ["Vite", "Redux Toolkit", "React DevTools"]
    },
    "vue": {
        "resources": ["Vue.js official guide", "Vue Mastery"],
        "course_url": "https://vuejs.org/guide/introduction.html",
        "certifications": [],
        "tools": ["Vite", "Pinia", "Vue DevTools"]
    },
    "angular": {
        "resources": ["Angular official docs", "Angular University"],
        "course_url": "https://angular.io/docs",
        "certifications": [],
        "tools": ["Angular CLI", "RxJS", "NgRx"]
    },
    # Backend
    "fastapi": {
        "resources": ["FastAPI official docs", "TestDriven.io FastAPI course"],
        "course_url": "https://fastapi.tiangolo.com/tutorial/",
        "certifications": [],
        "tools": ["Uvicorn", "Pydantic", "SQLAlchemy"]
    },
    "django": {
        "resources": ["Django official tutorial", "Django for Beginners (book)"],
        "course_url": "https://docs.djangoproject.com/en/stable/intro/tutorial01/",
        "certifications": [],
        "tools": ["Django REST Framework", "Celery", "PostgreSQL"]
    },
    "node.js": {
        "resources": ["Node.js official docs", "The Odin Project"],
        "course_url": "https://nodejs.org/en/docs/guides/getting-started-guide/",
        "certifications": ["OpenJS Node.js Application Developer"],
        "tools": ["Express", "npm", "PM2"]
    },
    # Databases
    "postgresql": {
        "resources": ["PostgreSQL official tutorial", "pgexercises.com"],
        "course_url": "https://www.postgresql.org/docs/current/tutorial.html",
        "certifications": ["EDB PostgreSQL Associate"],
        "tools": ["pgAdmin", "DBeaver", "Prisma"]
    },
    "mongodb": {
        "resources": ["MongoDB University (free)", "MongoDB docs"],
        "course_url": "https://university.mongodb.com/",
        "certifications": ["MongoDB Associate Developer"],
        "tools": ["MongoDB Compass", "Mongoose", "Atlas"]
    },
    "redis": {
        "resources": ["Redis University", "Redis docs"],
        "course_url": "https://redis.com/university/",
        "certifications": ["Redis Certified Developer"],
        "tools": ["RedisInsight", "ioredis"]
    },
    # Cloud & DevOps
    "aws": {
        "resources": ["AWS Skill Builder (free)", "A Cloud Guru"],
        "course_url": "https://explore.skillbuilder.aws/learn",
        "certifications": ["AWS Certified Cloud Practitioner", "AWS Solutions Architect Associate"],
        "tools": ["AWS CLI", "CloudFormation", "CDK"]
    },
    "docker": {
        "resources": ["Docker official get-started guide", "Play with Docker"],
        "course_url": "https://docs.docker.com/get-started/",
        "certifications": ["Docker Certified Associate"],
        "tools": ["Docker Desktop", "Docker Compose", "Portainer"]
    },
    "kubernetes": {
        "resources": ["Kubernetes official tutorials", "KodeKloud"],
        "course_url": "https://kubernetes.io/docs/tutorials/",
        "certifications": ["CKA – Certified Kubernetes Administrator", "CKAD"],
        "tools": ["kubectl", "Helm", "k9s", "Minikube"]
    },
    "terraform": {
        "resources": ["HashiCorp Learn (free)", "Terraform: Up & Running (book)"],
        "course_url": "https://developer.hashicorp.com/terraform/tutorials",
        "certifications": ["HashiCorp Certified Terraform Associate"],
        "tools": ["Terraform Cloud", "Terragrunt", "tfsec"]
    },
    # ML / AI
    "machine learning": {
        "resources": ["Andrew Ng ML Specialization (Coursera)", "fast.ai"],
        "course_url": "https://www.coursera.org/specializations/machine-learning-introduction",
        "certifications": ["Google Professional ML Engineer", "AWS ML Specialty"],
        "tools": ["scikit-learn", "MLflow", "Weights & Biases"]
    },
    "deep learning": {
        "resources": ["Deep Learning Specialization (Coursera)", "fast.ai Part 2"],
        "course_url": "https://www.coursera.org/specializations/deep-learning",
        "certifications": ["TensorFlow Developer Certificate"],
        "tools": ["PyTorch", "TensorFlow", "CUDA"]
    },
    "pytorch": {
        "resources": ["PyTorch official tutorials", "Zero to Mastery PyTorch"],
        "course_url": "https://pytorch.org/tutorials/beginner/basics/intro.html",
        "certifications": [],
        "tools": ["torchvision", "Lightning", "Hugging Face"]
    },
    "tensorflow": {
        "resources": ["TensorFlow official tutorials", "DeepLearning.AI TF course"],
        "course_url": "https://www.tensorflow.org/tutorials",
        "certifications": ["TensorFlow Developer Certificate"],
        "tools": ["Keras", "TensorBoard", "TFX"]
    },
    "nlp": {
        "resources": ["Hugging Face NLP Course (free)", "Speech and Language Processing (Jurafsky)"],
        "course_url": "https://huggingface.co/learn/nlp-course/",
        "certifications": [],
        "tools": ["Hugging Face Transformers", "spaCy", "NLTK"]
    },
    "data science": {
        "resources": ["Kaggle Learn (free)", "Python for Data Analysis (book)"],
        "course_url": "https://www.kaggle.com/learn",
        "certifications": ["IBM Data Science Professional Certificate", "Google Data Analytics"],
        "tools": ["Jupyter", "Pandas", "Matplotlib", "Seaborn"]
    },
    # Tools
    "git": {
        "resources": ["Pro Git book (free)", "Learn Git Branching (interactive)"],
        "course_url": "https://git-scm.com/doc",
        "certifications": [],
        "tools": ["GitHub", "GitLab", "SourceTree"]
    },
    "linux": {
        "resources": ["Linux Journey (free)", "The Linux Command Line (book)"],
        "course_url": "https://linuxjourney.com/",
        "certifications": ["LPIC-1", "CompTIA Linux+"],
        "tools": ["Ubuntu", "bash", "vim", "tmux"]
    },
    "graphql": {
        "resources": ["GraphQL official docs", "How to GraphQL"],
        "course_url": "https://graphql.org/learn/",
        "certifications": [],
        "tools": ["Apollo", "Hasura", "GraphQL Playground"]
    },
    "kafka": {
        "resources": ["Confluent Kafka tutorials", "Kafka: The Definitive Guide (free)"],
        "course_url": "https://developer.confluent.io/learn-kafka/",
        "certifications": ["Confluent Certified Developer for Apache Kafka"],
        "tools": ["Confluent Platform", "Kafka UI", "ksqlDB"]
    },
}

DEFAULT_SUGGESTION = {
    "resources": ["Search on Coursera, Udemy, or YouTube for beginner tutorials"],
    "course_url": "",
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
            "course_url": info.get("course_url", ""),
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
