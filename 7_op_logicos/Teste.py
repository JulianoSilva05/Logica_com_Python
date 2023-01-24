recebe_distancia = float(input("Distancia da Viajem km: "))
recebe_velocidade_media = int(input("Velocidade media kmh: "))
tempo_horas = recebe_distancia / recebe_velocidade_media
tempo_minutos = tempo_horas * 60
print("A viajem vai levar {:.0f} Horas ou {:.0f} Minutos".format(tempo_horas, tempo_minutos))