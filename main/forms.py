from django import forms
from .models import Avaliacao

class AvaliacaoForm(forms.ModelForm):
    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome",
                "class": "input100",
                "required":"true",

            }
        ))
    sexo = forms.ChoiceField(choices=Avaliacao.SEXO_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "input100",
                "required":"true",

            }
        ))
    nascimento = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "placeholder": "Data de Nascimento",
                "class": "input100",
                "required":"true",
                "type":"date"

            }
        ))
    
    celular = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Celular",
                "class": "input100",
                "type":"phone",
            }
        ))
    social = forms.CharField(
        required=False,  # Indica que o campo não é obrigatório no formulário
        widget=forms.TextInput(
            attrs={
                "placeholder": "Redes Sociais",
                "class": "input100",
            }
        )
    )

    relacao = forms.ChoiceField(choices=Avaliacao.RELACAO_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "input100",
                "required":"true",

            }
        ))
    sociedade = forms.MultipleChoiceField(
        choices=Avaliacao.SOCIEDADES_CHOICES,  # As escolhas definidas no modelo
        widget=forms.CheckboxSelectMultiple(  # Usa o widget CheckboxSelectMultiple
            attrs={
                "type": "checkbox",
                 # Adiciona o atributo tipo 'checkbox' a cada input
            }
        )
    )
    sobre_a_igreja = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Como enxegar a IP josé Américo",
                "class": "input100"
            }
        ))
    louvor = forms.ChoiceField(choices=Avaliacao.QUALIDADE_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "input100",
                "required":"true",

            }
        ))
    visitacao = forms.ChoiceField(choices=Avaliacao.QUALIDADE_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "input100",
                "required":"true",

            }
        ))
    recepcao = forms.ChoiceField(choices=Avaliacao.QUALIDADE_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "input100",
                "required":"true",

            }
        ))
    evengelizacao = forms.ChoiceField(choices=Avaliacao.QUALIDADE_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "input100",
                "required":"true",

            }
        ))
    comunicacao = forms.ChoiceField(choices=Avaliacao.QUALIDADE_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "input100",
                "required":"true",

            }
        ))
    escola_dominical = forms.ChoiceField(choices=Avaliacao.QUALIDADE_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "input100",
                "required":"true",

            }
        ))
    diaconos = forms.ChoiceField(choices=Avaliacao.QUALIDADE_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "input100",
                "required":"true",

            }
        ))
    
    presbiteros = forms.ChoiceField(choices=Avaliacao.QUALIDADE_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "input100",
                "required":"true",

            }
        ))
    pastor = forms.ChoiceField(choices=Avaliacao.QUALIDADE_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "input100",
                "required":"true",

            }
        ))
    seu_compromisso = forms.ChoiceField(choices=Avaliacao.QUALIDADE_PESSOAL_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "input100",
                "required":"true",

            }
        ))
    leitura = forms.ChoiceField(choices=Avaliacao.QUALIDADE_PESSOAL_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "input100",
                "required":"true",

            }
        ))
    observacao_diaconos = forms.CharField(
        required=False,
        widget=forms.Textarea(
            
            attrs={
                "placeholder": "Observações sobre a junta Diaconal?",
                "class": "input100"
            }
        ))
    
    observacao_presbiteros = forms.CharField(
        required=False,
        widget=forms.Textarea(
            
            attrs={
                "placeholder": "Observações sobre a Atuação Presbiteral?",
                "class": "input100"
            }
        ))
    
    observacao_pastor = forms.CharField(
        required=False,
        widget=forms.Textarea(
            
            attrs={
                "placeholder": "Observações sobre a Atuação Pastoral?",
                "class": "input100"
            }
        ))
    area_interesse_comunicacao = forms.IntegerField(
        required=False,
        
        widget=forms.TextInput(
            attrs={
                "placeholder": "de 1 a 5",
                "class": "input100",
                "type":"number",
                "max":"5",
                "min":"0",

               
            }
           
            ),
        initial=0,
        )
    def clean(self):
        cleaned_data = super().clean()
        
        # Itera sobre os campos para processar aqueles que começam com 'area_interesse'
        for field in cleaned_data.keys():
            if field.startswith('area_interesse'):
                value = cleaned_data.get(field)
                if value in (None, ''):  # Se o valor é None ou string vazia
                    cleaned_data[field] = 0  # Define o valor padrão como 0

        return cleaned_data
    
    area_interesse_evangelismo_missoes = forms.CharField(
        required=False,
        widget=forms.TextInput(
            
            attrs={
                "placeholder": "de 1 a 5",
                "class": "input100",
                "type":"number",
                "max":"5", "min":"0",
               
            }
        ))
    area_interesse_projeto_viver = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "de 1 a 5",
                "class": "input100",
                "type":"number",
                "max":"5",
                "min":"0",

               
            }
        ))
    area_interesse_departamento_infantil = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "de 1 a 5",
                "class": "input100",
                "type":"number",
                "max":"5",
                "min":"0",

               
            }
        ))
    area_interesse_acao_social_diaconia = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "de 1 a 5",
                "class": "input100",
                "type":"number",
                "max":"5",
                "min":"0",
               
            }
        ))
    area_interesse_visitacao = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "de 1 a 5",
                "class": "input100",
                "type":"number",
                "max":"5",
                "min":"0",

               
            }
        ))
    area_interesse_recepcao = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "de 1 a 5",
                "class": "input100",
                "type":"number",
                "max":"5",
                "min":"0",
               
            }
        ))
    area_interesse_zeladoria = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "de 1 a 5",
                "class": "input100",
                "type":"number",
                "max":"5",
                "min":"0"
               
            }
        ))
    area_interesse_eventos = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "de 1 a 5",
                "class": "input100",
                "type":"number",
                "max":"5",
                "min":"0",

               
            }
        ))
    area_interesse_ensino = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "de 1 a 5",
                "class": "input100",
                "type":"number",
                "max":"5",
                "min":"0",

               
            }
        ))
    area_interesse_secretaria = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "de 1 a 5",
                "class": "input100",
                "type":"number",
                "max":"5",
                "min":"0",

               
            }
        ))
    area_interesse_comunicacao = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "de 1 a 5",
                "class": "input100",
                "type":"number",
                "max":"5",
                "min":"0",
               
            }
        ))
    
    area_interesse_louvor = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "de 1 a 5",
                "class": "input100",
                "type":"number",
                "max":"5",
                "min":"0",
               
            }
        ))
    area_interesse_pregacao = forms.IntegerField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "de 1 a 5",
                "class": "input100",
                "type":"number",
                "max":"5",
                "min":"0",

               
            }
        ))
    dizimo = forms.DecimalField(
        required=False,
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'R$ 0,00',
                'class': 'input100',  # Pode ser ajustado conforme seu CSS
                'step': '0.01',  # Para aceitar centavos
                'min': '0'  # Para evitar valores negativos
            }
        )
    )
    
    class Meta:
        model = Avaliacao
        fields = ('nome','sexo', 'nascimento', 'celular', 'social','relacao','sociedade','sobre_a_igreja','louvor','visitacao','recepcao','evengelizacao','comunicacao','escola_dominical','diaconos','observacao_diaconos','presbiteros','observacao_presbiteros','pastor','observacao_pastor','seu_compromisso','leitura','area_interesse_comunicacao','area_interesse_evangelismo_missoes','area_interesse_projeto_viver','area_interesse_departamento_infantil','area_interesse_acao_social_diaconia','area_interesse_visitacao','area_interesse_recepcao','area_interesse_zeladoria','area_interesse_eventos','area_interesse_pregacao','area_interesse_ensino','area_interesse_secretaria','area_interesse_louvor','dizimo')


    