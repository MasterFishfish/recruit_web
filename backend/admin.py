from django.contrib import admin
from .models import Recruit, Proxy, Firm, ShapedData
# import_export 为 django　插件
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class FirmResource(resources.ModelResource):
    class Meta:
        model = Firm


class RecruitResource(resources.ModelResource):
    class Meta:
        model = Recruit
        exclude = ('release',)


@admin.register(Proxy)
class ProxyAdmin(admin.ModelAdmin):
    list_display = ('head', 'addr', 'is_alive', 'is_http_and_https')
    list_editable = ('is_alive',)
    list_per_page = 50

@admin.register(Recruit)
class RecruitAdmin(ImportExportModelAdmin):
    resource_class = RecruitResource
    list_display = ('resource', 'name', 'degree', 'release', 'work_place','salary_from', 'salary_to', 'is_alive')
    list_filter = ('resource', 'created_time')


@admin.register(Firm)
class FirmAdmin(ImportExportModelAdmin):
    resource_class = FirmResource
    list_display = ('firm_name', 'firm_nature', 'firm_industry',
                    'firm_scale_from', 'firm_scale_to', 'is_alive')

@admin.register(ShapedData)
class ShapeAdmin(admin.ModelAdmin):
    # list_display = ('head', 'addr', 'is_alive', 'is_http_and_https')
    # list_editable = ('is_alive',)
    list_per_page = 50
