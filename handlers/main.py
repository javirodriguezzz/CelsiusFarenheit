#!/usr/bin/env python
#
# El programa acepta unos grados en un formulario, y visualiza como respuesta ese valor convertido a grados Celsius, y
# el mismo valor convertido a grados Farenheit. Realiza comprobaciones en el formulario para estar seguro de que lo
# introducido es un numero, es decir, ni esta vacio ni contiene letras o simbolos.
#
import webapp2
from webapp2_extras import jinja2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        plantilla = {

        }
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template(
            "index.html", **plantilla
        ))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
