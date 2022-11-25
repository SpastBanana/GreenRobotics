from django.db import models

class GreenPermissions(models.Model):
    Permission = models.TextField()

    class Meta:
        permissions = (
            ('GreenSystemAdmin', 'GreenSystemAdmin'),
            ('GreenPermissions', 'GreenPermissions'),
            ('GreenWaterSystem', 'GreenWatherSystem'),
            ('GreenWeedSystem', 'GreenWeedSystem'),
            ('GreenSeedSystem', 'GreenSeedSystem'),
            ('GreenCameraOne', 'GreenCameraOne'),
            ('GreenCameraTwo', 'GreenCameraTwo'),
        )

    def __str__(self):
        return self.Permission