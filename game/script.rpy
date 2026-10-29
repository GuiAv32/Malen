# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:
define m = Character("[name]", color = "#A30031")
define y = Character("Baba Yaga", color = "#9B00A3")
define r = Character("Baba Roga", color = "#0085A3")

# Definiendo algunas variables:
python:
    tBv = False
    tCv = False
    sv = False
    rooms = 0

# El juego comienza aquí.

label start:
    ### Acto 1 ###

    # Pantalla: negra 
    # Audio: viento invernal y traqueteo de caballos
    "Deberías sentir el frío habitual de esta época del año"
    "El infame aliento de Dios en tus poros"
    "Pero en esta ocasión, no es así"

    # Pantalla: carruaje
    "Has despertado en un carruaje en movimiento" 
    "Te toca los cachetes y confirmas algo"
    "No estás soñando"
    "Lo cual, es demasiado bueno para ser real"

    "???" "Estamos entrando… en la residencia de la señora Yaga, chico. Deberías irte despertando"

    "Escuchas esa voz, hosca y algo torpe, diciéndote que has llegado a tu destino"
    "No hace falta pensar demasiado para recordarlo…"
    "Es el mismo hombre que te preguntó si aceptabas ser acogido"

    # Audio: lobos ladrando
    "???" "Ay, ay, ay…. ¡Chuchos… estúpidos! aléjense, asustaraaaán al nene"

    "Unos ladridos y golpeteos a la puerta te sobresaltan. Parecen perros. Puede que sean algo más grande que un perro"

    "???" "Será un shooooock enorme… para él verlos tan pronto. Aguantense. Él eeeees su amo a partir de ahora… también"

    # --Tal vez podríamos no poner esto y más bien solo hacerle fadeout al audio.
    "Los sonidos de esos supuestos sabuesos se alejan"

    "???" "Bueno, chicoooo, disculpa el susto. Son algo… salvajes"
    "???" "…"
    "???" "Amables"
    "???" "Amablemente… salvajes"
    "???" "Tú piensa que son como pooooooddles," 
    "???" "Con colmillos, pelaje gris, ojos afilados…"
    "???" "Poodles… en toda regla"
    "???" "Eso sí, no acerques tus maaaaanos a ellos. Pueden morder demasiado fuerte"
    "???" "Así fue como perdí un dedo mío…"
    "???" "…"
    "???" "…Ehh, olvida esooooo, ¿Quieres?"

    # Audio: nada
    "No tardas mucho en finalmente llegar. El transporte dejó de vibrar. Te toca bajarte y entrar a un enorme Castillo"

    # Pantalla: Entrada Enorme
    # Personajes en Pantalla: Roga
    "???" "Ufff, Ha sido un largo. Encontrarte fue una suerte chico. Estabas helado. Te iba a dar hipotermia si llegaba demasiado tarde"
    "???" "O algo mucho peor"
    "???" "En fin. Es tal y como te prometí. Ahora eres acogido en nuestro humilde hogar"
    "???" "La señora Yagaaaaa debe estar en la Sala de estar para recibirte"
    "???" "Ella es una buena samaritana. Sabía que algún niño… podía estar en un deplorable estado"
    "???" "Ven, te guío"

    # Pantalla: negra
    "Te preguntas si esto tiene sentido"
    "En el Mundo de los Adultos, no hay nada gratis, ¿no?"
    "Siempre buscan algo. De tu padre buscaron deudas, de tu madre su cuerpo… de tí, ¿Qué quieren?"
    "De por sí, no tienes nada que ofrecer. Piensas que sirves más muerto que vivo"
    "El hecho de que aparentemente quieran darte felicidad es…"
    "Tan falso."

    # Pantalla: Sala
    # Audio: Música
    "???" "Juo, juo, juo…"
    "???" "Pero mira que tierno niño"

    # Personajes en Pantalla: Yaga
    y "Hola, mi buen mozo,  mi nombre es Yaga. Pero a algunos les gusta llamarme Baba Yaga"

    # Personajes en Pantalla: Yaga, Roga
    "???" "¿Algunos? A todos, mi señora"

    y "Solo algunos, simio pálido. Gente sin modales, como tú"
    y "Le estás dando mal ejemplo al niño"

    menu:
        "Baba Yaga no suena mal, en verdad. Es bonito apodo":
            jump yaga_smile

        "Baba Yaga, Baba Yaga, Baba Yagaaaa-":
            jump yaga_frown

