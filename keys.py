import pygame

def key():
    key_map = {
    pygame.K_a: "a",
    pygame.K_b: "b",
    pygame.K_c: "c",
    pygame.K_d: "d",
    pygame.K_e: "e",
    pygame.K_f: "f",
    pygame.K_g: "g",
    pygame.K_h: "h",
    pygame.K_i: "i",
    pygame.K_j: "j",
    pygame.K_k: "k",
    pygame.K_l: "l",
    pygame.K_m: "m",
    pygame.K_n: "n",
    pygame.K_o: "o",
    pygame.K_p: "p",
    pygame.K_q: "q",
    pygame.K_r: "r",
    pygame.K_s: "s",
    pygame.K_t: "t",
    pygame.K_u: "u",
    pygame.K_v: "v",
    pygame.K_w: "w",
    pygame.K_x: "x",
    pygame.K_y: "y",
    pygame.K_z: "z",
    pygame.K_SPACE: " ",
    pygame.K_0: "0",
    pygame.K_1: "1",
    pygame.K_2: "2",
    pygame.K_3: "3",
    pygame.K_4: "4",
    pygame.K_5: "5",
    pygame.K_6: "6",
    pygame.K_7: "7",
    pygame.K_8: "8",
    pygame.K_9: "9",
    pygame.K_KP0: "0",
    pygame.K_KP1: "1",
    pygame.K_KP2: "2",
    pygame.K_KP3: "3",
    pygame.K_KP4: "4",
    pygame.K_KP5: "5",
    pygame.K_KP6: "6",
    pygame.K_KP7: "7",
    pygame.K_KP8: "8",
    pygame.K_KP9: "9",
    pygame.K_RIGHTPAREN: ")",
    pygame.K_COMMA: ",",
    pygame.K_MINUS: "-",
    pygame.K_PLUS: "+",
    pygame.K_PERIOD: ".",
    pygame.K_SEMICOLON: ";",
    pygame.K_EQUALS: "=",
    pygame.K_BACKSLASH: "\\",
    pygame.K_KP_PERIOD: ".",
    pygame.K_KP_DIVIDE: "/",
    pygame.K_KP_MULTIPLY: "*",
    pygame.K_KP_MINUS: "-",
    pygame.K_KP_PLUS: "+",
    pygame.K_KP_EQUALS: "=",
    }
    keys = pygame.key.get_pressed()
    
    for key in key_map:
        if keys[key]:
            return key_map[key]
        
def fun_key():
    key_map = {
    pygame.K_BACKSPACE: "backspace",
    pygame.K_TAB: "tab",
    pygame.K_RETURN: "enter",
    pygame.K_KP_ENTER: "enter",
    pygame.K_ESCAPE: "escape",
    pygame.K_LSHIFT: "shift",
    pygame.K_RSHIFT: "shift",
    pygame.K_LCTRL: "left ctrl",
    pygame.K_RCTRL: "right ctrl",
    pygame.K_LALT: "left alt",
    pygame.K_RALT: "right alt",
    pygame.K_CAPSLOCK: "caps lock",
    pygame.K_PAUSE: "pause",
    pygame.K_HOME: "home",
    }

    keys = pygame.key.get_pressed()
    
    for key in key_map:
        if keys[key]:
            return key_map[key]