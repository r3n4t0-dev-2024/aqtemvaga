from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from app.forms import VagaForm #IMPORTAÇÃO DE FORMUMLÁRIOS DJANGO/FORMS.
from django.views.generic import DetailView #IMPORTAÇÃO/URL.PPY.
from django.contrib import messages  #MENSAGENS
from django.contrib.auth.models import User,auth #USER/AUTENTICAÇÂO
from django.contrib.auth import authenticate,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .utils import enviar_email_empregador #REQUERIMENTO DE LOGIN.
from .models import* #IMPORTANDO MODELOS DJANGO.
from .forms import CurriculoForm
from .forms import PerfilCandidatoForm
from django.contrib.auth.forms import PasswordChangeForm
from .forms import VisualizacaoForm



#Home Principal do site AQ!temvagas, vagas de todos os "ESTADOS DO BRASIL".
def index(request):
    nome = request.GET.get('nome')
    estado = request.GET.get('estado')
    cidade = request.GET.get('cidade')
    bairro = request.GET.get('bairro')
    
    vagas = vaga_oferecido.objects.all()

    if nome:
        vagas = vagas.filter(Cargo__icontains=nome.lower())

    if estado:
        vagas = vagas.filter(Estado__Estado__icontains=estado)
        cidades = vaga_oferecido.objects.filter(Estado__Estado=estado).values('Cidade').distinct()
        bairros = vaga_oferecido.objects.filter(Estado__Estado=estado).values('Bairro').distinct()
    else:
        cidades = vaga_oferecido.objects.values('Cidade').distinct()
        bairros = vaga_oferecido.objects.values('Bairro').distinct()

    if cidade:
        vagas = vagas.filter(Cidade__icontains=cidade)
        bairros = vagas.filter(Cidade=cidade).values('Bairro').distinct()

    if bairro:
        vagas = vagas.filter(Bairro__icontains=bairro)
        
    
    estados = aqtemvaga_brasil.objects.values('Estado').distinct()
    
    
    context = {
        'vagas': vagas,
        'nome': nome if nome else '',
        'estado': estado,
        'cidade': cidade,
        'bairro': bairro,
        'estados': estados,
        'cidades': cidades,
        'bairros': bairros,
    }
    
    return render(request, 'page/index.html', context)


#Página de contato do site AQ!temvagas.
def contato_aqtemvaga(request):
  return render(request,'page/contato_aqtemvaga.html')


#Blog do site AQ!temvagas.
def blog_aqtemvaga(request):
  posts = BlogPost.objects.all()
  
  context = {
    
    'posts': posts
  }
  return render(request,'page/blog_aqtemvaga.html',context)


#Sobre.
def sobre(request):
  return render(request,'page/sobre.html')


# Somente uma Url de apresentação do Paraná AQ!temvagas.
def parana_aqtemvaga(request):
 
  return render(request,'parana/parana_aqtemvaga.html')


#Página url Curitiba/Região fazendo uma prévia da vaga.
def curitiba_sabermais(request):
    cidades = vaga_oferecido.objects.values('Região', 'Cidade').distinct()
    context = {
        'cidades': cidades,
    }
    return render(request, 'parana/pagina_principal.html', context)


def resultados(request):
    regiao_id = request.GET.get('regiao')
    nome = request.GET.get('nome')
    
    curitiba = vaga_oferecido.objects.all()
    
    if nome:
        curitiba = curitiba.filter(Cargo__icontains=nome)
    
    if regiao_id:
        curitiba = curitiba.filter(Região=regiao_id)
    
    context = {
        'curitiba': curitiba,
    }
    
    return render(request, 'parana/resultados.html', context)


#Página url Maringá/Região fazendo uma prévia da vaga.
def maringa_sabermais(request):
  nome = request.GET.get('nome')
  if nome:
    maringa = maringa_regiao.objects.filter(Cargo__icontains= nome)
    
  else:
   maringa = maringa_regiao.objects.all()
  context = {
    'maringa':maringa,
    'nome': nome,
  }
  
  return render(request, 'parana/maringa_sabermais.html', context)
  

#página url Curitiba/Região, detalhando a vaga.
class curitibavagas(DetailView):
  context_object_name="curitiba_regiao"
  template_name="parana/curitibavagas.html"
  model = curitiba_regiao
  
  
#página url Maringá/Região, detalhando a vaga. 
class maringavagas(DetailView):
    
  context_object_name="maringa_regiao"
  template_name="parana/maringavagas.html"
  model = maringa_regiao
  
  
