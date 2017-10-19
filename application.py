from . import app
from .sasukekun_service.views import service
from .carwler.views import carwler

app.register_blueprint(service)
app.register_blueprint(carwler)
