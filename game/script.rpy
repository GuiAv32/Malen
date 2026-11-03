# Declara los personajes usados en el juego:
define m = Character("[name]", color = "#A30031")
define y = Character("Baba Yaga", color = "#9B00A3")
define r = Character("Baba Roga", color = "#0085A3")
image carruaje_bg = Movie(play="video/Carruaje.webm", loop=True)
image Entrada1= "images/Fondos/Entrada_con_cabeza.png"
image Entrada2= "images/Fondos/Entrada_sin_cabeza.png"
image Dormitorio= "images/Fondos/Dormitorio.png"
image Dormitorio1= "images/Fondos/DormitorioPostMes.png"
image Cocina="images/Fondos/Cocina.png"
image B1="images/Fondos/Balanza0.png"
image B2="images/Fondos/BalanzaOro.png"
image Comedor="images/Fondos/Comedor.png"

# Variables
default visited_kitchen = False
default visited_tower_a = False
default visited_tower_b = False
default visited_tower_c = False
default visited_storage = False
default visited_entrance = False
default rooms = 0

default asked_yaga = False
default asked_kids = False
default asked_food = False
default sospecha = 0
default duda = 0
default diario_leido = False
default tiene_linterna = False
default tiene_huevo = False
default tiene_balde = False
default tiene_cuchillo = False
default tiene_llave_huevo = False
default visita_cuarto_3 = False
default tiene_llave_alce = False
default roga_vivo = True

label start:
    ### Acto 1 ###
    scene black
    with fade
    play music "audio/efectos/Carruaje .mp3" volume 3.0 fadein 2.0
    
    # Pantalla: negra 
    # Audio: viento invernal y traqueteo de caballos
    "Deberías sentir el frío habitual de esta época del año"
    "El infame aliento de Dios en tus poros"
    "Pero en esta ocasión, no es así"

    scene carruaje_bg
    with fade

    # Pantalla: carruaje
    "Has despertado en un carruaje en movimiento" 
    "Te tocas los cachetes y confirmas algo"
    "No estás soñando"
    "Lo cual, es demasiado bueno para ser real"
    "???" "Estamos entrando… en la residencia de la señora Yaga, chico. Deberías irte despertando"
    "Escuchas esa voz, hosca y algo torpe, diciéndote que has llegado a tu destino"
    "No hace falta pensar demasiado para recordarlo…"
    "Es el mismo hombre que te preguntó si aceptabas ser acogido"

    play sound "audio/efectos/Ladridos.mp3" volume 2.0

    # Audio: lobos ladrando
    "???" "Ay, ay, ay…. ¡Chuchos… estúpidos! aléjense, asustaraaaán al nene"

    play sound "audio/efectos/GolpeLobo.mp3" volume 2.0

    "Unos ladridos y golpeteos a la puerta te sobresaltan. Parecen perros. Puede que sean algo más grande que un perro"

    play sound "audio/efectos/Ladridos.mp3" volume 2.0

    "???" "Será un shooooock enorme… para él verlos tan pronto. Aguantense. Él eeeees su amo a partir de ahora… también"

    stop sound fadeout 1.0

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

    stop music fadeout 2.0

    scene black
    with fade
    # Audio: nada
    "No tardas mucho en finalmente llegar. El transporte dejó de vibrar. Te toca bajarte y entrar a un enorme Castillo"
    play sound "audio/efectos/PuertaAbrir.mp3" volume 2.0
    # Pantalla: Entrada Enorme
    scene Entrada1

    # Personajes en Pantalla: Roga
    "???" "Ufff, Ha sido un largo. Encontrarte fue una suerte chico. Estabas helado. Te iba a dar hipotermia si llegaba demasiado tarde"
    "???" "Y eso te hubiera llevado a algo... mucho peor"
    "???" "En fin. Es tal y como te prometí. Ahora eres acogido en nuestro humilde hogar"
    "???" "La señora Yagaaaaa debe estar en su cuarto"
    "???" "Ella es una buena samaritana. Sabía que algún niño… podía estar en un deplorable estado"
    "???" "Espera aquí, ya regreso"
    scene black
    with fade

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
    scene Entrada1
    with fade
    play music "audio/Musica/Impertinence.mp3" volume 3.0 fadein 1.0
    # Personajes en Pantalla: Yaga
    y "Hola, mi buen mozo,  mi nombre es Yaga. Pero a algunos les gusta llamarme Baba Yaga"

    # Personajes en Pantalla: Yaga, Roga
    "???" "¿Algunos? A todos, mi señora"
    y "Solo algunos, simio pálido. Gente sin modales, como tú"
    y "Le estás dando mal ejemplo al niño"

    menu:
        "Baba Yaga no suena mal, en verdad. Es bonito apodo":
            y "¿Eh?"
            y "¿Te gusta?"    
            y "Bueno, tienes razón. No es un mal apodo"
            "???" "Si usted dice… mi señora"
            jump act1

        "Baba Yaga, Baba Yaga, Baba Yagaaaa-":
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
    scene Dormitorio
    with fade
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
        "Ir a la Cocina" if not tiene_huevo:
            jump kitchen
        "Ir al Torreon A":
            jump tower_A
        "Ir al Torreon B" if not visited_tower_b or not diario_leido:
            jump tower_B
        "Ir al Torreon C":
            jump tower_C
        "Ir al Almacén" if not visited_storage or not diario_leido:
            jump storage
        "Ir a la Entrada":
            jump entrance
        "Ir al Comedor" if not diario_leido:
            jump dine
        "Ir al Cuarto de Baba Roga" if tiene_llave_huevo:
            jump roga_room

