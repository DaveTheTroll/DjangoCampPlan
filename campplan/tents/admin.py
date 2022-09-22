from django.contrib import admin
import tents.models as T

admin.site.register(T.Nation)
admin.site.register(T.FieldGroup)
admin.site.register(T.TentType)
admin.site.register(T.Event)
admin.site.register(T.Tent)
admin.site.register(T.TentAtEvent)