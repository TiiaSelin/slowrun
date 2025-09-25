from django.test import TestCase, override_settings
from django.urls import reverse
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile
from uutiset.models import Uutinen
import os, tempfile, shutil

@override_settings(MEDIA_ROOT=tempfile.mkdtemp())
class UutisetTest(TestCase):
    def setUp(self):
        fake_image = SimpleUploadedFile(
            name="test.jpg",
            content=b"",
            content_type="image/jpeg"
        )
        self.test_uutinen_0 = Uutinen.objects.create(id=1, title="testiotsikko", content="testikontentti", date=timezone.now(), picture=fake_image)
        self.test_uutinen_1 = Uutinen.objects.create(picture=fake_image)
        self.test_uutinen_2 = Uutinen.objects.create(picture=fake_image)

    def tearDown(self):
        shutil.rmtree(self._overridden_settings["MEDIA_ROOT"])

    def test_uutinen_creation(self):
        self.assertEqual(Uutinen.objects.count(), 3)

    def test_uutinen_string(self):
        self.assertEqual(self.test_uutinen_0.__str__(), "testiotsikko")

    def test_uutiset_view(self):
        response = self.client.get(reverse("uutiset"))
        self.assertContains(response, "testiotsikko")

    def test_uutiset_detail(self):
        response = self.client.get(reverse("uutinen_detail", args=[self.test_uutinen_0.id]))
        self.assertContains(response, "testiotsikko")

    def test_picture_deletion(self):
        for object in Uutinen.objects.all():
            object.delete()
        self.assertEqual(len(os.listdir(self._overridden_settings["MEDIA_ROOT"])), 0)