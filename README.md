# Kaar-Leads-DB

## Eseguire il progetto

### Ambiente di sviluppo

In questo ambiente non viene usato nginx reverse proxy ed il server si riavvia quando vengono modificati i file, senza necessità di rebuildare il container

1. COPIARE `template.env` in `.env`
2. In `.env` inserire gli opportuni valori per tutte le variabili (più informazioni nella sezione successiva)
3. Eseguire il progetto con `./run_dev.sh` (esegue `docker-compose.yml`)

### Ambiente server di produzione

Questo dockerfile è modificato per un ambiente di produzione:

- Debug disattivato
- Uso del reverse proxy nginx
- Uso di gunicorn
- Migrazione delle tabelle e compilazione dei file statici all'avvio del container
- Non espone direttamente la porta ma utilizza dei label per segnalare al container di traefik su che dominio esporlo

## Variabili d'ambiente

- SECRET_KEY: stringa di caratteri casuali
- DEBUG: (facoltativo) impostare ad 1 per abilitare il debug
- EMAIL_HOST: host mail server
- EMAIL_HOST_PASSWORD: password account email
- EMAIL_HOST_USER: username account email
- EMAIL_PORT: porta mail server
- EMAIL_ADMIN: indirizzo email al quale inviare le email.
- CORS_HOST: hostname dal quale permettere cors, separati da virgole
- MYSQL_PASSWORD: password per il database. NON CAMBIARE DOPO LA CREAZIONE DEL DB

## Deployment

Sono stati creati due workflow per pubblicare l'applicazione sul server:

- Accesso tramite SSH ed esecuzione dei comandi per pullare le modifiche (modificare il nome della cartella nello script)
- Notifica tramite webhook ad un servizio di deployment (strategia preferita con Portainer)
