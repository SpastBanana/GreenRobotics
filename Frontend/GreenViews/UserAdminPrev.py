from django.contrib.auth import get_user_model

def getPageInfo(userName, perms):

    activatedPerms = []
    passed = []

    availablePerms = [
        'GreenCameraOne',
        'GreenCameraTwo',
        'GreenSeedSystem',
        'GreenSystemAdmin',
        'GreenWatherSystem',
        'GreenWeedSystem',
        'GreenDatabase',
    ]

    for item in perms:
        if item not in passed:
            passed += item
            for perm in availablePerms:
                if perm in item:
                    print(perm)
                    activatedPerms.append([perm, True])
                else:
                    activatedPerms.append([perm, False])

    User = get_user_model()
    users = User.objects.all()
        

    data = {
        'page': 'UserAdmin/profile.html',
        'perms': activatedPerms,
        'username': userName,
        'users': users,
    }
    return data