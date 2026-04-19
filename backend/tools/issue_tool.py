def issue_tool(state):
    data = state["input"]
    issues = []

    # Nitrogen - adjust for fertilizer usage
    effective_n = data["N"] + (data["Fertilizer_Used"] * 0.2)  # Assume 20% N in fertilizer
    if effective_n < 80:  # Raised from 50 to be more sensitive
        issues.append({"type": "nitrogen_deficiency", "severity": "high" if effective_n < 50 else "medium"})

    # Phosphorus - adjust for fertilizer usage  
    effective_p = data["P"] + (data["Fertilizer_Used"] * 0.1)  # Assume 10% P in fertilizer
    if effective_p < 60:  # Raised from 40 to be more sensitive
        issues.append({"type": "phosphorus_deficiency", "severity": "high" if effective_p < 40 else "medium"})

    # Potassium - adjust for fertilizer usage
    effective_k = data["K"] + (data["Fertilizer_Used"] * 0.1)  # Assume 10% K in fertilizer
    if effective_k < 60:  # Raised from 40 to be more sensitive
        issues.append({"type": "potassium_deficiency", "severity": "high" if effective_k < 40 else "medium"})

    # Rainfall - consider irrigation type
    if data["Rainfall"] < 600 and data["Irrigation_Type"] in ["Rainfed"]:  # Raised from 500
        issues.append({"type": "low_rainfall", "severity": "high" if data["Rainfall"] < 400 else "medium"})
    elif data["Rainfall"] < 400 and data["Irrigation_Type"] in ["Flood"]:  # Raised from 300
        issues.append({"type": "low_rainfall", "severity": "medium"})

    # Soil Moisture - new detection
    if data["Soil_Moisture"] < 30:  # New threshold
        issues.append({"type": "low_soil_moisture", "severity": "high" if data["Soil_Moisture"] < 20 else "medium"})

    # Organic Carbon
    if data["Organic_Carbon"] < 0.75:  # Raised from 0.5 to be more sensitive
        issues.append({"type": "low_soil_fertility", "severity": "high" if data["Organic_Carbon"] < 0.5 else "medium"})

    # Soil pH - consider crop type tolerance
    crop_ph_ranges = {
        "Rice": (5.5, 7.0),
        "Wheat": (6.0, 7.5), 
        "Maize": (5.8, 7.0),
        "Barley": (6.0, 7.8),
        "Jute": (5.5, 6.5)
    }
    
    crop = data["Crop_Type"]
    ph_min, ph_max = crop_ph_ranges.get(crop, (6.0, 7.5))
    
    if data["Soil_pH"] < ph_min:
        issues.append({"type": "acidic_soil", "severity": "medium"})
    elif data["Soil_pH"] > ph_max:
        issues.append({"type": "alkaline_soil", "severity": "medium"})

    # Temperature - consider season and region
    temp_thresholds = {
        ("Kharif", "North"): 35, ("Kharif", "South"): 38, ("Kharif", "Central"): 36,
        ("Rabi", "North"): 32, ("Rabi", "South"): 35, ("Rabi", "Central"): 34,
        ("Zaid", "North"): 40, ("Zaid", "South"): 42, ("Zaid", "Central"): 41
    }
    
    season = data["Season"]
    region = data["Region"]
    threshold = temp_thresholds.get((season, region), 38)
    
    if data["Temperature"] > threshold:
        issues.append({"type": "heat_stress", "severity": "high"})

    state["issues"] = issues
    return state
