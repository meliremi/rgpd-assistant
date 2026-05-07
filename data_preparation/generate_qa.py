import json

# Tes 50 questions intégrées pour éviter les erreurs d'API au début
MANUAL_QA_DATA = [
    {"question": "Qu'est-ce qu'une donnée à caractère personnel ?", "answer": "Toute information se rapportant à une personne physique identifiée ou identifiable (nom, IP, numéro de sécurité sociale)."},
    {"question": "Quel est l'objectif principal du RGPD ?", "answer": "Protéger les libertés et droits fondamentaux des personnes physiques à l'égard du traitement de leurs données."},
    {"question": "Qui est le 'Responsable de traitement' ?", "answer": "L'entité qui détermine les finalités et les moyens du traitement des données."},
    {"question": "Qu'est-ce qu'un 'Sous-traitant' ?", "answer": "La personne physique ou morale qui traite des données pour le compte du responsable de traitement."},
    {"question": "Quelle est la durée de conservation des données ?", "answer": "Elles ne doivent pas être conservées plus longtemps que nécessaire aux finalités pour lesquelles elles sont traitées."},
    {"question": "Qu'est-ce que le consentement explicite ?", "answer": "Une manifestation de volonté libre, spécifique, éclairée et univoque par laquelle la personne accepte le traitement."},
    {"question": "Peut-on retirer son consentement ?", "answer": "Oui, la personne concernée a le droit de retirer son consentement à tout moment aussi simplement qu'elle l'a donné."},
    {"question": "Qu'est-ce que le 'Droit à l'oubli' ?", "answer": "Le droit d'obtenir l'effacement de données à caractère personnel dans les meilleurs délais."},
    {"question": "Qu'est-ce que la portabilité des données ?", "answer": "Le droit de recevoir ses données dans un format structuré et couramment utilisé pour les transmettre à un autre responsable."},
    {"question": "Quand la désignation d'un DPO est-elle obligatoire ?", "answer": "Pour les autorités publiques ou si les activités de base impliquent un suivi régulier et systématique à grande échelle."},
    {"question": "Quel est le rôle de la CNIL en France ?", "answer": "Elle est l'autorité de contrôle chargée de veiller à la protection des données personnelles."},
    {"question": "Quel est le montant maximum des amendes administratives ?", "answer": "Jusqu'à 20 millions d'euros ou 4 % du chiffre d'affaires annuel mondial total de l'exercice précédent."},
    {"question": "Qu'est-ce qu'un traitement de données sensibles ?", "answer": "Traitement révélant l'origine raciale, les opinions politiques, les données de santé ou l'orientation sexuelle."},
    {"question": "Le RGPD s'applique-t-il aux entreprises hors UE ?", "answer": "Oui, s'ils ciblent des résidents de l'UE ou surveillent leur comportement au sein de l'Union."},
    {"question": "Qu'est-ce que le principe de 'Minimisation' ?", "answer": "Les données doivent être adéquates, pertinentes et limitées à ce qui est nécessaire."},
    {"question": "Qu'est-ce qu'une violation de données ?", "answer": "Un incident de sécurité entraînant la destruction, la perte, l'altération ou la divulgation non autorisée de données."},
    {"question": "Sous quel délai faut-il notifier une violation à la CNIL ?", "answer": "Dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance."},
    {"question": "Doit-on informer les personnes en cas de fuite de données ?", "answer": "Oui, si la violation est susceptible d'engendrer un risque élevé pour leurs droits et libertés."},
    {"question": "Qu'est-ce que l'AIPD (ou PIA) ?", "answer": "Une analyse d'impact relative à la protection des données pour les traitements à haut risque."},
    {"question": "Qu'est-ce que le principe de 'Transparence' ?", "answer": "L'obligation d'informer clairement l'utilisateur sur la manière dont ses données sont utilisées."},
    {"question": "Qu'est-ce que le 'Privacy by Design' ?", "answer": "L'intégration de la protection des données dès la conception d'un produit ou service."},
    {"question": "Qu'est-ce que le 'Privacy by Default' ?", "answer": "Garantir que, par défaut, seules les données nécessaires sont traitées."},
    {"question": "Quelles sont les bases légales d'un traitement ?", "answer": "Consentement, contrat, obligation légale, sauvegarde des intérêts vitaux, mission de service public, intérêt légitime."},
    {"question": "Un enfant peut-il consentir seul ?", "answer": "À partir de 15 ans en France (l'âge peut varier entre 13 et 16 ans selon les pays de l'UE)."},
    {"question": "Qu'est-ce que le droit d'accès ?", "answer": "Le droit pour une personne d'obtenir la confirmation que ses données sont traitées et d'en recevoir une copie."},
    {"question": "Qu'est-ce que le droit de rectification ?", "answer": "Le droit d'obtenir la correction de données inexactes ou incomplètes."},
    {"question": "Qu'est-ce que le droit à la limitation ?", "answer": "Le droit de geler l'utilisation des données pendant une période donnée (ex: temps d'une vérification)."},
    {"question": "Qu'est-ce que le 'Registre des traitements' ?", "answer": "Un document recensant toutes les activités de traitement de données d'une organisation."},
    {"question": "Qui doit tenir un registre des traitements ?", "answer": "Toutes les entreprises de plus de 250 salariés, ou celles dont le traitement présente un risque ou n'est pas occasionnel."},
    {"question": "Quelles informations doit contenir le registre ?", "answer": "Finalités, catégories de données, destinataires, délais de conservation, mesures de sécurité."},
    {"question": "Qu'est-ce qu'un transfert de données hors UE ?", "answer": "L'envoi de données vers un pays tiers ne garantissant pas forcément un niveau de protection adéquat."},
    {"question": "Comment sécuriser un transfert hors UE ?", "answer": "Via une décision d'adéquation, des clauses contractuelles types (CCT) ou des règles d'entreprise contraignantes (BCR)."},
    {"question": "Le DPO peut-il être sanctionné pour ses avis ?", "answer": "Non, il doit pouvoir exercer ses missions en toute indépendance, sans recevoir d'instructions."},
    {"question": "À qui le DPO rend-il compte ?", "answer": "Directement au niveau le plus élevé de la direction de l'organisme."},
    {"question": "Qu'est-ce qu'un profilage ?", "answer": "Un traitement automatisé consistant à utiliser des données pour évaluer certains aspects de la personnalité d'une personne."},
    {"question": "Peut-on s'opposer au profilage ?", "answer": "Oui, la personne a le droit de ne pas faire l'objet d'une décision fondée exclusivement sur un traitement automatisé."},
    {"question": "Qu'est-ce que l'intérêt légitime ?", "answer": "Une base légale permettant de traiter des données sans consentement si cela ne lèse pas les droits de la personne."},
    {"question": "Qu'est-ce que le 'Guichet unique' ?", "answer": "Le mécanisme permettant à une entreprise présente dans plusieurs pays de l'UE de n'avoir qu'une seule autorité référente."},
    {"question": "Qu'est-ce que le CEPD (EDPB) ?", "answer": "Le Comité Européen de la Protection des Données qui regroupe les autorités de contrôle de l'UE."},
    {"question": "Qu'est-ce que l'exactitude des données ?", "answer": "L'obligation de tenir les données à jour et d'effacer celles qui sont inexactes."},
    {"question": "Quelle est la différence entre anonymisation et pseudonymisation ?", "answer": "L'anonymisation est irréversible, la pseudonymisation permet de réidentifier la personne avec des infos supplémentaires."},
    {"question": "Les données de santé sont-elles protégées ?", "answer": "Oui, elles font partie des catégories particulières dont le traitement est par principe interdit (sauf exceptions)."},
    {"question": "Qu'est-ce que l'intégrité et la confidentialité ?", "answer": "Garantir que les données sont protégées contre le traitement non autorisé, la perte ou les dégâts."},
    {"question": "Qu'est-ce que la responsabilité (Accountability) ?", "answer": "L'obligation pour l'entreprise de démontrer qu'elle respecte le RGPD à tout moment."},
    {"question": "Combien de temps a une entreprise pour répondre à un droit d'accès ?", "answer": "Un mois maximum (prolongeable de deux mois en cas de complexité)."},
    {"question": "L'exercice des droits est-il gratuit ?", "answer": "Oui, en principe, l'entreprise ne peut pas facturer de frais pour répondre à une demande de droit."},
    {"question": "Que faire si une demande est manifestement infondée ?", "answer": "Le responsable peut soit exiger des frais raisonnables, soit refuser de donner suite à la demande."},
    {"question": "Qui est responsable en cas de sous-traitance ?", "answer": "Le responsable de traitement reste le garant, mais le sous-traitant a des obligations de sécurité spécifiques."},
    {"question": "Qu'est-ce qu'une autorité de contrôle ?", "answer": "Un organisme public indépendant institué par un État membre pour surveiller l'application du RGPD."},
    {"question": "Le RGPD s'applique-t-il aux données de personnes décédées ?", "answer": "Non, le RGPD ne s'applique qu'aux personnes vivantes, sauf dispositions nationales contraires."}
]

SYSTEM_PROMPT = """Tu es un expert en création de datasets pour LLM. 
A partir d'un passage RGPD, génère exactement 3 paires Q/R. 
Questions variées factuelles, analytiques, compréhension.
Réponses précises, complètes, basées uniquement sur le texte.
Retourne UNIQUEMENT un JSON valide."""

def generate_qa_pairs(client=None, chunk_text=None, use_manual=True):
    """
    Si use_manual est True, retourne les 50 questions intégrées.
    Sinon, appelle l'API pour générer à partir du texte.
    """
    if use_manual:
        return MANUAL_QA_DATA
    
    # Sinon, on utilise ton code original avec l'API
    prompt = f"{SYSTEM_PROMPT}\n\nTexte source: {chunk_text}"
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return json.loads(response.choices[0].message.content)

# Pour tester et générer le fichier JSON tout de suite :
if __name__ == "__main__":
    dataset = generate_qa_pairs(use_manual=True)
    with open("dataset_test_50.json", "w", encoding="utf-8") as f:
        json.dump(dataset, f, indent=4, ensure_ascii=False)
    print("Fichier dataset_test_50.json créé avec les 50 questions !")