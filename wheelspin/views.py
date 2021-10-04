from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
import random,math,string

ERROR = JsonResponse({
    "RES" : "ERROR"
})

def home(request, *args, **kwargs):
    try:
        code = kwargs.get('ref_code')
        profile = RefferUser.objects.get(code=code)
        request.session['ref_profile'] =  profile.id
    except:
        pass

    result = "WON"
    results = GameDetails.objects.filter(result=result).order_by('-id')[:10]
    context = {
        "results": results,
    }
    return render(request, 'wheelspin/index.html', context)

def err404(request, *args, **kwargs):
    return render(request, 'wheelspin/404.html')

def about(request, *args, **kwargs):
    return render(request, 'wheelspin/about.html')

def affiliate(request, *args, **kwargs):
    return render(request, 'wheelspin/affiliate.html')

def awards(request, *args, **kwargs):
    return render(request, 'wheelspin/awards.html')

def bonus(request, *args, **kwargs):
    return render(request, 'wheelspin/bonus.html')

def cart(request, *args, **kwargs):
    return render(request, 'wheelspin/cart.html')

def contact(request, *args, **kwargs):
    return render(request, 'wheelspin/contact.html')

def faq(request, *args, **kwargs):
    return render(request, 'wheelspin/faq.html')

def howItWork(request, *args, **kwargs):
    return render(request, 'wheelspin/how-it-work.html')

def lottery(request, *args, **kwargs):
    return render(request, 'wheelspin/lottery.html')

def play(request, *args, **kwargs):
    return render(request, 'wheelspin/play.html')

def termsConditionsDetails(request, *args, **kwargs):
    return render(request, 'wheelspin/terms-conditions-details.html')

def termsConditions(request, *args, **kwargs):
    return render(request, 'wheelspin/terms-conditions.html')

def tournaments(request, *args, **kwargs):
    return render(request, 'wheelspin/tournaments.html')

def game(request, *args, **kwargs):
    return render(request, 'wheelspin/wheelgame.html')

def slots(request, *args, **kwargs):
    slots = Slots.objects.all()
    lof = []
    for slot in slots:
        if slot.bet not in lof:
            lof.append(slot.bet)
    return render(request, 'wheelspin/slots.html',{
        'lof':lof
    })

def slotlist(request,bet, *args, **kwargs):
    slots = Slots.objects.filter(bet=int(bet))
    return render(request, 'wheelspin/slotlist.html',{
        "slots":slots
    })

def gameresults(request, *args, **kwargs):
    username = request.user.id
    results = GameDetails.objects.filter(username=username).order_by('-id')[:10]
    context = {
        "results": results,
        "nextid": 10,
        "preid" : -10
    }
    return render(request, 'wheelspin/gameresults.html', context)

def nextGresult(request, id):

    id = int(id)
    username = request.user.id
    results = GameDetails.objects.filter(username=username).order_by('-id')[id:id+10]
    context = {
        "results": results,
        "nextid": id + 10,
        "preid": id - 10
    }
    return render(request, 'wheelspin/gameresults.html', context)

def preGresult(request, id):
    id = int(id)
    username = request.user.id
    results = GameDetails.objects.filter(username=username).order_by('-id')[id:id+10]
    context = {
        "results": results,
        "nextid": id + 10,
        "preid": id - 10
    }
    return render(request, 'wheelspin/gameresults.html', context)


def transactions(request, *args, **kwargs):
    return render(request, 'wheelspin/transactions.html')
def exchange(request, *args, **kwargs):
    return render(request, 'wheelspin/exchange.html')
def inplay(request, *args, **kwargs):
    user_obj = User.objects.get(id=request.user.id)
    rooms = Rooms.objects.filter(users_m=user_obj)
    running = []
    for room in rooms:
        if room.status == "RUNNING":
            running.append(room)
    return render(request, 'wheelspin/inplay.html',{
        'rooms':running
    })
def prejoin(request, *args, **kwargs):
    return render(request, 'wheelspin/prejoin.html')


@login_required
def reqForROOM(request,bet,total):
    slots = Slots.objects.all()
    valid = False
    bet,total = int(bet),int(total)
    for slot in slots:
        if slot.bet==bet and slot.capacity==total:
            valid = True
    if not valid:
        return ERROR 
    isBroke = Credits.objects.get(user_f=request.user.id)
    if isBroke.amount < bet:
        return ERROR
    exist =  Rooms.objects.filter(status = "RUNNING",bet=bet,total=total)
    if exist:
        room = exist[0]
        me = User.objects.get(id=request.user.id)    
        active_users = sum([1 for user in room.users_m.all()])
        alreadyIN = [user for user in room.users_m.all() if user.username == me.username]
        if alreadyIN:
            return redirect('wheelspin:room',room_name = room.room_name)
        if active_users < room.total:
            room.users_m.add(me)
            cutMONEYCOMPANYV2(room,me)
            return redirect('wheelspin:room',room_name = room.room_name)
        else:
            return ERROR
    else:
        me = User.objects.get(id=request.user.id)
        createRoom = Rooms(
            room_name = roomGEN(),
            bet = bet,
            deg = -1,
            total = total
        )
        createRoom.save()
        createRoom.users_m.add(me)
        cutMONEYCOMPANYV2(createRoom,me)
        return redirect('wheelspin:room',room_name = createRoom.room_name)

@login_required
def room(request, room_name, *args, **kwargs):
    exist =  Rooms.objects.get(room_name=room_name,status = "RUNNING")
    if not exist:
        return ERROR
    userValid = User.objects.get(id=request.user.id)
    isValid = [user for user in exist.users_m.all() if user.username == userValid.username]
    activeCouter = sum([1 for user in exist.users_m.all()])
    if isValid:
        return render(request,'wheelspin/room.html',{
            'room_name': room_name,
            'activeCouter' : activeCouter,
            'total' : exist.total,
            'bet' : exist.bet
        })
    else:
        return ERROR

