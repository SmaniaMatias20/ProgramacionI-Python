import sys
import pygame as py
import os

def rescale_images(animations: dict, widht: int, height: int):
    """
    Brief: Reescala las imágenes en las animaciones a las dimensiones especificadas.

    Descripción:
        Esta función toma un diccionario de animaciones, donde las claves son nombres de animaciones
        y los valores son listas de imágenes. Reescala cada imagen en todas las animaciones al ancho
        y alto especificados.

    Parámetros:
        - animations (dict): Diccionario de animaciones.
        - width (int): Nuevo ancho de las imágenes.
        - height (int): Nuevo alto de las imágenes.

    Retorno:
        Ninguno
    """
    for key in animations:
        for i in range(len(animations[key])):
            img = animations[key][i]
            animations[key][i] = py.transform.scale(img, (widht, height))

def flip_images(images: list):
    """
    Brief: Voltea horizontalmente las imágenes en la lista.

    Descripción:
        Esta función toma una lista de imágenes y las voltea horizontalmente.

    Parámetros:
        - images (list): Lista de imágenes.

    Retorno:
        list: Lista de imágenes volteadas horizontalmente.
    """
    list_images = []
    for i in range(len(images)):
        flip_image = py.transform.flip(images[i],True,False)
        list_images.append(flip_image)
    
    return list_images


# DB 
DB = r"Modules\Data\scores.db"

# ATMOSPHERE
GAME_ICON = r"Modules\Assets\Images\icon.png" 
PLATFORM_IMAGE = r"Modules\Assets\Images\Atmosphere\platform.png"
BACKGROUND_IMAGE = r"Modules\Assets\Images\Atmosphere\background.png" 

# HERO
HERO_QUIET = r"Modules\Assets\Images\Hero\hero.png"
HERO_WALK_RIGHT_A = r"Modules\Assets\Images\Hero\hero-1.png"
HERO_WALK_RIGHT_B = r"Modules\Assets\Images\Hero\hero-2.png"
HERO_WALK_RIGHT_C = r"Modules\Assets\Images\Hero\hero-3.png"
HERO_WALK_RIGHT_D = r"Modules\Assets\Images\Hero\hero-4.png"
HERO_WALK_RIGHT_E = r"Modules\Assets\Images\Hero\hero-5.png"
HERO_JUMP = r"Modules\Assets\Images\Hero\hero-6.png"
PROJECTILE =r"Modules\Assets\Images\Hero\projectile.png" 
ONE_LIVE =r"Modules\Assets\Images\Hero\1-3.png" 
TWO_LIVE =r"Modules\Assets\Images\Hero\2-3.png"
THREE_LIVE =r"Modules\Assets\Images\Hero\3-3.png" 

# ITEMS
COIN = r"Modules\Assets\Images\Item\coin.png"
CROWN = r"Modules\Assets\Images\Item\crown.png"
STAR = r"Modules\Assets\Images\Item\star.png"
GEM = r"Modules\Assets\Images\Item\gem.png"

# ENEMY
ENEMY_WALK_RIGHT_A = r"Modules\Assets\Images\Enemy\enemy-1.png" 
ENEMY_WALK_RIGHT_B = r"Modules\Assets\Images\Enemy\enemy-2.png" 
ENEMY_WALK_RIGHT_C = r"Modules\Assets\Images\Enemy\enemy-3.png"
ENEMY_WALK_RIGHT_D = r"Modules\Assets\Images\Enemy\enemy-4.png"
ENEMY_WALK_RIGHT_E = r"Modules\Assets\Images\Enemy\enemy-5.png"
ENEMY_WALK_RIGHT_F = r"Modules\Assets\Images\Enemy\enemy-6.png"
ENEMY_WALK_RIGHT_G = r"Modules\Assets\Images\Enemy\enemy-7.png"
ENEMY_WALK_RIGHT_H = r"Modules\Assets\Images\Enemy\enemy-8.png"

# TRAP
TRAP_ONE = r"Modules\Assets\Images\Trap\trap.png"
TRAP_TWO = r"Modules\Assets\Images\Trap\trap-1.png"

