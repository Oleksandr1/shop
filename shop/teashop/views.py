from django.shortcuts import render





# Create your views here.
def main(request):
    #добавляем динамику в главный шаблон
    categories = ({"name":"Улун", "description":"По классификации по степени ферментации ферментируется на 50 % (в идеале).",
    	                    "photo":"{% static 'pic/tea.png' %}"},
    	                    {"name":"name_2",
    	                    "description":"Описание товар",
    	                    "photo":"{% static 'pic/tea.png' %}"},
    	                    {"name":"name_3",
    	                    "description":"Описание товар",
    	                    "photo":"{% static 'pic/tea.png' %}"},
    	                    )
    products = ({"name":"тянь-сянь-херянь", "details":"bla bla bla bla bla bla bla bla", "price":233})
    return render(request, 'shop/index.html', {"categories":categories, "products":products})

def category_1(request):
    return render(request, 'shop/category.html', {})

def good_description(request):
    return render(request,'shop/goods/category_1/good_1.html', {})

def shopping_card(request):
    return render(request,'shop/shopping_card.html', {})

def contacts(request):
    return render(request, 'shop/contacts.html',{})