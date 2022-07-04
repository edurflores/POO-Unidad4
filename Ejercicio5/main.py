from VistaPacientes import PacientesView
from ObjectEncoder import ObjectEncoder
from Mpacientes import ManejaPaciente
from Controlador import Controlador
if __name__ == "__main__":
    encoder = ObjectEncoder()
    try: 
        aux=encoder.Leer("Pacientes.json")
        aux=encoder.Decoder(aux)
    except FileNotFoundError:
        aux=ManejaPaciente()
    vista=PacientesView()
    control=Controlador(vista, aux)
    vista.setControlador(control)
    control.start()
    encoder.Guardar(control.salir(), "Pacientes.json") 