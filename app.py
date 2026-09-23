import streamlit as st
import joblib
import numpy as np

st.set_page_config(
    page_title="AgriCare – Crop Recommendation",
    page_icon="🌾",
    layout="centered"
)

# ══════════════════════════════════════════════════════════════════════════════
# CUSTOM CSS
# ══════════════════════════════════════════════════════════════════════════════

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&family=DM+Serif+Display&display=swap');

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }

    .main {
        background-color: #f5f7f0;
    }

    .block-container {
        padding-top: 1.5rem;
        max-width: 720px;
    }

    /* ═══════════════════════════════════════
       AGRICARE NAVIGATION
       ═══════════════════════════════════════ */

    .agri-nav {
        background: linear-gradient(135deg, #163516 0%, #2d6a35 100%);
        border-radius: 14px;
        padding: 14px;
        margin-bottom: 20px;
        text-align: center;
        border: 1px solid #3a6b40;
    }

    .agri-title {
        font-family: 'DM Serif Display', serif;
        color: #d9f0c9;
        font-size: 1.8rem;
        margin-bottom: 3px;
    }

    .agri-subtitle {
        color: #a9cba9;
        font-size: 0.8rem;
        margin-bottom: 10px;
    }

    /* ── Hero ── */

    .hero {
        background: linear-gradient(135deg, #1a3d1f 0%, #2d6a35 100%);
        border-radius: 16px;
        padding: 2rem 2.5rem;
        color: white;
        margin-bottom: 2rem;
    }

    .hero h1 {
        font-family: 'DM Serif Display', serif;
        font-size: 2rem;
        margin: 0 0 0.4rem 0;
        color: white;
    }

    .hero p {
        margin: 0;
        opacity: 0.8;
        font-size: 0.95rem;
    }

    /* ── Section ── */

    .section-label {
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: #5a7a5e;
        margin: 1.5rem 0 0.5rem 0;
    }

    /* ── Result ── */

    .result-card {
        background: linear-gradient(135deg, #1a3d1f 0%, #2d6a35 100%);
        border-radius: 16px;
        padding: 1.5rem 2rem;
        color: white;
        margin: 1.5rem 0;
        text-align: center;
    }

    .result-card .label {
        font-size: 0.8rem;
        opacity: 0.7;
        letter-spacing: 0.1em;
        text-transform: uppercase;
    }

    .result-card .crop-name {
        font-family: 'DM Serif Display', serif;
        font-size: 2.5rem;
        margin: 0.3rem 0;
        text-transform: capitalize;
    }

    /* ── Tips ── */

    .tip-card {
        background: #fff8e6;
        border-left: 4px solid #e6a817;
        border-radius: 0 8px 8px 0;
        padding: 0.75rem 1rem;
        margin: 0.5rem 0;
        font-size: 0.9rem;
        color: #6b4e00;
    }

    .tip-good {
        background: #eaf5eb;
        border-left: 4px solid #2d6a35;
        color: #1a3d1f;
    }

    .tip-icon {
        font-size: 1.1rem;
        margin-right: 0.5rem;
    }

    /* ── Inputs ── */

    .stNumberInput > div > div > input {
        border-radius: 8px !important;
        border: 1.5px solid #c8dbc9 !important;
        background: #fff !important;
    }

    /* ── Buttons ── */

    .stButton > button {
        background: #2d6a35 !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.6rem 2rem !important;
        font-size: 1rem !important;
        font-weight: 500 !important;
        width: 100%;
        transition: background 0.2s;
    }

    .stButton > button:hover {
        background: #1a3d1f !important;
    }

    /* ── Nutrient bars ── */

    .nutrient-bar-wrap {
        margin: 0.3rem 0;
    }

    .nutrient-label {
        font-size: 0.82rem;
        color: #5a7a5e;
        margin-bottom: 2px;
        display: flex;
        justify-content: space-between;
    }

    .nutrient-bar-bg {
        background: #dde8dd;
        border-radius: 99px;
        height: 7px;
    }

    .nutrient-bar-fill {
        background: #2d6a35;
        border-radius: 99px;
        height: 7px;
    }
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# AGRICARE NAVIGATION
# ══════════════════════════════════════════════════════════════════════════════

st.markdown("""
<div class="agri-nav">
    <div class="agri-title">🌱 AgriCare</div>
    <div class="agri-subtitle">
        Smart Agriculture Assistant
    </div>
</div>
""", unsafe_allow_html=True)

nav1, nav2, nav3 = st.columns(3)

with nav1:
    st.link_button(
        "🌿 Disease Detection",
        "https://plant-disease-detection21.streamlit.app/",
        use_container_width=True
    )

with nav2:
    st.link_button(
        "🌾 Crop Recommendation",
        "https://crop-recommendation21.streamlit.app/",
        use_container_width=True
    )

with nav3:
    st.link_button(
        "🤖 Kisan Mitra",
        "https://farmer-chatbot21.streamlit.app/",
        use_container_width=True
    )

st.markdown("<br>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# LOAD MODEL
# ══════════════════════════════════════════════════════════════════════════════

@st.cache_resource
def load_model():
    return joblib.load("crop_model.pkl")


model = load_model()


# ══════════════════════════════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════════════════════════════

st.markdown("""
<div class="hero">
    <h1>🌾 Crop Recommendation</h1>
    <p>
        Enter your soil & climate data to get the best crop
        suggestion for your land.
    </p>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SOIL NUTRIENTS
# ══════════════════════════════════════════════════════════════════════════════

st.markdown(
    '<div class="section-label">🧪 Soil Nutrients</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    N = st.number_input(
        "Nitrogen (N)",
        min_value=0.0,
        max_value=200.0,
        value=50.0,
        step=1.0,
        help="Nitrogen content in soil (kg/ha)"
    )

with col2:
    P = st.number_input(
        "Phosphorus (P)",
        min_value=0.0,
        max_value=200.0,
        value=50.0,
        step=1.0,
        help="Phosphorus content in soil (kg/ha)"
    )

with col3:
    K = st.number_input(
        "Potassium (K)",
        min_value=0.0,
        max_value=200.0,
        value=50.0,
        step=1.0,
        help="Potassium content in soil (kg/ha)"
    )


# ══════════════════════════════════════════════════════════════════════════════
# NUTRIENT BARS
# ══════════════════════════════════════════════════════════════════════════════

def bar_html(label, value, max_val, unit):

    pct = min(int((value / max_val) * 100), 100)

    color = "#2d6a35" if value >= 50 else "#e6a817"

    return f"""
    <div class="nutrient-bar-wrap">
        <div class="nutrient-label">
            <span>{label}</span>
            <span>{value:.0f} {unit}</span>
        </div>

        <div class="nutrient-bar-bg">
            <div class="nutrient-bar-fill"
                 style="width:{pct}%; background:{color};">
            </div>
        </div>
    </div>
    """


st.markdown(
    bar_html("Nitrogen", N, 200, "kg/ha")
    + bar_html("Phosphorus", P, 200, "kg/ha")
    + bar_html("Potassium", K, 200, "kg/ha"),
    unsafe_allow_html=True
)


# ══════════════════════════════════════════════════════════════════════════════
# CLIMATE & SOIL CONDITIONS
# ══════════════════════════════════════════════════════════════════════════════

st.markdown(
    '<div class="section-label">🌡️ Climate & Soil Conditions</div>',
    unsafe_allow_html=True
)

col4, col5 = st.columns(2)

with col4:

    temp = st.number_input(
        "Temperature (°C)",
        min_value=0.0,
        max_value=60.0,
        value=25.0,
        step=0.1
    )

    ph = st.number_input(
        "Soil pH",
        min_value=0.0,
        max_value=14.0,
        value=6.5,
        step=0.1,
        help="Ideal range: 5.5 – 7.5"
    )

with col5:

    humidity = st.number_input(
        "Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=60.0,
        step=0.1
    )

    rainfall = st.number_input(
        "Rainfall (mm)",
        min_value=0.0,
        max_value=500.0,
        value=100.0,
        step=1.0
    )


# ══════════════════════════════════════════════════════════════════════════════
# PREDICTION
# ══════════════════════════════════════════════════════════════════════════════

st.write("")

predict = st.button("🌱 Recommend a Crop")


if predict:

    sample = np.array([
        [N, P, K, temp, humidity, ph, rainfall]
    ])

    result = model.predict(sample)

    crop = result[0].capitalize()


    # ══════════════════════════════════════════════════════════════════════════
    # RESULT
    # ══════════════════════════════════════════════════════════════════════════

    st.markdown(f"""
    <div class="result-card">
        <div class="label">Recommended crop</div>

        <div class="crop-name">
            {crop}
        </div>

        <div style="opacity:0.75; font-size:0.85rem;">
            Based on your soil & climate inputs
        </div>
    </div>
    """, unsafe_allow_html=True)


    # ══════════════════════════════════════════════════════════════════════════
    # SOIL HEALTH TIPS
    # ══════════════════════════════════════════════════════════════════════════

    st.markdown(
        '<div class="section-label">💡 Soil Health Tips</div>',
        unsafe_allow_html=True
    )

    tips = []


    if N < 50:

        tips.append(
            (
                "warn",
                "⚠️",
                f"Nitrogen is low ({N:.0f} kg/ha). "
                "Apply urea or ammonium sulfate to boost N levels above 50 kg/ha."
            )
        )

    else:

        tips.append(
            (
                "good",
                "✅",
                f"Nitrogen is adequate ({N:.0f} kg/ha). "
                "No action needed."
            )
        )


    if P < 50:

        tips.append(
            (
                "warn",
                "⚠️",
                f"Phosphorus is low ({P:.0f} kg/ha). "
                "Apply DAP or superphosphate fertilizer."
            )
        )

    else:

        tips.append(
            (
                "good",
                "✅",
                f"Phosphorus is adequate ({P:.0f} kg/ha). "
                "Soil looks healthy."
            )
        )


    if K < 50:

        tips.append(
            (
                "warn",
                "⚠️",
                f"Potassium is low ({K:.0f} kg/ha). "
                "Apply muriate of potash (MOP) to improve K levels."
            )
        )

    else:

        tips.append(
            (
                "good",
                "✅",
                f"Potassium is adequate ({K:.0f} kg/ha). "
                "Good for plant strength."
            )
        )


    if ph < 5.5:

        tips.append(
            (
                "warn",
                "⚠️",
                f"Soil is too acidic (pH {ph:.1f}). "
                "Apply agricultural lime to raise pH."
            )
        )

    elif ph > 7.5:

        tips.append(
            (
                "warn",
                "⚠️",
                f"Soil is too alkaline (pH {ph:.1f}). "
                "Apply sulfur or acidifying fertilizers."
            )
        )

    else:

        tips.append(
            (
                "good",
                "✅",
                f"Soil pH is ideal ({ph:.1f}). "
                "Great for nutrient absorption."
            )
        )


    if humidity < 30:

        tips.append(
            (
                "warn",
                "⚠️",
                f"Humidity is very low ({humidity:.0f}%). "
                "Consider irrigation or mulching."
            )
        )


    if rainfall < 50:

        tips.append(
            (
                "warn",
                "⚠️",
                f"Rainfall is low ({rainfall:.0f} mm). "
                "Supplemental irrigation may be required."
            )
        )


    # ══════════════════════════════════════════════════════════════════════════
    # DISPLAY TIPS
    # ══════════════════════════════════════════════════════════════════════════

    for kind, icon, text in tips:

        css_class = (
            "tip-card"
            if kind == "warn"
            else "tip-card tip-good"
        )

        st.markdown(
            f"""
            <div class="{css_class}">
                <span class="tip-icon">{icon}</span>
                {text}
            </div>
            """,
            unsafe_allow_html=True
        )


    # ══════════════════════════════════════════════════════════════════════════
    # INPUT SUMMARY
    # ══════════════════════════════════════════════════════════════════════════

    st.markdown("<br>", unsafe_allow_html=True)

    with st.expander("📊 Input Summary"):

        col_a, col_b = st.columns(2)

        with col_a:

            st.metric(
                "Nitrogen (N)",
                f"{N:.0f} kg/ha"
            )

            st.metric(
                "Phosphorus (P)",
                f"{P:.0f} kg/ha"
            )

            st.metric(
                "Potassium (K)",
                f"{K:.0f} kg/ha"
            )

            st.metric(
                "Soil pH",
                f"{ph:.1f}"
            )

        with col_b:

            st.metric(
                "Temperature",
                f"{temp:.1f} °C"
            )

            st.metric(
                "Humidity",
                f"{humidity:.1f} %"
            )

            st.metric(
                "Rainfall",
                f"{rainfall:.0f} mm"
            )


# ══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════════════════════

st.markdown(
    """
    <p style='text-align:center;color:#5a7a5e;
    font-size:0.78rem;margin-top:2rem'>
        🌱 AgriCare · Smart Agriculture Assistant
    </p>
    """,
    unsafe_allow_html=True
)