label kitchen:
    scene Cocina
    with fade
    # Pantalla: Cocina
    # Personajes en Pantalla: Roga

    # --IMPLEMENTAR FASE DISTINTA--
    if not visited_kitchen:
        $ visited_kitchen = True
        $ rooms += 1

    r "Oh… has venido conmiiiigo. Que… “encantador”"
    r "Disculpe. Estoy ocupadoooo en esto, querido huesped"

    if not diario_leido:
        menu roga_dial1:
            "¿Eres el esposo de Baba Yaga?":
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

            "¿Uy, qué sopa haces? Huele bien":
                r "¿Ah sí?"
                r "Creía que estaba arruinándola"
                r "Tengo dificultades para oler…"
                r "Y saborear. Sobre todo saborear"
                r "Ahhhhh…"
                r "Extraño mi juventud"
                jump roga_dial1

            "¿Por qué tan pálido?":
                r "Oh, por nada en especial"
                r "Soy sensible a la luz"
                r "La del sol, más que nada"
                r "Aunque a veces un foco bieeeen potente me hace daño"
                r "No te sorprendas por eso si ves que apago las luces a mi paso"
                jump roga_dial1

            "¡Adiós!":
                r "Chao, chico"
                jump where
    else:
        if not tiene_balde:
            "No, aún no tienes lo necesario para conseguir lo que buscas aquí."
            jump where
        else:
            "Sería útil tirar el agua aquí"
            "Tiras el agua para distraer a Roga"
            r "¿Qué ocurre chico?"
            r "¿Has tirado... aguaaaa por accidente?"
            if sospecha < 2:
                r "Jajajaja"
                r "Eres muy torpe"
                r "Ya me encargaré"
            else:
                r ".... No tiene gracia... chico"
                r "Esa vieja pueeeede ser mi “jefa”..."
                r "Pero lo es porque se lo permito"
                r "Tú no estarás lo suficiente..... para que tenga que llamarte “jefe”"
            "Ahora que se ha ido, robas el huevo"
            "No hay que perder el tiempo"
            $ tiene_huevo = True
            jump tower_C


label tower_A:
    if not visited_tower_a:
        $ visited_tower_a = True
        $ rooms += 1

    # Pantalla: Torreón A (Estantería con libros, mesa y sofá)
    "Ves una estantería con varios libros, además de una mesa y un sofá donde sentarse"
    "Hay tres libros que llaman tu atención por sus títulos"
    # Cambiar la escena a los 3 libros
    label tower_A_menu:
        menu:
            "Examinar 'La Odisea'":
                "Agarras el libro y lees un poco"
                "Te cuesta mucho leer como para empezar con esto ahora, así que lo dejas tal como está"
                jump tower_A_menu
            "Examinar 'La Biblia'":
                "Pasas las hojas un momento"
                "Te cuesta mucho leer como para empezar con esto ahora, así que la dejas tal como está"
                jump tower_A_menu
            "Examinar 'El Cíclope' de Eurípides":
                "Revisas las páginas de la obra de Eurípides"
                "Te cuesta mucho leer como para empezar con esto ahora, así que lo dejas tal como está"
                jump tower_A_menu
            "Regresar":
                jump where

label tower_B:
    # Pantalla: Armario
    if not visited_tower_b:
        $ visited_tower_b = True
        $ rooms += 1
    "No hay mucho aquí, solo un armario."
    menu closet_choice:
        "Husmear en el Armario":
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
            jump where
        "Regresar":
            jump where

label tower_C:
    # Pantalla: Mesa con Balanza
    scene B2
    with fade
    if not visited_tower_c:
        $ visited_tower_c = True
        $ rooms += 1
    "Describir lo extraño de la escena es imposible"
    "Igualmente te causa curiosidad"
    menu egg:
        "Inspeccionar la balanza":
            if not tiene_huevo:
                # Al intentar agarrar el huevo
                "No es buena idea quitar el huevo falso sin reemplazarlo por algo de un mismo tamaño"
                "¿Tal vez robar un huevo en la cocina sea buena idea?"
                jump where
            else:
                # Al intentar distraer a Roga
                "Ahora que tienes el huevo, lo cambias por el de la Jaula"
                "¡Ya lo tienes en tus manos!"
                "Lo notas al instante. Es un huevo falso"
                "Se puede abrir con un giro, permitiendo extraer la llave de Baba Roga"
                $ tiene_llave_huevo = True
                jump where
        "Irte":
            "Mejor es hora de irte"
            jump where

label storage:
    # Pantalla: Almacén
    if not visited_storage:
        $ visited_storage = True
        $ rooms += 1
    "Cuanto polvo…"
    "Si de aquí sale la comida, no quieres averiguar qué te están preparando"
    "Es tan desolado el lugar que sientes una ligera brisa helada en tus tobillos"
    jump where

