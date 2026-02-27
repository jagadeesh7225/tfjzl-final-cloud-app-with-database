from django.shortcuts import render, get_object_or_404
from .models import Question, Choice, Submission


def submit(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    if request.method == "POST":
        selected_choice_id = request.POST.get("choice")
        selected_choice = get_object_or_404(Choice, id=selected_choice_id)

        Submission.objects.create(
            question=question,
            selected_choice=selected_choice
        )

        return render(request, "result.html", {
            "question": question,
            "selected_choice": selected_choice
        })

    return render(request, "submit.html", {"question": question})


def show_exam_result(request):
    submissions = Submission.objects.all()
    return render(request, "exam_result.html", {
        "submissions": submissions
    })