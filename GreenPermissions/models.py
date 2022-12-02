from django.db import models

class GreenPermissions(models.Model):
    Permission = models.TextField()

    class Meta:
        permissions = (
            ('GreenSystemAdmin', 'GreenSystemAdmin'),
            ('GreenSystemUser', 'GreenSystemUser'),
            ('GreenSystemGuest', 'GreenSystemGuest'),
            ('GreenAddPermissions', 'GreenAddPermissions'),
            ('GreenWaterSystem', 'GreenWatherSystem'),
            ('GreenWeedSystem', 'GreenWeedSystem'),
            ('GreenSeedSystem', 'GreenSeedSystem'),
            ('GreenCameraOne', 'GreenCameraOne'),
            ('GreenCameraTwo', 'GreenCameraTwo'),
            ('GreenDatabase', 'GreenDatabase'),
        )

    def __str__(self):
        return self.Permission