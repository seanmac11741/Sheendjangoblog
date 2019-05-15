from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # one to one relationship with the Users model
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):  #this is a "Dunder method" Double underscore, it lets other things know what to do when calling this
                        #object, like what string to print out when calling the Profile
        return f'{self.user.username} Profile'

#   override of the save method that is run when you use this model
    # def save(self, *args, **kwargs):
    #     super(Profile, self).save(*args, **kwargs)
    #
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
#commented out for the AWS bucket stuff. Pillow doesn't work like this anymore
