from django.test import TestCase
from . import models
from datetime import datetime

class FlightTestCase(TestCase):
    def setUp(self):
        models.Flight.objects.create(from_location="testFromLocation", to_location="testToLocation", takeoff_time=datetime.strptime('01/01/01 12:00:00', '%m/%d/%y %H:%M:%S'), landing_time=datetime.strptime('01/01/01 12:00:00', '%m/%d/%y %H:%M:%S'), plane_type="testPlaneType", plane_id="testPlaneId", pilot_name="testPilotName", normal_ticket_count=10, business_ticket_count=20,normal_ticket_price=10, business_ticket_price=20)

    def test_Create(self):
        obj = models.Flight.objects.get(from_location="testFromLocation")
        self.assertIsNotNone(obj)

    def test_Read(self):
        obj = models.Flight.objects.get(from_location="testFromLocation")
        self.assertIsNotNone(obj)
    
    def test_Update(self):
        obj = models.Flight.objects.get(from_location="testFromLocation")
        obj.pilot_name = "testPilotName2"

        self.assertEqual(obj.pilot_name, "testPilotName2")

    def test_Delete(self):
        models.Flight.objects.get(from_location="testFromLocation").delete()
        obj = None
        try:
            obj = models.Flight.objects.get(from_location="testFromLocation")
        except:
            pass
        self.assertIsNone(obj)

    def tearDown(self) -> None:
        try:
            models.Flight.objects.delete(from_location="testFromLocation")
        except:
            pass

        return super().tearDown()


