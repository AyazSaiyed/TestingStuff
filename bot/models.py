# ------------------------------ Developer - Ayaz Saiyed M.
# ----------------- Final Release July,2020
# ------------- GasLeadGeneration


from django.db import models

# Create your models here.
class UsersDetails(models.Model):
	username = models.TextField(blank=False)
	restaurantSelected = models.TextField()
	city = models.TextField()
	address = models.TextField()
	date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.username


