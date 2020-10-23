Live Project

Introduction

The live project was two weeks of working with my cohort as a team developing a MVC Web Application in Django. The was an excellent opportunity to get hands on experience with version control and working on a schedule. In those two weeks to learn how to use version control to prevent merge conflicts and uploading nonfunctional code, how to use Django Template Language, while writing functions in Python for webpage functionality. I was working on web scraping pages for my site when we timed out. I was looking forward to working with API. I was pushing so hard to get to these stories that I did not focus on the front as much as I could have.
Below are descriptions of the stories I worked on along with code snippets. I also have full code files in this repository for further inspection.

Accessing Individual Items in the Database
This page displays the details of the items from the database and gives the user an interface to edit or delete those items.

views:

def details(request, pk):
    clinic = get_object_or_404(Acu, pk=pk)
    context = {'clinic': clinic}
    return render(request, 'Acu_Insurance/Acu_Insurance_details.html', context)

display page:



