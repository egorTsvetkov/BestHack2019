from app import app, db
from app.models import meals, info_meals, cart
from app import routes, models, errors

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'meals': meals, 'info_meals': info_meals, 'cart': cart}