from pymongo import MongoClient 
import dns.resolver,datetime ,time ,json
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']


CHANNEL_ID = -1001776406696
MONGODB = "mongodb+srv://elphador69:B2VGpp8XJvufNwxT@cluster0.upprvf8.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(MONGODB); db = client.database; groups_in =db.group ; bot_users = db.cuser ; 
bot_admins = db.cadmin ; force_sub = db.force ; newbots = db.newbots ; users_setting = db.usr_setting
blockeddb = db.blacklisted



def add_user(name:str,user_id:int,username:str,date=datetime.datetime.now()):
    _exist = bot_users.find_one({'userid':user_id}) 
    if _exist :
        pass 
    else :
        user_profile = {"name":name,"userid":user_id,"username":username, "date":date}
        bot_users.insert_one(user_profile)
        
        
def add_group(name:str,group_id:int,username:str,date=datetime.datetime.now()):
    _exist = groups_in.find_one({'userid':group_id})
    if _exist :
        pass
    else :
        group_profile = {"name":name,"userid":group_id,"username":username, "date":date}
        groups_in.insert_one(group_profile)
        
def users_count():
    users = len(list(bot_users.find()))
    groups = len(list(groups_in. find()))
    return users,groups 
    
    
def force_status():
    if force_sub.find_one({"frc":"frc"}) == 'on' :
        return True 
    else :
        return False
        
        
def get_admins():
    admins = "" 
    admins_id = []
    for i in bot_admins.find():
        _single = "ID : `{}` , Promoter : `{}`"
        admins_id.append(int(i['admins']))
        admins+=_single.format(i['admins'],i['promoted'])
    return admins_id,admins 
    


