from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from api.models import University, Univ_detail, Category


# Create your views here.

# class SampleTemplate(TemplateView):

    # template_name = "api/base.html"
	#
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs) # はじめに継承元のメソッドを呼び出す
    #     context["universities"] = University.objects.all().order_by('id')
    #     context["subjects"] = Univ_detail.objects.all().values()
    #     return context


def Top(request):
	# Topページ
	# return HttpResponse('this page is Top page.')
	universities = University.objects.all().order_by('id')
	subjects = Univ_detail.objects.all()
	print(type(universities))
	print(subjects)
	return render(request,
				  'api/base.html',  # 使用するテンプレート
				  {'univ_names': universities,'subject_names': subjects}# テンプレートに渡すデータ
				  )

def Show_belonging(request):
	parents = []
	parents = Category.objects.all().order_by('id').filter(parent = "")
	print(type(parents))
	child = []
	for p in parents:
		child = Category.objects.all().filter(parent = p).values_list("child",flat=True)
		print(child)
	return render(request,
				  'api/base.html',  # 使用するテンプレート
				  {'univ_names': parents,'dep_name':child}# テンプレートに渡すデータ
				  )