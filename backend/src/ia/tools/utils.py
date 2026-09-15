def somar(a: float, b: float) -> float:
    """[TEST] Função para somar dois valores. Retorna apenas o número final. Não faz arredondamentos."""
    print('[DEBUG] Entrou na função \'somar\'')
    return a + b

def subtrair(a: float, b: float) -> float:
    """[TEST] Função para subtrair dois valores. Retorna apenas o número final. Não faz arredondamentos."""
    print('[DEBUG] Entrou na função \'subtrair\'')
    return a - b

def clima(cidade: str) -> str:
    """[TEST] Função para informar o clima de uma cidade. Retorna apenas a descrição do clima."""
    print('[DEBUG] Entrou na função \'clima\'')
    return f"O clima em {cidade} é ensolarado com temperatura de 25°C."