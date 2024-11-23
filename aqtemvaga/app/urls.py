from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import*
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', index, name='home'),
    path('page/curriculo_enviado/',curriculo_enviado, name='curriculo_enviado'),
    path('page/mudar_senha/', mudar_senha, name='mudar_senha'),
    path('page/atualizar_perfil/', atualizar_perfil, name='atualizar_perfil'),
    path('deletar_curriculo_enviado/<int:id>/',deletar_curriculo_enviado, name='deletar_curriculo_enviado'),
    path('delete_curriculo/<int:curriculo_id>/', delete_curriculo,name='delete_curriculo'),
    path('page/curriculo_recebido.html', curriculo_recebido,name='curriculo_recebido'),
    path('page/saber_mais_detalhes/<int:vaga_id>/', saber_mais_detalhes, name='saber_mais_detalhes'),
    path('page/perfil_empregador.html', perfil_empregador, name='perfil_empregador'),
    path('page/editar_vaga/<int:vaga_id>/', editar_vaga, name='editar_vaga'),
    path('page/deletar_vaga/<int:vaga_id>/', deletar_vaga, name='deletar_vaga'),
    path('page/upload_curriculo/', upload_curriculo, name='upload_curriculo'),
    path('page/perfil_candidato/', perfil_candidato, name='perfil_candidato'),
    path('page/dash_empregador/', dash_empregador, name='dash_empregador'),
    path('page/register_empregador.html/', register_empregador, name='register_empregador'),
    path('page/register_view.html/', register_view, name='register_view'),
    path('page/area_empregador.html/', area_empregador, name='area_empregador'),
    path('page/login_view.html/', login_view, name='login_view'),
    path('page/logout_web/', logout_web, name='logout_web'),
    path('page/contato_aqtemvaga.html/', contato_aqtemvaga, name='contato_aqtemvaga'),
    path('page/blog_aqtemvaga.html/', blog_aqtemvaga, name='blog_aqtemvaga'),
    path('page/sobre.html/', sobre, name='sobre'),
    path('parana/parana_aqtemvaga.html/', parana_aqtemvaga, name='parana_aqtemvaga'),
    path('api/curitiba_sabermais/',curitiba_sabermais, name='curitiba_sabermais'),
    path('parana/maringa_sabermais.html/', maringa_sabermais, name='maringa_sabermais'),
    path('parana/curitibavagas/<int:pk>/', curitibavagas.as_view(), name='curitibavagas'),
    path('parana/maringavagas/<int:pk>/', maringavagas.as_view(), name='maringavagas'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='page/password_reset.html'), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='page/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='page/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='page/password_reset_done.html'), name='password_reset_complete'),


    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
