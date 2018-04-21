from api.profiles.models import Profile


def save_profile(backend, user, response, *args, **kwargs):
    try:
        profile = Profile.objects.get(owner=user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(owner=user)
    print(response)
    profile.save()
