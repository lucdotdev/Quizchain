import hashlib
from bitcoinlib.services.services import Service
import praw
import csv


# Initialisation de l'API Reddit
reddit = praw.Reddit(
    client_id='',
    client_secret='',
    user_agent='',
    password="",
    username=""
)
def readDataFromCSV(filename):

    with open(filename, mode='r') as file:
        reader = csv.reader(file, delimiter=',')
        data = []
        for row in reader:
            data.append(row)
        return data
    
def saveDataToCSV(data, filename):
    with open(filename, mode='w', newline='\r\n') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(data)   

def getTransactionHashFromReddit():



    subreddit_name = 'bitcoinpuzzles'
    
    subreddit = reddit.subreddit(subreddit_name)


    posts = subreddit.new();

    hashs = []

    for post in posts:
        print(f"Titre du post : {post.title}")
        print("Liens trouvés dans le texte du post :")
        # Si le post a un texte
        if post.selftext:
            # Division du texte en lignes et recherche des liens
            lignes = post.selftext.split('\n')
            for ligne in lignes:
                if 'http' in ligne:
                    # Impression du lien
                    if "https://www.smartbit.com.au/tx/" in ligne:
                        print(ligne)
                        hashs.append(ligne.replace("https://www.smartbit.com.au/tx/", "").strip())
        print("-------------------------")

    saveDataToCSV(hashs, "v1/hashs.csv")
    return hashs





def getTransactionDetails(transaction_hash):

    # Initialiser le service Bitcoin
    service = Service('bitcoin')

    # Obtenir les détails de la transaction
    transaction = service.gettransaction(transaction_hash)

    adresses = []

    # Afficher les détails de la transaction
    print("Détails de la transaction:")
    print("ID de la transaction:", transaction.txid)
    for input_tx in transaction.inputs:
        adresses.append(input_tx.address)
        print("   Adresse source:", input_tx.address)
    print("Sorties de la transaction:")
    for output_tx in transaction.outputs:
        adresses.append(output_tx.address)
        print("   Adresse de destination:", output_tx.address)
    
    saveDataToCSV(adresses, "v1/adresses.csv")
    return adresses


def main():

    solutionhashstart = 'f8e'
    adressess = []

    solutions =[]

    md5 = []

    for i in getTransactionHashFromReddit():
        adressess.extend(getTransactionDetails(i))

    

    for i in adressess:
        solution = "Bitcoin Grycoin TOMI " + str(i)[0:1].replace("1", "7") + str(i)[1:]

        solutions.append(solution)

        print("Solution proposée: ", solution)
        hash = hashlib.md5(solution.encode('utf-8')).hexdigest()

        md5.append(hash)
        if(hash[0:3] == solutionhashstart):
            print("Solution trouvée: ", solution)
            break;
    
    saveDataToCSV(solutions, "v1/solutions.csv")
    saveDataToCSV(md5, "v1/md5.csv")
    print("Fin du programme")
    

main();
