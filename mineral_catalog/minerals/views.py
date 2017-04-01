from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect

from . models import Mineral


def mineral_list(request, pk=None):
    query = request.GET.get('search')
    if query:
        minerals = (Mineral.objects.only('id', 'name')
                    .filter(Q(name__icontains=query) |
                            Q(image_filename__icontains=query) |
                            Q(image_caption__icontains=query) |
                            Q(category__icontains=query) |
                            Q(formula__icontains=query) |
                            Q(strunz_classification__icontains=query) |
                            Q(crystal_system__icontains=query) |
                            Q(unit_cell__icontains=query) |
                            Q(color__icontains=query) |
                            Q(crystal_symmetry__icontains=query) |
                            Q(cleavage__icontains=query) |
                            Q(mohs_scale_hardness__icontains=query) |
                            Q(luster__icontains=query) |
                            Q(streak__icontains=query) |
                            Q(diaphaneity__icontains=query) |
                            Q(optical_properties__icontains=query) |
                            Q(refractive_index__icontains=query) |
                            Q(crystal_habit__icontains=query) |
                            Q(specific_gravity__icontains=query) |
                            Q(group__icontains=query)))
    elif pk is None:
        return redirect('minerals:list', pk='A')
    else:
        if len(pk) == 1:
            minerals = (Mineral.objects.only('id', 'name')
                        .filter(name__istartswith=pk))
        else:
            if 'group/' in pk:
                minerals = (Mineral.objects.only('id', 'name')
                            .filter(group=pk[6:]))
            elif 'category/' in pk:
                minerals = (Mineral.objects.only('id', 'name')
                            .filter(category=pk[9:]))
            else:
                minerals = (Mineral.objects.only('id', 'name')
                            .filter(name__icontains=pk))
    return render(request, 'minerals/mineral_list.html',
                  {'minerals': minerals})


def mineral_detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'minerals/mineral_detail.html',
                  {'mineral': mineral})


def mineral_random(request):
    mineral = Mineral.objects.order_by('?').first()
    return render(request, 'minerals/mineral_detail.html',
                  {'mineral': mineral})