#página de registro do Empregador/CNPJ.
def register_empregador(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        nome_da_empresa=request.POST['nome_da_empresa']
        cnpj = request.POST['cnpj']
        primeiro_nome=request.POST['primeiro_nome']
        
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Este email já existe!')
                return redirect('register_empregador')
            elif User.objects.filter(username=usuario).exists():
                messages.info(request, 'Este usuário já existe!')
                return redirect('register_empregador')
            else:
                user = User.objects.create_user(username=usuario,password=password, email=email,first_name=primeiro_nome)
                user.save()

                empregador = Empregador.objects.create(
                    user=user,
                    nome_da_empresa=nome_da_empresa,
                    cnpj=cnpj,
                    primeiro_nome=primeiro_nome,
                )
                empregador.save()

                # log user in
                user_login = auth.authenticate(username=usuario, password=password)
                auth.login(request, user_login)
                messages.success(request, 'Cadastro de empregador criado com sucesso!')
                return redirect('/')
        else:
            messages.info(request, 'As senhas não coincidem!')
            return redirect('register_empregador')

    return render(request, 'page/register_empregador.html')
  

#página de registro do usuário Candidato/CPF
def register_view(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        next_url = request.GET.get('next', 'saber_mais_detalhes')
       
        

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Este email já existe!')
                return redirect('register_view')
            elif User.objects.filter(username=usuario).exists():
                messages.info(request, 'Este usuário já existe!')
                return redirect('register_view')
            else:
                user = User.objects.create_user(username=usuario, password=password, email=email)
                user.save()
                
                if user is not None:
                    messages.success(request, 'Cadastro efetuado com sucesso!')
                    messages.success(request, 'Já pode efetuar o seu login.')
                    next_url = request.POST.get('next', next_url)
                    return HttpResponseRedirect(next_url)
                
        else:
            messages.info(request, 'As senhas não coincidem!')
            return redirect('register_view')
    next_url = request.GET.get('next', '/')
    return render(request, 'page/register_view.html',{'next':next_url})


#página de login do usuário.
def login_view(request):
    if request.method == "POST":
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        next_url = request.GET.get('next', 'saber_mais_detalhes')
        user = authenticate(username=usuario, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login efetuado com sucesso!')
            next_url = request.POST.get('next', next_url)
            return HttpResponseRedirect(next_url)
        
        else:
            messages.info(request, 'Usuário ou senha inválidos!')
        return redirect('login_view')
    else:
        next_url = request.GET.get('next', '/')
    return render(request, 'page/login_view.html',{'next':next_url})


#logout usuário.
def logout_web(request):
    auth.logout(request)
    request.session.flush()  # Isso garante que a sessão seja completamente encerrada
    return redirect('/')



#página de registro de vagas feito pelas empresas.
def area_empregador(request):
    if not request.user.is_authenticated:
        return redirect('login_view')
    if request.method == 'POST':
        form = VagaForm(request.POST)
        if form.is_valid():
            vaga = form.save(commit=False)
            vaga.Empregador = request.user.empregador  # Usando o campo Empregador/user
            vaga.save()
            messages.info(request,'Vaga adicionada com sucesso!')
            return redirect('area_empregador')  # Redirecionar para a view de dashboard
    else:
        form = VagaForm()
        
        
    return render(request,'page/area_empregador.html', {'form': form})


#Editar vaga/Empregador
def editar_vaga(request, vaga_id):
    vaga = get_object_or_404(vaga_oferecido, id=vaga_id)
    if request.method == 'POST':
        form = VagaForm(request.POST, instance=vaga)
        if form.is_valid():
            form.save()
            return redirect('dash_empregador')
    else:
        form = VagaForm(instance=vaga)

    context = {
        'form': form,
        'vaga': vaga
    }
    return render(request, 'page/editar_vaga.html', context)


#Deletar vaga/Empregador
def deletar_vaga(request, vaga_id):
    vaga = get_object_or_404(vaga_oferecido, id=vaga_id)
    if request.method == 'POST':
        vaga.delete()
        return redirect('dash_empregador')
    
    context = {
        'vaga':vaga
    }
    return render(request, 'page/area_empregador.html',context)



#Dash-Board/Empregador
def dash_empregador(request):
    if not request.user.is_authenticated:
        return redirect('login_view')
    vagas = vaga_oferecido.objects.filter(Empregador__user=request.user) #Campo do Empregado/User
    context = {
        'vagas': vagas
    }
    return render(request, 'page/dash_empregador.html', context)


#Currículo/Candidato/painel do Candidato
def upload_curriculo(request):
    user = request.user
    curriculo_existente = Curriculo.objects.filter(usuario=user).first()
    
    if curriculo_existente:
        messages.info(request, 'Você já possui um currículo anexado. Substitua-o anexando um novo.')
    
    if request.method == 'POST':
        form = CurriculoForm(request.POST, request.FILES)
        if form.is_valid():
            if curriculo_existente:
                curriculo_existente.arquivo.delete()  # Apaga o arquivo antigo
                curriculo_existente.arquivo = form.cleaned_data['arquivo']
                curriculo_existente.save()
            else:
                curriculo = form.save(commit=False)
                curriculo.usuario = request.user
                curriculo.save()
            messages.success(request, 'Currículo anexado com sucesso!')
            return redirect('perfil_candidato')
    else:
        form = CurriculoForm()
    
    return render(request, 'page/upload_curriculo.html', {'form': form})


#Página Perfil do empregador
@login_required
def perfil_empregador(request):
    user = request.user

    # Recupera os currículos disponíveis
    curriculos = Curriculo.objects.all()

    # Registrar visualização apenas se o visualizador não for o proprietário do currículo
    for curriculo in curriculos:
        
        if user != curriculo.usuario:
            visualizacao, created = VisualizacaoCurriculo.objects.get_or_create(
                curriculo=curriculo,
                visualizador=user
            )
            if not created:
                visualizacao.visualizacoes_count += 1
                visualizacao.save()
            
    # Recupera as visualizações feitas pelo empregador
    visualizacoes = VisualizacaoCurriculo.objects.filter(visualizador=user)
    

    context = {
        'curriculos': curriculos,
        'visualizacoes': visualizacoes,
        'user': user,
    }

    return render(request, 'page/perfil_empregador.html', context)


#página url de todo o Brasil, detalhando a vaga/enviar CV.
def saber_mais_detalhes(request, vaga_id):
    detalhes=vaga_oferecido.objects.filter(id=vaga_id)
    vaga = get_object_or_404(vaga_oferecido, id=vaga_id)
    empregador = vaga.Empregador  # Supondo que vaga_oferecido tem um campo empregador
    if request.method == 'POST':
        # Verifique se o usuário deseja utilizar o currículo existente
        if request.POST.get('utilizar_curriculo_existente') == 'true':
            curriculo_existente = Curriculo.objects.filter(usuario=request.user).first()
            if curriculo_existente:
                curriculo_existente.vaga = vaga
                curriculo_existente.empregador = empregador
                curriculo_existente.save()
                messages.success(request, 'Currículo enviado com sucesso!')
            else:
                messages.error(request, 'Currículo não encontrado no seu perfil. Por favor, anexe um currículo no seu perfil antes de enviar.')
        else:
            form = CurriculoForm(request.POST, request.FILES)
            if form.is_valid():
                curriculo = form.save(commit=False)
                curriculo.usuario = request.user
                curriculo.vaga = vaga
                curriculo.empregador = empregador
                curriculo.save()
                messages.success(request, 'Currículo enviado com sucesso!')
    else:
        form = CurriculoForm()
    return render(request, 'page/saber_mais_detalhes.html', {'form': form, 'vaga': vaga,'detalhes':detalhes})



def curriculo_recebido(request):
    empregador = Empregador.objects.get(user=request.user)
    curriculos = Curriculo.objects.filter(empregador=empregador,deletado_pelo_empregador=False)
    
    context = {
        'empregado':empregador,
        'curriculos':curriculos,
    }
    
    return render(request, 'page/curriculo_recebido.html', context)


# DELETAR_CURRÍCULO/EMPREGADOR
@login_required
def delete_curriculo(request, curriculo_id):
    curriculo = get_object_or_404(Curriculo, id=curriculo_id)
    if request.user == curriculo.empregador.user:
        curriculo.deletado_pelo_empregador=True
        curriculo.save()
    return redirect('curriculo_recebido')


# ATUALIZAR_PERFIL/CANDIDATO.
def atualizar_perfil(request):
    try:
        perfil = PerfilCandidato.objects.get(usuario=request.user)
    except PerfilCandidato.DoesNotExist:
        perfil = PerfilCandidato(usuario=request.user)

    if request.method == 'POST':
        form = PerfilCandidatoForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('perfil_candidato')  # Redireciona para a página do perfil do candidato
    else:
        form = PerfilCandidatoForm(instance=perfil)
    
    return render(request, 'page/atualizar_perfil.html', {'form': form})


# MUDAR_SENHA
def mudar_senha(request):
    
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.info(request,'Senha alterado com Sucesso!')
            return redirect('mudar_senha')              
    else:
        form = PasswordChangeForm(user=request.user, data=request.POST)
    context = {
        
        'form':form
    }
    return render(request,'page/mudar_senha.html',context)


@login_required
def perfil_candidato(request):
    
    
    
    return render(request, 'page/perfil_candidato.html')



@login_required
def curriculo_enviado(request):
    user = request.user

    # Recupera os currículos ativos do usuário, sem exibir visualizações
    curriculos = Curriculo.objects.filter(usuario=user, deletado_pelo_candidato=False)

    context = {
        'curriculos': curriculos,
        'user': user,
    }
    return render(request, 'page/curriculo_enviado.html', context)


# DELETAR_CURRICULO_ENVIADO/CANDIDATO
@login_required
def deletar_curriculo_enviado(request, id):
    curriculo = get_object_or_404(Curriculo, pk=id)
    if request.user == curriculo.usuario:
        curriculo.deletado_pelo_candidato = True
        curriculo.save()
        messages.success(request, 'Currículo  deletado com sucesso!')
    return redirect('curriculo_enviado')


# ESQUECEU SENHA 1/3



