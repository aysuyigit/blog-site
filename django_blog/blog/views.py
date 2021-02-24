from django.shortcuts import render,HttpResponse,Http404,get_object_or_404,HttpResponseRedirect,reverse
from django.contrib import messages

from .models import Blog
from .forms import IletisimForm,BlogForm


# Create your views here.
mesajlar=[]
def iletisim(request):
    print(request.GET)
    form=IletisimForm(data=request.GET or None)
    if form.is_valid():
        isim=form.cleaned_data.get('isim')
        soyisim=form.cleaned_data.get('soyisim')
        email=form.cleaned_data.get('email')
        icerik=form.cleaned_data.get('icerik')
        data={'isim':isim,'soyisim':soyisim,'email':email,'icerik':icerik}
        mesajlar.append(data)

        return render(request,'iletisim.html',context={'mesajlar':mesajlar,'form':form})

    return render(request,'iletisim.html',context={'form':form})
def post_list(request):


    gelen_deger = request.GET.get('id', None)

    posts = Blog.objects.all()
    if gelen_deger:
        posts = posts.filter(id=gelen_deger)
    context = {'posts': posts}
    return render(request, 'blog/post-list.html', context)
def post_update(request,slug):
    blog = get_object_or_404(Blog, slug=slug)
    form = BlogForm(instance=blog, data=request.POST or None)
    if form.is_valid():
        form.save()
        msg = "Tebrikler <strong> %s </strong> isimli gönderiniz başarıyla güncellendi." % (blog.title)
        messages.success(request, msg, extra_tags='info')
        return HttpResponseRedirect(blog.get_absolute_url())
    context = {'form': form, 'blog': blog}
    return render(request, 'blog/post-update.html', context=context)

def post_delete(request,slug):
    blog = get_object_or_404(Blog, slug=slug)
    blog.delete()
    msg = "<strong> %s </strong> isimli gönderiniz başarıyla silindi." % (blog.title)
    messages.success(request, msg, extra_tags='danger')
    return HttpResponseRedirect(reverse('post-list'))
def post_detail(request,slug):

    blog = get_object_or_404(Blog,slug=slug)
    return render(request, 'blog/post-detail.html', context={'blog': blog})


def post_create(request):
    form = BlogForm()
    if request.method == "POST":
        form = BlogForm(data=request.POST)
        if form.is_valid():
            blog = form.save()
            msg = "Tebrikler <strong> %s </strong> isimli gönderiniz başarıyla oluşturuldu." %(blog.title)
            messages.success(request, msg, extra_tags='success')
            #reverse('post-detail', kwargs={'pk': blog.pk})
            return HttpResponseRedirect(blog.get_absolute_url())
    return render(request,'blog/post-create.html',context={'form': form})
def sanatcilar(request, sayi):
     sanatcilar_sozluk = {
         '1': 'Eminem',
         '2': 'Tupack',
         '3': 'Tarkan',
         '4': 'Aleyna Tilki',
         '5': 'Müslüm Gürses',
         '6': 'Neşat Ertaş',
         '98': 'Teoman',
        '9': 'Demir Demirkan',
         'eminem': "Without me"
     }

     sanatci=sanatcilar_sozluk.get(sayi,"Bu id numarasına ait sanatçı bulunamadı")
     return HttpResponse(sanatci)

