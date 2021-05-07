from django.shortcuts import render
from order.models import Orders
from product.models import Product
from django.conf import settings
from num2words import num2words
import qrcode

# Create your views here.

def index(request):
     products = Product.objects.all()  #getting all the products available and printing them in orders page
     return render(request,'order.html',{'products':products})
 
 
def ViewOrderDetails(request):
     if request.method == 'POST':#checking
         productids=request.POST.getlist('selectedproductlist[]')#get select product list
         quantityamounts=request.POST.getlist('quantitylist[]')# get quantity list
         while ('' in quantityamounts):#removing the empty quantity amounts
              quantityamounts.remove('')
         customername=request.POST.get('customername')#getting customer info
         customeremail=request.POST.get('customeremail')
         customerphone=request.POST.get('customerphone')
         #generating qr code
         qr=qrcode.QRCode(
              version=1,
              error_correction=qrcode.constants.ERROR_CORRECT_M,
              box_size=10,
              border=5
         )
         #adding customer info in qr code
         qr.add_data(customername)
         qr.add_data("\n")
         qr.add_data(customerphone)
         qr.add_data("\n")
         qr.add_data(customeremail)
         qr.add_data("\n")
         qr.make(fit=True)
         img = qr.make_image(fill='black', back_color='white')
         img.save(settings.STATICFILES_DIRS[0]+"/qrcode1.png")#saving image
         orderdict={}#first storing order temporarily in dictionary
         orderlist=[]#finally adding the dictionary in list
         total=0
         flag=1
         #selected product operations
         for i in range(len(productids)):
             v1=int(productids[i])
             prod=Product.objects.get(pk=v1)
             currentprice=int(prod.unitprice)
             currentItemname=str(prod.productname)
             currentstock=prod.currentstock
             q1=int(quantityamounts[i])
             if(q1<=currentstock):# if inputted quantity is less than or equal to stock remaining then this operation will happen
                  orderdict.update({'idx':i+1,'itemname':currentItemname,'itemprice':currentprice,'itemquantity':q1,'currenttotal':currentprice*q1})
                  orderlist.append(orderdict.copy())
                  total+=(currentprice*q1)
             else:#if less than current stock then this is triggered 
                  flag=0
                  if(flag==0):
                       res1="Update quantity amount of "+str(currentItemname)+" properly"
                       return render(request,'orderdetails.html',{'msg':res1})
         #updating the stock values
         for i in range(len(productids)):
              v2=int(productids[i])
              prod1=Product.objects.get(pk=v2)
              q2=int(quantityamounts[i])
              val2=prod1.currentstock-q2
              prod1.currentstock=val2
              prod1.save()
         order1=Orders(customername=customername,customerphone=customerphone,customeremail=customeremail,totalordersum=total)#inserting order as future reference
         order1.save()     
         amountinwords=num2words(total, lang='en_IN')                      
         return render(request,'orderdetails.html',{'data': orderlist,'totalamount':total,'amountinwords':amountinwords})
