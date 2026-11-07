import datetime
from django.utils import timezone
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.portfolio.models import Profile, WebsiteSetting, SocialLink
from apps.skills.models import SkillCategory, Skill
from apps.projects.models import Project, ProjectTechnology
from apps.experience.models import Experience
from apps.education.models import Education
from apps.certifications.models import Certification
from apps.achievements.models import Achievement
from apps.blog.models import BlogPost, BlogTag
from apps.documents.models import Document


class Command(BaseCommand):
    help = 'Seeds initial portfolio CMS data with Bhola Kumar profile and structure.'

    def handle(self, *args, **options):
        self.stdout.write("Starting database seeding...")

        # 1. Profile
        profile, created = Profile.objects.get_or_create(
            name="Bhola Kumar",
            defaults={
                'professional_title': "Full-Stack Developer & Machine Learning Engineer",
                'short_intro': "Passionate about engineering scalable web applications, robust backends with Django, and cutting-edge Machine Learning / NLP architectures.",
                'bio': "I am an enthusiastic Full-Stack Developer and Machine Learning practitioner with deep expertise in Django, Python, MySQL, and modern JavaScript. I specialize in designing database-driven web platforms, creating seamless user experiences, and integrating intelligent predictive pipelines.",
                'career_objective': "To lead high-impact engineering projects, create scalable backend architectures, and develop full-stack applications that solve complex problems.",
                'current_focus': "Full-Stack Web Systems & Large Language Model Applications",
                'email': "bholasaw8347@gmail.com",
                'email2': "bk2821120@gmail.com",
                'phone': "+91 9905845253",
                'phone2': "+91 9279343240",
                'location': "India",
                'resume_tagline': "Dedicated software developer with extensive full-stack and data science background.",
                'years_of_experience': 2,
            }
        )
        self.stdout.write(f"Profile: {profile.name} (Created: {created})")

        # 2. Website Settings
        settings, s_created = WebsiteSetting.objects.get_or_create(
            site_name="Bhola Kumar | Portfolio",
            defaults={
                'seo_title': "Bhola Kumar â€” Full-Stack Developer & ML Engineer",
                'seo_description': "Official portfolio website of Bhola Kumar. Explore projects, technical skills, certifications, work experience, and articles.",
                'primary_color': "#6366f1",
                'secondary_color': "#8b5cf6",
                'footer_text': "Â© 2026 Bhola Kumar. All Rights Reserved. Built with Django & Bootstrap 5.",
            }
        )
        self.stdout.write(f"Website Settings initialized (Created: {s_created})")

        # 3. Social Links
        socials = [
            ('github', 'https://github.com', 'bi-github', 1),
            ('linkedin', 'https://linkedin.com', 'bi-linkedin', 2),
            ('twitter', 'https://x.com', 'bi-twitter-x', 3),
            ('kaggle', 'https://kaggle.com', 'bi-trophy', 4),
        ]
        for plat, url, icon, order in socials:
            SocialLink.objects.get_or_create(
                platform=plat,
                defaults={'url': url, 'icon': icon, 'display_order': order, 'active': True}
            )

        # 4. Skill Categories & Skills
        categories = [
            ("Programming", "programming", 1),
            ("Web Development", "web_development", 2),
            ("Machine Learning & AI", "machine_learning", 3),
            ("NLP", "nlp", 4),
            ("Deep Learning", "deep_learning", 5),
            ("Data & Analytics", "data_analytics", 6),
            ("Database", "database", 7),
            ("Tools & Cloud", "tools", 8),
        ]
        cat_objs = {}
        for name, slug, order in categories:
            cat, _ = SkillCategory.objects.get_or_create(
                name=name, defaults={'slug': slug, 'display_order': order, 'active': True}
            )
            cat_objs[slug] = cat

        skills_data = [
            ("Python", "programming", 5, "bi-filetype-py", 1),
            ("JavaScript", "programming", 4, "bi-filetype-js", 2),
            ("SQL", "programming", 4, "bi-database", 3),
            ("Django", "web_development", 5, "bi-hdd-network", 1),
            ("HTML5 / CSS3", "web_development", 5, "bi-filetype-html", 2),
            ("Bootstrap 5", "web_development", 5, "bi-bootstrap", 3),
            ("REST APIs", "web_development", 4, "bi-gear-wide-connected", 4),
            ("Scikit-Learn", "machine_learning", 4, "bi-cpu", 1),
            ("Pandas & NumPy", "data_analytics", 5, "bi-graph-up", 1),
            ("MySQL", "database", 5, "bi-database-fill-gear", 1),
            ("PostgreSQL", "database", 4, "bi-database-check", 2),
            ("Git / GitHub", "tools", 5, "bi-github", 1),
            ("Docker", "tools", 3, "bi-box-seam", 2),
            ("Transformers / HuggingFace", "nlp", 4, "bi-robot", 1),
            ("PyTorch", "deep_learning", 4, "bi-lightning-charge", 1),
        ]
        for name, cat_slug, level, icon, order in skills_data:
            Skill.objects.get_or_create(
                name=name,
                defaults={
                    'category': cat_objs.get(cat_slug),
                    'level': level,
                    'icon': icon,
                    'display_order': order,
                    'active': True
                }
            )

        # 5. Sample Projects
        projects_data = [
            {
                'title': "Personal Portfolio CMS & Portal",
                'short_description': "A fully database-driven developer portfolio CMS built with Django, MySQL, and modern glassmorphism UI.",
                'description': "Comprehensive personal portfolio CMS featuring an independent, secure owner administration portal for content management, dynamic public pages, and full CRUD for projects, experience, documents, and messages.",
                'problem_statement': "Most developer portfolios require manual HTML/CSS file edits whenever new projects, certificates, or skills are added.",
                'solution': "Engineered a dynamic Django architecture with MySQL that allows instantaneous updates to all site sections via an intuitive owner dashboard.",
                'category': 'web_development',
                'status': 'completed',
                'featured': True,
                'technologies': ['Django', 'Python', 'MySQL', 'Bootstrap 5', 'JavaScript'],
                'github_url': 'https://github.com',
                'live_demo_url': 'https://example.com',
                'start_date': datetime.date(2026, 1, 1),
                'end_date': datetime.date(2026, 2, 1),
            },
            {
                'title': "Intelligent NLP Document Classifier",
                'short_description': "Automated text categorization and sentiment analysis engine powered by PyTorch and Transformers.",
                'description': "An end-to-end natural language processing pipeline capable of analyzing unstructured documents, clustering technical subjects, and providing confidence metrics.",
                'problem_statement': "Manual sorting of extensive legal and technical repositories is slow and error-prone.",
                'solution': "Fine-tuned transformer architecture on domain-specific corpora to attain 94.8% classification precision.",
                'category': 'nlp',
                'status': 'completed',
                'featured': True,
                'technologies': ['PyTorch', 'HuggingFace', 'Python', 'Flask', 'Docker'],
                'github_url': 'https://github.com',
                'live_demo_url': 'https://example.com',
                'start_date': datetime.date(2025, 9, 1),
                'end_date': datetime.date(2025, 12, 1),
            },
            {
                'title': "Predictive Customer Churn Engine",
                'short_description': "Data analytics and machine learning solution for proactive subscriber retention.",
                'description': "Engineered predictive machine learning models incorporating feature engineering, hyperparameter optimization, and real-time inference dashboards.",
                'problem_statement': "High customer attrition rates without advance behavioral indicators.",
                'solution': "Built gradient boosting classifier with explainable AI (SHAP) metrics.",
                'category': 'machine_learning',
                'status': 'completed',
                'featured': True,
                'technologies': ['Scikit-Learn', 'Pandas', 'XGBoost', 'MySQL', 'Streamlit'],
                'github_url': 'https://github.com',
                'live_demo_url': 'https://example.com',
                'start_date': datetime.date(2025, 5, 1),
                'end_date': datetime.date(2025, 8, 1),
            }
        ]

        for p_data in projects_data:
            techs = p_data.pop('technologies')
            p, p_c = Project.objects.get_or_create(
                title=p_data['title'],
                defaults=p_data
            )
            if p_c:
                for tech in techs:
                    ProjectTechnology.objects.create(project=p, name=tech)

        # 6. Education
        Education.objects.get_or_create(
            degree="Bachelor of Technology in Computer Science & Engineering",
            defaults={
                'institution': "University Institute of Technology",
                'university_or_board': "State Technical University",
                'start_year': 2021,
                'end_year': 2025,
                'result': "8.5 CGPA",
                'description': "Specialized in Software Engineering, Database Management Systems, Data Structures, and Machine Learning.",
                'display_order': 1,
                'active': True
            }
        )

        # 7. Experience
        Experience.objects.get_or_create(
            position="Full-Stack Developer Intern",
            defaults={
                'company': "Tech Innovations Lab",
                'employment_type': 'internship',
                'location': "Bengaluru, India (Remote)",
                'start_date': datetime.date(2025, 6, 1),
                'end_date': datetime.date(2025, 12, 1),
                'currently_working': False,
                'description': "Contributed to backend API architecture, database schema design, and responsive web portal interfaces.",
                'responsibilities': "Architected RESTful endpoints utilizing Django REST Framework.\nOptimized MySQL query execution times by 35% using composite indexes.\nCollaborated with UI/UX engineers to deploy accessible Bootstrap components.",
                'skills_used': "Python, Django, MySQL, Bootstrap 5, Git",
                'display_order': 1,
                'active': True
            }
        )

        # 8. Certifications
        Certification.objects.get_or_create(
            name="Python for Data Science & Machine Learning",
            defaults={
                'organization': "Coursera / DeepLearning.AI",
                'issue_date': datetime.date(2025, 4, 1),
                'credential_id': "CERT-PY-2025-9988",
                'verification_url': "https://coursera.org",
                'description': "Comprehensive training in NumPy, Pandas, Scikit-Learn, Supervised & Unsupervised Learning.",
                'display_order': 1,
                'active': True
            }
        )

        # 9. Achievements
        Achievement.objects.get_or_create(
            title="1st Runner-Up â€” National Level AI Hackathon",
            defaults={
                'organization': "TechFest 2025",
                'date': datetime.date(2025, 10, 15),
                'description': "Developed a real-time accessibility translation tool using NLP and Computer Vision within a 36-hour sprint.",
                'verification_url': "https://example.com",
                'display_order': 1,
                'active': True
            }
        )

        # 10. Blog Tags & Posts
        admin_user = User.objects.filter(is_superuser=True).first()
        t1, _ = BlogTag.objects.get_or_create(name="Django")
        t2, _ = BlogTag.objects.get_or_create(name="Python")
        t3, _ = BlogTag.objects.get_or_create(name="Machine Learning")

        post, post_c = BlogPost.objects.get_or_create(
            title="Building Scalable Database-Driven Web Applications with Django & MySQL",
            defaults={
                'content': "Django is one of the most reliable and mature web frameworks in the Python ecosystem. Combined with MySQL, it provides a rock-solid foundation for enterprise web applications, content management systems, and high-throughput APIs.\n\nIn this article, we explore the architectural advantages of clean app decoupling, environment-driven configurations, and database query optimization techniques.",
                'author': admin_user,
                'published': True,
                'featured': True,
                'published_at': timezone.now(),
            }
        )
        if post_c:
            post.tags.add(t1, t2)

        # 11. Freelance Services
        from apps.services.models import Service

        services_data = [
            {
                'title': "Excel Data Cleaning & Analysis",
                'short_description': "Transform messy spreadsheets into clean, structured datasets and automated executive reports.",
                'description': "Professional Excel spreadsheet solutions including data cleaning, structure normalization, dynamic formula modeling, and executive summary dashboards.",
                'deliverables': "Data cleaning and formatting\nDuplicate and missing-value handling\nPivot Tables and XLOOKUP\nExcel dashboards and reports",
                'technologies': "Microsoft Excel, Advanced Excel",
                'icon': "bi-file-earmark-spreadsheet",
                'starting_price': "Starting at $49",
                'display_order': 1,
                'is_active': True,
            },
            {
                'title': "Power BI Dashboard Development",
                'short_description': "Interactive business intelligence dashboards and executive KPI reports with real-time analytics.",
                'description': "Custom Power BI solutions with multi-source data modeling (Power Query), DAX metrics, intuitive drill-downs, and executive KPI monitoring.",
                'deliverables': "Sales dashboards\nBusiness performance reports\nKPI visualization\nInteractive charts and filters",
                'technologies': "Power BI, Power Query, DAX",
                'icon': "bi-bar-chart-steps",
                'starting_price': "Starting at $99",
                'display_order': 2,
                'is_active': True,
            },
            {
                'title': "Python Data Analysis",
                'short_description': "End-to-end data processing, exploratory data analysis, and automated insight generation.",
                'description': "Complete data pipelines using Python ecosystem. Cleaning messy datasets, performing exploratory statistical analysis, and generating visual data stories.",
                'deliverables': "Data cleaning using Pandas\nExploratory Data Analysis\nData visualization\nAutomated data reports",
                'technologies': "Python, Pandas, NumPy, Matplotlib, Seaborn",
                'icon': "bi-filetype-py",
                'starting_price': "Starting at $79",
                'display_order': 3,
                'is_active': True,
            },
            {
                'title': "SQL Database Services",
                'short_description': "High-performance SQL queries, schema optimizations, complex joins, and business data extraction.",
                'description': "Robust SQL query writing, complex joins, CTEs, aggregation pipelines, and schema enhancements for MySQL and PostgreSQL databases.",
                'deliverables': "SQL query writing\nJoins and subqueries\nAggregations\nBusiness data extraction",
                'technologies': "SQL, PostgreSQL, MySQL",
                'icon': "bi-database-check",
                'starting_price': "Starting at $49",
                'display_order': 4,
                'is_active': True,
            },
            {
                'title': "Basic Machine Learning",
                'short_description': "Predictive modeling, regression, and classification pipelines to forecast trends and automate decisions.",
                'description': "Practical machine learning solutions covering feature engineering, model training, cross-validation, and inference prediction systems.",
                'deliverables': "Data preprocessing\nRegression and classification\nModel training and evaluation\nBasic prediction systems",
                'technologies': "Python, Scikit-learn, Pandas",
                'icon': "bi-cpu",
                'starting_price': "Starting at $119",
                'display_order': 5,
                'is_active': True,
            },
            {
                'title': "Django Website Development",
                'short_description': "Custom database-driven web platforms, owner admin portals, bug fixing, and full-stack solutions.",
                'description': "End-to-end full-stack web applications built with Django, PostgreSQL/MySQL, and modern frontend styling. Clean architecture and secure admin portals.",
                'deliverables': "Personal portfolio websites\nDjango-based websites\nAdmin dashboards\nWebsite bug fixing and customization",
                'technologies': "Python, Django, HTML, CSS, JavaScript, Bootstrap",
                'icon': "bi-hdd-network",
                'starting_price': "Starting at $149",
                'display_order': 6,
                'is_active': True,
            },
        ]

        for s_data in services_data:
            Service.objects.get_or_create(
                title=s_data['title'],
                defaults=s_data
            )

        self.stdout.write(self.style.SUCCESS("Database seeding completed successfully!"))
