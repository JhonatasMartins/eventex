# coding: utf-8
from django.test import TestCase
from django.db   import IntegrityError
from datetime    import datetime
from eventex.subscriptions.models import Subscription

class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
        	name='Jhonatas Santos',
        	cpf='98712354398',
        	email='jhonatas1992@gmail.com',
        	phone='61-98674378')

    def test_create(self):
        """
        Subscription must have name, cpf, email, phone
        """
        self.obj.save()
        self.assertEqual(1, self.obj.pk)

    def test_has_created_at(self):
    	"""
    	Subscription must have automatic created_at 
    	"""
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        self.assertEqual(u'Jhonatas Santos', unicode(self.obj))

class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        #Create a first entry to force collision
        Subscription.objects.create(name='Jhonatas Santos', cpf='98712354398',
        	                        email='teste@email.com', phone='61-98674378')

    def test_cpf_unique(self):
        """ CPF must be unique """
        s = Subscription(name='Jhonatas Santos', cpf='98712354398',
        	             email='outro@email.com', phone='61-98674378')
        self.assertRaises(IntegrityError, s.save)

    def test_email_unique(self):
        """ Email must be unique """
        s = Subscription(name='Jhonatas Santos', cpf='00112354398',
         	             email='teste@email.com', phone='61-98674378')
        self.assertRaises(IntegrityError, s.save)
        