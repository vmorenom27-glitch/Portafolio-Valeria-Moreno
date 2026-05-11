import streamlit as st

st.set_page_config(
    page_title="Portafolio IA — Valeria Moreno",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

APPS = [
    {"nombre": "RAG — Chat con PDF", "desc": "Agente inteligente que analiza y responde preguntas sobre documentos PDF usando recuperacion aumentada.", "url": "https://99aqcjkqz6yv9qjct4aveb.streamlit.app", "emoji": "🤖", "tag": "NLP · OpenAI"},
    {"nombre": "Control por Voz", "desc": "Interfaces multimodales que transcriben comandos de voz en tiempo real usando reconocimiento automatico.", "url": "https://ctrlvoicesrd.streamlit.app", "emoji": "🎙️", "tag": "Audio · Speech"},
    {"nombre": "Tablero Inteligente", "desc": "Dibuja un boceto en el panel y la IA lo interpreta, genera descripciones e historias sobre el dibujo.", "url": "https://drawrecogsrd.streamlit.app", "emoji": "🎨", "tag": "Vision · GPT-4"},
    {"nombre": "Reconocimiento de Digitos", "desc": "Red neuronal artificial que reconoce digitos escritos a mano dibujados directamente en el canvas.", "url": "https://handwsrd.streamlit.app", "emoji": "✍️", "tag": "RNA · MNIST"},
    {"nombre": "OCR + Audio", "desc": "Reconocimiento optico de caracteres que extrae texto de imagenes con camara o archivo y lo convierte a audio.", "url": "https://ocraudiosrd.streamlit.app", "emoji": "🔊", "tag": "OCR · TTS"},
    {"nombre": "Analisis de Sentimiento", "desc": "Analiza la polaridad y subjetividad de textos, determina si el sentimiento es positivo, negativo o neutro.", "url": "https://tuckwc2itphatfncwb7asb.streamlit.app", "emoji": "😊", "tag": "NLP · TextBlob"},
    {"nombre": "TF-IDF en Espanol", "desc": "Demo que compara documentos usando TF-IDF para encontrar el mas relevante segun una pregunta en espanol.", "url": "https://tdfespsrd.streamlit.app", "emoji": "🔍", "tag": "NLP · TF-IDF"},
    {"nombre": "Traductor por Voz", "desc": "Escucha lo que dices y traduce tu voz de forma automatica entre multiples idiomas al instante.", "url": "https://traductorvozatextosrd.streamlit.app", "emoji": "🌐", "tag": "Audio · Translate"},
    {"nombre": "Analisis de Imagen", "desc": "Vision App que describe imagenes de forma inteligente usando modelos multimodales de OpenAI.", "url": "https://interpretacion-de-imagenes-dk3usrlcblnx3xeueaydl6.streamlit.app", "emoji": "🖼️", "tag": "GPT-4V · Vision"},
    {"nombre": "Reconocimiento Optico OCR", "desc": "Elige la fuente de imagen, camara o archivo, y extrae el texto visible usando OCR con traduccion.", "url": "https://fjgt24nkkwrws6e6kyvnkb.streamlit.app", "emoji": "📄", "tag": "OCR · Camera"},
]

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Syne:wght@700;800&display=swap');
html, body, [class*="css"] { font-family: 'Space Grotesk', sans-serif; background-color: #FFFBEB; color: #1C1917; }
.stApp { background: #FFFBEB; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
.hero-wrap { position: relative; background: linear-gradient(135deg, #1C1917 0%, #2C2520 60%, #1C1917 100%); padding: 3.5rem 2rem 5rem; overflow: hidden; text-align: center; }
.hero-dots { position: absolute; top: 0; left: 0; right: 0; bottom: 0; background-image: radial-gradient(rgba(251,191,36,0.13) 1.5px, transparent 1.5px); background-size: 30px 30px; pointer-events: none; }
.hero-glow-left { position: absolute; top: -100px; left: -100px; width: 400px; height: 400px; background: radial-gradient(circle, rgba(251,191,36,0.16) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.hero-glow-right { position: absolute; bottom: -120px; right: -80px; width: 450px; height: 450px; background: radial-gradient(circle, rgba(234,179,8,0.13) 0%, transparent 65%); border-radius: 50%; pointer-events: none; }
.hero-badge { display: inline-block; background: rgba(251,191,36,0.12); border: 1px solid rgba(251,191,36,0.45); color: #FCD34D; font-size: 0.68rem; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase; padding: 0.38rem 1.1rem; border-radius: 99px; margin-bottom: 1.5rem; position: relative; z-index: 2; }
.hero h1 { font-family: 'Syne', sans-serif; font-size: clamp(3rem, 7vw, 5.5rem); font-weight: 800; margin: 0 0 0.6rem; line-height: 1; color: #fff; position: relative; z-index: 2; }
.hero h1 .yellow { background: linear-gradient(90deg, #FBBF24 0%, #FDE68A 50%, #F59E0B 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
.hero-sub { font-size: 1rem; color: #A8A29E; margin-top: 0.6rem; position: relative; z-index: 2; }
.hero-stats { display: inline-flex; margin-top: 2.5rem; background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; overflow: hidden; position: relative; z-index: 2; }
.stat-box { padding: 1rem 2rem; border-right: 1px solid rgba(255,255,255,0.08); text-align: center; }
.stat-box:last-child { border-right: none; }
.stat-num { font-family: 'Syne', sans-serif; font-size: 2rem; font-weight: 800; color: #FBBF24; display: block; line-height: 1; }
.stat-label { font-size: 0.65rem; color: #78716C; text-transform: uppercase; letter-spacing: 0.14em; margin-top: 0.3rem; display: block; }
.wave-divider { line-height: 0; background: #1C1917; }
.wave-divider svg { display: block; width: 100%; }
.section-wrap { background: #FFFBEB; padding: 2.5rem 2rem 3.5rem; position: relative; }
.grid-bg { position: absolute; inset: 0; background-image: linear-gradient(rgba(251,191,36,0.07) 1px, transparent 1px), linear-gradient(90deg, rgba(251,191,36,0.07) 1px, transparent 1px); background-size: 50px 50px; pointer-events: none; }
.section-title { font-family: 'Syne', sans-serif; font-size: 0.82rem; font-weight: 700; color: #B45309; text-transform: uppercase; letter-spacing: 0.25em; text-align: center; margin-bottom: 2rem; position: relative; z-index: 1; }
.card { background: #fff; border: 1.5px solid #FEF3C7; border-radius: 16px; padding: 1.2rem 1.3rem 1.4rem; position: relative; overflow: hidden; transition: transform 0.3s cubic-bezier(.34,1.56,.64,1), box-shadow 0.3s, border-color 0.3s; }
.card:hover { transform: translateY(-6px) scale(1.015); box-shadow: 0 20px 45px -10px rgba(217,119,6,0.18); border-color: #FCD34D; }
.card-accent { height: 3px; border-radius: 99px; background: linear-gradient(90deg, #FBBF24, #FDE68A, #F59E0B, #FBBF24); background-size: 200% 100%; animation: shimmer 3s linear infinite; margin-bottom: 1rem; }
@keyframes shimmer { 0% { background-position: 200% 0; } 100% { background-position: -200% 0; } }
.card-header { display: flex; align-items: center; gap: 0.65rem; margin-bottom: 0.5rem; }
.card-emoji { font-size: 1.8rem; line-height: 1; flex-shrink: 0; }
.card-title { font-family: 'Syne', sans-serif; font-size: 0.95rem; font-weight: 800; color: #1C1917; margin: 0 0 0.28rem; line-height: 1.2; }
.card-tag { display: inline-block; font-size: 0.58rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: #92400E; background: #FEF3C7; border: 1px solid #FDE68A; padding: 0.15rem 0.55rem; border-radius: 99px; }
.card-desc { font-size: 0.8rem; color: #78716C; line-height: 1.6; margin: 0.65rem 0 1.1rem; }
.card-btn { display: inline-flex; align-items: center; gap: 0.4rem; background: #1C1917; color: #FBBF24 !important; font-family: 'Space Grotesk', sans-serif; font-size: 0.78rem; font-weight: 700; text-decoration: none !important; padding: 0.45rem 1.05rem; border-radius: 99px; transition: background 0.2s, transform 0.15s; }
.card-btn:hover { background: #292524; transform: scale(1.04); color: #FCD34D !important; text-decoration: none !important; }
.card-num { position: absolute; bottom: 0.5rem; right: 0.9rem; font-family: 'Syne', sans-serif; font-size: 2.8rem; font-weight: 800; color: rgba(251,191,36,0.06); line-height: 1; user-select: none; }
.footer-wrap { background: #1C1917; padding: 2rem; text-align: center; }
.footer-line { height: 3px; background: linear-gradient(90deg, transparent 0%, #FBBF24 30%, #FDE68A 50%, #FBBF24 70%, transparent 100%); margin-bottom: 1.2rem; }
.footer-text { color: #57534E; font-size: 0.82rem; margin: 0; }
.footer-name { color: #FBBF24; font-weight: 700; }
[data-testid="column"] { padding: 0.4rem !important; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-wrap">
    <div class="hero-dots"></div>
    <div class="hero-glow-left"></div>
    <div class="hero-glow-right"></div>
    <div class="hero-badge">&#10022; Portafolio Academico &nbsp;&middot;&nbsp; IA &amp; Machine Learning</div>
    <h1>Valeria <span class="yellow">Moreno</span></h1>
    <p class="hero-sub">Aplicaciones construidas con Python, Streamlit y modelos de inteligencia artificial</p>
    <div class="hero-stats">
        <div class="stat-box"><span class="stat-num">10</span><span class="stat-label">Proyectos</span></div>
        <div class="stat-box"><span class="stat-num">5</span><span class="stat-label">Tecnologias</span></div>
        <div class="stat-box"><span class="stat-num">1</span><span class="stat-label">Semestre</span></div>
    </div>
</div>
<div class="wave-divider">
  <svg viewBox="0 0 1440 80" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="none">
    <path d="M0,50 C200,90 400,10 600,50 C800,90 1000,10 1200,50 C1320,75 1390,30 1440,50 L1440,80 L0,80 Z" fill="#FFFBEB"/>
  </svg>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-wrap"><div class="grid-bg"></div><p class="section-title">&#10022; &nbsp; Explora los proyectos &nbsp; &#10022;</p>', unsafe_allow_html=True)

cols_per_row = 3
rows = [APPS[i:i+cols_per_row] for i in range(0, len(APPS), cols_per_row)]

for row_idx, row in enumerate(rows):
    cols = st.columns(cols_per_row, gap="medium")
    for col_idx, (col, app) in enumerate(zip(cols, row)):
        num = row_idx * cols_per_row + col_idx + 1
        with col:
            st.markdown(f"""
<div class="card">
    <div class="card-accent"></div>
    <div class="card-header">
        <div class="card-emoji">{app['emoji']}</div>
        <div>
            <p class="card-title">{app['nombre']}</p>
            <span class="card-tag">{app['tag']}</span>
        </div>
    </div>
    <p class="card-desc">{app['desc']}</p>
    <a class="card-btn" href="{app['url']}" target="_blank">Abrir app &rarr;</a>
    <div class="card-num">{str(num).zfill(2)}</div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="footer-wrap">
    <div class="footer-line"></div>
    <p class="footer-text">Construido con &#10084;&#65039; usando Streamlit &nbsp;&middot;&nbsp; <span class="footer-name">Valeria Moreno</span> &nbsp;&middot;&nbsp; 2025</p>
</div>
""", unsafe_allow_html=True)
