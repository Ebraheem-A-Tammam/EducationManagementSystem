from django.urls import path

from .views import (
    category_list_view, 
    categorized_quiz_list_view,
    quiz_detail_view,
    quiz_result_view,
    search_view,
    admin_create_quiz,
    admin_update_quiz,
    admin_quiz_detail_view,
    admin_questions_list_view,
    admin_create_questions,
    admin_َquestion_detail_view,
)

app_name = 'quizzes'

urlpatterns = [
    path('', category_list_view, name='quiz_list'),
    path('questions',admin_questions_list_view,name='admin-questions-list'),
    path('add-question',admin_create_questions,name='admin-question-create'),
    path('question-detail/<int:question_id>',admin_َquestion_detail_view,name='admin-question-detail'),
    path('add-quiz',admin_create_quiz,name='admin-quiz-create'),
    path('edit-quiz/<int:quiz_id>/',admin_update_quiz,name='admin-quiz-update'),
    path('quiz-detail/<int:quiz_id>',admin_quiz_detail_view,name='admin-quiz-detail'),
    path('categories/<slug:category_id>/', categorized_quiz_list_view, name='categorized_quiz_list'),
    path('categories/<slug:category_id>/<int:quiz_id>/', quiz_detail_view, name='quiz_detail'),
    path('categories/<slug:category_id>/<int:quiz_id>/result/<slug:submission_id>/', quiz_result_view, name='quiz_result'),
    path('search/', search_view, name='search'),
]