label entrance:
    if not visited_entrance:
        $ visited_entrance = True
        $ rooms += 1
    scene Entrada1
    with fade

    # Pantalla: Entrada (Paredes adoquinadas, alfombra con líneas amarillas, focos)
    "Estás en la enorme entrada del castillo"
    menu entrance_menu:
        "Tocar la cabeza de alce":
            "Ese alce parece estar viéndote con disgusto..."
            "Te gustaría tirarlo de su egocéntrico lugar"
            jump entrance_menu
        "Revisar las escaleras":
            "Ves dos escaleras que conducen hacia una segunda planta y una puerta en medio de estas"
            menu:
                "Subir a la segunda planta":
                    jump planta_dos
                "Quedarse en la planta baja":
                    jump entrance_menu
        "Regresar":
            jump where

label roga_room:
    # En el cuarto de Baba Roga
    "Encuentras una serie de notas casi decorando el cuarto"
    "'La señora me ha pedido cuidar de la llave de los invitados'"
    "'Seguro le retuerce el estómago... recordar el pecado que se esconde en cada habitación...'"
    "'Solo en los niños siente pena. ¿Por qué no en mí, su sirviente?'"
    "'Como sea, he dejado la llave en el jardín. En el altar del centro'"
    "'Eeeees imposible que el niño llegué ahí. Los árboles bañan el jardín con sombras y los chuchos estáaaan rondando'"
    "..."
    "Hay un foco aquí"

    if tiene_linterna:
        "Podría ser útil con tu linterna, así que se la colocas"
    else:
        "...aunque no tienes nada con lo que te sirva aún"

    # Patio y Huida
    "Ya tienes la llave de invitados"
    "Puede que halles pistas ahí"

    menu:
        "Salir":
            pass

    # Confrontación con Baba Roga
    if sospecha < 2:
        r "¿Qué haces aquí?"
        r "Chico... ¿abriste la Jaula... y robaste la llave?"
        r "... niño..."
        r "¿Acaso te diste cuenta?"
        r "¿Saaaabes lo que nosotros...?"
        r "..."
        r "Lo... siento"

        if tiene_linterna:
            menu:
                "Usar la linterna contra Baba Roga":
                    r "ΑΗΗΗΗΗΗΗΗΗΗΗΗΗΗ"
                    r "AGH, ¡No! ¿¡Por qué tú..!?"
                    r "No, por favor..."
                    r "Solo seguía... sus órdenes..."
                    "..."
                    "Ya puedes mirar los cuartos de invitados"
                    $ roga_vivo = False
                "Huir":
                    "Eludes sus garras"
                    "Intenta capturarte, pero es lento"
                    "Lo esquivas lo suficiente y escapas a la puerta. La cierras con llave para que no te siga"
                    r "Chiicccooooo, abreeee"
                    r "Por favor... ella me castigará si no..."
                    r "ChicoooooooooOOOOOOOO"
                    "Habla y habla"
                    "Su voz se va cansando..."
                    "Es inútil preocuparte porque él entre. No hay otra entrada. Decides irte y explorar los cuartos de invitados"
                    "Ya puedes mirar los cuartos de invitados"
        else:
            "Eludes sus garras"
            "Intenta capturarte, pero es lento"
            "Lo esquivas lo suficiente y escapas a la puerta. La cierras con llave para que no te siga"
            r "Chiicccooooo, abreeee"
            r "Por favor... ella me castigará si no..."
            r "ChicoooooooooOOOOOOOOOOO"
            "Habla y habla"
            "Su voz se va cansando..."
            "Es inútil preocuparte porque él entre. No hay otra entrada. Decides irte y explorar los cuartos de invitados"
            "Ya puedes mirar los cuartos de invitados"

    else: # sospecha >= 2
        r "..."
        r "Así queeee..."
        r "¿Looo sabías, eh?"
        r "Pareceeee que su pésima actitud... no fue lo único que te quedaste de ella"
        r "Ja... ja... ja... ja..."
        r "A ella no puedo hacerle nada..."
        r "Ella es mi maestra"
        r "¿Peroooo a tí?"
        r "Me servirás para desestresarmeeee..."

        if tiene_linterna:
            "Baba Roga te amenaza, así que usas la linterna"
            "Es eficaz, lo oyes gritar"
            "Fue instintivo. Te iba a atacar..."
            "Aún así, te duele. No sabes si tenía sentido o no su furia..."
            r "Agh... agh..."
            "Baba Roga se retuerce. No puede hablar. Su piel se incendia..."
            ".. y termina por convertirse en polvo"
            "Ya puedes mirar los cuartos de invitados"
            $ roga_vivo = False
        else:
            "Baba Roga intenta matarte"
            "Corres a un costado cuando él usa sus uñas para tratar de matarte"
            "No intenta capturarte, te quiere usar como carne de desestrés"
            "Tiene sentido... le trataste mal. Mal, mal, mal"
            "Ni siquiera sabiendo cómo se siente, lo trataste mejor..."
            "Aún así, evitas sus garras..."
            "Es lento. Tú más joven y ágil. A prisas, corres a la puerta, sales, y cierras la puerta con la llave"
            r "ABREEEE LA PUERTAAAAAAAAAAAAAAAA"
            r "Túuuuuuuuuuuuuuuuu"
            r "Te mereeeeces tooooodo lo malo"
            r "TOOOOODOOOOO"
            "Baba Roga sigue tocando la puerta. Decides irte."
            "Ya puedes mirar los cuartos de invitados"
    jump act3

