# Nanode Explorer
## http://ledgerfiles.banano.cc/
The purpose of this project is to create a front end for a Nano node. Nano is a feeless cryptocurrency with a growing userbase. When I first heard about it a few years back it was under a dollar. Today it seems to have grown signigicantly and still running stable. I have decided to create my own Node monitor in order to expand my understanding of the mechanics behind the block chain. My end goal is to create a time series database on Nanos growth and full on block chain explorer.


## Requirements:
### Nano / Banano Node running. 
Setup is out of scope of this readme. Please refer to official documentation for your specific os. 
#### Banano node setup
```https://github.com/BananoCoin/banano#running-a-docker-node```
#### Nano node setup
```https://docs.nano.org/running-a-node/node-setup/```

#### Python 3.11
```bash
pip install django
```



## Contact:
I am available for hire for custom blockchain work. I only ask for high pay and high patience. Working on financial systems make me nervous, it is important to get it done right the first time. Money is on the line and I have seen too many amateur developers get devoured alive by simple mistakes. 
#### Email: ```freelance@datasource.blog```

## Donate
#### Nano Wallet Address: ```nano_ajksdhasdaj```
#### Banano Wallet Address: ```nano_ajksdhasdaj```
#### BTC Wallet Address: ```nano_ajksdhasdaj```
#### LTC Wallet Address: ```nano_ajksdhasdaj```
#### KOFI Wallet Address: ```nano_ajksdhasdaj```


# Action wallet_create
    curl -d '{ "action": "wallet_create"}' http://127.0.0.1:7072
    "wallet": "B001237DAC3F4C2E3D299C8E0DB4C7D6E1176D312DF6EBB2114905FF5C43B6AA"



    docker exec ${NANO_CONTAINER_NAME} nano_node --wallet_decrypt_unsafe --wallet E3E67B1B3FFA46F606240F1D0B964873D42E9C6D0B7A0BF376A2E128541CC446
# docker exec 1f64c0e3a500 bananode --wallet_decrypt_unsafe --wallet B001237DAC3F4C2E3D299C8E0DB4C7D6E1176D312DF6EBB2114905FF5C43B6AA
    Seed: A1D142963628733FF5BED3561B4CDCAE05A55F8C08F9FDEEA016B6820663670D


## change password 
```    
curl -d '{ "action": "password_change", "wallet": "B001237DAC3F4C2E3D299C8E0DB4C7D6E1176D312DF6EBB2114905FF5C43B6AA", "password": "KOP3BPgOPSest2eEH9oSAqvTR39v53dE6v"}' http://127.0.0.1:7072
```

## enter password  to unlock it
```    
curl -d '{ "action": "password_enter", "wallet": "B001237DAC3F4C2E3D299C8E0DB4C7D6E1176D312DF6EBB2114905FF5C43B6AA", "password": "KOP3BPgOPSest2eEH9oSAqvTR39v53dE6v"}' http://127.0.0.1:7072
```


## Create accoutns for the waller
```    
curl -d '{ "action": "account_create", "wallet": "B001237DAC3F4C2E3D299C8E0DB4C7D6E1176D312DF6EBB2114905FF5C43B6AA"}' http://127.0.0.1:7072
```
```
    ban_3pjf6h7o38oi7em7o4615n484xzyc1eat5qsiygtz6oentpoansq1keyrkcx
    "account": "ban_3qb49yycn55oip55i4uqxxsn9kb4d37iwozrdjuyekp46965md6tjr35a4tw"
    "account": "ban_1trfc8xp43qsawcoqbq4ohmf7eb1aiyufip9c6qbhtzp3sq4tb658k6b1ihz"
    "account": "ban_11xegqyua6gmburwmusr61q3fttewm7ghz77t7ojqts3w1dc9efkg7beqgmd"

```

`// Colors



sass --no-source-map bulma.sass:css/bulma_generated.css
