from django.db import models



class color(models.Model):
    color_name=models.CharField(max_length=200)
    def __str__(self):
        return self.color_name


class roles(models.Model):
    role_title=models.CharField(max_length=200,null=True)
    color=models.ForeignKey(color,on_delete=models.SET_NULL, null=True)
    class Meta:
        permissions = (
            ("can_add_cost_price", "Can add cost price"),
        )
    def __str__(self):
        return self.role_title