label planta_dos:
    # Pantalla: Segunda Planta
    "Ya estás en la Segunda Planta, ¿a dónde vas?"
    menu planta_dos_menu:
        "Ir a la Sala de estar" if not diario_leido:
            jump segunda_sala_estar
        "Ir al Almacén de materiales" if not tiene_linterna:
            jump almacen_materiales
        "Ir al Baño":
            jump bano_planta_dos
        "Bajar a la planta baja":
            jump entrance


label segunda_sala_estar:
    # Pantalla: Sala de estar (segunda planta - varios sofás y una mesa en el centro)
    "Ves varios sofás y, en el centro de estos, una mesa"
    "Notas que debajo de esa mesa hay un papel asomándose"

    menu sala_estar_menu:
        "Examinar el papel bajo la mesa":
            "Lees lo que dice el papel:"
            "“La bestia fue eclipsada. El héroe de los dioses fue victorioso tras terminar su viaje. Pero su civilización cambió de fe pese a sus logros”"
            "¿Qué sentido tendrá esto?"
            
            # Aparición sorpresa de Baba Yaga según el PDF
            y "Oh, aquí estabas"
            y "Al final, decidiste explorar, ¿Eh?"
            y "Qué bueno, qué bueno"
            y "Eso dice mucho de tí. ¿Debes estar contento, no?"
            y "Los niños como tú no merecen vivir con la incompetencia de los adultos"
            y "Por lo tanto, supongo que expío los pecados de mis congéneres"
            y "Como sea, he estado esperando en el Comedor"
            y "Ven cuando te sientas listo"
            y "El idiota de Roga es horrible, pero sabe hacer platillos... “decentes”"  
            "Baba Yaga se marcha"
            jump planta_dos_menu
        "Regresar al distribuidor de la segunda planta":
            jump planta_dos

label almacen_materiales:
    # Pantalla: Almacén de materiales (mesas, cajas)
    "Es una habitación llena de mesas y cajas"
    "En una de ellas hay una linterna enorme, sin foco"
    menu almacen_menu:
        "Examinar la linterna":
            "Te suena haber visto eso en algún lugar"
            "Recuerdas que los policías lo llamaban “linterna” en la calle, y que sirve para iluminar"
            "Solo que esta es más grande que una normal"
            $ tiene_linterna = True
            "¡Te has quedado con la linterna!"
            jump almacen_menu
        "Regresar":
            jump planta_dos


label bano_planta_dos:
    # Pantalla: Baño
    "Sientes el vapor tocar tu piel. El agua no es fría. No es sucia"
    "Es agua para asearte"
    "¿Siquiera... eso es posible?"  
    menu bano_menu:
        "Inspeccionar balde" if diario_leido:
            "Tal vez tirar agua sea una buena distracción"
            "Has llenado el balde"
            $ tiene_balde = True
            jump planta_dos
        "Regresar":
            jump planta_dos

label dine:
    scene Comedor
    with fade
    # Pantalla: Comedor Enorme (mesas con mantas, candelabro, pinturas)
    # Personajes en Pantalla: Yaga

    # Caso 1: Si exploró al menos dos habitaciones ($ rooms >= 2)
    if rooms >= 2:
        y "¡Bienvenido chico!"
        y "Te ves...feliz"
        y "Un momento, en serio ¿Lo que veo ahí es una sonrisa?"
        y "Jujujuju. ¡Qué chuecos tienes tus dienticos de leche!"
        y "Una gran diferencia para tu... “aspecto original”"
    # Caso 2: Si fue directo al comedor ($ rooms < 2)
    else:
        y "Has sido muy rápido"
        y "Supongo que tienes mucha hambre"
        y "Pues bien, este es el comedor, querido"
        y "No recibimos muchas visitas, pero es una herencia de otros tiempos más lejanos"
        y "Lástima que nuestro “sirviente” no sea más competente por eso"

    # Personajes en Pantalla: Yaga, Roga
    y "¡Oh, mira que te tardas, lenturro!"
    r "Es lo que... hay... señora"
    r "Mi pierna no estáaaaaa en sus mejores días"
    y "¿Y por eso el niño tendrá menos hambre?"
    y "¡Ya dale de comer!"
    "Recibes el plato en tu mesa..."
    "Se ve sano"
    "Demasiado sano..."
    "¿Es tarde para retractarte y marcharte?"
    "¿No es este un paso demasiado difícil?"
    "Te llevas una cuchara a la boca"
    "Sorbes"
    "Tragas"
    "Esperas"
    "....."
    "..."
    "Estaba... delicioso..."
    y "¿Hmmm?"
    y "¿Estás llorando, niño?"
    y "Oh, pobrecito"
    y "Deja que Yaga te dé un abrazo"
    "La señora te rodea con sus brazos sin permiso"
    "No duele. No se siente falso"
    "Sientes la calidez inundarte"
    "....."
    "No..."
    "No lo entiendes"
    y "Ya te sientes mejor, ¿no, muchacho?"
    y "¡No hay nada mejor que una sopa, un abrazo y un techo encima tuyo!"
    y "Sé que los jóvenes como tú tienden a costarles dejarse amar. No los culpo, las calles los han convertido en niños-adultos. Adultos rotos"
    y "No quiero que temas aquí"
    y "No eres el único niño que ha estado aquí"
    y "Siempre hay chiquillos como tú que merecen una oportunidad"
    r "Mi señora tieeeene razón, chico. Estás a salvo aquí"
    y "Si necesitas cualquier cosa, aquí estamos para tí"
    y "Aquí tu abuela Yaga para servirte"

    $ asked_yaga = False
    $ asked_kids = False
    $ asked_food = False

