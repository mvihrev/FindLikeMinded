from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import TagSerializer, LanguageSerializer, UserSerializer, UserEducationSerializer, \
    UserPortfolioSerializer, UserTagSerializer, UserLanguageSerializer, ProjectSerializer, \
    ProjectImageSerializer, ProjectTagSerializer, ProjectLanguageSerializer, VacancySerializer, \
    VacancyReplySerializer, ParticipantSerializer, NewsSerializer, NewsImageSerializer, SubscriptionSerializer, \
    ReactionSerializer
from ..models import Tag, Language, User, UserEducation, UserPortfolio, UserTag, UserLanguage, \
    Project, ProjectImage, ProjectTag, ProjectLanguage, Vacancy, VacancyReply, Participant, News, NewsImage, \
    Subscription, Reaction


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = TagSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = LanguageSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def education(self, request, pk=None):
        user = self.get_object()
        user_education_by_user = UserEducation.objects.filter(user=user)
        user_education_by_user_json = UserEducationSerializer(user_education_by_user, many=True)

        return Response(user_education_by_user_json.data)

    @action(detail=True, methods=['get'])
    def portfolio(self, request, pk=None):
        user = self.get_object()
        user_portfolio_by_user = UserPortfolio.objects.filter(user=user)
        user_portfolio_by_user_json = UserPortfolioSerializer(user_portfolio_by_user, many=True)

        return Response(user_portfolio_by_user_json.data)

    @action(detail=True, methods=['get'])
    def projects(self, request, pk=None):
        user = self.get_object()
        user_as_participant = Participant.objects.filter(user=user)
        user_projects = Project.objects.filter(id__in=user_as_participant)
        user_projects_json = ProjectSerializer(user_projects, many=True)

        return Response(user_projects_json.data)

    @action(detail=True, methods=['get'])
    def subscriptions(self, request, pk=None):
        user = self.get_object()
        user_subscriptions_by_user = Subscription.objects.filter(user=user)
        user_subscriptions_by_user_json = SubscriptionSerializer(user_subscriptions_by_user, many=True)

        return Response(user_subscriptions_by_user_json.data)

    @action(detail=True, methods=['get'])
    def reactions(self, request, pk=None):
        user = self.get_object()
        user_reactions_by_user = Reaction.objects.filter(user=user)
        user_reactions_by_user_json = SubscriptionSerializer(user_reactions_by_user, many=True)

        return Response(user_reactions_by_user_json.data)

    @action(detail=True, methods=['get'])
    def tags(self, request, pk=None):
        user = self.get_object()
        user_tags_by_user = UserTag.objects.filter(user=user)
        user_tags_by_user_json = UserTagSerializer(user_tags_by_user, many=True)

        return Response(user_tags_by_user_json.data)

    @action(detail=True, methods=['get'])
    def languages(self, request, pk=None):
        user = self.get_object()
        user_languages_by_user = UserLanguage.objects.filter(user=user)
        user_languages_by_user_json = UserLanguageSerializer(user_languages_by_user, many=True)

        return Response(user_languages_by_user_json.data)


class UserEducationViewSet(viewsets.ModelViewSet):
    queryset = UserEducation.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserEducationSerializer


class UserPortfolioViewSet(viewsets.ModelViewSet):
    queryset = UserPortfolio.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserPortfolioSerializer


class UserTagViewSet(viewsets.ModelViewSet):
    queryset = UserTag.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserTagSerializer


class UserLanguageViewSet(viewsets.ModelViewSet):
    queryset = UserLanguage.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserLanguageSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProjectSerializer

    @action(detail=True, methods=['get'])
    def images(self, request, pk=None):
        project = self.get_object()
        project_images_by_project = ProjectImage.objects.filter(project=project)
        project_images_by_project_json = ProjectImageSerializer(project_images_by_project, many=True)

        return Response(project_images_by_project_json.data)

    @action(detail=True, methods=['get'])
    def participants(self, request, pk=None):
        project = self.get_object()
        participants_by_project = Participant.objects.filter(project=project)
        participants_by_project_json = ParticipantSerializer(participants_by_project, many=True)

        return Response(participants_by_project_json.data)

    @action(detail=True, methods=['get'])
    def vacancies(self, request, pk=None):
        project = self.get_object()
        vacancies_by_project = Vacancy.objects.filter(project=project)
        vacancies_by_project_json = VacancySerializer(vacancies_by_project, many=True)

        return Response(vacancies_by_project_json.data)

    @action(detail=True, methods=['get'])
    def vacancies_replies(self, request, pk=None):
        project = self.get_object()
        vacancies_by_project = Vacancy.objects.filter(project=project)
        vacancies_replies_by_vacancies = VacancyReply.objects.filter(vacancy__in=vacancies_by_project)
        vacancies_replies_by_vacancies_json = VacancyReplySerializer(vacancies_replies_by_vacancies, many=True)

        return Response(vacancies_replies_by_vacancies_json .data)

    @action(detail=True, methods=['get'])
    def news(self, request, pk=None):
        project = self.get_object()
        news_by_project = News.objects.filter(project=project)
        news_by_project_json = NewsSerializer(news_by_project, many=True)

        return Response(news_by_project_json.data)

    @action(detail=True, methods=['get'])
    def subscribers(self, request, pk=None):
        project = self.get_object()
        project_subscribers_by_project = Subscription.objects.filter(project=project)
        project_subscribers_by_project_json = SubscriptionSerializer(project_subscribers_by_project, many=True)

        return Response(project_subscribers_by_project_json.data)

    @action(detail=True, methods=['get'])
    def tags(self, request, pk=None):
        project = self.get_object()
        project_tags_by_project = ProjectTag.objects.filter(project=project)
        project_tags_by_project_json = ProjectTagSerializer(project_tags_by_project, many=True)

        return Response(project_tags_by_project_json.data)

    @action(detail=True, methods=['get'])
    def languages(self, request, pk=None):
        project = self.get_object()
        project_languages_by_project = ProjectLanguage.objects.filter(project=project)
        project_languages_by_project_json = ProjectLanguageSerializer(project_languages_by_project, many=True)

        return Response(project_languages_by_project_json.data)


class ProjectImageViewSet(viewsets.ModelViewSet):
    queryset = ProjectImage.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProjectImageSerializer


class ProjectTagViewSet(viewsets.ModelViewSet):
    queryset = ProjectTag.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProjectTagSerializer


class ProjectLanguageViewSet(viewsets.ModelViewSet):
    queryset = ProjectLanguage.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProjectLanguageSerializer


class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = VacancySerializer


class VacancyReplyViewSet(viewsets.ModelViewSet):
    queryset = VacancyReply.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = VacancyReplySerializer


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ParticipantSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = NewsSerializer

    @action(detail=True, methods=['get'])
    def images(self, request, pk=None):
        news = self.get_object()
        news_images_by_news = NewsImage.objects.filter(news=news)
        news_images_by_news_json = NewsImageSerializer(news_images_by_news, many=True)

        return Response(news_images_by_news_json.data)


class NewsImageViewSet(viewsets.ModelViewSet):
    queryset = NewsImage.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = NewsImageSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = SubscriptionSerializer


class ReactionViewSet(viewsets.ModelViewSet):
    queryset = Reaction.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ReactionSerializer
