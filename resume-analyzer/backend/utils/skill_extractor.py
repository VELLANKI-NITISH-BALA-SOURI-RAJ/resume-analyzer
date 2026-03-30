import re
from typing import List

# Comprehensive skill taxonomy
SKILL_TAXONOMY = {
    "programming_languages": [
        "python", "java", "javascript", "typescript", "c++", "c#", "c", "go", "golang",
        "rust", "kotlin", "swift", "ruby", "php", "scala", "r", "matlab", "perl",
        "bash", "shell", "powershell", "dart", "lua", "haskell", "elixir", "clojure"
    ],
    "web_frontend": [
        "html", "css", "react", "reactjs", "react.js", "angular", "angularjs", "vue",
        "vuejs", "vue.js", "nextjs", "next.js", "nuxtjs", "svelte", "jquery", "bootstrap",
        "tailwind", "tailwindcss", "sass", "scss", "webpack", "vite", "redux", "graphql"
    ],
    "web_backend": [
        "nodejs", "node.js", "express", "expressjs", "fastapi", "django", "flask",
        "spring", "springboot", "spring boot", "laravel", "rails", "ruby on rails",
        "asp.net", "nestjs", "fastify", "gin", "fiber", "actix"
    ],
    "databases": [
        "sql", "mysql", "postgresql", "postgres", "mongodb", "redis", "sqlite",
        "oracle", "mssql", "sql server", "cassandra", "dynamodb", "firebase",
        "elasticsearch", "neo4j", "couchdb", "mariadb", "supabase"
    ],
    "cloud_devops": [
        "aws", "azure", "gcp", "google cloud", "docker", "kubernetes", "k8s",
        "terraform", "ansible", "jenkins", "ci/cd", "github actions", "gitlab ci",
        "helm", "prometheus", "grafana", "nginx", "apache", "linux", "unix",
        "cloudformation", "pulumi", "vagrant", "chef", "puppet"
    ],
    "ml_ai": [
        "machine learning", "deep learning", "neural networks", "nlp",
        "natural language processing", "computer vision", "tensorflow", "pytorch",
        "keras", "scikit-learn", "sklearn", "pandas", "numpy", "matplotlib",
        "seaborn", "hugging face", "transformers", "bert", "gpt", "llm",
        "reinforcement learning", "opencv", "xgboost", "lightgbm", "catboost",
        "mlflow", "kubeflow", "airflow", "spark", "hadoop", "data science"
    ],
    "tools_practices": [
        "git", "github", "gitlab", "bitbucket", "jira", "confluence", "agile",
        "scrum", "kanban", "rest api", "restful", "microservices", "tdd",
        "unit testing", "pytest", "jest", "selenium", "postman", "swagger",
        "openapi", "grpc", "kafka", "rabbitmq", "celery", "websocket"
    ],
    "data_engineering": [
        "etl", "data pipeline", "apache spark", "apache kafka", "airflow",
        "dbt", "snowflake", "bigquery", "redshift", "databricks", "tableau",
        "power bi", "looker", "data warehouse", "data lake", "hadoop"
    ],
    "security": [
        "cybersecurity", "penetration testing", "oauth", "jwt", "ssl", "tls",
        "encryption", "authentication", "authorization", "owasp", "soc2",
        "gdpr", "compliance", "vulnerability assessment", "firewalls"
    ],
    "soft_skills": [
        "leadership", "communication", "teamwork", "problem solving",
        "critical thinking", "project management", "time management",
        "collaboration", "mentoring", "presentation"
    ],
    "certifications": [
        "aws certified", "azure certified", "gcp certified", "pmp", "cissp",
        "ceh", "comptia", "ccna", "ccnp", "cka", "ckad", "google certified",
        "tensorflow developer", "databricks certified"
    ]
}

ALL_SKILLS = []
SKILL_CATEGORY_MAP = {}

for category, skills in SKILL_TAXONOMY.items():
    for skill in skills:
        ALL_SKILLS.append(skill)
        SKILL_CATEGORY_MAP[skill] = category


def extract_skills(text: str) -> List[str]:
    text_lower = text.lower()
    found_skills = set()

    for skill in ALL_SKILLS:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text_lower):
            found_skills.add(skill)

    # Normalize duplicates (e.g., react / reactjs)
    normalized = normalize_skills(list(found_skills))
    return sorted(normalized)


def normalize_skills(skills: List[str]) -> List[str]:
    alias_map = {
        "reactjs": "react",
        "react.js": "react",
        "vuejs": "vue",
        "vue.js": "vue",
        "nodejs": "node.js",
        "angularjs": "angular",
        "golang": "go",
        "sklearn": "scikit-learn",
        "postgres": "postgresql",
        "k8s": "kubernetes",
        "springboot": "spring boot",
    }
    normalized = set()
    for skill in skills:
        normalized.add(alias_map.get(skill, skill))
    return list(normalized)


def get_skill_category(skill: str) -> str:
    return SKILL_CATEGORY_MAP.get(skill, "general")


def get_all_skills() -> List[str]:
    return ALL_SKILLS