label dine_questions:
    menu:
        "Muchas gracias, Abuela Yaga" if not asked_yaga:
            $ asked_yaga = True
            y "No hay de qué"
            y "Esto debió serte dado desde hace mucho antes"
            y "Realmente, enfrentarte a un destino desafortunado sin vivir la alegría de vivir. ¿Qué horrible sería, no crees?"
            r "¿Y a míiii no me agradecerán nada?"
            y "Cállate"
            jump dine_questions
        "¿Qué pasó con los otros niños?" if not asked_kids:
            $ asked_kids = True
            r "Oh, tuvieron que marcharse"
            r "No tuvieron mucho tiem-"
            y "¡Mucho tiempo con nosotros!"
            y "Mira, chico, te ofrecemos vivir aquí"
            y "Sin embargo, en un mes. Quiero que termines de tomar una decisión"
            y "Hasta ahora, parece que te hemos secuestrado"
            r "Buenoooo... en la práctica... es eso"  
            y "¡Silencio, animal!"
            y "Como decía, no quiero que pienses de inmediato en quedarte aquí"
            y "Tienes muchas oportunidades en la vida"
            y "Por lo cual, piensa en eso, ¿sí?"
            jump dine_questions
        "¿Ustedes no van a comer?" if not asked_food:
            $ asked_food = True
            y "¡Uh, no, tranquilo, no!"
            y "Ya he comido"
            y "No necesito comer... en un tiempo"
            r "Yo de por sí no como" 
            y "Jojojo, qué gracioso eres"
            y "¿Verdad?"
            jump dine_questions
        "Concluir conversación" if asked_yaga and asked_kids and asked_food:
            jump dine_end

label dine_end:
    y "Muy bien, ya se está haciendo tarde"
    y "Más te vale descansar a partir de ahora, [name]"
    y "Te esperan varios días de deliberación"

    # Transición: Cuarto del niño
    "La habitación ya está climatizada"
    "Te espera una agradable cama para tí"
    "No sabes si esto es real"
    "Si siquiera tiene sentido para tí"
    "Da igual"
    "Decides escapar en menos de una semana. Robarás todo lo que puedas para largarte"
    "No confías ni confiarás nunca en los adultos"
    "Así que, ¿Por qué te quedarías a pensar si quedarte o no?"
    scene black
    with fade

    # Transición: Pantalla negra
    # Texto en pantalla / Ilustraciones: "1 Mes después"
    jump act2

### ACTO 2 ###

label act2:
    # Pantalla: Habitación del niño (con dibujos y juguetes)
    "La mañana se siente fresca"
    "El invierno azota fuera y no por eso se cuela en tu ventana"
    "De saber que estarías aquí hace más de un mes..."
    "No te lo creerías"
    r "Pequeño granuja, es hora de que te levantes"
    menu:
        "5 minutos más...":
            r "Sabes queeeee no"
            r "Venga, vamos para que puedas desayunar"
        "¡Cállate, sirviente!":
            $ sospecha += 1
            r "Ahg... la señora Yaga sí que le enseña malos modales"
            r "Me gustabas más antes de ser tan atrevido"
            r "No es una pregunta. Ven, chico..."

    # Transición: Comedor
    y "Miren nada más, como está el muchacho"
    y "Te ves mejor con ropa de hombrecito bien portado"
    y "¿Cómo amaneciste?"
    menu:
        "¡Genial, como Odiseo en la isla de Circe!":
            y "¡Ah, has leído libros!"
            y "Buen niño. Mereces un aplauso"
        "Habría dormido mejor si el sirviente fuera más educado":
            $ sospecha += 1
            r "Perooo... solo hiceeee... mi trabajo"  
            y "Bueno, ese trabajo no es suficiente"
            y "Como siempre, siendo torpe. ¡Ten más educación!"

    y "En fin, chico"
    y "Desayuna bien..."
    y "Yo hoy no estaré para acompañarte. Y, no, no porque “ya comí antes que tú”"
    y "En realidad, me tengo que marchar un rato. Una señora como yo debe ir a la Iglesia por lo menos una vez al mes, ¿sabes?"
    y "Cuando regrese, bueno, espero verte en la Cena"
    y "Y que ahí, me digas qué quieres hacer con tu vida"
    y "Te apoyaré en lo que decidas"
    "Sus palabras te llegan"
    "Hace tiempo que te empiezan a convencer, de verdad..."
    "Así que, decides pedirle otro abrazo"
    y "¡Oh, ¿en serio?"
    y "Jojojojo"
    y "¡No paras de darme abrazos, chaval!"
    y "Eres adicto a los abrazos de tu yaya, ¿cómo negarme?"
    "Los dos se abrazan"
    "El cómo se aferra tí, el cómo te tapa con su tela..."
    "Se siente auténtico"
    y "Listo. Con este cariño dado, tu Yaga se despide, [name]"
    y "Tú, sirviente, más te vale empezar con la preparación de la cena"
    r "Como ordene..."
    y "Bien, bien. ¡Chaito, mi niño!"

    # Transición: Cuarto del niño
    "Tras comer, te retiras a tu habitación"
    "Todas estas cosas... TUS cosas están aquí"
    "Nunca creíste que las tendrías"
    "Y, sin duda..."
    "Quisieras que en realidad sí fueran tuyas"
    "Así que, hoy, después de tantos intentos, podrás confirmar que así es"
    "Tras tantos abrazos, te hiciste por fin con la llave de su cuarto"
    "La prueba definitiva para todo"
    "Que sea lo que Dios quiera..."
    "Aquí es"
    "No sabes si esto es justo para ella..."
    "Pero sí es justo para tí"

    # Transición: Cuarto de Baba Yaga / Caldero
    "¿Así que esto es su cuarto?"
    "Jurarías que no... no pinta con su apariencia"

