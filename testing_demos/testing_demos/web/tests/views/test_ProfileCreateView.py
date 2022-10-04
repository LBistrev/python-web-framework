from django.test import TestCase
from django.urls import reverse

from testing_demos.web.models import Profile


class ProfileCreateViewTest(TestCase):
    VALID_PROFILE_DATA = {
        'first_name': 'Lyubo',
        'last_name': 'Bistrev',
        'age': 17,
    }

    def test_create_profile__when_all_valid__expect_to_create(self):
        self.client.post(
            reverse('create profile'),
            data=self.VALID_PROFILE_DATA,
        )

        profile = Profile.objects.first()
        self.assertIsNotNone(profile)
        self.assertEqual(self.VALID_PROFILE_DATA['first_name'], profile.first_name)
        self.assertEqual(self.VALID_PROFILE_DATA['last_name'], profile.last_name)
        self.assertEqual(self.VALID_PROFILE_DATA['age'], profile.age)

        # Test redirects
        # Test status code

    def test_create_profile__when_all_valid__expect_to_redirect_to_details(self):
        response = self.client.post(
            reverse('create profile'),
            data=self.VALID_PROFILE_DATA,
        )

        profile = Profile.objects.first()
        expected_url = reverse('details profile', kwargs={'pk': profile.pk})

        self.assertRedirects(response, expected_url)
