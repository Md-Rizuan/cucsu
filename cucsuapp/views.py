# elections/views.py
from django.shortcuts import render, get_object_or_404
from .models import Candidate, POSITION_CHOICES
from django.shortcuts import redirect

def home(request):
    # candidates = Candidate.objects.all()
    # return render(request, 'home.html', {'candidates': candidates})

        # Query parameter থেকে position নাও (?position=vp এইভাবে আসবে)
    position = request.GET.get('position', '')

    if position:  # যদি filter select করা থাকে
        candidates = Candidate.objects.filter(position=position)
    else:  # default সব দেখাবে
        candidates = Candidate.objects.all()

    return render(request, 'home.html', {
        'candidates': candidates,
        'positions': POSITION_CHOICES,
        'selected_position': position,
    })
def details(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    return render(request, 'details.html', {'candidate': candidate})
def candidate_form(request):
    if request.method == 'POST':
        # Form থেকে data নাও
        name = request.POST.get('name')
        department = request.POST.get('department')
        session = request.POST.get('session')
        student_id = request.POST.get('student_id')
        position = request.POST.get('position')
        ballot = request.POST.get('ballot')
        panel = request.POST.get('panel')
        manifesto = request.POST.get('manifesto')
        election_type = request.POST.get('election_type')
        image = request.FILES.get('image')
          # ফাইল handle করার জন্য

        # Save to database
        candidate = Candidate(
            name=name,
            department=department,
            session=session,
            student_id=student_id,
            position=position,
            ballot=ballot,
            panel=panel,
            manifesto=manifesto,
            election_type=election_type,
            image=image
        )
        candidate.save()

        # success page এ redirect বা render করতে পারো
        return redirect('home')

    # GET request এ ফর্ম দেখাও
    return render(request, 'candidate_form.html')

