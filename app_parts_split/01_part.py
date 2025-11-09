# DX Fábrica – Panel de KPI (versión con SOLO los cambios solicitados por Nico)
# Cambios exactos:
# - Indicadores: % vs esperado en "Costo MO fabricado" y "Costo MO recuperado" + card de "Costo mensual total de la fábrica".
# - Detalle de SKU: formato moneda en Costo MO unit. y total; en Ventas por SKU agregar CRM y Margen Bruto por SKU, orden descendente por Margen Bruto.
# - Nada más fue modificado.

import io
import re
import requests
import numpy as np
import pandas as pd
import streamlit as st
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from pytz import timezone

# ============================
# Utilidades de fechas (Buenos Aires)
# ============================
TZ = timezone("America/Argentina/Buenos_Aires")

def today_ba() -> date:
    return datetime.now(TZ).date()

def month_bounds(dt: date):
    start = dt.replace(day=1)
    end = (start + relativedelta(months=1)) - relativedelta(days=1)
    return start, end

def business_days_count(start: date, end: date) -> int:
    return int(np.busday_count(start, end + relativedelta(days=1)))

