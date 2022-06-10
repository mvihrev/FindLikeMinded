from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=32, primary_key=True)


class Language(models.Model):
    name = models.CharField(max_length=32, primary_key=True)


class User(models.Model):
    login = models.CharField(max_length=32, primary_key=True)
    password = models.CharField(max_length=32)
    email = models.EmailField(max_length=32, unique=True)
    avatar = models.ImageField(upload_to='images/users', blank=True)
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    birthday = models.DateField()
    country = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    profession = models.CharField(max_length=32)
    description = models.TextField(blank=True)
    signup_date = models.DateField(auto_now_add=True)


class UserEducation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institution = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    degree = models.CharField(max_length=32)


class UserPortfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=32)
    link = models.URLField(max_length=100)


class UserTag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class UserLanguage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)


class Project(models.Model):
    title = models.CharField(max_length=32, unique=True)
    description = models.TextField()
    country = models.CharField(max_length=32, blank=True)
    city = models.CharField(max_length=32, blank=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    creation_date = models.DateField(auto_now_add=True)


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/projects')


class ProjectTag(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class ProjectLanguage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)


class Vacancy(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    position = models.CharField(max_length=32)
    description = models.TextField()
    requirements = models.TextField()
    wage = models.IntegerField(blank=True)


class VacancyReply(models.Model):
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class News(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField()
    posting_date = models.DateField(auto_now_add=True)


class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/news')


class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=False)
    position = models.CharField(max_length=32)

    class Meta:
        unique_together = ('user', 'project')


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Reaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    reaction = models.BooleanField()  # 1 - like, 0 - dislike

    def save(self, *args, **kwargs):
        super(Reaction, self).save(*args, **kwargs)
        if self.reaction:
            self.project.likes += 1
        else:
            self.project.dislikes += 1

        self.project.save()

    class Meta:
        unique_together = ('user', 'project')
