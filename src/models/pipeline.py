""" from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.pipeline import Pipeline """

#from gradient_boosting_model.processing import preprocessors as pp
#from gradient_boosting_model.config.core import config

#import logging


""" _logger = logging.getLogger(__name__)


model_pipe = Pipeline(
    [
        (
            "numerical_imputer",
            pp.SklearnTransformerWrapper(
                variables=config.model_config.numerical_vars,
                transformer=SimpleImputer(strategy="most_frequent"),
            ),
        ),
        (
            "gb_model",
            GradientBoostingRegressor(
                loss=config.model_config.loss,
                random_state=config.model_config.random_state,
                n_estimators=config.model_config.n_estimators,
            ),
        ),
    ]
) """
