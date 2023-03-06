"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):xx
    if power_pellet_active == True & touching_ghost == True:
        return True
    else:
        return False



def score(touching_power_pellet, touching_dot):
    if touching_power_pellet == True or touching_dot == True:
        return True
    else:
        return False


def lose(power_pellet_active, touching_ghost):
    if power_pellet_active != True & touching_ghost != False:
        return True
    else:
        return False


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    if has_eaten_all_dots == True & power_pellet_active == True & touching_ghost == True:
        return True
    elif has_eaten_all_dots == True & power_pellet_active == True & touching_ghost == False:
        return True
    elif has_eaten_all_dots == True & power_pellet_active == True & touching_ghost != True:
        return True
    elif has_eaten_all_dots == True & power_pellet_active == False or True & touching_ghost == False:
        return True
    else:
        return False
    
    
    

print(win(True, True, False))
print(win(True, False, False))
    
# %%
