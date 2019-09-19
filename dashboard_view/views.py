from dashboard_view.models import *
from django.db.models import Count, Q
from django.shortcuts import render, HttpResponse


def home(request):
    return render(request,'home.html')


def dashboard(request):
    iphonex = Iphone_Data.objects.filter(product_name__contains='Apple iPhone X')
    iphone8 = Iphone_Data.objects.filter(product_name__contains='Apple iPhone 8')
    iphone7 = Iphone_Data.objects.filter(product_name__contains='Apple iPhone 7')
    iphone6 = Iphone_Data.objects.filter(product_name__contains='Apple iPhone 6')

    rating_iphonex = [list.ratings for list in iphonex]
    total_ratings_iphonex = sum(rating_iphonex)
    average_ratings_iphonex = []
    avg_ratings_iphonex = total_ratings_iphonex / len(rating_iphonex)
    average_ratings_iphonex.append(avg_ratings_iphonex)

    rating_iphone8 = [list.ratings for list in iphone8]
    total_ratings_iphone8 = sum(rating_iphone8)
    average_ratings_iphone8 = []
    avg_ratings_iphone8 = total_ratings_iphone8 / len(rating_iphone8)
    average_ratings_iphone8.append(avg_ratings_iphone8)

    rating_iphone7 = [list.ratings for list in iphone7]
    total_ratings_iphone7 = sum(rating_iphone7)
    average_ratings_iphone7 = []
    avg_ratings_iphone7 = total_ratings_iphone7 / len(rating_iphone7)
    average_ratings_iphone7.append(avg_ratings_iphone7)

    rating_iphone6 = [list.ratings for list in iphone6]
    total_ratings_iphone6 = sum(rating_iphone6)
    average_ratings_iphone6 = []
    avg_ratings_iphone6 = total_ratings_iphone6 / len(rating_iphone6)
    average_ratings_iphone6.append(avg_ratings_iphone6)

    context = {
        'iphonex_rating': avg_ratings_iphonex, 'iphone8_ratings': avg_ratings_iphone8,
        'iphone7_ratings': avg_ratings_iphone7, 'iphone6_ratings': avg_ratings_iphone6
    }

    return render(request, 'dashboard.html', context)


def dashboard_review(request):
    iphonex = Iphone_Data.objects.filter(product_name__contains='Apple iPhone X')
    iphone8 = Iphone_Data.objects.filter(product_name__contains='Apple iPhone 8')
    iphone7 = Iphone_Data.objects.filter(product_name__contains='Apple iPhone 7')
    iphone6 = Iphone_Data.objects.filter(product_name__contains='Apple iPhone 6')

    review_iphonex = [list.reviews for list in iphonex]
    total_review_iphonex = sum(review_iphonex)
    average_review_iphonex = []
    avg_review_iphonex = total_review_iphonex
    average_review_iphonex.append(avg_review_iphonex)

    review_iphone8 = [list.reviews for list in iphone8]
    total_review_iphone8 = sum(review_iphone8)
    average_review_iphone8 = []
    avg_review_iphone8 = total_review_iphone8
    average_review_iphone8.append(avg_review_iphone8)

    review_iphone7 = [list.reviews for list in iphone7]
    total_review_iphone7 = sum(review_iphone7)
    average_review_iphone7 = []
    avg_review_iphone7 = total_review_iphone7 /2
    average_review_iphone7.append(avg_review_iphone7)

    review_iphone6 = [list.reviews for list in iphone6]
    total_review_iphone6 = sum(review_iphone6)
    average_review_iphone6 = []
    avg_review_iphone6 = total_review_iphone6 / len(review_iphone6)
    average_review_iphone6.append(avg_review_iphone6)

    context = {
        'iphonex_review': avg_review_iphonex, 'iphone8_ratings': avg_review_iphone8,
        'iphone7_ratings': avg_review_iphone7, 'iphone6_ratings': avg_review_iphone6
    }

    return render(request, 'review.html', context)
