import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

# ---------------- CONFIGURARE ----------------
st.set_page_config(page_title="CV Diana HÎNCU", layout="wide")

# ---------------- SIDEBAR ----------------
st.sidebar.title("📂 Află mai multe despre:")
sectiune = st.sidebar.radio("", [
    "Profil",
    "Educație",
    "Voluntariat",
    "Proiecte",
    "Concursuri",
    "Competențe"
])

# ---------------- PROFIL ----------------
if sectiune == "Profil":
    col1, col2 = st.columns([1, 3])

    with col1:
        imagine = Image.open("images/diana_cv.jpg")
        st.image(imagine, width=300)

    with col2:
        st.title("Diana HÎNCU")
        st.write("📍 București, România  |  📧 dianahincu10@gmail.com")
        st.write("""
        Sunt o persoană creativă, dinamică și orientată spre dezvoltare continuă, deschisă permanent către noi provocări.
        M-a interesat domeniul tehnologiei încă din copilărie, iar în prezent urmăresc să îmi consolidez cunoștințele și să evoluez într-o direcție profesională solidă în acest sector.
        Dorința de autodepășire mă motivează să ies din zona de confort și să îmi valorific potențialul la maxim.

        Cinci cuvinte care mă definesc cel mai bine sunt: creativitate, punctualitate, seriozitate, perseverență și entuziasm.

        Prietenii spun că aș fi și amuzantă — dar până nu apar dovezi concrete, rămân sceptică.
        """)

    st.markdown("---")

    # HOBBY-URI
    st.subheader("🎨 Hobby-uri")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("images/electronica.png", caption="Electronică", width=150)
        st.image("images/reading.png", caption="Citit", width=200)

    with col2:
        st.image("images/programming.png", caption="Programare", width=200)
        st.image("images/music.png", caption="Muzică", width=180)

    with col3:
        st.image("images/origami.png", caption="Lucru manual - Origami", width=200)
        st.image("images/board_games.png", caption="Boardgames", width=200)

# ---------------- EDUCAȚIE ----------------
elif sectiune == "Educație":
    st.header("🎓 Educație")

    # Facultate
    st.subheader("Facultatea de Electronică, Telecomunicații și Tehnologia Informației")
    st.write("2023 - prezent")
    st.markdown("""
- Specializarea: Calculatoare și Tehnologia Informației  
- Media An 1: 9.40  
- Media An 2 Semestrul 1: 9.88  
- Activități relevante: participarea la comunicările științifice studențești  
- Materii preferate: PCLP1, PCLP2, SDA, SO, AMP, CID  
    """)

    st.markdown("---")

    # Liceu
    st.subheader("Colegiul Național „Mihai Eminescu”, Suceava")
    st.write("2019 - 2023")
    st.markdown("""
- Specializarea: Matematică-Informatică, intensiv Informatică  
- Media Bacalaureat: 9.58  
- Lucrarea de atestat: Informatică  
- Activități relevante: participarea la Centrul de Excelență de Informatică  
    """)



