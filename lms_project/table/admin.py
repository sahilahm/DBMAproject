from django.contrib import admin


from table.models import (users_table, login_time, num_of_leaves, cur_running,
                          app_status, cse_dept, ee_dept, mec_dept, hoddean,
                          cse_hod, mec_hod, ee_hod, hod_dean, director, dean, hodapp, deanapp, dirapp)

admin.site.register(users_table)
admin.site.register(login_time)
admin.site.register(num_of_leaves)
admin.site.register(cur_running)
admin.site.register(app_status)
admin.site.register(cse_dept)
admin.site.register(ee_dept)
admin.site.register(mec_dept)
admin.site.register(hoddean)
admin.site.register(cse_hod)
admin.site.register(mec_hod)
admin.site.register(ee_hod)
admin.site.register(hod_dean)
admin.site.register(director)
admin.site.register(dean)
admin.site.register(hodapp)
admin.site.register(deanapp)
admin.site.register(dirapp)