# FALLING OBJECTS
STONE = r"Modules\Assets\Images\Falling\stone.png"  

# BOSS
BOSS_WALK_RIGHT_A = r"Modules\Assets\Images\Boss\boss-1.png"
BOSS_WALK_RIGHT_B = r"Modules\Assets\Images\Boss\boss-2.png"
BOSS_WALK_RIGHT_C = r"Modules\Assets\Images\Boss\boss-3.png"
BOSS_WALK_RIGHT_D = r"Modules\Assets\Images\Boss\boss-4.png"
BOSS_WALK_RIGHT_E = r"Modules\Assets\Images\Boss\boss-5.png"
BOSS_WALK_RIGHT_F = r"Modules\Assets\Images\Boss\boss-6.png"
BOSS_WALK_RIGHT_G = r"Modules\Assets\Images\Boss\boss-7.png"
BOSS_WALK_RIGHT_H = r"Modules\Assets\Images\Boss\boss-8.png"
BOSS_WALK_RIGHT_I = r"Modules\Assets\Images\Boss\boss-9.png"

BOSS_QUIET_A = r"Modules\Assets\Images\Boss\boss-quiet-1.png"
BOSS_QUIET_B = r"Modules\Assets\Images\Boss\boss-quiet-2.png"
BOSS_QUIET_C = r"Modules\Assets\Images\Boss\boss-quiet-3.png"
FIRE = r"Modules\Assets\Images\Boss\fire.png"

# SOUND
COIN_SOUND = r"Modules\Assets\Music\coin.mp3"
ZOMBIE_SOUND = r"Modules\Assets\Music\zombie.mp3" 
PROJECTILE_SOUND =r"Modules\Assets\Music\projectile.mp3" 
BANG_SOUND =  r"Modules\Assets\Music\bang.mp3" 
STAR_SOUND = r"Modules\Assets\Music\star.mp3"
TRAP_SOUND =  r"Modules\Assets\Music\trap.mp3"
GEM_SOUND =  r"Modules\Assets\Music\gem.mp3" 
FIRE_SOUND =   r"Modules\Assets\Music\fire.mp3" 
BACKGROUND_SOUND =r"Modules\Assets\Music\background.mp3" 
GAME_SOUND = r"Modules\Assets\Music\game.mp3"  
SCREAM_SOUND = r"Modules\Assets\Music\scream.mp3"

# MENU
TABLE =r"Modules\Assets\Images\Menu\table.png"
CONFIG = r"Modules\Assets\Images\Menu\config.png"
WINDOW = r"Modules\Assets\Images\Menu\window.png"
HOME =  r"Modules\Assets\Images\Menu\home.png"
SOUND =  r"Modules\Assets\Images\Menu\sound.png"
PAUSE = r"Modules\Assets\Images\Menu\pause.png"


# script_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
# script_dir_without_values = os.path.dirname(os.path.dirname(script_dir))

# # DB 

# DB = os.path.join(script_dir_without_values,'Modules', 'Data', 'scores.db') 

# # ATMOSPHERE
# GAME_ICON = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'icon.png') 
# PLATFORM_IMAGE = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Atmosphere', 'platform.png') 
# BACKGROUND_IMAGE = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Atmosphere', 'background.png')

# # HERO
# HERO_QUIET = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Hero', 'hero.png')
# HERO_WALK_RIGHT_A = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Hero', 'hero-1.png')
# HERO_WALK_RIGHT_B = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Hero', 'hero-2.png')
# HERO_WALK_RIGHT_C = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Hero', 'hero-3.png') 
# HERO_WALK_RIGHT_D = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Hero', 'hero-4.png') 
# HERO_WALK_RIGHT_E = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Hero', 'hero-5.png') 
# HERO_JUMP = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Hero', 'hero-6.png')
# PROJECTILE = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Hero', 'projectile.png')
# ONE_LIVE = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Hero', '1-3.png')
# TWO_LIVE = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Hero', '2-3.png')
# THREE_LIVE = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Hero', '3-3.png')