label yaga_diary:
    $ diario_leido = True
    "Esto... parece un Diario"
    "Por suerte, has mejorado en leer"
    "Entrada, nombre del niño: [name]"
    "Ya ha pasado casi un mes"
    "Estamos cerca de la fecha. Es horrible. Pero el destino es inevitable"
    "Puedes tratar de desafiarlo todo lo que quieras, solo harás que sea más creativo a la hora de llevarte donde quiere"
    "Recuerdo todavía lo que vi ese día en el Caldero..."
    "Era un triste. Muy triste. Un niño sin amor que ni pudo aceptarlo"
    "¿Por qué Dios permitiría algo así? ¿Por qué dejaría que fuese una opción?"
    "No me importa. El destino es inevitable... siempre que siga con vida"
    "Así que..."
    "Ya toca ponerlo a dormir"
    "Baba Roga hará la mejor cena de su vida. Con Cianuro de Potasio mezclado con el calor de la sopa"
    "Solo es posible cambiar el desenlace antes de que llegue. El desarrollo igualmente puede ser distinto"
    "Si eso es lo que necesito para que él pueda ser feliz en su final, que así sea"
    "Iré a orar hasta que sea la hora... aunque ese idiota en el cielo sea injusto, veremos si se ablanda un poco con él en el más allá"

    # Transición: Sala / Niño arrodillado
    "¿...Por qué...?"
    "¿Por qué?"
    "¿¡Por qué!?"
    "¿Por qué? ¿Por qué? ¿Por qué? ¿Por qué? ¿Por qué? ¿Por qué? ¿Por qué?"
    "...Necesitas escapar de aquí"

    # Textos de pistas e interacciones de la fase de resolución
    "..."
    "A lo mejor no es buena idea salir del cuarto todavía. Pueden haber pistas"

    menu clues:
        "Revisar más el diario":
            "Pasas página tras página, pero no encuentras nada de interés ahí"
            jump clues
        "Ver hojas sueltas":
            "Agarras unas hojas que estaban fuera del diario..."
            "..."
            "'Como el niño lleva un buen tiempo merodeando los alrededores, esconderé las llaves mejor. La principal la dejaré en el lugar habitual'"
            "'La de los Invitados se la dejaré al idiota de Roga. Mientras que la copia de la llave de Roga estará en su “creativa trampa” del huevo.'" 
            "'No sé qué manía tiene por intentar crear cosas tan estúpidas como esas. Pero espero que sea lo bastante seguro como él presume'"
            "..."
            "Ya has visto suficiente. Es mejor irse ahora"
            jump where

### ACTO 3: CUARTOS DE INVITADOS Y FINAL ###

label act3:
    menu:
        "Cuarto de Invitados 1":
            jump guest_room_1
        "Cuarto de Invitados 2":
            jump guest_room_2
        "Cuarto de Invitados 3":
            jump guest_room_3
        "Cuarto de Invitados 4":
            jump guest_room_4
        "Cuarto de Invitados 5":
            jump guest_room_5
        "Regresar" if visita_cuarto_3:
            jump escape_attempt

label guest_room_1:
    "El cuarto estaba cerrado, pero no hay polvo acumulado. Alguien cuidaba con esmero esta habitación"
    "Ves una nota, ¿La lees?"
    menu:
        "Sí":
            "<Poko a poko aprendo a escribir. Baba Yama me dió muchas clases estos dias. Aprendo rápidoooo>"
            "<Eso la pone triste. No lo entiendo, pero tampoko está en desacuerdo con que aprenda>"
            "<Ya puedo leer libros. Descubro mucxo del mundo>"
            "<Algún día espero viajar... tal vez con la Abuela Yaga>"
            "Hay una anotación debajo de este párrafo..."
            "<Lo siento, Lucy. No podré viajar contigo>"
        "No":
            pass
    jump act3

label guest_room_2:
    "El cuarto estaba cerrado, pero no hay polvo acumulado. Alguien cuidaba con esmero esta habitación"
    "Ves una nota, ¿La lees?"
    menu:
        "Sí":
            "<Ufff... con el frío que hace fuera, estoy feliz de estar aquí dentro>"
            "<En la calle, habría muerto de frío. Es muy común en esta zona>"
            "<Mi hermano Joseff pereció... cuanto lo extraño>"
            "<Juro por él aprovechar esta oportunidad que me dió la señora Yaga. Me quedaré con ella para servirle. Es lo menos que puedo hacer>"
        "No":
            pass
    jump act3

