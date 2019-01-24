from django.shortcuts import render
from warehouses.models import Warehouse
from django.http import JsonResponse
from django.shortcuts import render, redirect

import csv,os

def upload_warehouses(request):
	"""Uploads necessary warehouses to development enviroment, after db is populated, view redirects to an 404 page"""
	try:
		file = csv.reader(open(os.path.join(os.path.dirname(__file__), '.', 'warehouses.csv'), 'r'), delimiter=',')
		warehouse = Warehouse.objects.all()[0]
		return render(request,'404.html',status=404)	

	except (IndexError) as e:
		#There are no warehouses on database, populate db.
		for line in file:			
			warehouse = Warehouse.objects.create(
					pdv = line[1],
					sub_inventory_id =line[0]
				)
			warehouse.save()

		return JsonResponse({"success":True})	

