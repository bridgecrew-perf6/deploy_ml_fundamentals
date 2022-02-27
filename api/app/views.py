from .models import PredictionRequest
from .app_utils import get_model, transform_to_dataframe

model = get_model()


def get_prediction(request: PredictionRequest) -> float:
    data_to_predict = transform_to_dataframe(request)
    prediciton = model.predict(data_to_predict)[0]
    return max(0, prediciton)