label guest_room_3:
    "El cuarto estaba cerrado, pero no hay polvo acumulado. Alguien cuidaba con esmero esta habitación"
    "Ves una nota, ¿La lees?"
    menu:
        "Sí":
            "La escritura es errática. Fue hecha con prisa"
            "<No puedo creerlo. No puedo creerlo. ¡No puedo!>"
            "<Me han mentido, ¡ellos...! ¡Ellos! ¡Son unos monstruos!>"
            "<El otro día, entré al cuarto de esa bruja. Tenía la puerta abierta>"
            "<Pensaba que cocinaba en su cuarto o algo así. Me dió risa y quise probar qué platillo hacía...>"
            "<¡Pero en eso, vi huesos flotando!>"
            "<¡Huesos humanos!>"
            "<No podía dudar una vez vi flotar una calavera...>"
            "<Tengo que irme. ¡Ahora! Por suerte, la vi una vez esconder la copia de la llave principal...>"
            "<¡Esta en la cabeza del alce! ¡ya decía yo! Siempre me dió la sensación de burlarse en mi cara...>"
            "Hay una anotación debajo de esa última línea..."
            "<Estuviste cerca, hijo. Dolorosamente cerca...>"
            "<Debería destruir esta hoja, ¿pero eso no sería destruir tus esfuerzos?>"
            "<Merezco recordar cada tanto cómo soy un monstruo para ellos>"
            "<Ser un monstruo es mejor que ser indiferente, ¿no lo crees, Dios?>"
            $ visita_cuarto_3 = True
        "No":
            pass
    jump act3

label guest_room_4:
    "El cuarto estaba cerrado, pero no hay polvo acumulado. Alguien cuidaba con esmero esta habitación"
    "Ves una nota, ¿La lees?"
    menu:
        "Sí":
            "<Si el destino es justo, ¿ellos seguirían aquí?>"
            "¿Yo seguiría aquí?"
            "Me lo pregunto siempre. Cada segundo del día"
            "Y si el destino fuese justo... ¿mi hijo estaría aquí?"
            "¿me estará esperando en el más allá para juzgarme?"
            "No... no quiero averiguarlo>"
        "No":
            pass
    jump act3

label guest_room_5:
    "El cuarto estaba cerrado, pero no hay polvo acumulado. Alguien cuidaba con esmero esta habitación"
    "Ves una nota, ¿La lees?"
    menu:
        "Sí":
            "<Hoy he visto al viejo Roga llorar>"
            "<Fue cuando estaba en ese armario del Comedor. Escuché a la abue Yaga y al anciano Roga acercarse>"
            "<Él le exigía libertad. Entre lágrimas, rogaba y pedía perdón por asesinarlo>"
            "<No entendía a quién mató. Me asustó muchísimo...>"
            "<Solo sé que Yaga le dijo que no había vuelta atrás. Que él quiso ser inmortal y, por ende, obtuvo inmortalidad>"
            "<Se me hizo muy confuso. ¿Por qué Roga mató a alguien? ¿Por qué Yaga dijo que era inmortal?>"
            "El escrito tiene una anotación en un costado..."
            "<Me da igual si lees esto, Yaga>"
            "<Quiero que sepas que te odio. Más de lo que me odio a mí mismo>"
            "<Sí. Lloro y lloro. ¿Y qué?>"
            "<Tu hijo se quedará muerto>"
        "No":
            pass
    jump act3

