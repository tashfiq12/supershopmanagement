from django.shortcuts import render, redirect  
from product.forms import  ProductForm  
from product.models import Product  

# Create new product.
def createproduct(request):  
    if request.method == "POST":  
        form = ProductForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = ProductForm()  
    return render(request,'index.html',{'form':form})


#listing products
def showproduct(request):  
    products = Product.objects.all()  
    return render(request,"show.html",{'products':products}) 

#edit page view
def edit(request, id):  
    product = Product.objects.get(id=id)  
    return render(request,'edit.html', {'product':product}) 

#updating products
def update(request, id):  
    product = Product.objects.get(id=id)  
    form = ProductForm(request.POST, instance = product)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'product': product}) 

#deleting products
def destroy(request, id):  
    product = Product.objects.get(id=id)  
    product.delete()  
    return redirect("/show")   
