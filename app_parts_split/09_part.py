with tab_detalle:
    cfg = st.session_state.get("cfg", {})
    data = cfg.get("data")
    if not data:
        st.info("Cargá primero los datos en la pestaña **Configuración**.")
        st.stop()

    unit_cost = compute_unit_labor_cost(data["mat"], data["bom"])  # costo MO unitario por SKU
    agg = aggregate_current_month(data["mov"], data["rep"], unit_cost, cfg["today"])  # métricas del mes

    st.subheader("📦 Producción por SKU")
    prod = agg["prod"].copy()
    prod["COSTO_MO_UNIT"] = prod["COSTO_MO_UNIT"].apply(lambda x: f"$ {x:,.0f}")
    prod["COSTO_MO_TOTAL"] = prod["COSTO_MO_TOTAL"].apply(lambda x: f"$ {x:,.0f}")
    st.dataframe(prod.rename(columns={"SKU":"SKU","CANTIDAD":"Cantidad","COSTO_MO_UNIT":"Costo MO unit.","COSTO_MO_TOTAL":"Costo MO total"}))

    st.subheader("🧾 Ventas por SKU")
    ventas = agg["ventas"].copy()
    