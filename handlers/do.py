import webapp2
from webapp2_extras import jinja2


class DoHandler(webapp2.RequestHandler):
    def post(self):
        grados_txt = self.request.get("edGrados", "ERROR")  # Identificador dentro del form, si no ERROR por defecto
        jinja = jinja2.get_jinja2(app=self.app)
        farenheit = (float(grados_txt) * 1.8) + 32
        sust = {
            "celsius": grados_txt,
            "farenheit": str(farenheit)
        }
        self.response.write(jinja.render_template("respuesta.html", **sust))


app = webapp2.WSGIApplication([
    ('/do', DoHandler)
], debug=True)