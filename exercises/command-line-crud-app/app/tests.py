from django.test import TestCase
from app import models
# Create your tests here.
class TestCommand(TestCase):
    def test_can_create_info(self):
        command = models.create_info(
            "Markel",
            "None",
            "18",
            False,
        )

        self.assertEqual(command.id, 1)
        self.assertEqual(command.name, "Markel")
        self.assertEqual(command.job, "None")
        self.assertEqual(command.age, "18")
        self.assertEqual(command.employed, False)

    def test_view_all_info(self):
        infos_data = [
            {
                "name": "Chris",
                "job": "None",
                "age": "18",
                "employed": False,
            },
            {
                "name": "Arthur",
                "job": "caterer",
                "age": "19",
                "employed": True,
            },
            {
                "name": "Tanner",
                "job": "None",
                "age": "18",
                "employed": False,
            },
        ]

        for info in infos_data:
            models.create_info(
                info["name"],
                info["job"],
                info["age"],
                info["employed"],
            )
        command = models.view_all_info()

        self.assertEqual(len(command), len(infos_data))
         
        infos_data = sorted(infos_data, key=lambda c: c["name"])
        command = sorted(command, key=lambda c: c.name)

        for data, command in zip(infos_data, command):
            self.assertEqual(data["name"], command.name)
            self.assertEqual(data["job"], command.job)
            self.assertEqual(data["age"], command.age)
            self.assertEqual(data["employed"], command.employed)

    def test_search(self):
        infos_data = [
            {
                "name": "Chris",
                "job": "None",
                "age": "18",
                "employed": False,
            },
            {
                "name": "Arthur",
                "job": "caterer",
                "age": "19",
                "employed": True,
            },
            {
                "name": "Tanner",
                "job": "None",
                "age": "18",
                "employed": False,
            },

        ]

        for info in infos_data:
            models.create_info(
                info["name"],
                info["job"],
                info["age"],
                info["employed"],
            )

        self.assertIsNone(models.view_cert_info("jacob"))

        command = models.view_cert_info("Arthur")

        self.assertIsNotNone(command)
        self.assertEqual(command.job,"caterer")
    def test_employed(self):
        infos_data = [
            {
                "name": "Chris",
                "job": "None",
                "age": "18",
                "employed": False,
            },
            {
                "name": "Arthur",
                "job": "caterer",
                "age": "19",
                "employed": True,
            },
            {
                "name": "Tanner",
                "job": "None",
                "age": "18",
                "employed": False,
            },
        ]

        for info in infos_data:
            models.create_info(
                info["name"],
                info["job"],
                info["age"],
                info["employed"],
            )
        self.assertEqual(len(models.employed_command()),1)

    def test_update(self):
        test = models.create_info("tanner","none","18",False)
        self.assertEqual(models.command.objects.first().name,"tanner")
        models.update_info("tanner","number1capper",True)
        self.assertEqual(models.command.objects.first().name,"tanner")

    def test_delete_info(self):
        infos_data = [
            {
                "name": "Chris",
                "job": "None",
                "age": "18",
                "employed": False,
            },
            {
                "name": "Arthur",
                "job": "caterer",
                "age": "19",
                "employed": True,
            },
            {
                "name": "Tanner",
                "job": "None",
                "age": "18",
                "employed": False,
            },
        ]

        for info in infos_data:
            models.create_info(
                info["name"],
                info["job"],
                info["age"],
                info["employed"],
            )

        models.delete_info("Chris")

        self.assertEqual(len(models.view_all_info()),2)
