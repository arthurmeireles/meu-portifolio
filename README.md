# meu-portifolio



#### Para criar um banco psql utilize o comando:

```shell
psql
```

```shell
create database nomedobanco;
```


#### Para rodar o projeto utilize o comando abaixo:
```shell
python manage.py runserver
```

### Para a utilização dos comandos abaixo, é necessario incluir o comando abaixo no inicio do arquivo:
  > {% load static %} 

#### Para INCLUIR uma imagem no projeto utilize o seguinte formato:
```html
<img class="logo" src="{% static 'img/logo.png' %}" alt="" srcset="">
```
#### Para INCLUIR um arquivo de estilo (CSS) no projeto utilize o seguinte formato:
```html
<link rel="stylesheet" href="{% static 'css/style.css' %}"
```

#### Para INCLUIR um arquivo de eventos (JS) no projeto utilize o seguinte formato:
```html
<script src="{% static 'js/scripts.js' %}"></script>
```

### Para criar um model, deve ser seguido o padrão abaixo. Esse trecho deve se colocado no arquivo models.py.

```

```



