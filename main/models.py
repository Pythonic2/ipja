from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from multiselectfield import MultiSelectField

# Create your models here.

class Avaliacao(models.Model):
    RELACAO_CHOICES = [
        ('MC', 'Membro Comungante'),
        ('MNC', 'Membro Não Comungante'),
        ('CON', 'Congregado'),
        ('OFC', 'Oficial'),
        
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
        ('MR', 'Muito Ruim'),
        ('R', 'Ruim'),
        ('B', 'Bom'),
        ('E', 'Excelente'),
    ]
    
    QUALIDADE_PESSOAL_CHOICES = [
        ('TV', 'Tenho Vergonha'),
        ('PM', 'Preciso Melhorar Muito'),
        ('S', 'Satisfatório'),
        ('E', 'Excelente'),
    ]
    nome = models.CharField(max_length=100, blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    nascimento = models.DateField()
    celular = models.CharField(max_length=11)
    social = models.CharField(max_length=255)
    relacao = models.CharField(max_length=3, choices=RELACAO_CHOICES)
    sociedade = MultiSelectField(choices=SOCIEDADES_CHOICES)
    
    sobre_a_igreja = models.TextField()
    louvor = models.CharField(max_length=2, choices=QUALIDADE_CHOICES)
    visitacao = models.CharField(max_length=2, choices=QUALIDADE_CHOICES)
    recepcao = models.CharField(max_length=2, choices=QUALIDADE_CHOICES)
    evengelizacao = models.CharField(max_length=2, choices=QUALIDADE_CHOICES)
    comunicacao = models.CharField(max_length=2, choices=QUALIDADE_CHOICES)
    escola_dominical = models.CharField(max_length=2, choices=QUALIDADE_CHOICES)
    diaconos = models.CharField(max_length=2, choices=QUALIDADE_CHOICES)
    observacao_diaconos = models.TextField()
    presbiteros = models.CharField(max_length=2, choices=QUALIDADE_CHOICES)
    observacao_presbiteros= models.TextField()
    pastor = models.CharField(max_length=2, choices=QUALIDADE_CHOICES)
    observacao_pastor = models.TextField()
    seu_compromisso = models.CharField(max_length=2, choices=QUALIDADE_PESSOAL_CHOICES)
    leitura = models.CharField(max_length=2, choices=QUALIDADE_PESSOAL_CHOICES)
    area_interesse_comunicacao = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],  # Restringe o valor a 1 dígito, de 1 a 5
        help_text="Escolha um número de 1 a 5 para definir a prioridade"
    )
    area_interesse_evangelismo_missoes = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],  # Restringe o valor a 1 dígito, de 1 a 5
        help_text="Escolha um número de 1 a 5 para definir a prioridade"
    )
    area_interesse_projeto_viver = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],  # Restringe o valor a 1 dígito, de 1 a 5
        help_text="Escolha um número de 1 a 5 para definir a prioridade"
    )
    area_interesse_departamento_infantil = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],  # Restringe o valor a 1 dígito, de 1 a 5
        help_text="Escolha um número de 1 a 5 para definir a prioridade"
    )
    area_interesse_acao_social_diaconia = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],  # Restringe o valor a 1 dígito, de 1 a 5
        help_text="Escolha um número de 1 a 5 para definir a prioridade"
    )
    area_interesse_visitacao = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],  # Restringe o valor a 1 dígito, de 1 a 5
        help_text="Escolha um número de 1 a 5 para definir a prioridade"
    )
    area_interesse_recepcao = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],  # Restringe o valor a 1 dígito, de 1 a 5
        help_text="Escolha um número de 1 a 5 para definir a prioridade"
    )
    area_interesse_zeladoria = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],  # Restringe o valor a 1 dígito, de 1 a 5
        help_text="Escolha um número de 1 a 5 para definir a prioridade"
    )
    area_interesse_eventos = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],  # Restringe o valor a 1 dígito, de 1 a 5
        help_text="Escolha um número de 1 a 5 para definir a prioridade"
    )
    area_interesse_pregacao = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],  # Restringe o valor a 1 dígito, de 1 a 5
        help_text="Escolha um número de 1 a 5 para definir a prioridade"
    )
    area_interesse_ensino = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],  # Restringe o valor a 1 dígito, de 1 a 5
        help_text="Escolha um número de 1 a 5 para definir a prioridade"
    )
    area_interesse_secretaria = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],  # Restringe o valor a 1 dígito, de 1 a 5
        help_text="Escolha um número de 1 a 5 para definir a prioridade"
    )
    area_interesse_louvor = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],  # Restringe o valor a 1 dígito, de 1 a 5
        help_text="Escolha um número de 1 a 5 para definir a prioridade"
    )
    dizimo = models.DecimalField(max_digits=10, decimal_places=2,default=0)