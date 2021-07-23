from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Block


class BlockListView(View):
    def get(self, request):
        block_list = Block.objects.all().order_by('id')
        paginator = Paginator(block_list, 50)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'block/index.html', {'page_obj': page_obj})


class BlockView(View):
    def get(self, request, height):
        block = get_object_or_404(Block, height=height)
        return render(request, 'block/detail.html', {'block': block})
