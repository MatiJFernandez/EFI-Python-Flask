from flask_wtf import FlaskForm
from wtforms import (
    DecimalField,
    IntegerField,
    SelectField,
    StringField,
    SubmitField,
)
from wtforms.validators import (
    DataRequired,
    Length, 
)

class MarcaForm(FlaskForm):
    # Campo para el nombre del proveedor
    nombre = StringField(
        'Nombre  ',
        validators=[Length(min=3, max=100), DataRequired()],
        render_kw={"class": "form-control", "placeholder": "Nombre"}
    )

    # Campo para el contacto del proveedor (por ejemplo, teléfono o correo)
    modelo = StringField(
        'Modelo',
        validators=[Length(min=3, max=50), DataRequired()],
        render_kw={"class": "form-control", "placeholder": "Modelo"}
    )

    # Botón de envío
    submit = SubmitField(
        'Agregar',
        render_kw={"class": "form-control btn btn-success"}
    )
    