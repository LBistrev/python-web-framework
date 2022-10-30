from django.test import TestCase
from django.urls import reverse

from testing_demos.web.models import Profile


class ProfileEditViewTests(TestCase):
    VALID_PROFILE_DATA = {
        'first_name': 'Lyubo',
        'last_name': 'Bistrev',
        'age': 17,
    }

    def test_Edit_profile_with_valid_data(self):
        profile = Profile.objects.create(**self.VALID_PROFILE_DATA)

        response = self.client.post(
            reverse('edit profile', kwargs={
                'pk': profile.pk,
            }),
            data={
                'first_name': 'Lyubo',
                'last_name': 'Bistrev',
                'age': 18, }
        )

        updated_profile = Profile.objects.get(pk=profile.pk)

        self.assertEqual(18, updated_profile.age)
