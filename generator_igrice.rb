imena = [ "TEA GAMES -", "SALVE -", "BEZVEZDA -", "RITO GAMES -", "UBILAGANO -", "MOJANGULAR -" ]
nastavci = [ "CALL OF THE DOOTLE ", "FIFO ", "DOTO ", "MINEKEMPF ", "GRASS GROWING SIMULATOR ", "THE LEMMINGS ", "WATCH CATS ", "FALLIN " ]
zanr = [ "ACTION", "FANTASY", "SF", "ADVENTURE", "STEAMPUNK", "INDY", "MANAGEMENT", "SIMULATION", "RPG", "CASUAL" ]

i = 0
while i < 200 do
	#  ime|zanr|min_cpu|min_gra_cpu|min_gra_ram|min_ram|ocjena|cijena
	puts imena.sample + " " + nastavci.sample + rand(0..10).to_s + "|" + zanr.sample + "|" + rand(2..1000).to_s + "|" + rand(2..1000).to_s + "|" + rand(2..1000).to_s + "|" + rand(2..1000).to_s + "|" + rand(1..10).to_s + "|" + rand(5..200).to_s
	i+=1
end