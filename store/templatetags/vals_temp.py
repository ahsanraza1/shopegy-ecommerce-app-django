from django import template
register = template.Library()

def show_stars( val = 0):
    stars = ''
    for i in range(val):
        stars += '<i class="fa fa-star"></i>' 
    return stars