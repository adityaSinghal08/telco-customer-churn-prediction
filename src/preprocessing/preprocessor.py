import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler


class Preprocessor(BaseEstimator, TransformerMixin):
    """
    Custom preprocessing transformer.

    Parameters
    ----------
    scaling : bool, default=False
        Whether to apply StandardScaler to numerical features.
    """

    def __init__(self, scaling: bool = False):
        self.scaling = scaling

    def fit(self, X, y=None):
        # Defensive copy
        X = X.copy()

        # Identify categorical and numerical columns
        self.categorical_cols_ = [
            col for col in X.columns if X[col].nunique() < 7
        ]

        self.numerical_cols_ = [
            col for col in X.columns if col not in self.categorical_cols_
        ]

        # Define transformers
        categorical_transformer = OneHotEncoder(
            handle_unknown="ignore",
            sparse_output=False
        )

        numerical_transformer = (
            StandardScaler() if self.scaling else "passthrough"
        )

        # Build ColumnTransformer
        self.column_transformer_ = ColumnTransformer(
            transformers=[
                ("cat", categorical_transformer, self.categorical_cols_),
                ("num", numerical_transformer, self.numerical_cols_),
            ],
            remainder="drop"
        )

        # Fit transformer
        self.column_transformer_.fit(X)

        return self

    def transform(self, X):
        X = X.copy()
        return self.column_transformer_.transform(X)

    def get_feature_names_out(self):
        cat_features = self.column_transformer_.named_transformers_[
            "cat"
        ].get_feature_names_out(self.categorical_cols_)

        num_features = self.numerical_cols_

        return list(cat_features) + list(num_features)
