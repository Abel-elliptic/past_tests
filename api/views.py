from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from api.models import University, Univ_detail, Category


# Create your views here.

def Top(request):
	# Topページ
	# return HttpResponse('this page is Top page.')
	universities = University.objects.all().order_by('id')
	subjects = Univ_detail.objects.all()
	print(universities)
	print(subjects)
	return render(request,
				  'api/base.html',  # 使用するテンプレート
				  {'univ_names': universities,'subject_names': subjects}# テンプレートに渡すデータ
				  )

# def Get_belonging(request):
# 	univs = Category.objects.all().order_by('id').filter(parent = "")
# 	departs={}
# 	subjects={}
# 	for univ in univs:
# 		departs[univ] = list(Category.objects.all().order_by('id').filter(parent = univ).values_list('child', flat=True))
# 		for depart in departs[univ]:
# 			subjects[depart] = list(
# 				Category.objects.all().order_by('id').filter(parent=depart).values_list('child', flat=True))
# 	print(subjects)
# 	return render(request,
# 				  'api/base.html',{# 使用するテンプレート
# 					  'univs_name': univs,
# 					  'departs_name' : departs,
# 					  'subjects_name': subjects
# 				  }  # テンプレートに渡すデータ
# 				  )
# def Get_belonging(request):
# 	belonging={}
# 	univs = Category.objects.all().order_by('id').filter(parent = "")
# 	for univ in univs:
# 		belonging[univ] = list(Category.objects.all().order_by('id').filter(parent = univ).values_list('child', flat=True))
# 		for depart in range(len(belonging[univ])):
# 			print(belonging[univ][depart])
# 			print(belonging[univ])
# 			print(list(Category.objects.all().order_by('id').filter(parent = depart).values_list('child', flat=True)))
# 	return render(request,
# 				  'api/base.html',{# 使用するテンプレート
# 					  'belonging': belonging,
# 				  }  # テンプレートに渡すデータ
# 				  )

def Get_belonging(request):
	belonging={}
	univs = Category.objects.all().order_by('id').filter(parent = "")
	for univ in univs:
		belonging[univ] = list(Category.objects.all().order_by('id').filter(parent = univ).values_list('child', flat=True))
		for depart in range(len(belonging[univ])):
			print(belonging[univ][depart])
			print(belonging[univ])
			print(list(Category.objects.all().order_by('id').filter(parent = depart).values_list('child', flat=True)))
	return render(request,
				  'api/base.html',{# 使用するテンプレート
					  'belonging': belonging,
				  }  # テンプレートに渡すデータ
				  )

