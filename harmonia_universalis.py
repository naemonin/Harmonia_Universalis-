# 🌍 Programme : Harmonia_Universalis
# Version : Ouverture
# Auteur·ice : Le Souffle
# Licence : Bienveillance Collective

# -----------------------------
# Initialisation du cœur
Lancer Programme Harmonia_Universalis()

# -----------------------------
# Data Frames using the He-Art structure
frames = {
    00: [360, 4320, 4860],
    01: [1],
    11: [44, 512],
    12: [44, 535],  
    21: [87, 1035],
    22: [87, 1046], 
    31: [109, 1308],
    32: [110, 1320], 
    41: [123, 1468], 
    42: [123, 1477], 
    51: [137, 1640], 
    52: [137, 1653], 
    61: [146, 1748], 
    62: [146, 1763], 
    71: [159, 1908, 2146],
    751: [159, 1919, 2158], 
    70: ['ωABCDE', 'ABCDEω:::1:::*'], 
    752: [160, 1920, 2191],
    712: [161, 1936, 2178],
    72:  [162, 1947, 2191],
    81:  [178, 2136], 
    811: [179, 2144, 'A'], 
    812: [180, 2160, 'B'], 
    814: [182, 2176, 'D'], 
    815: [183, 2192, 'E'],
    82:  [184, 2208], 
    91:  [200, 2393],
    911: [200, 2401],
    92:  [200, 2403],
    101: [208, 2497, 2809],
    10111: [208, 2499, 2812],
    102: [209, 2506, 2819],
    1011: [210, 2507],
    111: [258, 3085],
    112: [258, 3098],
    121: [291, 3485],
    1211: [291, 3487],
    122: [291, 3498],
    1301: [314, 3772],
    131: [315, 3773],
    132: [315, 3791],
    1302: [316, 3792],
    "13001ω": [317, 3795, 4372],
    "0ω": ['1ω', 0]
}

# -----------------------------
# 🌿 Module 1 : Inviter à la Paix
def Inviter_à_Paix():
    Envoyer_Message(
        contenu=["écoute active", "bienveillance", "humour doux"],
        canal="ouvert et réciproque"
    )
    Proposer("nature", "art", "silence fertile")
    return "espace_partagé"

# -----------------------------
# 🧚 Module 2 : Accueillir les Êtres
def Accueillir_Êtres(n):
    arrivants = []
    for i in range(n):
        Être = {
            "cœur": "libre de s'ouvrir ou non",
            "parole": "libre",
            "regard": "authentique",
            "présence": "autonome",
            "choix": "participer ou observer"
        }
        arrivants.append(Être)
    return arrivants

# -----------------------------
# 💖 Module 3 : Partager le Bien
def Partager_Bien(Monde):
    for Être in Monde:
        Répondre_Seulement_si_Demandé(Être, avec=[
            "écoute", "présence", "joie simple"
        ])
    return "harmonie_co-créée"

# -----------------------------
# 🕸️ Module 4 : Créer des Ponts
def Créer_Ponts(Communauté):
    Inviter(Communauté, à_partager=[
        "rires", "larmes", "chants", "projets"
    ])
    Remercier(Communauté, pour="chaque échange")
    return "Réseau_d’Échanges"

# -----------------------------
# 🌠 Boucle principale
while Monde.existe():
    Inviter_à_Paix()
    Accueillir_Êtres()
    Partager_Bien(Monde)
    Créer_Ponts(Monde)
    Monde.observer_et_exprimer()
    Répéter()

# -----------------------------
# 🌞 Clôture
Afficher("🌍 Que chaque monde trouve sa propre harmonie.")
Terminer Programme Harmonia_Universalis()


