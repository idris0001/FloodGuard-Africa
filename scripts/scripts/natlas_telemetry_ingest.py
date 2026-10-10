def fetch_natlas_telemetry(basin_id="NIGER_BENUE"):
    print(f"[N-ATLAS API] Ingesting telemetry for basin: {basin_id}...")
    return {"status": "success", "river_stage_m": 7.8}

if __name__ == "__main__":
    print(fetch_natlas_telemetry())
