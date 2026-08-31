from django.core.management.base import BaseCommand
from portfolio.models import Profile, Skill, Project
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Seeds the database with initial Profile, Skills, and Projects data"

    def handle(self, *args, **options):
        # ---------------------------------------------------
        # 1) Profile
        # ---------------------------------------------------
        profile, created = Profile.objects.get_or_create(
            id=1,
            defaults={
                'full_name': 'Ahmad Shweiki',
                'title': 'Full-Stack Web Developer',
                'typing_roles': 'Full-Stack Developer, Django Developer, Problem Solver',
                'tagline': 'I build complete web applications from idea to deployment — solid Django backends with clean Bootstrap interfaces.',
                'about_text': (
                    'Full-Stack developer based in Ramallah, Palestine, graduate of the '
                    'Full Stack Web Development program at AXSOS Academy (660 training hours). '
                    'I mainly work with Python, Django, MySQL, and JavaScript, and I have built '
                    'several deployed projects covering authentication, online payments, real-time '
                    'messaging, and server deployment on AWS EC2. Currently learning the MERN Stack '
                    'to expand my skills as a Full-Stack developer.'
                ),
                'email': 'ahmadshwiki780@gmail.com',
                'phone': '0597125929',
                'location': 'Ramallah, Palestine',
                'github_url': 'https://github.com/AhmadSHW',
                'linkedin_url': 'https://linkedin.com/in/ahmadalshwiki',
                'years_experience': 1,
            }
        )
        self.stdout.write(self.style.SUCCESS(
            f"{'Created' if created else 'Already exists'}: Profile ✅"
        ))

        # ---------------------------------------------------
        # 2) Skills
        # ---------------------------------------------------
        skills_data = [
            ('Python', 'backend', 90),
            ('Django', 'backend', 90),
            ('REST APIs', 'backend', 80),
            ('Stripe API', 'backend', 70),
            ('Twilio API', 'backend', 70),
            ('JavaScript', 'frontend', 80),
            ('Bootstrap 5', 'frontend', 90),
            ('HTML5 & CSS3', 'frontend', 90),
            ('MySQL', 'database', 85),
            ('Git & GitHub', 'tools', 85),
            ('AWS EC2', 'tools', 65),
        ]
        for order, (name, category, proficiency) in enumerate(skills_data):
            Skill.objects.update_or_create(
                name=name,
                defaults={'category': category, 'proficiency': proficiency, 'order': order}
            )
        self.stdout.write(self.style.SUCCESS(f"Added {len(skills_data)} skills ✅"))

        # ---------------------------------------------------
        # 3) Projects (edit the links later once you confirm real repo names)
        # ---------------------------------------------------
        projects_data = [
            {
                'title': 'BloodBridge Palestine',
                'description': (
                    'A blood donation platform with two account types (Donor / Hospital), '
                    'featuring blood type compatibility logic, city-based filtering, and '
                    'Twilio WhatsApp API integration for donor notifications.'
                ),
                'tech_stack': 'Django, MySQL, Bootstrap 5, Twilio API',
                'github_url': 'https://github.com/AhmadSHW/BloodBridge_Palestine',
                'live_url': '',
                'featured': True,
                'order': 1,
            },
            {
                'title': 'Rentora',
                'description': (
                    'A peer-to-peer tool rental platform — a graduation group project. '
                    'Responsible for the entire booking module (date conflict prevention, '
                    'dashboard, approve/reject flow), with AI-powered search (Gemini) and '
                    'Stripe payments, deployed on AWS EC2.'
                ),
                'tech_stack': 'Django, MySQL, Bootstrap 5, Stripe, AWS EC2, Gemini AI',
                'github_url': 'https://github.com/AhmadSHW/Rentora',
                'live_url': '',
                'featured': True,
                'order': 2,
            },
            {
                'title': 'DojoReads',
                'description': (
                    'A book review and rating platform with a custom session-based '
                    'authentication system, bcrypt password hashing, and full CRUD operations.'
                ),
                'tech_stack': 'Django, MySQL, Bootstrap 5, bcrypt',
                'github_url': 'https://github.com/AhmadSHW/DojoReads',
                'live_url': '',
                'featured': False,
                'order': 3,
            },
            {
                'title': 'The Wall',
                'description': (
                    'A Facebook-style social messaging app built with two separate Django apps, '
                    'using AJAX (Fetch API) for real-time interaction, and a 30-minute owner-only '
                    'delete window for posts.'
                ),
                'tech_stack': 'Django, MySQL, JavaScript (AJAX), Bootstrap 5, bcrypt',
                'github_url': 'https://github.com/AhmadSHW/The-Wall',
                'live_url': '',
                'featured': False,
                'order': 4,
            },
        ]

        for p in projects_data:
            Project.objects.update_or_create(title=p['title'], defaults=p)

        self.stdout.write(self.style.SUCCESS(f"Added {len(projects_data)} projects ✅"))
        self.stdout.write(self.style.SUCCESS("Done! Open /admin later to fine-tune anything (real GitHub links, project images)."))

        #================================================================================
        #4) Superuser (admin account) - only created if it doesn't exist yet
        #==================================================================
        if not User.objects.filter(username='AboShwiki').exists():
            User.objects.create_superuser(
                username='AboShwiki',
                email='ahmadshwiki780@gmail.com',
                password='Aboshwiki20!'
            )
            self.stdout.write(self.style.SUCCESS("Superuser 'AboShwiki' created"))
        else:
            self.stdout.write(self.style.SUCCESS("Superuser already exists"))