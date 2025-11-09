# ============================
# Cálculos base
# ============================

def compute_unit_labor_cost(df_material: pd.DataFrame, df_bom: pd.DataFrame) -> pd.DataFrame:
    """Costo de mano de obra unitario por SKU = Σ(cant_op × costo_op)."""
    mat = df_material.rename(columns={"MATE_CODIGO": "OPERACION", "MATE_CRM": "COSTO_OPERACION"})
    bom = df_bom.rename(columns={"MBOM_CODIGO": "SKU", "MATE_CODIGO": "OPERACION", "DEBO_CANTIDAD": "CANTIDAD_OP"})
    merged = bom.merge(mat[["OPERACION", "COSTO_OPERACION"]], on="OPERACION", how="left")
    merged["COSTO_PARCIAL"] = merged["CANTIDAD_OP"].fillna(0) * merged["COSTO_OPERACION"].fillna(0)
    return merged.groupby("SKU", as_index=False)["COSTO_PARCIAL"].sum().rename(columns={"COSTO_PARCIAL": "COSTO_MO_UNIT"})
