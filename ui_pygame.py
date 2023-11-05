import pygame as pg

ui_strings = []

#to link dispatch and ui
def init_stack_for_user():
    global stack_for_user
    stack_for_user = []
    return stack_for_user

def get_user_settings(screen : pg.display, dict_1, dict_2):
    H = 40
    screen.fill((255, 255, 255))
    font_1 = pg.font.Font(None, 24)

    text_1_1 = font_1.render("Введи инструкции в формате:", False, (0, 0, 0))
    text_1_2 = font_1.render("A 'space' B 'kp enter'", False, (0, 0, 0))

    screen.blit(text_1_1, (screen.get_width()//2-100, H))
    H+= 40
    screen.blit(text_1_2, (screen.get_width()//2-100, H))
    H+= 40 


    if len(stack_for_user) > 1 and stack_for_user[-1] == chr(pg.K_RETURN):
        ui_strings.append(''.join(stack_for_user[:-1:]))
        list.clear(stack_for_user)

    if len(stack_for_user) == 1 and stack_for_user[-1] == chr(pg.K_RETURN):
        str_text = font_1.render("Press p to continue", False, (0, 0, 0))
        screen.blit(str_text, (screen.get_width()//2-100, H))
    
    user_text = font_1.render(''.join(stack_for_user), False, (0, 0, 0))

    screen.blit(user_text, (screen.get_width()//2-100, H))
    H+= 40

    for str in ui_strings:
        str_text = font_1.render(str, False, (0, 0, 0))
        screen.blit(str_text, (screen.get_width()//2-100, H))
        H+=40




