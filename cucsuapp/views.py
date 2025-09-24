# elections/views.py
from django.shortcuts import render, get_object_or_404
from .models import Candidate, POSITION_CHOICES
from django.shortcuts import redirect
from django.contrib import messages

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
def central(request):
    position = request.GET.get('position', '')

    if position: 
        candidates = Candidate.objects.filter(position=position)
    else:  # default সব দেখাবে
        candidates = Candidate.objects.filter(election_type='CUCSU')
    return render(request, 'central.html', {
        'candidates': candidates,
        'positions': POSITION_CHOICES,
        'selected_position': position,
        })


def hall(request):
    position = request.GET.get('position', '')
    if position: 
        candidates = Candidate.objects.filter(position=position)
    else:  # default সব দেখাবে
        candidates = Candidate.objects.filter(election_type='HALL')
    return render(request, 'central.html', {
        'candidates': candidates,
        'positions': POSITION_CHOICES,
        'selected_position': position,
        })
def details(request, pk):
    candidate = get_object_or_404(Candidate, pk=pk)
    return render(request, 'details.html', {'candidate': candidate})
def candidate_form(request):
    if request.method == 'POST':
        
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
        banner_image = request.FILES.get('banner_image')
        youtube_link = request.POST.get('youtube_link')
        experience = request.POST.get('experience')

        if Candidate.objects.filter(student_id=student_id).exists():
                messages.error(request, "এই Student ID দিয়ে ইতিমধ্যেই একজন প্রার্থী আছে।")
                return redirect('candidate_form') 
        if image and image.size > 3 * 1024 * 1024:
                messages.error(request, "ছবির আকার 3MB এর বেশি হতে পারবে না।")
                return redirect('candidate_form')
          

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
            experience=experience,
            banner_image=banner_image,
            election_type=election_type,
            image=image,
            youtube_link=youtube_link,

            
        )
        candidate.save()

        # success page এ redirect বা render করতে পারো
        return redirect('home')

    # GET request এ ফর্ম দেখাও
    return render(request, 'candidate_form.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')

