# Введение

Кейс для пакет OpenFoam с возможностью генерации сетки в salome без запуска декстоп-приложения. Кейс подготовлен для [Simput](https://github.com/Kitware/simput).
<br /><br />
![Viz](https://snipboard.io/r43DFb.jpg)
<center style="margin-top: -10px;">Визуализация</center>
<br />


# Зависимости

Для запуска кейса требуются:
- Salome 9.3.0
- OpenFoam >= 5.0

# Запуск

Необходимо скопировать env-файл
```
cp sample.env .env
```
В этом файле указывается путь к папке salome, в моем случае файл `.env` содержит следующее:
```

SALOME_PATH=/home/dealenx/salome/appli_V9_3_0

```
Вам соответственно необходимо отредактировать `.env`

Далее запускаем `run.sh`:
```
./run.sh
```
