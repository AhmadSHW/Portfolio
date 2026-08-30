from django.db import models


class Profile(models.Model):
    full_name = models.CharField(max_length=120)
    title = models.CharField(max_length=150)
    typing_roles = models.CharField(
        max_length=255,
        default="Full-Stack Developer, Django Developer, Problem Solver"
    )
    tagline = models.TextField(max_length=300)
    about_text = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    cv_file = models.FileField(upload_to='cv/', blank=True, null=True)

    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=120, blank=True)

    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True, verbose_name="X / Twitter URL")

    years_experience = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Profile (homepage data)"
        verbose_name_plural = "Profile (homepage data)"

    def __str__(self):
        return self.full_name

    def roles_list(self):
        return [r.strip() for r in self.typing_roles.split(',') if r.strip()]


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('database', 'Database'),
        ('tools', 'Tools & DevOps'),
    ]

    name = models.CharField(max_length=60)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='backend')
    proficiency = models.PositiveIntegerField(default=80)
    icon_class = models.CharField(max_length=60, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['category', 'order', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Project(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, blank=True)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)

    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)

    featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',') if t.strip()]


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=150, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject or 'No subject'}"