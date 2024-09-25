from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from multiselectfield import MultiSelectField


    
class Avaliacao(models.Model):
    RELACAO_CHOICES = [
        ('Membro Comungante', 'Membro Comungante'),
        ('Membro Não Comungante', 'Membro Não Comungante'),
        ('Congregado', 'Congregado'),
        ('Oficial', 'Oficial'),
        
    ]

    SOCIEDADES_CHOICES = [
        
        ('SAF', 'SAF'),
        ('UPH', 'UPH'),
        ('UMP', 'UMP'),
        ('UPA', 'UPA'),
        ('NA', 'Nemhuma'),
        
    ]
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    QUALIDADE_CHOICES = [
        ('Muito Ruim', 'Muito Ruim'),
        ('Ruim', 'Ruim'),
        ('Bom', 'Bom'),
        ('Excelente', 'Excelente'),
    ]
    
    QUALIDADE_PESSOAL_CHOICES = [
        ('Tenho Vergonha', 'Tenho Vergonha'),
        ('Preciso Melhorar Muito', 'Preciso Melhorar Muito'),
        ('Satisfatório', 'Satisfatório'),
        ('Excelente', 'Excelente'),
    ]
    nome = models.CharField(max_length=100, blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    nascimento = models.DateField()
    celular = models.CharField(max_length=255)
    social = models.CharField(max_length=255, blank=True, null=True, default='não tem')
    relacao = models.CharField(max_length=30, choices=RELACAO_CHOICES)
    sociedade = MultiSelectField(choices=SOCIEDADES_CHOICES)
    
    sobre_a_igreja = models.TextField(blank=True, null=True, default='não tem')
    louvor = models.CharField(max_length=30, choices=QUALIDADE_CHOICES)
    visitacao = models.CharField(max_length=30, choices=QUALIDADE_CHOICES)
    recepcao = models.CharField(max_length=30, choices=QUALIDADE_CHOICES)
    evengelizacao = models.CharField(max_length=30, choices=QUALIDADE_CHOICES)
    comunicacao = models.CharField(max_length=30, choices=QUALIDADE_CHOICES)
    escola_dominical = models.CharField(max_length=30, choices=QUALIDADE_CHOICES)
    diaconos = models.CharField(max_length=30, choices=QUALIDADE_CHOICES)
    observacao_diaconos = models.TextField(blank=True, null=True, default='não tem')
    presbiteros = models.CharField(max_length=30, choices=QUALIDADE_CHOICES)
    observacao_presbiteros= models.TextField(blank=True, null=True, default='não tem')
    pastor = models.CharField(max_length=30, choices=QUALIDADE_CHOICES)
    observacao_pastor = models.TextField(blank=True, null=True, default='não tem')
    seu_compromisso = models.CharField(max_length=30, choices=QUALIDADE_PESSOAL_CHOICES)
    leitura = models.CharField(max_length=30, choices=QUALIDADE_PESSOAL_CHOICES)
    area_interesse_comunicacao = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],  blank=True, null=True, default=0,
        help_text="Escolha um número de 1 a 5 para definir a prioridade"
    )
    area_interesse_evangelismo_missoes = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],  blank=True, null=True, default=0,
        help_text="Escolha um número de 1 a 5 para definir a prioridade"
    )
    area_interesse_projeto_viver = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)], blank=True, null=True, default=0,
        help_text="Escolha um número de 1 a 5 para definir a prioridade"
    )
    area_interesse_departamento_infantil = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],  blank=True, null=True, default=0,
        help_text="Escolha um número de 1 a 5 para definir a prioridade"
    )
    area_interesse_acao_social_diaconia = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],  blank=True, null=True, default=0,
        help_text="Escolha um número de 1 a 5 para definir a prioridade"
    )
    area_interesse_visitacao = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],  blank=True, null=True, default=0,
        help_text="Escolha um número de 1 a 5 para definir a prioridade"
    )
    area_interesse_recepcao = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],  blank=True, null=True, default=0,
        help_text="Escolha um número de 1 a 5 para definir a prioridade"
    )
    area_interesse_zeladoria = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],  blank=True, null=True, default=0,
        help_text="Escolha um número de 1 a 5 para definir a prioridade"
    )
    area_interesse_eventos = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],  blank=True, null=True, default=0,
        help_text="Escolha um número de 1 a 5 para definir a prioridade"
    )
    area_interesse_pregacao = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],  blank=True, null=True, default=0,
        help_text="Escolha um número de 1 a 5 para definir a prioridade"
    )
    area_interesse_ensino = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],  blank=True, null=True, default=0,
        help_text="Escolha um número de 1 a 5 para definir a prioridade"
    )
    area_interesse_secretaria = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],  blank=True, null=True, default=0,
        help_text="Escolha um número de 1 a 5 para definir a prioridade"
    )
    area_interesse_louvor = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],  blank=True, null=True, default=0,
        help_text="Escolha um número de 1 a 5 para definir a prioridade"
    )
    dizimo = models.DecimalField(max_digits=10, decimal_places=2,default=0, null=True, blank=True)

    data_avaliacao = models.DateField(auto_now_add=True)

    def __str__(self):

        return f" Avaliação de {self.nome} - data: {self.data_avaliacao}"


class PrevDizimos(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ano = models.IntegerField()  # Campo para armazenar o ano automaticamente
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Dízimo do ano {self.ano}: {self.valor}"
