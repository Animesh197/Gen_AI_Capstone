def issue_tool(state):
    data = state["input"]
    ml_negative_factors = state.get("ml_negative_factors", [])
    issues = []

    # === ML-DRIVEN ISSUE DETECTION ===
    # Check if ML model flagged these as negative contributors
    
    # Nitrogen
    effective_n = data["N"] + (data["Fertilizer_Used"] * 0.2)
    if effective_n < 80 or "N" in ml_negative_factors:
        issues.append({"type": "nitrogen_deficiency", "severity": "high" if effective_n < 50 else "medium"})

    # Phosphorus
    effective_p = data["P"] + (data["Fertilizer_Used"] * 0.1)
    if effective_p < 60 or "P" in ml_negative_factors:
        issues.append({"type": "phosphorus_deficiency", "severity": "high" if effective_p < 40 else "medium"})

    # Potassium
    effective_k = data["K"] + (data["Fertilizer_Used"] * 0.1)
    if effective_k < 60 or "K" in ml_negative_factors:
        issues.append({"type": "potassium_deficiency", "severity": "high" if effective_k < 40 else "medium"})

    # Rainfall
    rainfall_flagged = any("Rainfall" in f for f in ml_negative_factors)
    if data["Rainfall"] < 600 and data["Irrigation_Type"] in ["Rainfed"]:
        issues.append({"type": "low_rainfall", "severity": "high" if data["Rainfall"] < 400 else "medium"})
    elif data["Rainfall"] < 400 and data["Irrigation_Type"] in ["Flood"]:
        issues.append({"type": "low_rainfall", "severity": "medium"})
    elif rainfall_flagged and data["Rainfall"] < 800:
        issues.append({"type": "low_rainfall", "severity": "medium"})

    # Soil Moisture
    moisture_flagged = any("Soil_Moisture" in f for f in ml_negative_factors)
    if data["Soil_Moisture"] < 30 or moisture_flagged:
        issues.append({"type": "low_soil_moisture", "severity": "high" if data["Soil_Moisture"] < 20 else "medium"})

    # Fertilizer Usage (if ML flags it as negative, it means over-application)
    fertilizer_flagged = any("Fertilizer_Used" in f for f in ml_negative_factors)
    if fertilizer_flagged and data["Fertilizer_Used"] > 200:
        issues.append({"type": "excess_fertilizer", "severity": "medium"})

    # Organic Carbon
    carbon_flagged = any("Organic_Carbon" in f for f in ml_negative_factors)
    if data["Organic_Carbon"] < 0.75 or carbon_flagged:
        issues.append({"type": "low_soil_fertility", "severity": "high" if data["Organic_Carbon"] < 0.5 else "medium"})

    # Soil pH - crop-specific
    crop_ph_ranges = {
        "Rice": (5.5, 7.0),
        "Wheat": (6.0, 7.5), 
        "Maize": (5.8, 7.0),
        "Barley": (6.0, 7.8),
        "Jute": (5.5, 6.5)
    }
    
    crop = data["Crop_Type"]
    ph_min, ph_max = crop_ph_ranges.get(crop, (6.0, 7.5))
    ph_flagged = any("Soil_pH" in f or "pH" in f for f in ml_negative_factors)
    
    if data["Soil_pH"] < ph_min:
        issues.append({"type": "acidic_soil", "severity": "medium"})
    elif data["Soil_pH"] > ph_max:
        issues.append({"type": "alkaline_soil", "severity": "medium"})
    elif ph_flagged:
        # ML flagged pH but it's within range - flag as suboptimal
        if data["Soil_pH"] < (ph_min + ph_max) / 2:
            issues.append({"type": "acidic_soil", "severity": "low"})
        else:
            issues.append({"type": "alkaline_soil", "severity": "low"})

    # Temperature - season and region aware
    temp_thresholds = {
        ("Kharif", "North"): 35, ("Kharif", "South"): 38, ("Kharif", "Central"): 36,
        ("Kharif", "East"): 36, ("Kharif", "West"): 37,
        ("Rabi", "North"): 32, ("Rabi", "South"): 35, ("Rabi", "Central"): 34,
        ("Rabi", "East"): 33, ("Rabi", "West"): 34,
        ("Zaid", "North"): 40, ("Zaid", "South"): 42, ("Zaid", "Central"): 41,
        ("Zaid", "East"): 40, ("Zaid", "West"): 41
    }
    
    season = data["Season"]
    region = data["Region"]
    threshold = temp_thresholds.get((season, region), 38)
    temp_flagged = any("Temperature" in f for f in ml_negative_factors)
    
    if data["Temperature"] > threshold or temp_flagged:
        issues.append({"type": "heat_stress", "severity": "high"})

    # Humidity (if ML flags it)
    humidity_flagged = any("Humidity" in f for f in ml_negative_factors)
    if humidity_flagged:
        if data["Humidity"] < 40:
            issues.append({"type": "low_humidity", "severity": "medium"})
        elif data["Humidity"] > 90:
            issues.append({"type": "high_humidity", "severity": "medium"})

    state["issues"] = issues
    return state