# # ITEMS
# COIN = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Item', 'coin.png')
# CROWN = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Item', 'crown.png')
# STAR = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Item', 'star.png')
# GEM = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Item', 'gem.png') 

# # ENEMY
# ENEMY_WALK_RIGHT_A = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Enemy', 'enemy-1.png')
# ENEMY_WALK_RIGHT_B = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Enemy', 'enemy-2.png')
# ENEMY_WALK_RIGHT_C = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Enemy', 'enemy-3.png')
# ENEMY_WALK_RIGHT_D = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Enemy', 'enemy-4.png')
# ENEMY_WALK_RIGHT_E = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Enemy', 'enemy-5.png')
# ENEMY_WALK_RIGHT_F = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Enemy', 'enemy-6.png')
# ENEMY_WALK_RIGHT_G = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Enemy', 'enemy-7.png')
# ENEMY_WALK_RIGHT_H = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Enemy', 'enemy-8.png')

# # TRAP
# TRAP_ONE = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Trap', 'trap.png') 
# TRAP_TWO = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Trap', 'trap-1.png') 

# # FALLING OBJECTS
# STONE = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Falling', 'stone.png')  

# # BOSS
# BOSS_WALK_RIGHT_A = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Boss', 'boss-1.png')
# BOSS_WALK_RIGHT_B = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Boss', 'boss-2.png')
# BOSS_WALK_RIGHT_C = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Boss', 'boss-3.png')
# BOSS_WALK_RIGHT_D = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Boss', 'boss-4.png')
# BOSS_WALK_RIGHT_E = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Boss', 'boss-5.png')
# BOSS_WALK_RIGHT_F = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Boss', 'boss-6.png')
# BOSS_WALK_RIGHT_G = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Boss', 'boss-7.png')
# BOSS_WALK_RIGHT_H = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Boss', 'boss-8.png')
# BOSS_WALK_RIGHT_I = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Boss', 'boss-9.png')

# BOSS_QUIET_A = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Boss', 'boss-quiet-1.png')
# BOSS_QUIET_B = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Boss', 'boss-quiet-2.png')
# BOSS_QUIET_C = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Boss', 'boss-quiet-3.png')
# FIRE = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Boss', 'fire.png')

# # SOUND
# COIN_SOUND = os.path.join(script_dir_without_values,'Modules','Assets', 'Music', 'coin.mp3')  
# ZOMBIE_SOUND = os.path.join(script_dir_without_values,'Modules','Assets', 'Music', 'zombie.mp3')  
# PROJECTILE_SOUND = os.path.join(script_dir_without_values,'Modules','Assets', 'Music', 'projectile.mp3')  
# BANG_SOUND = os.path.join(script_dir_without_values,'Modules','Assets', 'Music', 'bang.mp3')  
# STAR_SOUND = os.path.join(script_dir_without_values,'Modules','Assets', 'Music', 'star.mp3') 
# TRAP_SOUND = os.path.join(script_dir_without_values,'Modules','Assets', 'Music', 'trap.mp3') 
# GEM_SOUND = os.path.join(script_dir_without_values,'Modules','Assets', 'Music', 'gem.mp3')  
# FIRE_SOUND = os.path.join(script_dir_without_values,'Modules','Assets', 'Music', 'fire.mp3')   
# BACKGROUND_SOUND = os.path.join(script_dir_without_values,'Modules','Assets', 'Music', 'background.mp3') 
# GAME_SOUND = os.path.join(script_dir_without_values,'Modules','Assets', 'Music', 'game.mp3')  
# SCREAM_SOUND = os.path.join(script_dir_without_values,'Modules','Assets', 'Music', 'scream.mp3')

# # MENU
# TABLE = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Menu', 'table.png') 
# CONFIG = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Menu', 'config.png') 
# WINDOW = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Menu', 'window.png') 
# HOME = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Menu', 'home.png')  
# SOUND = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Menu', 'sound.png')  
# PAUSE = os.path.join(script_dir_without_values,'Modules','Assets', 'Images', 'Menu', 'pause.png')  


# print(f"{script_dir_without_values}")