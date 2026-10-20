#!/usr/bin/env python3
"""
Erzeugt die Startseite in allen Sprachen und die übersetzten Datenschutzerklärungen.

    python3 tools/build.py

Texte werden nur hier geändert, nicht in den erzeugten HTML-Dateien.
Deutsche Datenschutzerklärung (datenschutz.html) und Impressum (impressum.html)
sind von Hand gepflegt und gelten als massgebende Fassung.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMAIL = 'kontakt@frauenkompass.ch'
LANGS = ['de', 'en', 'pt', 'es', 'fr']

T = {
'de': dict(
  title='Frauenkompass · im Aufbau',
  desc='Frauenkompass. Rund um die Wechseljahre. Ein neues Projekt von Sara Casellini-Machado Sousa, Fachärztin für Gynäkologie und Geburtshilfe in Liechtenstein. Die Seite ist im Aufbau.',
  lang_label='Sprache',
  h1='Gut informiert durch die Wechseljahre',
  lede='Von der Perimenopause bis in die Zeit nach der Menopause. Klar, ehrlich, ärztlich begleitet.',
  body='Hier entsteht gerade etwas Neues. Die Seite ist noch im Aufbau, die Inhalte wachsen Schritt für Schritt. Wenn du wissen möchtest, wann es losgeht, trag dich unten ein.',
  news_h='Bescheid bekommen, wenn es losgeht',
  news_p='Ein kurzes Mail, wenn die Seite steht und wenn es Neues gibt. Selten, ruhig, ohne Werbung. Abmelden geht jederzeit mit einem Klick.',
  f_name='Vorname', f_opt='(optional)', f_email='E-Mail', f_hp='Bitte leer lassen',
  f_consent='Ich möchte News von Frauenkompass per E-Mail erhalten. Die Einwilligung kann ich jederzeit widerrufen. Mehr dazu in der <a href="{privacy}">Datenschutzerklärung</a>.',
  f_btn='Anmelden',
  role='Fachärztin für Gynäkologie und Geburtshilfe',
  bio_h='Über mich',
  bio=[
    'Geboren bin ich in Lissabon, aufgewachsen in Basel. Dort habe ich auch Medizin studiert. Danach ging es in die Ostschweiz: In Grabs und Chur habe ich mich zur Fachärztin für Gynäkologie und Geburtshilfe ausgebildet, zuletzt als Oberärztin. Heute lebe ich mit meinem Mann und unseren zwei Kindern in Liechtenstein. Seit 2023 arbeite ich in der Praxis Gynorina in Buchs SG.',
    'Die Wechseljahre beginnen oft Jahre vor der letzten Periode und wirken lange danach weiter. In der Sprechstunde fehlt meist die Zeit für die Fragen, die Frauen in dieser Phase wirklich beschäftigen. Manche werden gar nicht erst gestellt. Frauenkompass soll dafür Raum schaffen: verständlich erklärt, fachlich fundiert, ohne Panik und ohne Floskeln.',
    'Ich spreche Deutsch, Portugiesisch, Englisch, Spanisch und Französisch.',
  ],
  cv=[
    ('2014', 'Abschluss Humanmedizin, Universität Basel'),
    ('2015–2019', 'Assistenzärztin, Frauenkliniken Spital Grabs und Kantonsspital Graubünden'),
    ('2019–2022', 'Oberärztin, Frauenklinik Spital Grabs'),
    ('2022', 'Facharzttitel Gynäkologie und Geburtshilfe'),
    ('Seit Feb. 2023', 'Fachärztin, Praxis Gynorina, Buchs SG'),
    ('Weiterbildung', 'Fähigkeitsausweis Schwangerschaftsultraschall'),
  ],
  quote='«Keine Frage ist zu klein. Und keine zu persönlich.»',
  imprint='Impressum', privacy='Datenschutz',
  js=dict(
    bad_email='Bitte eine gültige E-Mail-Adresse eingeben.',
    no_consent='Bitte die Einwilligung bestätigen.',
    mail_subject='News-Anmeldung',
    mail_body='Bitte nehmt mich in die News-Liste auf.',
    mail_name='Vorname',
    mail_open='Dein Mailprogramm öffnet sich. Einfach absenden, fertig.',
    thanks='Danke. Bitte bestätige die Anmeldung über den Link im Mail, das wir dir gerade geschickt haben.',
    error='Das hat nicht geklappt. Bitte später nochmals versuchen.',
  ),
),
'en': dict(
  title='Frauenkompass · coming soon',
  desc='Frauenkompass. All about menopause. A new project by Sara Casellini-Machado Sousa, specialist in gynaecology and obstetrics in Liechtenstein. This site is under construction.',
  lang_label='Language',
  h1='Well informed through menopause',
  lede='From perimenopause to the years after menopause. Clear, honest, with a doctor at your side.',
  body='Something new is taking shape here. The site is still under construction and the content will grow step by step. If you would like to know when it launches, sign up below.',
  news_h='Get notified when we launch',
  news_p='A short email when the site is ready and when there is news. Rarely, calmly, no advertising. You can unsubscribe at any time with one click.',
  f_name='First name', f_opt='(optional)', f_email='Email', f_hp='Please leave empty',
  f_consent='I would like to receive news from Frauenkompass by email. I can withdraw my consent at any time. More in the <a href="{privacy}">privacy policy</a>.',
  f_btn='Sign up',
  role='Specialist in gynaecology and obstetrics',
  bio_h='About me',
  bio=[
    'I was born in Lisbon and grew up in Basel, where I also studied medicine. I then moved to eastern Switzerland and trained as a specialist in gynaecology and obstetrics in Grabs and Chur, most recently as a senior physician. Today I live in Liechtenstein with my husband and our two children. Since 2023 I have been working at the Gynorina practice in Buchs, Switzerland.',
    'Menopause often begins years before the last period and its effects continue long after. In a regular consultation there is rarely enough time for the questions women really have during this phase. Some never get asked at all. Frauenkompass is meant to make room for them: clearly explained, medically sound, without alarm and without empty phrases.',
    'I speak German, Portuguese, English, Spanish and French.',
  ],
  cv=[
    ('2014', 'Degree in human medicine, University of Basel'),
    ('2015–2019', 'Resident physician, women’s clinics at Grabs Hospital and Cantonal Hospital of Graubünden'),
    ('2019–2022', 'Senior physician, women’s clinic, Grabs Hospital'),
    ('2022', 'Specialist title in gynaecology and obstetrics'),
    ('Since Feb. 2023', 'Specialist, Gynorina practice, Buchs SG'),
    ('Further training', 'Certificate in obstetric ultrasound'),
  ],
  quote='“No question is too small. And none too personal.”',
  imprint='Legal notice', privacy='Privacy',
  js=dict(
    bad_email='Please enter a valid email address.',
    no_consent='Please confirm your consent.',
    mail_subject='Newsletter sign-up',
    mail_body='Please add me to the news list.',
    mail_name='First name',
    mail_open='Your email app is opening. Just send the message.',
    thanks='Thank you. Please confirm your sign-up using the link in the email we just sent you.',
    error='Something went wrong. Please try again later.',
  ),
),
'pt': dict(
  title='Frauenkompass · em construção',
  desc='Frauenkompass. Tudo sobre a menopausa. Um novo projeto de Sara Casellini-Machado Sousa, médica especialista em ginecologia e obstetrícia no Liechtenstein. O site está em construção.',
  lang_label='Idioma',
  h1='Bem informada ao longo da menopausa',
  lede='Da perimenopausa aos anos depois da menopausa. Com clareza, honestidade e acompanhamento médico.',
  body='Está a nascer aqui algo novo. O site ainda está em construção e os conteúdos vão crescendo passo a passo. Se quiseres saber quando arranca, inscreve-te abaixo.',
  news_h='Recebe um aviso quando arrancarmos',
  news_p='Um e-mail curto quando o site estiver pronto e quando houver novidades. Raramente, com calma, sem publicidade. Podes cancelar a qualquer momento com um clique.',
  f_name='Nome próprio', f_opt='(opcional)', f_email='E-mail', f_hp='Deixar em branco',
  f_consent='Quero receber novidades do Frauenkompass por e-mail. Posso retirar o meu consentimento a qualquer momento. Mais informações na <a href="{privacy}">política de privacidade</a>.',
  f_btn='Inscrever-me',
  role='Médica especialista em ginecologia e obstetrícia',
  bio_h='Sobre mim',
  bio=[
    'Nasci em Lisboa e cresci em Basileia, onde também estudei medicina. Depois mudei-me para o leste da Suíça e fiz a especialidade em ginecologia e obstetrícia em Grabs e Chur, por último como médica sénior. Hoje vivo no Liechtenstein com o meu marido e os nossos dois filhos. Desde 2023 trabalho no consultório Gynorina, em Buchs, na Suíça.',
    'A menopausa começa muitas vezes anos antes da última menstruação e os seus efeitos continuam muito depois. Numa consulta normal raramente há tempo para as perguntas que realmente preocupam as mulheres nesta fase. Algumas nem chegam a ser feitas. O Frauenkompass quer dar-lhes espaço: explicações claras, com base científica, sem alarmismo e sem frases feitas.',
    'Falo alemão, português, inglês, espanhol e francês.',
  ],
  cv=[
    ('2014', 'Licenciatura em Medicina, Universidade de Basileia'),
    ('2015–2019', 'Médica interna, serviços de ginecologia e obstetrícia do Hospital de Grabs e do Hospital Cantonal dos Grisões'),
    ('2019–2022', 'Médica sénior, serviço de ginecologia e obstetrícia, Hospital de Grabs'),
    ('2022', 'Título de especialista em ginecologia e obstetrícia'),
    ('Desde fev. 2023', 'Médica especialista, consultório Gynorina, Buchs SG'),
    ('Formação complementar', 'Certificado em ecografia obstétrica'),
  ],
  quote='«Nenhuma pergunta é pequena demais. Nem pessoal demais.»',
  imprint='Informação legal', privacy='Privacidade',
  js=dict(
    bad_email='Introduz um endereço de e-mail válido.',
    no_consent='Confirma o teu consentimento.',
    mail_subject='Inscrição nas novidades',
    mail_body='Por favor, incluam-me na lista de novidades.',
    mail_name='Nome próprio',
    mail_open='O teu programa de e-mail vai abrir. Basta enviar.',
    thanks='Obrigada. Confirma a inscrição através do link no e-mail que te acabámos de enviar.',
    error='Algo correu mal. Tenta novamente mais tarde.',
  ),
),
'es': dict(
  title='Frauenkompass · en construcción',
  desc='Frauenkompass. Todo sobre la menopausia. Un nuevo proyecto de Sara Casellini-Machado Sousa, especialista en ginecología y obstetricia en Liechtenstein. El sitio está en construcción.',
  lang_label='Idioma',
  h1='Bien informada durante la menopausia',
  lede='Desde la perimenopausia hasta los años después de la menopausia. Con claridad, honestidad y acompañamiento médico.',
  body='Aquí está naciendo algo nuevo. El sitio todavía está en construcción y los contenidos irán creciendo poco a poco. Si quieres saber cuándo empieza, apúntate abajo.',
  news_h='Recibe un aviso cuando empecemos',
  news_p='Un correo breve cuando el sitio esté listo y cuando haya novedades. Pocas veces, con calma, sin publicidad. Puedes darte de baja en cualquier momento con un clic.',
  f_name='Nombre', f_opt='(opcional)', f_email='Correo electrónico', f_hp='Dejar vacío',
  f_consent='Quiero recibir novedades de Frauenkompass por correo electrónico. Puedo retirar mi consentimiento en cualquier momento. Más información en la <a href="{privacy}">política de privacidad</a>.',
  f_btn='Apuntarme',
  role='Especialista en ginecología y obstetricia',
  bio_h='Sobre mí',
  bio=[
    'Nací en Lisboa y crecí en Basilea, donde también estudié medicina. Después me trasladé al este de Suiza y me formé como especialista en ginecología y obstetricia en Grabs y Chur, al final como médica adjunta. Hoy vivo en Liechtenstein con mi marido y nuestros dos hijos. Desde 2023 trabajo en la consulta Gynorina, en Buchs, Suiza.',
    'La menopausia suele empezar años antes de la última regla y sus efectos continúan mucho después. En una consulta normal casi nunca hay tiempo para las preguntas que de verdad preocupan a las mujeres en esta etapa. Algunas ni siquiera se llegan a hacer. Frauenkompass quiere darles espacio: explicaciones claras, con base médica, sin alarmismo y sin frases hechas.',
    'Hablo alemán, portugués, inglés, español y francés.',
  ],
  cv=[
    ('2014', 'Licenciatura en Medicina, Universidad de Basilea'),
    ('2015–2019', 'Médica residente, clínicas de la mujer del Hospital de Grabs y del Hospital Cantonal de los Grisones'),
    ('2019–2022', 'Médica adjunta, clínica de la mujer, Hospital de Grabs'),
    ('2022', 'Título de especialista en ginecología y obstetricia'),
    ('Desde feb. 2023', 'Especialista, consulta Gynorina, Buchs SG'),
    ('Formación continua', 'Certificado en ecografía obstétrica'),
  ],
  quote='«Ninguna pregunta es demasiado pequeña. Ni demasiado personal.»',
  imprint='Aviso legal', privacy='Privacidad',
  js=dict(
    bad_email='Introduce una dirección de correo válida.',
    no_consent='Confirma tu consentimiento.',
    mail_subject='Suscripción a las novedades',
    mail_body='Por favor, añadidme a la lista de novedades.',
    mail_name='Nombre',
    mail_open='Se abrirá tu programa de correo. Solo tienes que enviarlo.',
    thanks='Gracias. Confirma la suscripción con el enlace del correo que te acabamos de enviar.',
    error='Algo ha fallado. Inténtalo de nuevo más tarde.',
  ),
),
'fr': dict(
  title='Frauenkompass · en construction',
  desc='Frauenkompass. Tout sur la ménopause. Un nouveau projet de Sara Casellini-Machado Sousa, médecin spécialiste en gynécologie et obstétrique au Liechtenstein. Le site est en construction.',
  lang_label='Langue',
  h1='Bien informée tout au long de la ménopause',
  lede='De la périménopause aux années qui suivent la ménopause. Clair, honnête, avec un accompagnement médical.',
  body='Quelque chose de nouveau se prépare ici. Le site est encore en construction et son contenu s’étoffera pas à pas. Si vous souhaitez savoir quand il sera lancé, inscrivez-vous ci-dessous.',
  news_h='Être prévenue du lancement',
  news_p='Un court e-mail lorsque le site sera prêt et lorsqu’il y aura du nouveau. Rarement, sans bruit, sans publicité. Désinscription possible à tout moment en un clic.',
  f_name='Prénom', f_opt='(facultatif)', f_email='E-mail', f_hp='Merci de laisser vide',
  f_consent='Je souhaite recevoir les nouvelles de Frauenkompass par e-mail. Je peux retirer mon consentement à tout moment. Plus d’informations dans la <a href="{privacy}">politique de confidentialité</a>.',
  f_btn='M’inscrire',
  role='Médecin spécialiste en gynécologie et obstétrique',
  bio_h='À propos',
  bio=[
    'Je suis née à Lisbonne et j’ai grandi à Bâle, où j’ai aussi fait mes études de médecine. J’ai ensuite rejoint l’est de la Suisse et me suis formée en gynécologie et obstétrique à Grabs et à Coire, en dernier lieu comme cheffe de clinique. Aujourd’hui, je vis au Liechtenstein avec mon mari et nos deux enfants. Depuis 2023, je travaille au cabinet Gynorina à Buchs, en Suisse.',
    'La ménopause commence souvent des années avant les dernières règles et ses effets se prolongent bien après. En consultation, le temps manque généralement pour les questions qui préoccupent vraiment les femmes à cette période. Certaines ne sont même jamais posées. Frauenkompass veut leur faire de la place : des explications claires, médicalement fondées, sans alarmisme et sans formules toutes faites.',
    'Je parle allemand, portugais, anglais, espagnol et français.',
  ],
  cv=[
    ('2014', 'Diplôme de médecine humaine, Université de Bâle'),
    ('2015–2019', 'Médecin assistante, cliniques gynécologiques de l’hôpital de Grabs et de l’hôpital cantonal des Grisons'),
    ('2019–2022', 'Cheffe de clinique, clinique gynécologique, hôpital de Grabs'),
    ('2022', 'Titre de spécialiste en gynécologie et obstétrique'),
    ('Depuis fév. 2023', 'Médecin spécialiste, cabinet Gynorina, Buchs SG'),
    ('Formation continue', 'Attestation de formation en échographie obstétricale'),
  ],
  quote='« Aucune question n’est trop petite. Ni trop personnelle. »',
  imprint='Mentions légales', privacy='Confidentialité',
  js=dict(
    bad_email='Veuillez saisir une adresse e-mail valide.',
    no_consent='Veuillez confirmer votre consentement.',
    mail_subject='Inscription aux nouvelles',
    mail_body='Merci de m’ajouter à la liste des nouvelles.',
    mail_name='Prénom',
    mail_open='Votre messagerie s’ouvre. Il suffit d’envoyer le message.',
    thanks='Merci. Veuillez confirmer votre inscription via le lien de l’e-mail que nous venons de vous envoyer.',
    error='Une erreur s’est produite. Veuillez réessayer plus tard.',
  ),
),
}

# Übersetzte Datenschutzerklärungen. Massgebend ist die deutsche Fassung.
P = {
'en': dict(
  title='Privacy policy', h1='Privacy policy', stand='Last updated: October 2026',
  binding='This is a translation. In case of doubt, the <a href="../datenschutz.html">German version</a> applies.',
  intro=['This website is still under construction. It collects as little data as possible. This page explains which data that is, what it is used for and what rights you have.',
         'The applicable law is the EU General Data Protection Regulation (GDPR), which applies in Liechtenstein through the EEA Agreement, and the Liechtenstein Data Protection Act (DSG).'],
  s=[
    ('1. Controller', ['@controller', 'CM Ventures Anstalt operates this website on an interim basis while the project is being set up. If a separate operating entity is established, we will update this information.']),
    ('2. Visiting the website', ['When you visit the site, our hosting provider processes technically necessary data: IP address, date and time, page requested, browser and operating system. This is needed to deliver the site and to protect it from misuse (legitimate interest, Art. 6(1)(f) GDPR). These server logs are deleted automatically after a short time.',
                                'Hosting provider: NEXEUM Digital Services GmbH, Vaduz, Liechtenstein. A data processing agreement is in place with the provider. If data is transferred to a country outside the EEA, this is done on the basis of an adequacy decision or the European Commission’s standard contractual clauses.']),
    ('3. No cookies, no tracking', ['This website does not set cookies, does not use analytics or advertising services and does not embed social media plugins. The fonts are hosted locally, so no data is sent to Google or other font providers.']),
    ('4. News by email', ['If you sign up for news, we process your email address, optionally your first name, and the time of sign-up and confirmation. We use this data only to send you news about Frauenkompass.',
                          'The legal basis is your consent (Art. 6(1)(a) GDPR). Sign-up uses double opt-in: you first receive an email with a confirmation link. You are only added after clicking it.',
                          'You can withdraw your consent at any time via the unsubscribe link in every email or by sending us a short message. We then delete your data. To make sure we send you nothing after you unsubscribe, your email address may remain on a suppression list.',
                          'For sending we use <span class="todo">[name and location of the newsletter service]</span> as a data processor. Until this service is set up, sign-up takes place by email to the address above, and the details are added to the list by hand.']),
    ('5. Contact by email', ['If you write to us, we process your details to answer your enquiry (Art. 6(1)(b) and (f) GDPR). We delete messages once they have been dealt with and no retention obligation applies.',
                             '<strong>Important:</strong> No medical advice is given through this website or by email. Please do not send us any health data, findings or images. Normal emails are not end-to-end encrypted.']),
    ('6. Disclosure', ['We do not sell data and do not pass it on to third parties. Exceptions are the processors named above and legal obligations.']),
    ('7. Your rights', ['You have the right to:', '@rights', 'A short message to @mail is enough.', 'You can also lodge a complaint with the supervisory authority:', '@authority']),
    ('8. Changes', ['The site is still growing. When new features are added, we will update this policy. The current version on this page applies.']),
  ],
  rights=['access to the data we hold about you', 'rectification of inaccurate data', 'erasure or restriction of processing', 'data portability', 'object to processing based on legitimate interests', 'withdraw consent, with effect for the future'],
  email_label='Email', authority='Data Protection Authority Liechtenstein',
),
'pt': dict(
  title='Política de privacidade', h1='Política de privacidade', stand='Atualizada em: outubro de 2026',
  binding='Esta é uma tradução. Em caso de dúvida, prevalece a <a href="../datenschutz.html">versão alemã</a>.',
  intro=['Este site ainda está em construção. Recolhe o mínimo de dados possível. Aqui explicamos que dados são, para que servem e que direitos tens.',
         'Aplicam-se o Regulamento Geral sobre a Proteção de Dados da UE (RGPD), em vigor no Liechtenstein através do Acordo EEE, e a Lei de Proteção de Dados do Liechtenstein (DSG).'],
  s=[
    ('1. Responsável pelo tratamento', ['@controller', 'A CM Ventures Anstalt gere este site de forma provisória enquanto o projeto está em construção. Se for criada uma entidade própria, atualizaremos esta informação.']),
    ('2. Visita ao site', ['Quando visitas o site, o nosso fornecedor de alojamento trata dados tecnicamente necessários: endereço IP, data e hora, página visitada, navegador e sistema operativo. Isto é necessário para disponibilizar o site e protegê-lo contra abusos (interesse legítimo, art. 6.º, n.º 1, alínea f) do RGPD). Estes registos do servidor são apagados automaticamente após pouco tempo.',
                           'Fornecedor de alojamento: NEXEUM Digital Services GmbH, Vaduz, Liechtenstein. Existe um contrato de subcontratação com o fornecedor. Caso haja transferência de dados para um país fora do EEE, esta baseia-se numa decisão de adequação ou nas cláusulas contratuais-tipo da Comissão Europeia.']),
    ('3. Sem cookies, sem rastreamento', ['Este site não utiliza cookies, serviços de análise ou de publicidade, nem plugins de redes sociais. As fontes estão alojadas localmente, pelo que não são enviados dados à Google nem a outros fornecedores de fontes.']),
    ('4. Novidades por e-mail', ['Se te inscreveres nas novidades, tratamos o teu endereço de e-mail, opcionalmente o teu nome próprio, e a data e hora da inscrição e da confirmação. Usamos estes dados apenas para te enviar novidades sobre o Frauenkompass.',
                                 'A base legal é o teu consentimento (art. 6.º, n.º 1, alínea a) do RGPD). A inscrição é feita com dupla confirmação: primeiro recebes um e-mail com um link de confirmação. Só depois de clicares é que ficas inscrita.',
                                 'Podes retirar o consentimento a qualquer momento, através do link de cancelamento em cada e-mail ou com uma breve mensagem para nós. Depois apagamos os teus dados. Para garantirmos que não te enviamos mais nada após o cancelamento, o endereço de e-mail pode ficar numa lista de bloqueio.',
                                 'Para o envio utilizamos <span class="todo">[nome e sede do serviço de newsletter]</span> como subcontratante. Enquanto este serviço não estiver configurado, a inscrição é feita por e-mail para o endereço acima e os dados são adicionados à lista manualmente.']),
    ('5. Contacto por e-mail', ['Se nos escreveres, tratamos os teus dados para responder ao teu pedido (art. 6.º, n.º 1, alíneas b) e f) do RGPD). Apagamos as mensagens depois de tratadas, salvo obrigação legal de conservação.',
                                '<strong>Importante:</strong> Este site e o e-mail não servem para aconselhamento médico. Por favor, não nos envies dados de saúde, resultados de exames ou imagens. Os e-mails normais não são encriptados de ponta a ponta.']),
    ('6. Partilha de dados', ['Não vendemos dados nem os partilhamos com terceiros. As exceções são os subcontratantes acima referidos e obrigações legais.']),
    ('7. Os teus direitos', ['Tens direito a:', '@rights', 'Basta uma breve mensagem para @mail.', 'Podes também apresentar reclamação à autoridade de controlo:', '@authority']),
    ('8. Alterações', ['O site ainda está a crescer. Quando forem acrescentadas novas funções, atualizaremos esta política. Aplica-se sempre a versão atual publicada nesta página.']),
  ],
  rights=['aceder aos dados que guardamos sobre ti', 'retificar dados incorretos', 'apagar dados ou limitar o tratamento', 'portabilidade dos dados', 'opor-te a tratamentos baseados em interesses legítimos', 'retirar o consentimento, com efeitos para o futuro'],
  email_label='E-mail', authority='Autoridade de Proteção de Dados do Liechtenstein',
),
'es': dict(
  title='Política de privacidad', h1='Política de privacidad', stand='Actualizada: octubre de 2026',
  binding='Esta es una traducción. En caso de duda, prevalece la <a href="../datenschutz.html">versión alemana</a>.',
  intro=['Este sitio todavía está en construcción. Recoge los menos datos posibles. Aquí explicamos qué datos son, para qué se usan y qué derechos tienes.',
         'Se aplican el Reglamento General de Protección de Datos de la UE (RGPD), vigente en Liechtenstein a través del Acuerdo EEE, y la Ley de Protección de Datos de Liechtenstein (DSG).'],
  s=[
    ('1. Responsable del tratamiento', ['@controller', 'CM Ventures Anstalt gestiona este sitio de forma provisional mientras el proyecto está en construcción. Si se crea una entidad propia, actualizaremos esta información.']),
    ('2. Visita al sitio web', ['Cuando visitas el sitio, nuestro proveedor de alojamiento trata datos técnicamente necesarios: dirección IP, fecha y hora, página visitada, navegador y sistema operativo. Esto es necesario para mostrar el sitio y protegerlo frente a abusos (interés legítimo, art. 6.1.f RGPD). Estos registros del servidor se eliminan automáticamente al poco tiempo.',
                                'Proveedor de alojamiento: NEXEUM Digital Services GmbH, Vaduz, Liechtenstein. Existe un contrato de encargo del tratamiento con el proveedor. Si se transfieren datos a un país fuera del EEE, se hace sobre la base de una decisión de adecuación o de las cláusulas contractuales tipo de la Comisión Europea.']),
    ('3. Sin cookies, sin seguimiento', ['Este sitio no utiliza cookies, servicios de análisis ni de publicidad, ni plugins de redes sociales. Las fuentes están alojadas localmente, por lo que no se envían datos a Google ni a otros proveedores de fuentes.']),
    ('4. Novedades por correo electrónico', ['Si te apuntas a las novedades, tratamos tu dirección de correo, opcionalmente tu nombre, y la fecha y hora de la suscripción y de la confirmación. Usamos estos datos solo para enviarte novedades sobre Frauenkompass.',
                                            'La base legal es tu consentimiento (art. 6.1.a RGPD). La suscripción utiliza doble confirmación: primero recibes un correo con un enlace de confirmación. Solo después de hacer clic quedas apuntada.',
                                            'Puedes retirar tu consentimiento en cualquier momento, con el enlace de baja de cada correo o con un breve mensaje. Después eliminamos tus datos. Para asegurarnos de no enviarte nada tras la baja, tu dirección puede quedar en una lista de exclusión.',
                                            'Para el envío utilizamos <span class="todo">[nombre y sede del servicio de newsletter]</span> como encargado del tratamiento. Mientras este servicio no esté configurado, la suscripción se hace por correo a la dirección indicada arriba y los datos se añaden a la lista a mano.']),
    ('5. Contacto por correo electrónico', ['Si nos escribes, tratamos tus datos para responder a tu consulta (art. 6.1.b y f RGPD). Eliminamos los mensajes una vez resueltos, salvo obligación legal de conservación.',
                                           '<strong>Importante:</strong> A través de este sitio y por correo no se ofrece asesoramiento médico. Por favor, no nos envíes datos de salud, resultados ni imágenes. Los correos normales no están cifrados de extremo a extremo.']),
    ('6. Comunicación de datos', ['No vendemos datos ni los cedemos a terceros. Las excepciones son los encargados del tratamiento mencionados y las obligaciones legales.']),
    ('7. Tus derechos', ['Tienes derecho a:', '@rights', 'Basta con un breve mensaje a @mail.', 'También puedes presentar una reclamación ante la autoridad de control:', '@authority']),
    ('8. Cambios', ['El sitio todavía está creciendo. Cuando se añadan nuevas funciones, actualizaremos esta política. Se aplica siempre la versión vigente publicada en esta página.']),
  ],
  rights=['acceder a los datos que guardamos sobre ti', 'rectificar datos inexactos', 'suprimir datos o limitar su tratamiento', 'la portabilidad de los datos', 'oponerte a tratamientos basados en intereses legítimos', 'retirar tu consentimiento, con efecto para el futuro'],
  email_label='Correo electrónico', authority='Autoridad de Protección de Datos de Liechtenstein',
),
'fr': dict(
  title='Politique de confidentialité', h1='Politique de confidentialité', stand='Mise à jour : octobre 2026',
  binding='Ceci est une traduction. En cas de doute, la <a href="../datenschutz.html">version allemande</a> fait foi.',
  intro=['Ce site est encore en construction. Il collecte le moins de données possible. Cette page indique lesquelles, à quoi elles servent et quels sont vos droits.',
         'S’appliquent le Règlement général sur la protection des données de l’UE (RGPD), en vigueur au Liechtenstein par l’Accord EEE, ainsi que la loi liechtensteinoise sur la protection des données (DSG).'],
  s=[
    ('1. Responsable du traitement', ['@controller', 'CM Ventures Anstalt exploite ce site à titre provisoire pendant la mise en place du projet. Si une structure propre est créée, nous mettrons cette information à jour.']),
    ('2. Visite du site', ['Lors de votre visite, notre hébergeur traite des données techniquement nécessaires : adresse IP, date et heure, page consultée, navigateur et système d’exploitation. Cela est nécessaire pour afficher le site et le protéger contre les abus (intérêt légitime, art. 6, par. 1, let. f RGPD). Ces journaux serveur sont supprimés automatiquement après une courte durée.',
                           'Hébergeur : NEXEUM Digital Services GmbH, Vaduz, Liechtenstein. Un contrat de sous-traitance a été conclu avec l’hébergeur. Si des données sont transférées vers un pays hors de l’EEE, cela se fait sur la base d’une décision d’adéquation ou des clauses contractuelles types de la Commission européenne.']),
    ('3. Pas de cookies, pas de suivi', ['Ce site ne dépose aucun cookie, n’utilise aucun service d’analyse ou de publicité et n’intègre aucun plugin de réseaux sociaux. Les polices sont hébergées localement : aucune donnée n’est transmise à Google ni à d’autres fournisseurs de polices.']),
    ('4. Nouvelles par e-mail', ['Si vous vous inscrivez aux nouvelles, nous traitons votre adresse e-mail, éventuellement votre prénom, ainsi que la date et l’heure de l’inscription et de la confirmation. Nous utilisons ces données uniquement pour vous envoyer des nouvelles de Frauenkompass.',
                                 'La base légale est votre consentement (art. 6, par. 1, let. a RGPD). L’inscription se fait en double opt-in : vous recevez d’abord un e-mail avec un lien de confirmation. Vous n’êtes inscrite qu’après avoir cliqué dessus.',
                                 'Vous pouvez retirer votre consentement à tout moment, via le lien de désinscription présent dans chaque e-mail ou par un court message. Nous supprimons alors vos données. Pour être sûrs de ne plus rien vous envoyer, votre adresse peut rester sur une liste d’exclusion.',
                                 'Pour l’envoi, nous faisons appel à <span class="todo">[nom et siège du service de newsletter]</span> en tant que sous-traitant. Tant que ce service n’est pas en place, l’inscription se fait par e-mail à l’adresse ci-dessus et les données sont ajoutées manuellement à la liste.']),
    ('5. Contact par e-mail', ['Si vous nous écrivez, nous traitons vos données pour répondre à votre demande (art. 6, par. 1, let. b et f RGPD). Nous supprimons les messages une fois traités, sauf obligation légale de conservation.',
                               '<strong>Important :</strong> ce site et les e-mails ne servent pas à donner des conseils médicaux. Merci de ne pas nous envoyer de données de santé, de résultats d’examens ni d’images. Les e-mails ordinaires ne sont pas chiffrés de bout en bout.']),
    ('6. Transmission', ['Nous ne vendons pas de données et ne les transmettons pas à des tiers. Exceptions : les sous-traitants mentionnés ci-dessus et les obligations légales.']),
    ('7. Vos droits', ['Vous avez le droit :', '@rights', 'Un court message à @mail suffit.', 'Vous pouvez également déposer une plainte auprès de l’autorité de contrôle :', '@authority']),
    ('8. Modifications', ['Le site continue de se développer. Lorsque de nouvelles fonctions s’ajoutent, nous adaptons cette politique. La version en vigueur est celle publiée sur cette page.']),
  ],
  rights=['d’accéder aux données que nous détenons sur vous', 'de faire rectifier des données inexactes', 'de faire effacer vos données ou d’en limiter le traitement', 'à la portabilité des données', 'de vous opposer aux traitements fondés sur l’intérêt légitime', 'de retirer votre consentement, avec effet pour l’avenir'],
  email_label='E-mail', authority='Autorité de protection des données du Liechtenstein',
),
}


def prefix(lang):
    return '' if lang == 'de' else '../'


def home(lang, from_lang):
    p = prefix(from_lang)
    return f'{p}index.html' if lang == 'de' else f'{p}{lang}/index.html'


def privacy_href(lang):
    return 'datenschutz.html' if lang == 'de' else 'privacy.html'


def lang_nav(cur, label, target='home'):
    items = []
    for l in LANGS:
        if target == 'home':
            href = home(l, cur)
        else:
            href = (prefix(cur) + 'datenschutz.html') if l == 'de' else (prefix(cur) + f'{l}/privacy.html' if cur == 'de' else f'../{l}/privacy.html')
        cur_attr = ' aria-current="page"' if l == cur else ''
        items.append(f'<a href="{href}" hreflang="{l}" lang="{l}"{cur_attr}>{l.upper()}</a>')
    return f'<nav class="lang" aria-label="{label}">' + ''.join(items) + '</nav>'


def alternates(cur, target='home'):
    out = []
    for l in LANGS:
        if target == 'home':
            href = home(l, cur)
        else:
            href = (prefix(cur) + 'datenschutz.html') if l == 'de' else (f'{l}/privacy.html' if cur == 'de' else f'../{l}/privacy.html')
        out.append(f'<link rel="alternate" hreflang="{l}" href="{href}">')
    return '\n'.join(out)


def esc_js(s):
    return s.replace('\\', '\\\\').replace("'", "\\'")


def build_home(lang):
    t = T[lang]
    p = prefix(lang)
    priv = privacy_href(lang)
    js = t['js']
    bio = '\n'.join(f'          <p>{x}</p>' for x in t['bio'])
    cv = '\n'.join(f'            <dt>{a}</dt><dd>{b}</dd>' for a, b in t['cv'])
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{t['title']}</title>
<meta name="description" content="{t['desc']}">
<meta name="theme-color" content="#F6F1EE">
{alternates(lang)}
<link rel="icon" type="image/png" href="{p}assets/favicon.png">
<link rel="apple-touch-icon" href="{p}assets/apple-touch-icon.png">
<link rel="stylesheet" href="{p}assets/style.css">
</head>
<body>

<div class="wrap">
  <header class="top">
    <a class="wordmark" href="index.html">Frauenkompass</a>
    {lang_nav(lang, t['lang_label'])}
  </header>

  <main>
    <section class="hero">
      <div>
        <h1>{t['h1']}</h1>
        <p class="lede">{t['lede']}</p>
        <p class="body">{t['body']}</p>
      </div>
      <div class="hero-symbol">
        <img src="{p}assets/symbol.webp" width="404" height="537" alt="" aria-hidden="true">
      </div>
    </section>

    <section class="section" id="news">
      <div class="news">
        <div>
          <h2>{t['news_h']}</h2>
          <p>{t['news_p']}</p>
        </div>
        <div class="card">
          <form id="news-form" novalidate>
            <input type="hidden" name="sprache" value="{lang}">
            <label class="field">
              <span>{t['f_name']} <span class="opt">{t['f_opt']}</span></span>
              <input class="input" type="text" name="vorname" autocomplete="given-name" maxlength="80">
            </label>
            <label class="field">
              <span>{t['f_email']}</span>
              <input class="input" type="email" name="email" autocomplete="email" required maxlength="200">
            </label>
            <label class="hp" aria-hidden="true">{t['f_hp']} <input type="text" name="website" tabindex="-1" autocomplete="off"></label>
            <label class="check">
              <input type="checkbox" name="einwilligung" required>
              <span>{t['f_consent'].format(privacy=priv)}</span>
            </label>
            <button class="btn" type="submit">{t['f_btn']}</button>
            <p class="form-note" id="news-note" role="status" aria-live="polite"></p>
          </form>
        </div>
      </div>
    </section>

    <section class="section" id="ueber">
      <div class="person">
        <figure class="portrait">
          <img src="{p}assets/sara.webp" srcset="{p}assets/sara-480.webp 480w, {p}assets/sara.webp 960w" sizes="(max-width: 820px) 360px, 420px" width="960" height="1200" alt="Sara Casellini-Machado Sousa" loading="lazy">
          <figcaption>
            <span class="name">Sara Casellini-Machado Sousa</span>
            <span class="role">{t['role']}</span>
          </figcaption>
        </figure>
        <div class="bio">
          <h2>{t['bio_h']}</h2>
{bio}

          <dl class="cv">
{cv}
          </dl>
        </div>
      </div>
    </section>

    <section class="quote">
      <p>{t['quote']}</p>
    </section>
  </main>

  <footer class="foot">
    <span>© <span id="jahr">2026</span> Frauenkompass · Liechtenstein</span>
    <nav>
      <a href="{p}impressum.html">{t['imprint']}</a>
      <a href="{priv}">{t['privacy']}</a>
    </nav>
  </footer>
</div>

<script>
/*
  Newsletter-Anmeldung.
  ENDPOINT: URL des Newsletter-Dienstes (z.B. Brevo- oder Mailchimp-Formular-Action).
  Solange leer, öffnet das Formular ein vorbereitetes Mail an KONTAKT_EMAIL.
*/
var ENDPOINT = '';
var KONTAKT_EMAIL = '{EMAIL}';
var TXT = {{
  badEmail: '{esc_js(js['bad_email'])}',
  noConsent: '{esc_js(js['no_consent'])}',
  mailSubject: '{esc_js(js['mail_subject'])}',
  mailBody: '{esc_js(js['mail_body'])}',
  mailName: '{esc_js(js['mail_name'])}',
  mailOpen: '{esc_js(js['mail_open'])}',
  thanks: '{esc_js(js['thanks'])}',
  error: '{esc_js(js['error'])}'
}};

document.getElementById('jahr').textContent = new Date().getFullYear();

document.getElementById('news-form').addEventListener('submit', function (e) {{
  e.preventDefault();
  var f = e.target;
  var note = document.getElementById('news-note');
  note.className = 'form-note';
  if (f.website.value) return;
  var email = f.email.value.trim();
  if (!/^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(email)) {{ note.textContent = TXT.badEmail; f.email.focus(); return; }}
  if (!f.einwilligung.checked) {{ note.textContent = TXT.noConsent; return; }}

  if (!ENDPOINT) {{
    var body = TXT.mailBody + '\\n\\nE-Mail: ' + email + (f.vorname.value.trim() ? '\\n' + TXT.mailName + ': ' + f.vorname.value.trim() : '') + '\\n[{lang}]';
    window.location.href = 'mailto:' + KONTAKT_EMAIL + '?subject=' + encodeURIComponent(TXT.mailSubject) + '&body=' + encodeURIComponent(body);
    note.textContent = TXT.mailOpen;
    note.className = 'form-note ok';
    return;
  }}

  var btn = f.querySelector('button');
  btn.disabled = true;
  fetch(ENDPOINT, {{ method: 'POST', body: new FormData(f), mode: 'no-cors' }})
    .then(function () {{
      f.reset();
      note.textContent = TXT.thanks;
      note.className = 'form-note ok';
    }})
    .catch(function () {{
      note.textContent = TXT.error;
    }})
    .then(function () {{ btn.disabled = false; }});
}});
</script>
</body>
</html>
'''


def build_privacy(lang):
    t, d = T[lang], P[lang]
    mail = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
    controller = f'''<address>
      CM Ventures Anstalt<br>
      Duxgass 2<br>
      9494 Schaan, Liechtenstein<br>
      {d['email_label']}: {mail}
    </address>'''
    authority = f'''<address>
      {d['authority']}<br>
      Städtle 38, 9490 Vaduz<br>
      <a href="https://www.datenschutzstelle.li" rel="noopener">www.datenschutzstelle.li</a>
    </address>'''
    rights = '<ul>\n' + '\n'.join(f'      <li>{r}</li>' for r in d['rights']) + '\n    </ul>'
    parts = []
    for h, paras in d['s']:
        parts.append(f'    <h2>{h}</h2>')
        for x in paras:
            if x == '@controller':
                parts.append('    ' + controller)
            elif x == '@authority':
                parts.append('    ' + authority)
            elif x == '@rights':
                parts.append('    ' + rights)
            else:
                parts.append(f'    <p>{x.replace("@mail", mail)}</p>')
    intro = '\n'.join(f'    <p>{x}</p>' for x in d['intro'])
    body = '\n'.join(parts)
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{d['title']} · Frauenkompass</title>
<meta name="robots" content="noindex">
{alternates(lang, 'privacy')}
<link rel="icon" type="image/png" href="../assets/favicon.png">
<link rel="stylesheet" href="../assets/style.css">
</head>
<body>

<div class="wrap">
  <header class="top">
    <a class="wordmark" href="index.html">Frauenkompass</a>
    {lang_nav(lang, t['lang_label'], 'privacy')}
  </header>

  <main class="legal">
    <h1>{d['h1']}</h1>
    <p class="stand">{d['stand']}</p>
    <p class="note">{d['binding']}</p>

{intro}

{body}
  </main>

  <footer class="foot">
    <span>© 2026 Frauenkompass · Liechtenstein</span>
    <nav>
      <a href="index.html">Frauenkompass</a>
      <a href="../impressum.html">{t['imprint']}</a>
    </nav>
  </footer>
</div>

</body>
</html>
'''


def write(path, s):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w', encoding='utf-8') as f:
        f.write(s)
    print('geschrieben:', path)


if __name__ == '__main__':
    for lang in LANGS:
        write('index.html' if lang == 'de' else f'{lang}/index.html', build_home(lang))
    for lang in P:
        write(f'{lang}/privacy.html', build_privacy(lang))
