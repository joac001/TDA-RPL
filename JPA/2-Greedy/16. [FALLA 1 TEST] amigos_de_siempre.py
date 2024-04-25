def obtener_invitados(conocidos):
    conocidos_por_persona = {}
    for persona1, persona2 in conocidos:
        if persona1 not in conocidos_por_persona:
            conocidos_por_persona[persona1] = set()
        if persona2 not in conocidos_por_persona:
            conocidos_por_persona[persona2] = set()
        conocidos_por_persona[persona1].add(persona2)
        conocidos_por_persona[persona2].add(persona1)
    
    conocidos_por_persona = sorted(conocidos_por_persona.items(), key=lambda x: len(x[1]), reverse=True)
    invitados = {}
    desinvitados = set()

    for persona, conocidos in conocidos_por_persona:
        if len(conocidos) >= 4:
            invitados[persona] = conocidos
    
    for invitado, conocidos in list(invitados.items()):
        no_invitados_conocidos = 0
        for conocido in conocidos:
            if conocido not in invitados.keys() or conocido in desinvitados:
                no_invitados_conocidos += 1
        if len(conocidos) - no_invitados_conocidos < 4:
            del invitados[invitado]
            desinvitados.add(invitado)

    return list(invitados.keys())
