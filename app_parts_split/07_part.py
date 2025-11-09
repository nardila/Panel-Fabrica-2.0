with tab_config:
    default_url = st.secrets.get("DRIVE_FILE_URL", "")
    drive_url = st.text_input("Enlace de Google Drive o Google Sheet", value=default_url)
    mes_ini, mes_fin = month_bounds(hoy)

    c1, c2, c3 = st.columns(3)
    with c1:
        costo_mensual = st.number_input("Costo mensual total ($)", value=50_000_000.0, step=100_000.0)
    with c2:
        dias_mes = st.number_input("Días hábiles del mes", value=int(business_days_count(mes_ini, mes_fin)))
    with c3:
        dias_trans = st.number_input("Días hábiles transcurridos", value=int(business_days_count(mes_ini, hoy)))

    objetivo_diario = (costo_mensual / dias_mes) if dias_mes else 0.0
    objetivo_a_hoy = objetivo_diario * dias_trans

    data = None
    if drive_url:
        try:
            data = load_data_from_excel_bytes(fetch_excel_bytes(drive_url))
            st.success("Datos cargados correctamente ✅")
        except Exception as e:
            st.error(f"No se pudo obtener el archivo/Sheet. Error: {e}")

    st.session_state["cfg"] = dict(url=drive_url, costo=costo_mensual, dias_mes=dias_mes, dias_trans=dias_trans, obj_d=objetivo_diario, obj_h=objetivo_a_hoy, data=data, today=hoy)

