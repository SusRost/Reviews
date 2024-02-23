# review_app/views.py

from django.shortcuts import render
from .forms import ReviewForm
from .models import Review
import joblib
from datetime import datetime, timedelta

MODEL_PATH = 'C:/Users/Susanna/review_project/review_app/regression_model.joblib'
# Загрузка модели
regression_model = joblib.load(MODEL_PATH)

def predict_rating(content):
    # Предсказание рейтинга для текста
    rating = regression_model.predict([content])[0]
    return rating

def review_page(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            
            # Предсказание рейтинга с использованием модели
            rating = predict_rating(content)
            sentiment = 'pos' if rating >= 5 else 'neg'
            # Сохранение отзыва в базе данных
            review = Review(content=content, rating=rating, sentiment=sentiment)
            review.save()
    else:
        form = ReviewForm()
    #Review.objects.all().delete()
    reviews = Review.objects.all()
    return render(request, 'review_app/review_page.html', {'form': form, 'reviews': reviews})