label yaga_smile:
    
    y "¿Eh?"
    y "¿Te gusta?"    
    y "Bueno, tienes razón. No es un mal apodo"

    "???" "Si usted dice… mi señora"

    jump act1


label yaga_frown: 
    
    y "AHG, ¿Viste lo que hiciste?"
    y "¡Lo maleducaste!"

    "???" "O el chico es muy listoooo"

    jump act1

label act1:

    y "Disculpa mis modales. Mi sirviente, insolente y estúpido, no sabe cuándo respetar"
    y "Él será tu sirviente igual. Así que, si ves que desobedece. Dale un golpe"
    y "Mi parte favorita es su cabeza y su estómago"
    
    "???" "Mmmm… Ninguna de esas… es mi favorita…"

    y "A nadie le importa"
    y "Aunque eso sí. Debo saber, ¿Te has presentado como es debido, paleta blanca?"

    "???" "Noooo lo he hecho"
    "???" "Estaba conduciendo"

    y "Pudiste haberte presentado a la vez… como sea"
    y "El niño debe estar asustado"
    y "Él es Baba Roga. Como dije, es algo estúpido. Disculpa su falta de modales"
    y "Le comenté que buscase si había un necesitado en esta terrible época del año"
    y "Y, bueno, te halló a tí, por lo que veo"
    y "Debes estar con frío, chico"
    y "Ten, te dejo un abrigo"

    "Baba Yaga te da un abrigo afelpado"
    "Es cómodo. Demasiado cómodo"
    "Es mejor que cualquier bolsa de basura que hayas encontrado"

    y "Oh, te es placentero, ¿eh?"
    y "Es un regalo para tí"
    y "La mansión es cálida, pero más vale prevenir que lamentar"
    y "En fin, lamento cómo procedió tu recibida"
    y "Y, sea como sea, sepas que eres bienvenido"
    y "Qué a todo esto, ¿cómo te llamas?"

    # PARA DE PONER PUNTO AL FINAL.

    python:
        while True:
            name = renpy.input("¿Cuál es tu nombre?", length=32).strip()
            
            if not name:
                # Usamos renpy.say para mostrar texto dentro de un bloque python
                renpy.say(None, "Tienes que elegir un nombre. No puedes dejarlo en blanco.")
            elif name.lower() == "malen":
                renpy.say(None, "No, sabes que no vale la pena darles ese nombre")
                # Si quieres que se lo vuelva a pedir, dejamos el bucle activo (sin break)
            else:
                # Si pasa ambas validaciones, rompemos el bucle
                break

    y "¡Qué nombre tan bonito!"
    y "Y pensar que un alma como la tuya, acabaría desdichado en la calle…"
    y "¡Pero ya no será así!"
    y "Bienvenido seas a tu nuevo hogar"
    y "Siéntete como en casa"
    y "Al final y al cabo, lo será ahora"
    y "Oye, cara de poker"

    r "No necesita llamarme así…"

    y "Sí, sí. Perdona. Pero haz el favor de llevarlo a su nueva habitación"

    r "Como ordene"

    # Pantalla: Habitación
    # Personajes en Pantalla: Roga
    r "Esta es su… habitación. Anterioooormente le perteneció a unaaaa chiquilla que estuvo con nosotros"
    r "Era muy amigable. No obstante, quiso irse a estudiar en un colegio lejos de aquí"
    r "Así que, actualmente tú eres el dueño"
    r "Ven al Comedor cuando tengas hambre… iré preparando la comida. Diviéeeertete explorando"
    r "Eso sí, no puedes ir a todos loooos lugares. Hay cerraduras para ello"
    r "Por tu seguridad… claro"

    # Personajes en Pantalla: Nadie
    "Pensar que este lugar es de verdad tuyo…te incomoda"
    "Debería ser fácil pensar que hay gato encerrado"
    "Entonces, ¿Por qué te cuesta?"

    menu:
        "Ir al Comedor":
            jump dine

        "Explorar":
            jump where

label where:
    # Pantalla: Negra
    "¿A dónde irás?"

    menu:
        "Ir a la Cocina":
            jump kitchen

        "Ir al Torreon A":
            jump tower_A

        "Ir al Torreon B" if not tBv:
            jump tower_B

        "Ir al Torreon C" if not tCv:
            jump tower_C

        "Ir al Almacén" if not sv:
            jump storage

        "Ir a la Entrada":
            jump entrace

        "Ir al Comedor":
            jump dine