label escape_attempt:
    $ tiene_llave_alce = True
    "Decides regresar a la entrada para ver la cabeza de alce"
    "La toqueteas, la mueves..."
    # Cabeza de alce caída
    "..."
    "Agarras la llave escondida"
    "Ya puedes salir de aquí"
    "Te giras. Te centras en girar la perilla..."
    "Entonces, cuando por fin abres la puerta..."

    y "Oh... Así que aquí estabas"

    # Transición: Golpe en la cabeza / Pantalla oscura
    # Sonido: Golpe seco, ruido de interferencia, sonido burbujeante de sopa
    # Escena: Atado encima del caldero con Yaga delante

    y "...."
    y "......"
    y "..... ¿Me odias, no?"
    y "Es comprensible..."
    y "Al final, todos los niños me odian..."
    y "Ya sea en esta vida, o en la futura"
    y "Porque no puedo salvarles del Destino..."
    y "Chico, no sé si tú lo entiendes o no. Eres listo, muy listo. Eres el único que ha llegado a estas alturas de escapar..."
    y "..."
    y "Tú no debiste llegar aquí. A esta Mansión"
    y "Veo el futuro. Sé cuál era tu destino si seguías en las calles"
    y "La Muerte, chico. La Muerte"
    y "Una vez te marca, es inevitable. Una sombra que te acompaña con más consciencia una vez sabes que se aproxima"
    y "Por eso, si no puedes escapar de ella... lo mejor es morir de una mejor manera"
    y "Créeme, [name], es mejor de lo que piensas"
    y "Hace mucho, mucho, mucho tiempo, intenté cambiar el destino de un pequeño..."
    y "No funcionó. Terminó pereciendo."
    y "Porque una vez la muerte enlista una fecha, no se la salta. Las formas cambian, pero no el resultado. Por eso, no vale la pena luchar contra el resultado, sino con las causas"
    y "Tú, ¿me culpas?"

    menu:
        "Sí. Eres horrible.":
            y "Lo entiendo. Duele, pero lo entiendo"
            y "Sin embargo, sigue siendo por tu bien. Lo lamento tanto. Odíame de ser necesario, si eso ayuda"

        "No, pero sigue estando mal.":
            $ duda += 1
            y "..."
            y "Ya veo..."
            y "Es un poco patético, para una mujer como yo, que quiera hablar contigo antes de que fallezcas. Lamento molestarte con palabrerías vacías"

    if roga_vivo:
        y "Cabe decirte que, en cualquier caso, hiciste un buen trabajo..."
        y "Encerraste a Roga en su cuarto, por lo que vale la pena que se quede ahí castigado"
        y "Al final, no sirve ni para aliviar el dolor ni para controlarlo, ¿eh?"
    else:
        y "Si te sirve de consuelo, Roga se merecía su final. Tú hiciste lo que debiste. Él no era más que un pecador pagando su deuda"
        y "Así que, no llores, [name]. No merecía tus lágrimas."
        y "En eso, él y yo nos parecemos"

    y "En breve, el humo del caldero te hará olvidar todo lo que has descubierto ahora. Volverás a ser feliz. Ignorante de tu propio destino"
    y "Lo siento mucho..."

    # Sonido de llamas
    y "¿Ese ruido de dónde...?"
    y "Un momento... también huele a..."
    y "¡ESE IDIOTAAAAAAA!"

    # Yaga se va
    "Se está quemando algo. Debe ser por la cocina de Roga"
    "Es tu oportunidad de escapar... ¿Pero de verdad quieres escapar? Si te espera un destino horrible de por sí, ¿ser ignorante y fallecer por otras causas no es mejor?"

    menu:
        "Quedarse":
            jump ending_stay

        "Intentar liberarse":
            jump escape_choice


label ending_stay:
    "En vez de soltarte, hueles a profundidad"
    "Dejas que la mentira siga, que los colores sigan... porque la felicidad que tienes ahora es lo único en lo que puedes confiar"
    "Al final, esto ha sido lo que más te ha ayudado a no sentirte insignificante"

    # Transición a oscuridad / Música melancólica
    # Imagen del niño sonriendo sin vida en la cama, Yaga a su lado triste

    y "Adiós, mi dulce [name]. Te recordaré por siempre..."
    # FIN
    return


label escape_choice:
    "Forcejeas. No eres tan débil como antes de venir a este lugar..."
    "Sientes las cuerdas ceder... hasta que por fin consigues caer torpemente encima del caldero. Usas tus piernas para no acabar dentro y te mueves a un costado"
    "Necesitas recuperar la llave, a cualquier costo"
    "La anciana la debe tener. ¿Vas como estás, o robas un cuchillo de la mesa?"

    menu:
        "Llevar cuchillo":
            $ tiene_cuchillo = True
            "Que sea lo que Dios quiera"

        "Confrontarla como estás":
            $ tiene_cuchillo = False

    # Transición: Cocina con fuego
    "Yaga está de espaldas mientras intenta apagar el fuego"

    if tiene_cuchillo:
        "Es tu oportunidad"
        menu:
            "¿La Apuñalas?":
                jump stab_yaga
            "La amenazas":
                jump threaten_yaga
    else:
        jump threaten_yaga


label stab_yaga:
    "Te acercas sin dejarte notar..."
    "Injertas la cuchilla entre sus vertebras. Ella chilla de dolor"

    y "AAAAAAAAAAAAAAAAAAAA"
    y "¿Qu-qué? ¡Tú... tú!... ¿Cómo...?"

    if duda == 0:
        y ".... hk... hk"
        y "... ja.... ja..."
        y "S-supongo que da igual... el cómo, ¿no?"
        y "... Estás aquí... estás aquí... yo..."
        y "Dios... así que... aquí termina todo..."
        y "Merecía esto... lo merecía"
        y "... jo..."
        y "Sé que lo merezco, pero... ¿Por qué...?"
        y "¿Por qué tengo tanto miedo?"
        y "......."
        y "Ja..."
        y "Nunca pude confiar en ayudarte... igual que tú nunca pudiste confiarme tu verdadero nombre..."
        y ".... [name], ¿puedes decirme tu verdadero nombre?"
        y "...."
        y "¿Malen?"
        y "..... Es... un bonito nombre..."
    else:
        y "¿Por... qué?"
        y "Pensaba que tú... en el fondo... me querías..."
        y "Tú... tú..."
        y "Al final... sí que te volviste tan cruel cómo yo..."
        y ".... de verdad... que no sirvo como madre..."
        y "Ni siquiera pudiste... decirme tu verdadero nombre, ¿no, [name]?"
        y "¿Qué...? ¿Me dirás tu verdadero nombre?"
        y "..."
        y "¿Malen?"
        y "...... no sé si te sienta bien... o terriblemente mal..."

    # Yaga cae muerta
    # FINAL: MATASTE TU MENTIRA
    return


label threaten_yaga:
    # Continuación según las ramas finales del script cuando no se le apuñala directamente
    return