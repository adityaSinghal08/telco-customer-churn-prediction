import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, OrdinalEncoder


class Preprocessor(BaseEstimator, TransformerMixin):
    """
    Custom preprocessing transformer with explicit binary handling.

    Parameters
    ----------
    scaling : bool, default=False
        Whether to apply StandardScaler to numerical features.
    """

    def __init__(self, scaling: bool = False):
        self.scaling = scaling

    def fit(self, X, y=None):
        X = X.copy()

        # -------------------------
        # Column type identification
        # -------------------------
        self.binary_cols_ = [
            col for col in X.columns if X[col].nunique() == 2
        ]

        self.categorical_cols_ = [
            col for col in X.columns if 3 <= X[col].nunique() < 7
        ]

        self.numerical_cols_ = [
            col for col in X.columns
            if col not in self.binary_cols_ + self.categorical_cols_
        ]

        # -------------------------
        # Transformers
        # -------------------------
        binary_transformer = OrdinalEncoder(
            handle_unknown="use_encoded_value",
            unknown_value=-1
        )

        categorical_transformer = OneHotEncoder(
            handle_unknown="ignore",
            sparse_output=False
        )

        numerical_transformer = (
            StandardScaler() if self.scaling else "passthrough"
        )

        # -------------------------
        # ColumnTransformer
        # -------------------------
        self.column_transformer_ = ColumnTransformer(
            transformers=[
                ("bin", binary_transformer, self.binary_cols_),
                ("cat", categorical_transformer, self.categorical_cols_),
                ("num", numerical_transformer, self.numerical_cols_),
            ],
            remainder="drop"
        )

        self.column_transformer_.fit(X)

        return self

    def transform(self, X):
        X = X.copy()
        return self.column_transformer_.transform(X)

    def get_feature_names_out(self):
        feature_names = []

        # Binary
        feature_names.extend(self.binary_cols_)

        # Categorical (OHE)
        cat_features = self.column_transformer_.named_transformers_[
            "cat"
        ].get_feature_names_out(self.categorical_cols_)
        feature_names.extend(cat_features)

        # Numerical
        feature_names.extend(self.numerical_cols_)

        return feature_names
