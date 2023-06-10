import requests
import tkinter as tk

def search_pokemon():
    pokemon_name = entry.get().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        name_label.config(text="Name: " + pokemon_data["name"].capitalize())
        height_label.config(text="Height: " + str(pokemon_data["height"]))
        weight_label.config(text="Weight: " + str(pokemon_data["weight"]))

        sprite_url = pokemon_data["sprites"]["front_default"]
        
        if sprite_url:
            sprite_response = requests.get(sprite_url)
            sprite_data = sprite_response.content
            image = tk.PhotoImage(data=sprite_data)
            image_label.config(image=image)
            image_label.image = image
        else:
            image_label.config(image='')
    else:
        name_label.config(text="Pokémon not found")
        height_label.config(text="")
        weight_label.config(text="")
        image_label.config(image='')

root = tk.Tk()
root.title("Pokémon Search")

search_frame = tk.Frame(root)
search_frame.pack(pady=10)

entry = tk.Entry(search_frame, font=('Arial', 14))
entry.pack(side=tk.LEFT, padx=10)

search_button = tk.Button(search_frame, text="Search", command=search_pokemon)
search_button.pack(side=tk.LEFT)

info_frame = tk.Frame(root)
info_frame.pack(pady=10)

name_label = tk.Label(info_frame, text="")
name_label.pack()

height_label = tk.Label(info_frame, text="")
height_label.pack()

weight_label = tk.Label(info_frame, text="")
weight_label.pack()

image_label = tk.Label(root)
image_label.pack(pady=10)

root.mainloop()
