song_library = [("Ripples", "Maximillian"),
                ("Working", "Khalid ft. Tate McRae"),
                ("Perfectly Imperfect", "Declan J Donovan"),
                ("Easy On Me", "Adele"),
                ("Still Alive", "Maximilliian"),
                ("Rolling in the deep", "Adele")]

artists = set()
for song, artist in song_library:
    artists.add(artist)

print(artists)

print(3*"\n")

my_artist = {"Maximillian", "Khalid", "Adele", "Declan J Donovan", "Jay Z"}

autuburns_artists = {"Jay Z", "Eminem", "Khalid", "XXXTentacion", "Juice World"}

print("ALL: {}".format(my_artist.union(autuburns_artists)))
print("Both: {}".format(autuburns_artists.intersection(my_artist)))
print("Either but not Both: {}".format(my_artist.symmetric_difference(autuburns_artists)))

print(3*"\n")

print("My Artist is to autuburns_artists:")
print("issuperset: {}".format(my_artist.issuperset(autuburns_artists)))
print("issubset: {}".format(my_artist.issubset(autuburns_artists)))
print("difference: {}".format(my_artist.difference(autuburns_artists)))
print("\n")
print("My autuburns_artists is to Artist:")
print("issuperset: {}".format(autuburns_artists.issuperset(my_artist)))
print("issubset: {}".format(autuburns_artists.issubset(my_artist)))
print("difference: {}".format(autuburns_artists.difference(my_artist)))
