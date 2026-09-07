from django.contrib import messages
from django.shortcuts import redirect, render

from .models import ContactMessage


def home(request):
    """Serve the single-page portfolio and handle the contact form POST."""
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(
                request,
                "Thanks for your message. I will get back to you soon.",
            )
            return redirect("/#contact")

        messages.error(request, "Please fill in your name, email, and message.")
        return redirect("/#contact")

    return render(request, "index.html")
