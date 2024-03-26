from django.conf.urls import url

from . import views

app_name = "online_cms"

urlpatterns = [
    url(r"^$", views.viewcourses, name="viewcourses"),
    url(r"^(?P<course_code>[A-z]+[0-9]+[A-z]?)/$", views.course, name="course"),
    # url(r'^(?P<course_code>[A-z]+[0-9]+[A-z]?)/edit_marks$', views.edit_marks, name='edit_marks'),
    url(
        r"^(?P<course_code>[A-z]+[0-9]+[A-z]?)/get_exam_data$",
        views.get_exam_data,
        name="get_exam_data",
    ),
    url(r"^(?P<course_code>[A-z]+[0-9]+[A-z]?)/forum$", views.forum, name="forum"),
    url(
        r"^(?P<course_code>[A-z]+[0-9]+[A-z]?)/ajax_reply$",
        views.ajax_reply,
        name="ajax_reply",
    ),
    url(
        r"^(?P<course_code>[A-z]+[0-9]+[A-z]?)/ajax_new$",
        views.ajax_new,
        name="ajax_new",
    ),
    url(
        r"^(?P<course_code>[A-z]+[0-9]+[A-z]?)/ajax_remove$",
        views.ajax_remove,
        name="ajax_remove",
    ),
    url(
        r"^(?P<course_code>[A-z]+[0-9]+[A-z]?)/upload_assignment$",
        views.upload_assignment,
        name="upload_assignment",
    ),
    url(
        r"^(?P<course_code>[A-z]+[0-9]+[A-z]?)/add_documents$",
        views.add_document,
        name="add_document",
    ),
    url(
        r"^(?P<course_code>[A-z]+[0-9]+[A-z]?)/add_assignment$",
        views.add_assignment,
        name="add_assignment",
    ),
    # url(r'^(?P<course_code>[A-z]+[0-9]+[A-z]?)/add_video$', views.add_videos,
    #     name='add_videos'),
    url(r"^(?P<course_code>[A-z]+[0-9]+[A-z]?)/delete/$", views.delete, name="delete"),
    url(
        r"^(?P<course_code>[A-z]+[0-9]+[A-z]?)/ajax_assess$",
        views.ajax_assess,
        name="ajax_assess",
    ),
    url(
        r"^(?P<course_code>[A-z]+[0-9]+[A-z]?)/ajax_feedback$",
        views.ajax_feedback,
        name="ajax_feedback",
    ),
    url(r"^quiz/(?P<quiz_id>[0-9]+)/$", views.quiz, name="quiz"),
    url(
        r"^(?P<course_code>[A-z]+[0-9]+[A-z]?)/create_quiz/$",
        views.create_quiz,
        name="create_quiz",
    ),
    url(
        r"^(?P<course_code>[A-z]+[0-9]+[A-z]?)/edit_quiz/(?P<quiz_code>[0-9]+)/$",
        views.edit_quiz,
        name="edit_quiz",
    ),
    url(
        r"^(?P<course_code>[A-z]+[0-9]+[A-z]?)/edit_quiz/(?P<quiz_code>[0-9]+)/(?P<topic_id>[0-9]+)$",
        views.edit_quiz_topic,
        name="edit_quiz_topic",
    ),
    url(
        r"^(?P<course_code>[A-z]+[0-9]+[A-z]?)/(?P<quiz_id>[0-9]+)/add_question_topic$",
        views.add_question_topicwise,
        name="add_question_topicwise",
    ),
    url(
        r"^(?P<course_id>[0-9]+?)/(?P<quiz_id>[0-9]+)/add_questions_to_quiz$",
        views.add_questions_to_quiz,
        name="add_questions_to_quiz",
    ),
    url(
        r"^(?P<course_code>[A-z]+[0-9]+[A-z]?)/(?P<quiz_code>[0-9]+)/(?P<topic_id>[0-9]+)/remove_quiz_question$",
        views.remove_quiz_question,
        name="remove_quiz_question",
    ),
    url(
        r"^(?P<course_code>[A-z]+[0-9]+[A-z]?)/preview_quiz/(?P<quiz_code>[0-9]+)/$",
        views.preview_quiz,
        name="preview_quiz",
    ),
    url(
        r"^(?P<course_code>[A-z]+[0-9]+[A-z]?)/edit_quiz_details/(?P<quiz_code>[0-9]+)/$",
        views.edit_quiz_details,
        name="edit_quiz_details",
    ),
    url(r"^(?P<quiz_code>[0-9]+)/ajax$", views.ajax_q, name="ajax_q"),
    url(r"^(?P<quiz_code>[0-9]+)/submit$", views.submit, name="submit"),
    url(
        r"^(?P<course_code>[A-z]+[0-9]+[A-z]?)/remove_quiz$",
        views.remove_quiz,
        name="remove_quiz",
    ),
    url(
        r"^(?P<course_code>[A-z]+[0-9]+[A-z]?)/remove_bank$",
        views.remove_bank,
        name="remove_bank",
    ),
    url(
        r"^(?P<course_code>[A-z]+[0-9]+[A-z]?)/remove_topic$",
        views.remove_topic,
        name="remove_topic",
    ),
    url(
        r"^(?P<course_code>[A-z]+[0-9]+[A-z]?)/create_bank$",
        views.create_bank,
        name="create_bank",
    ),
    url(
        r"^(?P<course_code>[A-z]+[0-9]+[A-z]?)/create_topic$",
        views.create_topic,
        name="create_topic",
    ),
    url(
        r"^(?P<course_code>[A-z]+[0-9]+[A-z]?)/(?P<qb_code>[0-9]+)/(?P<topic_id>[0-9]+)$",
        views.edit_qb_topics,
        name="edit_qb_topics",
    ),
    url(
        r"^(?P<course_id>[0-9]+?)/(?P<qb_code>[0-9]+)/(?P<topic_id>[0-9]+)/add_question$",
        views.add_question,
        name="add_question",
    ),
    url(
        r"^(?P<course_code>[A-z]+[0-9]+[A-z]?)/(?P<qb_code>[0-9]+)/(?P<topic_id>[0-9]+)/remove_question$",
        views.remove_question,
        name="remove_question",
    ),
    url(
        r"^(?P<course_code>[A-z]+[0-9]+[A-z]?)/edit_bank/(?P<qb_code>[0-9]+)$",
        views.edit_bank,
        name="edit_bank",
    ),
    url(
        r"^(?P<course_code>[A-z]+[0-9]+[A-z]?)/attendance$",
        views.submit_attendance,
        name="submit_attendance",
    ),
]
