from django.shortcuts import render, redirect
from .models import Transaction, Customer
from django.http import JsonResponse, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


def home(request):
    return redirect('transaction_add')


def get_print(request, otp_1, otp_2):
    try:
        transaction = Transaction.objects.get(otp_1=otp_1, otp_2=otp_2)
        file_printed = transaction.printed
        python_dict = {'otp_found': True, 'color_model': transaction.color_model, 'amount': transaction.amount,
                       'payment_mode': transaction.payment_mode, 'file_path': transaction.file.url}
        python_dict.update({'file_printed': file_printed})
        return JsonResponse(python_dict, safe=False)
    except ObjectDoesNotExist:
        return JsonResponse({'otp_found': False})


@login_required
def otp_generated(request, otp_1, otp_2):
    try:
        transaction = Transaction.objects.filter(customer=request.user.customer, otp_1=otp_1, otp_2=otp_2)
        context = {'otp_1': otp_1, 'otp_2': otp_2}
        return render(request, 'portal/otp_generated.html', context)
    except ObjectDoesNotExist:
        return HttpResponse("You dont have transaction with otp {0} and {1}".format(otp_1, otp_2))

#
# @login_required
# def transaction_add(request):
#     if request.method == 'POST':
#         try:
#             post_dict = request.POST
#             payment_mode = str(post_dict.get('payment_mode'))
#             amount = float(post_dict.get('raw_amount'))
#             if payment_mode == 'account' and request.user.customer.balance < amount:
#                 return HttpResponse('no sufficient balance')
#             else:
#                 file = request.FILES['file']
#                 color_model = post_dict.get('color_model')
#                 customer = request.user.customer
#                 transaction = Transaction.objects.create(file=file, amount=amount, payment_mode=payment_mode, customer=customer, color_model=color_model)
#                 if payment_mode == 'Account':
#                     customer.Balance -= amount
#                     customer.save()
#                 return redirect('otp_generated', otp_1=transaction.otp_1, otp_2=transaction.otp_2)
#         except Exception as e:
#             error_message = 'Some error occured. Please try again.'
#             context = {'error_message': error_message}
#             return render(request, 'portal/transaction_add.html', context)
#     else:
#         return render(request, 'portal/transaction_add.html')
#

@login_required
def transaction_add(request):
    if request.method == 'POST':
        # try:
            post_dict = request.POST
            payment_mode = str(post_dict.get('payment_mode'))
            amount = 5
            if payment_mode == 'account' and request.user.customer.balance < amount:
                return HttpResponse('no sufficient balance')
            else:
                file = request.FILES['file']
                color_model = post_dict.get('color_model')
                customer = request.user.customer
                print(file, amount, payment_mode, customer, color_model)
                transaction = Transaction.objects.create(file=file, amount=amount, payment_mode=payment_mode, customer=customer, color_model=color_model)
                if payment_mode == 'Account':
                    customer.Balance -= amount
                    customer.save()
                return redirect('otp_generated', otp_1=transaction.otp_1, otp_2=transaction.otp_2)
        # except Exception as e:
        #     error_message = 'Some error occured. Please try again.'
        #     context = {'error_message': error_message}
        #     return render(request, 'portal/transaction_add.html', context)
    else:
        return render(request, 'portal/transaction_add.html')

