from django.http import JsonResponse
from django.shortcuts import get_object_or_404,render

from store.models import *
from .basket import Basket

def basket_summary(request):
    basket = Basket(request)
    context = {'basket': basket}
    return render(request, 'store/basket/summary.html', context)


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)

        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        
        return response
    

def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=str(product_id))
        response = JsonResponse({'Success': True})
        return response
    

def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty_str = request.POST.get('productqty')
        try:
            product_qty = int(product_qty_str)
        except ValueError:
            # handle the case where productqty cannot be converted to an int
            response = JsonResponse({'success': False, 'error': 'Invalid quantity'})
            response.status_code = 400 # Bad Request
            return response
        else:
            basket.update(product=product_id, qty=product_qty)
            response = JsonResponse({'success': True})
            return response
    else:
        # handle the case where the request method is not POST or action is not 'post'
        response = JsonResponse({'success': False, 'error': 'Invalid request'})
        response.status_code = 400 # Bad Request
        return response