elif sectiune == "Voluntariat":
    st.header("🤝 Voluntariat")

    col_text, col_image = st.columns([2, 1])

    with col_text:
        st.markdown("""
    Implicarea în activități de voluntariat a reprezentat un pilon esențial în formarea mea profesională și personală. În cadrul proiectelor în care am fost activă am avut ocazia să lucrez alături de oameni pasionați, să gestionez probleme reale și să contribui la schimbări concrete în comunitate.

    Această experiență mi-a oferit mai mult decât satisfacția de a ajuta: m-a învățat cum să comunic clar și empatic, cum să coordonez etapele unui proiect, să colaborez eficient în echipe diverse și să mă adaptez rapid la contexte și provocări noi. Toate aceste competențe sunt fundamentale într-o carieră în IT, unde lucrul în echipă, înțelegerea nevoilor clientului și capacitatea de a transpune o idee într-o soluție funcțională fac diferența între un proiect tehnic bun și unul cu adevărat valoros.

    Cred cu tărie că implicarea activă în comunitate oferă un sens mai profund parcursului profesional. Umanizează meseria de inginer, dezvoltator sau cercetător și îmi reamintește constant de „de ce”-ul din spatele pasiunii pentru tehnologie: acela de a crea pentru oameni, alături de oameni.
    """)

    with col_image:
        st.image("images/diana_lan.jpg", caption="Războiul cablurilor de la LanParty.v26", width=250)


    # LSE
    st.subheader("📘 Liga Studenților Electroniști")
    st.write("2023 - prezent")
    st.markdown("""
    - Implicare ca voluntar în evenimentele: Simulare Admitere, Concursul de Cultură Generală, Polifest, Preadmitere, LanParty  
    - Membră activă a departamentului IT și TechForge  
    - Arbitru în cadrul competiției [RoboChallenge](https://drive.google.com/file/d/1K-g3yZuBidAbf-Jo5w2eRKjMxvvrey5V/view?usp=drive_link)  
    - Voluntara săptămânii – [Diplomă de recunoaștere](https://drive.google.com/file/d/1jWK_QVl-Wc-krGNUM918vXjdHM2l2o6n/view?usp=drive_link)  
        """)
    st.markdown("""
    <div style='font-size:16px'>
    <b>Skilluri deprinse:</b> coordonare, organizare de evenimente, lucru în echipă, comunicare eficientă
    </div>
    """, unsafe_allow_html=True)

    # Moon Camp & NASA Space Settlement
    st.subheader("🚀 Moon Camp Challenge & NASA Space Settlement Workshop")
    st.write("Oct. 2022 – Apr. 2023")
    st.markdown("""
    - Predarea modulului de astrofizică pentru liceeni  
    - Coordonare echipă și gestionarea comunicării proiectului
        """)
    st.markdown("""
    <div style='font-size:16px'>
    <b>Skilluri deprinse:</b> public speaking, pedagogie, planificare, leadership în echipă
    </div>
    """, unsafe_allow_html=True)

    # AIVI
    st.subheader("💡 AIVI - Asociația Informală a Vocilor pentru Incluziune")
    st.write("Aug. 2020 – Oct. 2024")
    st.markdown("""
    - Coordonarea departamentelor #Cărticeală, #Cinematics și #Science  
    - Administrarea site-ului WordPress, redactarea și publicarea de articole, recenzii, cronici și interviuri  
    - Implicare activă în campanii de social media și design grafic pentru promovare  
    - Am fost în echipa media de la festivalurile: FILIT, BSF (2022, 2024), FFIR(14, 15, 16), Animest (2023, 2024), Izanagi (2023), TIFF (2023)  
    🔗 [Site AIVI](https://mhub.aiviong.ro/)  
        """)
    st.markdown("""
    <div style='font-size:16px'>
    <b>Skilluri deprinse:</b> redactare, editare vizuală, management de proiect, comunicare scrisă
    </div>
    """, unsafe_allow_html=True)

    # Sustenabil în Cetate
    st.subheader("🌱 SUstenabil în CEtate – Ateliere Vizuale pentru Adolescenți")
    st.write("Oct. 2022 – Apr. 2023")
    st.markdown("""
    - Facilitarea comunicării și îndrumarea participanților în cadrul atelierelor  
    - Responsabilă de editarea materialelor vizuale și comunicarea generală  
    🔗 [Proiect vizual](https://pubhtml5.com/flej/dqjq/)  
        """)
    st.markdown("""
    <div style='font-size:16px'>
    <b>Skilluri deprinse:</b> facilitare, colaborare, comunicare empatică, editare media
    </div>
    """, unsafe_allow_html=True)

    # GREEN in Hunedoara
    st.subheader("🌿 GREEN in Hunedoara – EUTeens4Green")
    st.write("Apr. 2023 – Apr. 2024")
    st.markdown("""
    - Organizarea și coordonarea proiectului GREENiH  
    - Facilitarea atelierelor educaționale pentru promovarea unui stil de viață sustenabil în rândul tinerilor  
    🔗 [Proiect GREENiH](https://mhub.aiviong.ro/green-in-hunedoara/)  
        """)
    st.markdown("""
    <div style='font-size:16px'>
    <b>Skilluri deprinse:</b> leadership, educație ecologică, lucru cu tineri, planificare de proiecte
    </div>
    """, unsafe_allow_html=True)



