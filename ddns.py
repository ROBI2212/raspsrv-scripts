# NEW VERSION OF DynamicDNS FOR CLOUDFLARE IN PYTHON
# 20.09.2025
# BY Robert Mazur

# NECESSARY IMPORTS
from cloudflare import Cloudflare
import public_ip as ip
import time

# CLOUDFLARE API CONFIG
def api_config():
    client = Cloudflare(
        api_token = "API_TOKEN_HERE"
    )
    token_verify = client.accounts.tokens.verify(
        account_id = "ACCOUNT_ID_HERE"
    )
    print("TOKEN VERIFY: "+token_verify.status)
    return client

# GETTING CURRENT IP FROM CLOUDFLARE
# IP IS GETTINTG FROM ONE OF DNS RECORD, WHO HAS OUR PUBLIC IP 
def get_cf_ip():
    record_details = client.dns.records.get(
        dns_record_id = "ID_RECORD_HERE",
        zone_id = "ZONE_ID_HERE"
    )
    return record_details.content

# CHECKING RECORDS WITH OLD PUBLIC IP AND UPDATE THEM
def update_records():
    record_details = client.dns.records.list(
        zone_id = "ZONE_ID_HERE"
    )
    for record in record_details:
        if record.content == old_ip:
            home_record_id = record.id
            home_record_name = record.name
            home_record_type = record.type
            record_update(home_record_id,home_record_name,home_record_type,pub_ip)

# UPDATE DNS RECORD
def record_update(record_id,record_name,record_type,new_ip):
    record_edit = client.dns.records.edit(
        dns_record_id = record_id,
        zone_id = "ZONE_ID_HERE",
        name = record_name,
        type = record_type,
        content = new_ip
    )
    print("UPDATE RECORD "+record_edit.name)


if __name__=="__main__":
    print(time.strftime("%d.%m.%Y %H:%M")+" - CHECKING IP")
    client = api_config()
    # GETTING PUBLIC IP
    old_ip = get_cf_ip()
    pub_ip = ip.get()
    print("NEW IP ADDR: "+pub_ip)
    print("CURRENT IP: "+old_ip)
    if old_ip != pub_ip:
        print("!CHANGING DNS RECORDS!")
        update_records()
    else:
        print("PUBLIC IP DOESN'T CHANGE. NO OPERATION.")