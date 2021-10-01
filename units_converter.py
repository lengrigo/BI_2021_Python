# Эта программа переведет концентрацию олигонуклеотидов из моль/литр в грамм/литр
print("Введите концентрацию нуклеотида в моль/литр")
concentration_mol = int(input())
print("Введите количество нуклеотидов")
num = int(input())
concentration_gram = round(concentration_mol / (345 * num), 4)
print("Концентрация олигонуклеотида", concentration_gram, "грамм/литр")