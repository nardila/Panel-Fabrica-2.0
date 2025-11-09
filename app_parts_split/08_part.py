with tab_kpi:
    cfg = st.session_state.get("cfg", {})
    data = cfg.get("data")
    if not data:
        st.info("Cargá primero los datos en la pestaña **Configuración**.")
        st.stop()

    unit_cost = compute_unit_labor_cost(data["mat"], data["bom"])  # costo MO unitario por SKU
    agg = aggregate_current_month(data["mov"], data["rep"], unit_cost, cfg["today"])  # métricas del mes

    obj_h = cfg.get("obj_h", 0.0)
    porc_fab = (agg["costo_fabricado"]/obj_h - 1) * 100 if obj_h else 0.0
    porc_rec = (agg["costo_recuperado"]/obj_h - 1) * 100 if obj_h else 0.0

    # Grilla original + agregado del % debajo del valor (mismo HTML / sin CSS nuevo)
    kpi_html = f"""
    <div class='dx-grid'>
      <div class='dx-card'>
        <div class='dx-label'>🪑 Muebles fabricados</div>
        <div class='dx-val'>{agg['fabricados']:,}</div>
      </div>
      <div class='dx-card'>
        <div class='dx-label'>🛠️ Costo MO fabricado</div>
        <div class='dx-val'>$ {agg['costo_fabricado']:,.0f}</div>
        <div class='dx-label' style='margin-top:4px'>{porc_fab:+.1f}% vs esperado</div>
      </div>
      <div class='dx-card'>
        <div class='dx-label'>🧾 Muebles vendidos</div>
        <div class='dx-val'>{agg['vendidos']:,}</div>
      </div>
      <div class='dx-card'>
        <div class='dx-label'>💵 Costo MO recuperado</div>
        <div class='dx-val'>$ {agg['costo_recuperado']:,.0f}</div>
        <div class='dx-label' style='margin-top:4px'>{porc_rec:+.1f}% vs esperado</div>
      </div>
    </div>
    <br>
    <div class='dx-card'><div class='dx-label'>🏭 Costo mensual total de la fábrica</div><div class='dx-val'>$ {cfg.get('costo',0):,.0f}</div></div>
    <br>
    <div class='dx-card'><div class='dx-label'>💹 Margen bruto actual</div><div class='dx-val'>$ {agg['margen']:,.0f}</div></div>
    """
    st.markdown(kpi_html.replace(",", "."), unsafe_allow_html=True)

