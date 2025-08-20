from django.contrib import admin
from .models import MemberProfile, ReadingClub, Fine


@admin.register(MemberProfile)
class MemberProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'borrower', 'phone_number', 'address')


@admin.register(ReadingClub)
class ReadingClubAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'get_members', 'get_books')

    # Custom method to display members
    def get_members(self, obj):
        return ", ".join([m.name for m in obj.members.all()])
    get_members.short_description = "Members"

    # Custom method to display books
    def get_books(self, obj):
        return ", ".join([b.title for b in obj.books.all()])
    get_books.short_description = "Books"

admin.site.register(Fine)
