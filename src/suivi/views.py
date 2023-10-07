from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from typing import Any
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404
from suivi.models import Serie
from suivi.forms import SerieForm
from django.views.decorators.csrf import csrf_exempt, csrf_protect


# Create your views here.
@login_required
def index(request):
    series = list(Serie.objects.all())
    return render(request, "suivi/index.html", context={"series": series})


#@csrf_protect
@csrf_exempt
def update_series(request, serie_id):
    try:
        serie = get_object_or_404(Serie, pk=serie_id)

        if request.method == 'POST':
            seen_seasons = request.POST.get('seen_seasons')
            number_of_seasons = request.POST.get('number_of_seasons')

            # Validate input data
            if seen_seasons is not None and seen_seasons.isdigit():
                serie.seen_seasons = int(seen_seasons)
            if number_of_seasons is not None and number_of_seasons.isdigit():
                serie.number_of_seasons = int(number_of_seasons)
            serie.save()
        return JsonResponse({'success': True})
    except Exception as e:
        return HttpResponseBadRequest(str(e))


