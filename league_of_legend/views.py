from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def senna(request):
    context_2 = {
        'name':'Senna',
        'img_src': 'https://ww.namu.la/s/bc9ef94249160e1616a761172c0ba100bcd5e98b7c357dfb27173239ad85ed6e69e80963ec3d725432e26eff4c3418e573cf362e43dee3ae701dc9375b350ff2a6ce79e17be18783f9b0e7c16b62e1146f37b61fda7f2cc480e6d75011830e6b95147b20891290f6761b8eea070787eb',
    }
    return render(request, 'league_of_legend/member.html', context=context_2)


def yone(request):
    context = {
        'name':'Yone',
        'img_src':'https://w.namu.la/s/f44a4e6af794fe134a4a1514298eba2dbcc0b51a68b9091f8933c614e075930107b916819699e55b122af887876c87ab7f88b51a9f1503ae08b5972d8dd310452d27c941e817c6bfec7a333700ae08da9bff1674b06e2599bf63fe18ea06679df46298dd38cd5aeca45656e7866baf54',
    }
    return  render(request,'league_of_legend/member.html',context = context)