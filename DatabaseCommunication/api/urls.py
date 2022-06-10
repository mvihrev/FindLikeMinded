from rest_framework import routers
from .api import TagViewSet, LanguageViewSet, UserViewSet, UserEducationViewSet, UserPortfolioViewSet, \
    UserTagViewSet, UserLanguageViewSet, ProjectViewSet, ProjectImageViewSet, ProjectTagViewSet, \
    ProjectLanguageViewSet, VacancyViewSet, VacancyReplyViewSet, ParticipantViewSet, NewsViewSet, NewsImageViewSet, \
    SubscriptionViewSet,  ReactionViewSet


router = routers.DefaultRouter()
router.register('api/users', UserViewSet, 'users')
router.register('api/users-education', UserEducationViewSet, 'users-education')
router.register('api/users-portfolio', UserPortfolioViewSet, 'users-portfolio')
router.register('api/users-tags', UserTagViewSet, 'users-tags')
router.register('api/users-languages', UserLanguageViewSet, 'users-languages')
router.register('api/projects', ProjectViewSet, 'project')
router.register('api/projects-images', ProjectImageViewSet, 'project-images')
router.register('api/projects-tags', ProjectTagViewSet, 'project-tags')
router.register('api/projects-languages', ProjectLanguageViewSet, 'project-languages')
router.register('api/tags', TagViewSet, 'tags')
router.register('api/languages', LanguageViewSet, 'languages')
router.register('api/vacancies', VacancyViewSet, 'vacancies')
router.register('api/vacancies-replies', VacancyReplyViewSet, 'vacancies-replies')
router.register('api/participants', ParticipantViewSet, 'participants')
router.register('api/news', NewsViewSet, 'news')
router.register('api/news-images', NewsImageViewSet, 'news-images')
router.register('api/subscriptions', SubscriptionViewSet, 'subscriptions')
router.register('api/reactions', ReactionViewSet, 'reactions')

urlpatterns = router.urls
