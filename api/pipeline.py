from api.profiles.models import Profile


def save_profile(backend, user, response, *args, **kwargs):
    try:
        profile = Profile.objects.get(owner=user)
    except Profile.DoesNotExist:
        profile = Profile.objects.create(owner=user)
    print(response)
    profile.display_name = response.get('displayName')
    user.first_name = response.get('name')['givenName']
    user.last_name = response.get('name')['familyName']
    profile.image = response.get('image')['url']
    user.save()
    profile.save()
