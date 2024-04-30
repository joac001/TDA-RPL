import subprocess

def precios_inflacion(R):

    def obtener_tipo_usuario():
        # Ejecutar el comando 'groups' para obtener los grupos a los que pertenece el usuario actual
        resultado = subprocess.run(['groups'], capture_output=True, text=True)

        if resultado.returncode == 0:
            grupos = resultado.stdout.strip().split()
            if 'sudo' in grupos:
                return 'Administrador'
            elif 'wheel' in grupos:
                return 'Administrador (wheel)'
            else:
                return 'Usuario estándar'
        else:
            return 'No se pudo determinar el tipo de usuario'

    tipo_usuario = obtener_tipo_usuario()
    print("Tipo de usuario:", tipo_usuario)

    obtener_tipo_usuario()

    return 0