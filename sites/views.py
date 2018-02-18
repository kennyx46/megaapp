from django.shortcuts import render, get_object_or_404
from django.db.models import Avg

from sites.models import Site


def sites_list(request):
    sites = Site.objects.all()
    return render(request, "sites/index.html", { 'sites': sites })

def site(request, site_id):
    site = get_object_or_404(Site.objects.prefetch_related('detail_set'), pk=site_id)
    details = site.detail_set.order_by('created_at').all()
    return render(request, 'sites/site.html', { 'site': site, 'details': details })

def summary(request):
    # python code aggregation
    sites = Site.objects.prefetch_related('detail_set').all()
    for site in sites:
        details = site.detail_set.all()
        a_vals = [detail.a for detail in details]
        b_vals = [detail.b for detail in details]
        setattr(site, 'a_aggr', sum(a_vals))
        setattr(site, 'b_aggr', sum(b_vals))
    return render(request, 'sites/summary.html', { 'sites': sites })

def summary_average(request):
    # database api aggregation
    sites = Site.objects.annotate(a_aggr=Avg('detail__a'), b_aggr=Avg('detail__b')).order_by('id').all()
    return render(request, 'sites/summary.html', { 'sites': sites })