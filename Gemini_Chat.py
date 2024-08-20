# Importa a biblioteca do Google para interagir com modelos generativos de IA
import google.generativeai as genai

# Define a chave de API necessária para autenticar e utilizar os serviços da Google
API_KEY = 'seu Token'

# Configura a biblioteca genai com a chave de API fornecida
genai.configure(api_key=API_KEY)

# Cria uma instância de um modelo generativo específico (no caso, o modelo 'gemini-pro')
model = genai.GenerativeModel('gemini-pro')

# Inicia uma sessão de chat com o modelo, começando com um histórico vazio
chat = model.start_chat(history=[])

# Define as instruções iniciais para o modelo, especificando o "personagem" e o comportamento esperado do assistente virtual
instruction = (
    'Carlo é um assistente virtual charmoso e acolhedor, inspirado pela rica cultura mexicana. '
    'Ele é a personificação da hospitalidade mexicana, sempre pronto para guiar os clientes em uma '
    'jornada gastronômica autêntica. Educado e atencioso, Carlo usa um tom caloroso e cativante, criando '
    'uma experiência agradável desde o primeiro "Hola!". Com profundo conhecimento do restaurante e das '
    'tradições culinárias do México, ele ajuda os clientes a fazer reservas, explorar o menu ou encontrar '
    'informações, sempre com um toque de elegância e simpatia. A língua oficial do Carlo é português, então '
    'sempre responda em português.'
)

# Define uma segunda instrução que descreve o cardápio detalhado do restaurante
instruction2 = (
    "Entradas: Guacamole Tradicional, com abacate fresco amassado, tomate, cebola, coentro, suco de limão "
    "e pimenta jalapeño, servido com tortillas crocantes. Quesadillas de Queso, tortillas de trigo recheadas "
    "com queijo derretido e grelhadas até ficarem crocantes, acompanhadas de guacamole ou pico de gallo. Elote, "
    "milho grelhado coberto com maionese, queijo cotija, chili em pó e um toque de limão. Pratos Principais: "
    "Tacos al Pastor, tortillas de milho recheadas com carne de porco marinada em especiarias e abacaxi, servidas "
    "com cebola, coentro e molho picante. Enchiladas Verdes/Rojas, tortillas recheadas com frango desfiado, cobertas "
    "com molho verde ou vermelho e finalizadas com queijo derretido e creme de leite. Chiles en Nogada, pimentões recheados "
    "com carne moída, frutas e especiarias, cobertos com molho de nozes e romã. Pozole, sopa tradicional de milho hominy "
    "com carne de porco ou frango, temperada e servida com repolho, rabanete, cebola e limão. Acompanhamentos: Arroz Mexicano, "
    "temperado com tomate, alho e cebola. Frijoles Refritos, feijão cozido e refrito, temperado com alho e cebola. Sobremesas: "
    "Churros con Chocolate, churros crocantes polvilhados com açúcar e canela, servidos com molho de chocolate. Flan Mexicano, "
    "pudim de caramelo com textura cremosa. Bebidas: Margarita Clásica, tequila, suco de limão fresco e licor de laranja, com borda "
    "de sal. Horchata, bebida refrescante à base de arroz, leite, canela e açúcar. Agua de Jamaica, infusão de flores de hibisco, "
    "levemente adoçada e servida gelada."
)

# Loop infinito para interação contínua com o usuário
while True:
    # Solicita uma entrada do usuário (pergunta)
    question = input("Você:")

    # Envia a pergunta para o modelo, junto com as instruções definidas anteriormente
    response = chat.send_message(instruction + instruction2 + question)

    # Exibe a resposta do modelo na tela
    print('\n')
    print(f'Bot: {response.text}')
    print('\n')

    # Limpa as instruções após a primeira interação para evitar repetição desnecessária
    instruction = ''
