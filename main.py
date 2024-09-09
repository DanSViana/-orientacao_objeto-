# NOTE: criar uma classe
class Carro:
    # atributos
    fabricante = 'Volkswagen'
    modelo = 'Gol'
    ano = '2008'
    cor = 'preto'
    placa = 'ABC-1234'

    # métodos
    def ligar(self, ignicao):
        if ignicao:
            return f'{self.modelo} está ligado.'
        else:
            return f'{self.modelo} está desligado.'
        
# NOTE: programa principal
if __name__ == '__main__':
    # instancia a classe carro (criar objeto)
    meu_carro = Carro()

    # exibir os atributos do objeto
    print(f'Fabricante: {meu_carro.fabricante}.')
    print(f'Modelo: {meu_carro.modelo}.')
    print(f'Ano de fabricação: {meu_carro.ano}.')
    print(f'Cor do carro: {meu_carro.cor}.')
    print(f'Placa do carro: {meu_carro.placa}.')

    # Ligar (ou não) o carro
    ignicao = True

    # chama o método do objeto
    print(meu_carro.ligar(ignicao))
  
