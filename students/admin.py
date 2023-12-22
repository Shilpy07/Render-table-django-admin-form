from django.contrib import admin
from .models import StudentDetails, Subject

class StudentAdmin(admin.ModelAdmin):
    # change_form_template = 'admin/change_form.html'
    change_form_template = 'admin/students/studentdetails/change_form.html'
    list_display = ["name", "address"]

    def changeform_view(self, request, object_id, form_url, extra_context=None):
        extra_context = extra_context or {}

        # Fetch records from Model
        records = list(StudentDetails.objects.all().values())

        if records:
            headers = list(records[0].keys())

            # Pass the records to the template
            extra_context.update({'records': records, 'headers': headers})

        return super(StudentAdmin, self).changeform_view(request, object_id, form_url, extra_context=extra_context)

class SubjectAdmin(admin.ModelAdmin):
    # change_form_template = 'students/studentdetails/change_form1.html'
    list_display = ["name"]

    def changeform_view(self, request, object_id, form_url, extra_context=None):
        extra_context = extra_context or {}

        # Fetch records from Model
        records = list(Subject.objects.all().values())

        if records:
            headers = list(records[0].keys())

            # Pass the records to the template
            extra_context.update({'records': records, 'headers': headers})

        return super(SubjectAdmin, self).changeform_view(request, object_id, form_url, extra_context=extra_context)

admin.site.register(StudentDetails, StudentAdmin)
admin.site.register(Subject, SubjectAdmin)
