imena = [ "ADI", "BVIDIA", "PINTEL", "KAMEKA", "XIOC" ]
nastavci = [ "OVERLOCK", "M", "TESS", "PARMESAN", "RAFT", "SNOO", "DUKE" ]

i = 0
while i < 100 do
	#  ime|cpu|ocjena|cijena
	puts imena.sample + " " + nastavci.sample + rand(0..1000).to_s + "|" + rand(2..1000).to_s + "|" + rand(1..10).to_s + "|" + rand(200..1000).to_s
	i+=1
end