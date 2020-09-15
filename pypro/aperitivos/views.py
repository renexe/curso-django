from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Vídeo Aperitivo: Motivação', 'vimeo_id': 74410733},
        'instalacao-windows': {'titulo': 'Instalação Windows', 'vimeo_id': 74410744},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
