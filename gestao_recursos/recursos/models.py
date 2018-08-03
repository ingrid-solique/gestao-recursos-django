from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pendendias = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.user.first_name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.perfil.save()


class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Recurso(models.Model):
    patrimonio = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=150, unique=True)
    statusRecurso = models.CharField(max_length=45, default='Disponivel')
    observacoes = models.TextField(null=True, blank=True)
    categoriaRecurso = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


class Reserva(models.Model):
    idReserva = models.AutoField(primary_key=True)
    statusReserva = models.CharField(max_length=45, default='Reservado')
    dataReserva = models.DateField()
    horaReserva = models.TimeField()
    observacoes = models.TextField(null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.statusReserva


class ReservaRecurso(models.Model):
    idReservaRecurso = models.AutoField(primary_key=True)
    reserva = models.ForeignKey(Reserva, on_delete=models.PROTECT)
    recurso = models.ForeignKey(Recurso, on_delete=models.PROTECT)
    dataEmprestimo = models.DateField()
    horaEmprestimo = models.TimeField()
    dataDevolucao = models.DateField()
    horaDevolucao = models.TimeField()
    dataDevolucaoEfetiva = models.DateField(null=True, blank=True)
    horaDevolucaoEfetiva = models.TimeField(null=True, blank=True)


class Dano(models.Model):
    idDano = models.AutoField(primary_key=True)
    dataDano = models.DateField()
    descricao = models.TextField()
    observacoes = models.TextField(null=True, blank=True)
    reserva = models.ForeignKey(Reserva, on_delete=models.PROTECT)

    def __str__(self):
        return self.idDano