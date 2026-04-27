from .models import Badge, UserBadge, Submission, Challenge
from django.db.models import Count

class BadgeEvaluator:
    def __init__(self, user):
        self.user = user

    def evaluate_all(self):
        """Evalúa todas las insignias que el usuario aún no tiene."""
        earned_badge_ids = UserBadge.objects.filter(user=self.user).values_list('badge_id', flat=True)
        available_badges = Badge.objects.exclude(id__in=earned_badge_ids)
        
        new_badges = []
        for badge in available_badges:
            if self.check_badge(badge):
                UserBadge.objects.create(user=self.user, badge=badge)
                new_badges.append(badge)
        return new_badges

    def check_badge(self, badge):
        """Verifica si el usuario cumple las condiciones de una insignia específica."""
        conditions = badge.conditions
        if not conditions:
            return False

        # Verificar pre-requisitos
        if badge.prerequisites.exists():
            earned_ids = UserBadge.objects.filter(user=self.user).values_list('badge_id', flat=True)
            for pre in badge.prerequisites.all():
                if pre.id not in earned_ids:
                    return False

        condition_type = conditions.get('type')

        # Soporte para condiciones combinadas (AND/OR)
        if condition_type == 'composite':
            # {"type": "composite", "operator": "AND", "conditions": [...]}
            operator = conditions.get('operator', 'AND')
            sub_conditions = conditions.get('conditions', [])
            
            results = []
            for sub_cond in sub_conditions:
                # Recursivamente evaluar sub-condiciones
                temp_badge = Badge(conditions=sub_cond)
                results.append(self.check_badge(temp_badge))
            
            if operator == 'AND':
                return all(results) if results else False
            elif operator == 'OR':
                return any(results) if results else False

        if condition_type == 'solve_count':
            # {"type": "solve_count", "count": 10, "category": "web"}
            category = conditions.get('category')
            target_count = conditions.get('count', 1)
            
            qs = Submission.objects.filter(user=self.user, is_correct=True)
            if category:
                qs = qs.filter(challenge__category=category)
            
            return qs.count() >= target_count

        if condition_type == 'specific_challenges':
            # {"type": "specific_challenges", "challenge_ids": ["uuid1", "uuid2"]}
            challenge_ids = conditions.get('challenge_ids', [])
            solved_count = Submission.objects.filter(
                user=self.user, 
                is_correct=True, 
                challenge_id__in=challenge_ids
            ).values('challenge').distinct().count()
            
            return solved_count >= len(challenge_ids)

        if condition_type == 'first_blood':
            # {"type": "first_blood"}
            # Verifica si el usuario fue el primero en resolver cualquier reto
            first_solves = Submission.objects.filter(is_correct=True).order_by('challenge', 'solved_at').distinct('challenge')
            return any(solve.user == self.user for solve in first_solves)

        return False
