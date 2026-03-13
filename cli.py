import typer
import questionary
from polynom import Polynom
from fft import FFT

app = typer.Typer()

def input_complex(text: str):
    while True:
        val = questionary.text(text).ask()
        if val == "":
            return None
        try:
            if 'j' in val:
                return complex(val)
            else:
                return complex(float(val))
        except ValueError:
            print("Ошибка: введите число (например 1, 2.5 или 1+2j)")

@app.command()
def run():
    action = questionary.select("Выберите действие:", 
                                choices=["Прямое FFT (коэф -> значения)", 
                                         "Обратное FFT (значения -> коэф)", 
                                         "Выход"]).ask()
    
    if action == "Выход":
        return
    
    if action == "Прямое FFT (коэф -> значения)":
        factors = []
        i = 0
        while True:
            val = questionary.text(f"Коэффициент при x^{i} (число):").ask()
            if val == "":
                break
            try:
                factors.append(float(val))
                i += 1
            except ValueError:
                print("Ошибка: введите число")
        
        if not factors:
            print("Нет коэффициентов")
            return
        
        polynom = Polynom(factors)
        print(f"Дополненный многочлен: {polynom.factors}")
        
        result = FFT.FFT(polynom.factors)
        for i, val in enumerate(result):
            print(f"P(ω^{i}) = {val}")
    
    else:
        values = []
        i = 0
        while True:
            val = input_complex(f"Значение P(ω^{i}):")
            if val is None:
                break
            values.append(val)
            i += 1
        
        if not values:
            print("Нет значений")
            return
        
        n = len(values)
        next_power = 1
        while next_power < n:
            next_power <<= 1
        if next_power > n:
            values.extend([0j] * (next_power - n))
            print(f"Дополнено до {next_power} значений нулями")
        
        result = FFT.IFFT(values)
        rounded = [round(c.real) if abs(c.imag) < 1e-10 and abs(c.real - round(c.real)) < 1e-10 
                  else c for c in result]
        for i, coef in enumerate(rounded):
            print(f"x^{i}: {coef/len(result)}")

if __name__ == "__main__":
    app()