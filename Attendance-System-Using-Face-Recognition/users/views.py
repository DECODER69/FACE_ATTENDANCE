from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# from .forms import reg_form


#utility functions
'''
def hours_vs_date_every_employee():
	qs = Attendance.objects.all()
	diff=[]
	
	for obj in qs:
		ti=obj.time_in
		to=obj.time_out
		hours=((to-ti).total_seconds())/3600
		diff.append(hours)
		
	df = read_frame(qs)
	df['hours']=diff
	figure=plt.figure()
	sns.barplot(data=df,x='date',y='')
	html_graph=mpld3.fig_to_html(fig)


'''







# Create your views here.

@login_required
def register(request):
	if request.user.username!='admin':
		return redirect('not-authorised')
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save() ###add user to database
			messages.success(request, f'Employee registered successfully!')
			return redirect('dashboard')
		


	else:
		form=UserCreationForm()
	return render(request,'users/register.html', {'form' : form})






# def reg(request):
# 	if request.user.username!='admin':
# 		return redirect('not-authorised')
# 	if request.method=='POST':
# 		form=reg_form(request.POST)
# 		data = request.POST.copy()
# 		username=data.get('username')
# 		if username_present(username):
# 			create_dataset(username)
# 			messages.success(request, f'Dataset Created')
# 			return redirect('add-photos')
# 		else:
# 			messages.warning(request, f'No such username found. Please register employee first.')
# 			return redirect('dashboard')


# 	else:
		

# 			form=reg_form()
# 			return render(request,'recognition/add_photos.html', {'form' : form})

