from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import StudentProgress, Submission, Badge

User = get_user_model()

@receiver(post_save, sender=User)
def create_student_progress(sender, instance, created, **kwargs):
    if created:
        StudentProgress.objects.get_or_create(user=instance)

@receiver(post_save, sender=Submission)
def check_for_badges(sender, instance, created, **kwargs):
    if created and instance.is_correct:
        user = instance.user
        progress, _ = StudentProgress.objects.get_or_create(user=user)
        
        # Example Badge Logic: "First Blood"
        if progress.solved_challenges.count() == 1:
            first_blood, _ = Badge.objects.get_or_create(
                name="First Blood",
                defaults={
                    "description": "Solved your first challenge!",
                    "image_url": "https://example.com/badges/first-blood.png",
                    "criteria_json": {"type": "count", "value": 1}
                }
            )
            progress.badges.add(first_blood)
        
        # Example Badge Logic: "Category Master"
        category = instance.challenge.category
        category_solves = progress.solved_challenges.filter(category=category).count()
        if category_solves >= 5:
            master_badge, _ = Badge.objects.get_or_create(
                name=f"{category.capitalize()} Master",
                defaults={
                    "description": f"Solved 5 challenges in {category}",
                    "image_url": f"https://example.com/badges/{category}-master.png",
                    "criteria_json": {"type": "category_count", "category": category, "value": 5}
                }
            )
            progress.badges.add(master_badge)
