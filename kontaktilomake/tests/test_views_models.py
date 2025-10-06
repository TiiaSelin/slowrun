from django.test import TestCase, override_settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError
from kontaktilomake.models import Etusivukuva, Viesti, Karttakuva
import os, tempfile, shutil
from django.urls import reverse



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

class LomakeTest(TestCase):
    def setUp(self):
        self.data = {
            "nimi": "Testaaja",
            "sahkoposti": "testaaja@example.com",
            "paikkakunta": "Turku",
            "viesti": "Tämä on testiviesti."
        }
        self.urls = ["index", "yhteystiedot"]

    def test_lomakkeet_post(self):
        """Testaa lomakkeiden POST-lähetyksen"""
        for url_name in self.urls:
            response = self.client.post(reverse(url_name), self.data)
            self.assertEqual(response.status_code, 200)
            self.assertTrue(Viesti.objects.filter(viesti="Tämä on testiviesti.").exists())
            self.assertContains(response, "Kiitos viestistäsi!")
            Viesti.objects.all().delete()
            
    def test_viesti_str(self):
        viesti = Viesti.objects.create(
            nimi="Testaaja",
            sahkoposti="testi@example.com",
            paikkakunta="Helsinki",
            viesti="Viesti"
        )
        self.assertEqual(str(viesti), "Testaaja")

class KarttakuvaTest(TestCase):
    def test_successful_karttakuva(self):
        test_karttakuva = Karttakuva.objects.create(
            url="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d586.0147216583372!2d25.0935470197192!3d60.3938491820283!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x469200837b9854fb%3A0xd2e75c30a3a74807!2sSienikatu%2C%2004260%20Kerava!5e0!3m2!1sfi!2sfi!4v1759327559912!5m2!1sfi!2sfi"
        )
        test_karttakuva.save()
        response = self.client.get(reverse("index"))
        self.assertEqual(Karttakuva.objects.count(), 1)
        self.assertContains(response, "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d586")

    def test_karttakuva_validation_in_index(self):
        test_karttakuva = Karttakuva.objects.create(
            url="fail_this"
        )
        response = self.client.get(reverse("index"))
        self.assertContains(response, "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2295")

    def test_unsuccessful_karttakuva(self):
        test_karttakuva = Karttakuva(
            url="fail_this"
        )
        with self.assertRaises(ValidationError):
            test_karttakuva.full_clean()
        self.assertEqual(Karttakuva.objects.count(), 0)