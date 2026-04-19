import numpy as np
import pandas as pd

def get_feature_contributions(model, input_df, scaler, columns):
    """
    Returns feature-wise contribution to prediction.
    Only includes features that are actually present in the input (non-zero after encoding).
    """

    # Step 1: Scale input (same as model)
    scaled_input = scaler.transform(input_df)

    # Step 2: Get model coefficients
    coefs = model.coef_

    # Step 3: Multiply feature values with coefficients
    contributions = scaled_input[0] * coefs

    # Step 4: Get the original (unscaled) input values to filter out zero-valued features
    original_values = input_df.values[0]

    # Step 5: Create dataframe
    contribution_df = pd.DataFrame({
        "Feature": columns,
        "Contribution": contributions,
        "Original_Value": original_values
    })

    # Step 6: Filter out features that are zero in the original input
    # (these are dummy variables that weren't selected or features not present)
    contribution_df = contribution_df[contribution_df["Original_Value"] != 0].copy()

    # Step 7: Drop the helper column
    contribution_df = contribution_df.drop(columns=["Original_Value"])

    # Step 8: Sort by impact
    contribution_df = contribution_df.sort_values(
        by="Contribution",
        key=abs,
        ascending=False
    )

    return contribution_df