from django.test import TestCase, override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from kontaktilomake.models import Etusivukuva
import os, tempfile, shutil

fake_image = SimpleUploadedFile(
    name="test.jpg",
    content=b"",
    content_type="image/jpeg"
)

@override_settings(MEDIA_ROOT=tempfile.mkdtemp())
class KontaktilomakeTest(TestCase):
    def setUp(self):        
        self.test_etusivukuva_0 = Etusivukuva.objects.create(picture=fake_image)
        self.test_etusivukuva_1 = Etusivukuva.objects.create(title="testikuva", picture=fake_image)

    def tearDown(self):
        shutil.rmtree(self._overridden_settings["MEDIA_ROOT"])

    def test_picture_string(self):
        self.assertEqual(self.test_etusivukuva_0.__str__(), f"Kuva lisätty: {self.test_etusivukuva_0.uploaded_at:%y-%m-%d}")
        self.assertEqual(self.test_etusivukuva_1.__str__(), f"testikuva: {self.test_etusivukuva_1.uploaded_at:%y-%m-%d}")

    def test_picture_deletion_on_update(self):
        new_pic = Etusivukuva.objects.create(picture=fake_image)
        old_path = new_pic.picture.path
        new_pic.picture = fake_image
        new_pic.save()
        self.assertFalse(os.path.exists(old_path))

    def test_picture_deletion(self):
        for object in Etusivukuva.objects.all():
            object.delete()
        self.assertEqual(len(os.listdir(self._overridden_settings["MEDIA_ROOT"])), 0)