label kitchen:
    # Pantalla: Cocina
    # Personajes en Pantalla: Roga
    r "Oh… has venido conmiiiigo. Que… “encantador”"
    r "Disculpe. Estoy ocupadoooo en esto, querido huesped"

    menu roga_dial1:
        "¿Eres el esposo de Baba Yaga?":
            jump yaga_roga

        "¿Uy, qué sopa haces? Huele bien":
            jump soup

        "¿Por qué tan pálido?":
            jump lantern

        "¡Adiós!":
            jump roga_bye

    label yaga_roga:
        r "Uy… no"
        r "No, no, no"
        r "NUNCA"
        r "Bueno, emmm"
        r "Disculpe la desafortunada confusión"
        r "Mi señora es llamada “Baba Yaga” y a mí no me molesta llamarla así"
        r "Pero la parte de “Baba” es solo por confundirla con mi “prometida” en el pueblo cercano"
        r "En realidad, su nombre es “Yaga”, a secas"
        r "Séeee que es raro, si no estamos comprometidos"
        r "Pero, aquí entre nos"
        r "Me gusta hacerme justicia por los excesos de sus insultos…"
        r "Así que, BABA YAGA, BABA YAGA"

        y "¡TE ESCUCHO DESDE LA OTRA PUNTA DEL CASTILLO, SARANGANO DE PELOS MUERTOS!"

        r "..."
        r "Uf, casi me escucha"

        jump roga_dial1

    label soup:
        r "¿Ah sí?"
        r "Creía que estaba arruinándola"
        r "Tengo dificultades para oler…"
        r "Y saborear. Sobre todo saborear"
        r "Ahhhhh…"
        r "Extraño mi juventud"

        jump roga_dial1

    label lantern:
        r "Oh, por nada en especial"
        r "Soy sensible a la luz"
        r "La del sol, más que nada"
        r "Aunque a veces un foco bieeeen potente me hace daño"
        r "No te sorprendas por eso si ves que apago las luces a mi paso"

        jump roga_dial1

    label roga_bye:
        r "Chao, chico"

        jump where

label tower_A:
    # Implementar Click de Libros
    jump where

label tower_B:
    # Pantalla: Armario
    "No hay mucho aquí, solo un armario."

    menu closet_choice:
        "Husmear en el Armario":
            jump yaga_arg

        "Regresar":
            jump where

    label yaga_arg:
        "Baba Yaga y Baba Roga se escuchan llegando"
        "Decides esconderte en el Armario"

        # Pantalla: Negra

        r "¿Me ha llamado… mi señora?"

        y "Sí, tonto. ¿Qué es ese nefasto aroma que desprende tu arte obsceno?"

        r "Le he dicho… que noooo llame así a mi comida…"

        y "¿Y cómo puedo si quiera considerarlo comida?"
        y "¡Más te vale arreglarlo, por los cielos, el chiquillo se nos va a enfermar con eso!"

        r "¿Deeeesde cuándo le importa que eso pase?"

        y "¿Te succionó una mosca el cerebro o qué? ¡Desde siempre!"
        y "Es un niño. Son quisquillosos con la comida"
        y "Y sabiendo bien que donde él viene, ¿te atreves a darle algo que recuerde su horrible paso por las calles?"
        y "Queremos hacerlo feliz, no infeliz, mentecato…"
        y "Al menos, para algo tan horrible, deberías tener más corazón"

        r "..."
        r "Usted sí que puede estar mal de la cabezaaaa, ¿eh?"

        y "¡A que te doy una…!"

        "Los gritos se alejan. Parece que no te notaron"
        "...Mejor regresar"

        $ tBv = True
        $ rooms += 1
        jump where

label tower_C:
    # Pantalla: Mesa con Balanza
    "Describir lo extraño de la escena ante es imposible"
    "Mejor es hora de irte"

    $ tCv = True
    $ rooms += 1
    jump where

label storage:
    # Pantalla: Almacén
    "Cuanto polvo…"
    "Si de aquí sale la comida, no quieres averiguar qué te están preparando"
    "Es tan desolado el lugar que sientes una ligera brisa helada en tus tobillos"

    $ sv = True
    $ rooms += 1
    jump where

label entrace:
    # Pantalla: Entrada
    # Implementar click a la cabeza del alce y escaleras
    jump where

# --HAY QUE IMPLEMENTAR TODA LA SEGUNDA PLANTA

label dine:
    # Pantalla: Comedor

    # Finaliza el juego:

    return
