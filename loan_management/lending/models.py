from django.db import models

# Create your models here.
class Borrower(models.Model):
	SSS = 1
	PAGIBIG = 2
	PHILHEALTH = 3
	HUMID = 4
	PASSPORT = 5
	VOTERS_ID = 6

	valid_id_types = (
		(SSS, "SSS"),
		(PAGIBIG, "PAGIBIG"), 
		(PHILHEALTH, "PHILHEALTH"), 
		(HUMID, "HUMID"), 
		(PASSPORT, "PASSPORT"),
		(VOTERS_ID, "VOTERS_ID"),
	)

	first_name = models.CharField(verbose_name = "First Name", max_length = 200)
	last_name = models.CharField(verbose_name = "Last Name", max_length = 200)
	address = models.CharField(verbose_name = "Address", max_length = 200)
	valid_id = models.IntegerField(verbose_name = "Valid ID", choices = valid_id_types)
	collaterals = models.CharField(verbose_name = "Collaterals", max_length = 200)
	loan_amount = models.FloatField(verbose_name = "Loan Amount")

	def __str__(self):
		return "%s" % self.first_name
		
	def get_first_name(self):
		return	self.first_name

	def get_last_name(self):
		return	self.last_name

	def get_address(self):
		return	self.address

	def get_valid_id(self):
		return	self.valid_id

	def get_collaterals(self):
		return	self.collaterals

	def get_loan_amount(self):
		return	self.loan_amount