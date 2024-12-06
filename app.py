import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import scipy.optimize as sco
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
from streamlit_extras.metric_cards import style_metric_cards

# Configuración de la página
st.set_page_config(page_title="Análisis de Portafolios", layout="wide")
st.markdown(
    """
    <style>
    body {
        background-color: #1D1E2C;
        color: white;
    }
    h1, h2, h3, h4, h5, h6, p, span, div {
        color: white !important;
    }
    .stApp {
        background-color: #1D1E2C;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("Análisis y Optimización de Portafolios")

ventanas = {
    "2010-2023": ("2010-01-01", "2023-12-31"),
    "2010-2020": ("2010-01-01", "2020-12-31"),
    "2021-2023": ("2021-01-01", "2023-12-31")
}

# Tabs de la aplicación
st.markdown(
    """
    <style>
    div[data-baseweb="tab-highlight"] {
        background-color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
tab1, tab2, tab3, tab4 = st.tabs([
    "Análisis de Activos Individuales",
    "Portafolios Óptimos",
    "Comparación de Portafolios",
    "Black-Litterman"
])

# Tab 1: Análisis de Activos Individuales
with tab1:
    st.markdown(
        """
        <div style="
            background-color: #FFB703;
            padding: 8px;
            border-radius: 20px;
            color: black;
            text-align: center;
        ">
            <h1 style="margin: 0; color: #black; font-size: 25px; ">Análisis de Activos Individuales</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <style>
        /* Centrar el título */
        .stRadio > label {
            display: block;
            text-align: center;
            color: black !important; /* Forzar el color negro */
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        
        /* Centrar los botones */
        div[role="radiogroup"] {
            display: flex;
            justify-content: center;
            gap: 10px;
        }
        
        /* Botones sin seleccionar */
        div[role="radiogroup"] > label {
            background-color: white !important;
            color: #1D1E2C !important; /* Asegurar texto visible */
            border: 2px solid black;
            border-radius: 10px;
            padding: 8px 16px;
            font-size: 16px;
            cursor: pointer;
            transition: all 0.3s ease;
            text-align: center;
        }
        
        /* Texto y contenido del botón */
        div[role="radiogroup"] > label > div {
            color: black !important; /* Forzar texto negro dentro de los botones */
        }
        
        /* Botón seleccionado */
        div[role="radiogroup"] > label[data-selected="true"] {
            background-color: #FFB703 !important; /* Color de fondo amarillo */
            color: #1D1E2C !important; /* Texto visible */
            border: 2px solid #FFB703;
            font-weight: bold;
        }
        
        /* Texto y contenido del botón seleccionado */
        div[role="radiogroup"] > label[data-selected="true"] > div {
            color: #1D1E2C !important; /* Texto negro */
        }
        
        /* Hover sobre botones no seleccionados */
        div[role="radiogroup"] > label:hover {
            background-color: #FFE5A1 !important; /* Color de fondo en hover */
            color: #1D1E2C !important; /* Texto negro */
        }
        
        /* Hover sobre el texto y punto del botón */
        div[role="radiogroup"] > label:hover > div {
            color: #1D1E2C !important; /* Texto negro */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Implementación del radio con ventanas de tiempo
    ventana_tiempo = st.radio(
        "Selecciona una ventana de tiempo:",
        list(ventanas.keys()),
        horizontal=True
    )
