from django.contrib import admin
from django.db.models import Count, Min, Max

from api.challenges.models import Challenge


class ChallengeAdmin(admin.ModelAdmin):
    change_list_template = 'admin/challenge_admin.html'
    pass

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)

        try:
            qs = response.context_data['cl'].queryset
        except(AttributeError, KeyError):
            return response

        dFrequency = Challenge.objects.values('difficulty').distinct().annotate(frequency=Count('difficulty'))
        difficulty_range = dFrequency.aggregate(low=Min('difficulty'), max=Max('difficulty'))

        high = difficulty_range.get('max', 0)
        low = difficulty_range.get('low', 0)

        response.context_data['challenge_difficulty_frequency'] = [{
            'period': x['difficulty'],
            'total': int(x['frequency']) or 0,
            'bar_height': self.get_bar_height(high, low, x['frequency'])}

            for x in dFrequency]

        response.context_data['summary'] = list(
            qs.values('title', 'difficulty')
            .order_by('-difficulty')
        )

        return response

    def get_bar_height(self, high, low, frequency):
            if frequency == 0:
                return 0
            else:
                return ((frequency - low) / (high - low)) * 100


admin.site.register(Challenge, ChallengeAdmin)
