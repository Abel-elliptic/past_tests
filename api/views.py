from django.shortcuts import render
from api.models import Category

def Get_belonging(request):
	belonging_ps={}
	belonging_up={}
	univs = Category.objects.all().order_by('id').filter(parent = "")
	for univ in univs:
		departs = list(Category.objects.all().order_by('id').filter(parent = univ).values_list('child', flat=True))
		for depart in departs:
			belonging_ps[depart] = list(Category.objects.all().order_by('id').filter(parent = depart).values_list('child', flat=True)).copy()
			belonging_up[univ]=belonging_ps.copy()
		belonging_ps={}
	return render(request,
				  'api/base.html',{# 使用するテンプレート
					  'belonging': belonging_up,
				  }  # テンプレートに渡すデータ
				  )