# ---------------- PROIECTE ----------------
elif sectiune == "Proiecte":
    st.header("💻 Proiecte")

    st.subheader("🕹️ PCB Runner – MiniGame (live din GitHub Pages)")
    st.write("Joc endless runner cu dinozaur PCB. Sari peste obstacole electronice și adună puncte.")

    # Embed jocul din GitHub Pages
    components.iframe("https://hdiana10.github.io/run_pcb_run/", height=200, width=800)
    # 🔘 Buton pentru a deschide jocul într-un tab nou
    if st.button("🎮 Lansează jocul într-o fereastră nouă"):
        components.html(
            '<script>window.open("https://hdiana10.github.io/run_pcb_run/", "_blank")</script>',
            height=0,
        )

    st.subheader("🔊 MP3 Player – Python")
    st.write("""
    Aplicație desktop pentru redarea fișierelor audio MP3, dezvoltată în Python.  
    Interfață grafică realizată cu Custom Tkinter, controlul audio prin biblioteca `pygame.mixer`.  
    Funcționalități: redare/pauză, selectare fișier, bară de progres, afișare titlu piesă, shuffle, repeat, crere playlist, next song, previous song.

    🔗 [Repository GitHub](https://github.com/HDiana10/Proiect_MP3)
    """)

    st.subheader("🎹 Pian electronic – Arduino")
    st.write("""
    Proiect hardware prezentat în cadrul sesiunii de comunicări științifice studențești.  
    Pianul electronic folosește un microcontroller Arduino UNO.
    """)

    st.subheader("🔋 Proiect MINERVA – CCP")
    st.write("""
    Cercetare aplicată în cadrul proiectului MINERVA – CCP:  
    **„Identificarea unui regim optim de funcționare în regim dinamic a acumulatorilor/bateriilor, 
    în ceea ce privește creșterea duratei de viață”**.  
    Am contribuit la analizarea ciclurilor de încărcare/descărcare și la modelarea impactului regimurilor dinamice asupra durabilității sistemelor de stocare.
    """)
    st.subheader("🛠️ Proiecte în desfășurare")
    st.markdown("""
    - 📊 **Generator documente orar facultate (Python + Streamlit)**  
    Aplicație web care generează orare în format Excel pe baza datelor introduse de utilizator (zile, intervale orare, materii, grupe, profesori).  
    Include autentificare, salvare a orarelor în baza de date și interfață intuitivă.
    - 🍷 **Etilotest – circuit electronic**  
    Proiect hardware în curs, pentru măsurarea alcoolemiei cu ajutorul senzorului MQ-3.  
    Afișaj digital al valorilor și avertizare LED pentru depășirea pragului critic.  
    Destinat utilizării educaționale și demonstrative.
    """)

# ---------------- CONCURSURI ----------------
elif sectiune == "Concursuri":
    st.header("🏆 Concursuri")
    st.subheader("Electron 2025")
    st.write("Locul 7")
    st.subheader("Pia Hunt 2024")
    st.write("Mențiune")
    st.subheader("ESA Moon Camp Challenge 2022")
    st.write("Locul 3, Pioneers")

# ---------------- COMPETENȚE ----------------
elif sectiune == "Competențe":
    st.header("🛠️ Competențe")
    st.write("""
    - Limbaje de programare: Python, C/C++, Arduino
    - Instrumente de dezvoltare: PyCharm, GitHub, Arduino IDE
    - Electronică și hardware: Arduino UNO, ESP32, ESP nano
    - Design UI/UX: Design de interfață pentru aplicații desktop
    - Limbi străine: Română (nativă), engleză (avansată), franceză (începător)
    - Lucru în echipă și colaborare - A lucrat eficient în proiecte studențești, echipe de voluntariat și inițiative științifice
    - Comunicare - A prezentat conținut tehnic în mod clar publicului academic; a coordonat voluntari și a condus întâlniri
    - Leadership - Și-a asumat roluri precum lider de proiect și jurnalist în cadrul organizațiilor de voluntariat
    - Adaptabilitate - A învățat rapid noi instrumente și tehnologii precum Python, GitHub și Arduino IDE
    - Rezolvarea problemelor - A făcut față provocărilor tehnice în proiectele de dezvoltare electronică și software
    - Gândire critică - A analizat sistemele de baterii și a contribuit la luarea deciziilor bazate pe cercetare
    - Creativitate - A proiectat interfețe ușor de utilizat și a participat la activități de comunicare științifică
    - Inițiativă - Implicare proactivă în concursuri, școli de excelență și provocări tehnice extracurriculare
    """)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("© 2025 Diana HÎNCU")