@login_required
def wheelgame(request,room_name, *args, **kwargs):
    exist =  Rooms.objects.get(room_name=room_name)
    if not exist:
        return ERROR
    # EXIST
    userValid = User.objects.get(id=request.user.id)
    isValid = [user for user in exist.users_m.all() if user.username == userValid.username]
    activeCouter = sum([1 for user in exist.users_m.all()])
    if exist.status == "RUNNING" and exist.total == activeCouter and isValid:        
        # old cutMoney
        exist.status = "FINISHED"
        deg = random.randint(1,359)
        if exist.total == 2:
            per = 360/(exist.total * 5)
            win_index = (exist.total-1) - (((math.ceil(deg/per)) - 1) % 2)
        elif exist.total == 3:
            per = 360/(exist.total * 4)
            win_index = (exist.total-1) - (((math.ceil(deg/per)) - 1) % 3)
        elif exist.total == 4:
            per = 360/(exist.total * 3)
            win_index = (exist.total-1) - (((math.ceil(deg/per)) - 1) % 4)
        elif exist.total > 4 and exist.total < 10:
            per = 360/(exist.total * 2)
            win_index = (exist.total-1) - (((math.ceil(deg/per)) - 1) % exist.total)
        else:
            per = 360/(exist.total)
            win_index = (exist.total-1) - ((math.ceil(deg/per)) - 1)
        allParticipents = [user for user in exist.users_m.all()]
        exist.winner = allParticipents[win_index].username
        exist.deg = deg
        addMoneyToWinner(exist,allParticipents[win_index].username)
        exist.showed.add(userValid)
        exist.save()
        
        userlist = [user.username for user in exist.users_m.all()]
        return render(request, 'wheelspin/wheelgame.html',{
            'room_name' : room_name,
            'userlist' : userlist,
            'deg' : deg ,
            'winner' : exist.winner
        })
    elif exist.status == "FINISHED" and exist.total == activeCouter and isValid:
        isShownToYou = [user for user in exist.showed.all() if user.username == userValid.username]
        if not isShownToYou:
            deg = exist.deg
            winner = exist.winner
            exist.showed.add(userValid)
            exist.save()
            countShow = sum([1 for user in exist.showed.all()])
            userlist = [user.username for user in exist.users_m.all()]
            if countShow == activeCouter:
                exist.delete()
            return render(request, 'wheelspin/wheelgame.html',{
                'room_name' : room_name,
                'userlist' : userlist,
                'deg' : deg ,
                'winner' : winner
            })
        else:
            ERROR
    else:
        return ERROR


def cutMONEYCOMPANY(room):
    for user in room.users_m.all():
        slot = Slots.objects.get(bet=room.bet,capacity=room.total)
        cutMoney = Credits.objects.get(user_f=user.id)
        cutMoney.amount = cutMoney.amount - (room.bet*(slot.charge/100)) #THA
        cutMoney.save()

def cutMONEYCOMPANYV2(room,user):
    cutMoney = Credits.objects.get(user_f=user.id)
    cutMoney.amount = cutMoney.amount - (room.bet)
    cutMoney.save()

def addMoneyToWinner(room,username):
    couter = sum([1 for user in room.users_m.all()])
    slot = Slots.objects.get(bet=room.bet,capacity=room.total)
    user = User.objects.get(username=username)
    addmoney = Credits.objects.get(user_f=user.id)
    addmoney.amount = addmoney.amount + ((room.bet)*room.total)*(1-(slot.charge/100)) + room.bet #THA
    addmoney.save()
    
    refPer = RefBonus.objects.all()
    refPer = refPer[0].percent
    print("\n"*20)

    ifREFBUDDY = RefferUser.objects.get(user = user)
    print(ifREFBUDDY.ref_by)
    if (ifREFBUDDY.ref_by):
        cutDDT = ((room.bet)*room.total)*((slot.charge/100)*(refPer/100))
        saveME = RefBonusDetails(
            from_user=user,
            to_user=ifREFBUDDY.ref_by,
            bonus=cutDDT
        )
        saveME.save()

        cdet = Credits.objects.get(user_f=ifREFBUDDY.ref_by.id)
        cdet.amount = cdet.amount + cutDDT
        cdet.save()
        
    else:
        pass

    for user in room.users_m.all():
        gTrans = GameDetails(
            username=user,
            slot=room.bet,
            capcity=room.total,
            result="WON" if room.winner==user.username else "LOST",
            charge=((room.bet)*room.total)*(1-(slot.charge/100)) if room.winner==user.username else (-room.bet) #THA
        )
        gTrans.save()

def roomGEN(size=30, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

@login_required
def leave_room(request,room_name):
    exist =  Rooms.objects.get(room_name=room_name,status = "RUNNING")
    if not exist:
        return ERROR
    userValid = User.objects.get(id=request.user.id)
    isValid = [user for user in exist.users_m.all() if user.username == userValid.username]
    activeCouter = sum([1 for user in exist.users_m.all()])
    if isValid:
        exist.users_m.remove(userValid)
        cutReturnMONEYCOMPANYV2(exist,userValid)
        exist.save()
        return render(request,'wheelspin/index.html')
    else:
        return ERROR

def cutReturnMONEYCOMPANYV2(room,user):
    cutMoney = Credits.objects.get(user_f=user.id)
    cutMoney.amount = cutMoney.amount + (room.bet)
    cutMoney.save()

@login_required
def profile(request):
    username = request.user.id
    results = GameDetails.objects.filter(username=username).order_by('-id')[:10]
    context = {
        "results": results,
    }
    return render(request,'wheelspin/profile.html', context)

