# from django.test import TestCase
def sending_template_data_by_mail(request):#in this multiple receiver and single sender whose send same msg(only one) for all receiver
    if request.method == "POST":
        to = request.POST.get('toemail')
        otp = random.randint(111111,999999)

        html_content = render_to_string('index.html',{'otp':otp})
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            'testing',
            text_content,
            EMAIL_HOST_USER,
            [to] 
        )
        email.attach_alternative(html_content,"text/html")
        email.send()
        return render(
            request,
            'index.html',
            {"otp":otp})

