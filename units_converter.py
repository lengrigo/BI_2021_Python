# Эта программа переведет концентрацию олигонуклеотидов из моль/литр в грамм/литр
print("Введите концентрацию нуклеотида в моль/литр")
concentration_mol = int(input())
print("Введите количество нуклеотидов")
num = int(input())
concentration_gram = concentration_mol / (345 * num)
print (f'Концентрация олигонуклеотида в грамм/литр - {concentration_gram}')