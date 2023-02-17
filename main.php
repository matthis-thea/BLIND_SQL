<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
</head>
<body>
<h1>Formulaire entrainement</h1>
<p> Saisissez votre identifiant et votre mot de passe</p>
<form method="post" action="main.php">
	Identifiant : <input type="text" name="identif"><br>
	Mot de passe :<input type="password" name="mdp"><br>
	<input type="submit" value="submit" />
</form>
<?php
if (isset($_POST['mdp']) && isset($_POST['identif']))
{
	// echo "Traitement du formulaire <br>";
	$identif = $_POST['identif'];
	$mdp = $_POST['mdp'];
	try
	{
		$con = new PDO('mysql:host=localhost;dbname=eni;charset=utf8', 'root', '92Ilastreetonestla&');
		echo ("Connexion au serveur de BDD<br>");
		$req = "SELECT nom, prenom FROM utilisateurs WHERE identifiant='".$identif."' AND motdepasse='".$mdp."';";
		echo ("Envoie de la requête $req <br>");
		$rep = $con->query($req);
		if ($rep)
		{
			$lignes = $rep->fetchAll();
			if ($lignes)
			{
				echo("<hr>");
				echo("Votre nom est ".$lignes[0]['nom']." et votre prénom est ".$lignes[0]['prenom']."");
			}
			else
				echo("Mauvais identifiant ou mot de passe !");
		}
		else
			echo ("Champ vide !");
		$con = null;
	}
	catch (PDOException $e)
	{
		print("Erreur de connexion ! <br>");
		die();
	}
}
?>
</body>
</html>