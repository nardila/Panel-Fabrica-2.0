# ============================
# Interfaz Streamlit con estilo (sin cambios de estructura)
# ============================
st.set_page_config(page_title="DX Fábrica – KPI", layout="wide")

# --- Estilos y header existentes (idénticos) ---
st.markdown("""
<style>
:root{ --bg:#0b1020; --card:#ffffff; --muted:#6b7280; --ink:#111827; --border:#e5e7eb; }
.block-container{ padding-top:.5rem; padding-bottom:0; max-width:1280px; }
.dx-header{ background:linear-gradient(90deg, var(--bg), #11193a); color:#fff; border-radius:10px; padding:4px 14px; margin:0 0 8px 0; }
.dx-head-row{ display:flex; align-items:flex-end; justify-content:space-between; gap:16px; }
.dx-title{ margin:0; line-height:1; font-weight:800; font-size:18px; }
.dx-upd{ margin:0; font-size:10px; opacity:.9; white-space:nowrap; }
.dx-shell{ background:#fff; border:1px solid var(--border); border-radius:16px; padding:14px 16px; box-shadow:0 2px 10px rgba(0,0,0,.04); }
.dx-grid{ display:grid; grid-template-columns:repeat(4,1fr); gap:12px; margin-top:8px }
.dx-card{ background:var(--card); border:1px solid var(--border); border-radius:14px; padding:12px 14px; box-shadow:0 2px 8px rgba(0,0,0,.05); }
.dx-label{ color:var(--muted); font-size:13px; margin-bottom:6px; display:flex; gap:6px; align-items:center }
.dx-val{ color:var(--ink); font-size:26px; font-weight:700; line-height:1.15; margin:0 }
</style>
""", unsafe_allow_html=True)

hoy = today_ba()
st.markdown(f"""
<div class=\"dx-header\">
  <div class=\"dx-head-row\">
    <h1 class=\"dx-title\">DX Fábrica — Panel de KPI</h1>
    <p class=\"dx-upd\">Datos del mes en curso · <b>Última actualización:</b> {hoy}</p>
  </div>
</div>
""", unsafe_allow_html=True)

