from flask import Flask, render_template
from dynaconf import FlaskDynaconf
app = Flask(__name__)
FlaskDynaconf(app)

datas =[{'_id': "ObjectId('63a612f625ce74028d35d3b0')",
        'cod': 1,
        'nome': 'Abrigo de Láminas',
        'nivel': 0,
        'tipo': 'Abjuração',
        'classes': ['Bardo', 'Bruxo', 'Feiticeiro', 'Mago'],
        'tempo': '1 acão',
        'alcance': 'Jogador',
        'componentes': ['V', 'G'],
        'duracao': '1 rodada',
        'descricao': 'O jogador estende sua mão e traça um símbolo de proteção no ar. Até o final do próximo turno do jogador ele ganha resistência contra danos do tipo de concussão, perfurante e cortante, causados por ataques com armas.',
        'imagem':'/static/imagens/evocacao.png'},
{
    '_id': "ObjectId('63aa049341b4b2e4e5515825')",
    'cod': 2,
    'nome': 'Arma Druídica',
    'nivel': 0,
    'tipo': 'Transmutação',
    'classes': ['Druida'],
    'tempo': '1 ação bônus',
    'alcance': '9 metros (6 quadrados)',
    'componentes': [
        
            'V',
            'G',
            'M'
    ],
    'material':
            {
                'Visco':'Visco',
                '1 folha de trevo':'1 folha de trevo',
                '1 porrete ou um cajado':'1 porrete ou um cajado'
            
            },
    'duracao': '1 minuto',
    'descricao': 'A madeira de um bordão ou clava que o jogador estiver segurando é imbuída com poderes da natureza. Pela duração da magia, o jogador pode usar seu atributo de conjuração ao invés de <strong>Força</strong> para as jogadas de ataque e dano feit as corpo a corpo com esta arma, e o dado de dano da arma se torna d8. A arma também se torna mágica, caso ela já não seja. A magia é encerrada se o jogador a lançar novamente ou se soltar a arma.',
    'imagem': '/static/imagens/evocacao.png'},
{
    '_id': "ObjectId('63aa049341b4b2e4e5515825')",
    'cod': 4,
    'nome': 'Bola de Fogo',
    'nivel': 3,
    'tipo': 'Evocação',
    'classes': ['Feiticeiro', 'Mago'],
    'tempo': '1 ação',
    'alcance': '45 metros (30 quadrados)',
    'componentes': [

            'V',
            'G',
            'M'
           ],
        'material':
        {
               '1 pequeno bolo de excremento de morcego e ': '1 pequeno bolo de excremento de morcego)',
               'enxofre': 'enxofre',
           },
    'duracao': 'Instantâneo',
    'descricao': 'Uma luz brilhante irrompe do dedo indicador do jogador até um ponto que ele possa ver dentro do alcance da magia e então se expande com um som baixo de um estrondo até detonar em uma explosão de chamas. Cada criatura em uma raio de 6 metros(4 quadrados) a partir do ponto central escolhido, deve fazer um TR de Destreza. Se falhar o alvo recebe 8d6 de dano, ou metade se tiver sucesso. O fogo alcança mesmo os cantos do ambiente, como quinas. O fogo danifica objetos na área e incendeia objetos inflamáveis que não estejam sendo utilizados ou carregados. Em níveis superiores. Quando o jogador lança esta magia usando o espaço de uma magia de 4º nível ou superior, o dano aumenta em 1d6 para cada nível acima do 3º.',
    'imagem':'/static/imagens/evocacao.png'},
{
    '_id': "ObjectId('63aa049341b4b2e4e5515825')",
    'cod': 3,
    'nome': 'Ataque Certeiro',
    'nivel': 0,
    'tipo': 'Adivinhação',
    'classes': ['Bardo', 'Bruxo', 'Feiticeiro', 'Mago'],
    'tempo': '1 ação',
    'alcance': '9 metros (6 quadrados)',
    'componentes': [
            'G',
    ],
    'duracao': 'Concentração, dura até 1 rodada',
    'descricao': 'O jogador estende sua mão e aponta seu dedo sobre o alvo dentro do alcance. A magia garante ao jogador uma breve intuição sobre as defesas do alvo. No próximo turno do jogador, ele ganha vantagem em sua primeira jogada de ataque contra o alvo, considerando que esta magia ainda não tenha acabado.',
    'imagem':'/static/imagens/evocacao.png'
},
]


@app.route('/')
def index():
    return render_template("index.html", datas=datas)


if __name__ == '__main__':
    app.run(debug=True)
