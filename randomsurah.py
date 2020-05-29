import random, sys

surahlist = ['Al-Fatihah (The Opening)','Al-Baqarah (The Cow)','Al-Imran (The Family of Amran)','An-Nisa (The Women)','Al-Maidah (The Food)','Al-Anam (The Cattle)','Al-Araf (The Elevated Places)','Al-Anfal (Voluntary Gifts)','Al-Baraat / At-Taubah(The Immunity)','Yunus (Jonah)','Hud (Hud)','Yusuf (Joseph)','Ar-Rad (The Thunder)','Ibrahim (Abraham)','Al-Hijr (The Rock)','An-Nahl (The Bee)','Bani Israil (The Israelites)','Al-Kahf (The Cave)','Maryam (Mary)','Ta Ha (Ta Ha)','Al-Anbiya (The Prophets)','Al-Hajj (The Pilgrimage)','Al-Muminun (The Believers)','An-Nur (The Light)','Al-Furqan (The Discrimination)','Ash-Shuara (The Poets)','An-Naml (The Naml)','Al-Qasas (The Narrative)','Al-Ankabut (The Spider)','Ar-Rum (The Romans)','Luqman (Luqman)','As-Sajdah (The Adoration)','Al-Ahzab (The Allies)','Al-Saba (The Saba)','Al-Fatir (The Originator)','Ya Sin (Ya Sin)','As-Saffat (Those Ranging in Ranks)','Sad (Sad)','Az-Zumar (The Companies)','Al-Mumin (The Believer)','Ha Mim (Ha Mim)','Ash-Shura (Counsel)','Az-Zukhruf (Gold)','Ad-Dukhan (The Drought)','Al-Jathiyah (The Kneeling)','Al-Ahqaf (The Sandhills)','Muhammad (Muhammad)','Al-Fath (The Victory)','Al-Hujurat (The Apartments)','Qaf (Qaf)','Ad-Dhariyat (The Scatterers)','At-Tur (The Mountain)','An-Najm (The Star)','Al-Qamar (The Moon)','Ar-Rahman (The Beneficent)','Al-Waqiah (The Event)','Al-Hadid (Iron)','Al-Mujadilah (The Pleading Woman)','Al-Hashr (The Banishment)','Al-Mumtahanah (The Woman who is Examined)','As-Saff (The Ranks)','Al-Jumuah (The Congregation)','Al-Munafiqun (The Hypocrites)','At-Taghabun (The Manifestation of Losses)','At-Talaq (Divorce)','At-Tahrim (The Prohibition)','Al-Mulk (The Kingdom)','Al-Qalam (The Pen)','Al-Haqqah (The Sure Truth)','Al-Maarij (The Ways of Ascent)','Nuh (Noah)','Al-Jinn (The Jinn)','Al-Muzzammil (The One Covering Himself)','Al-Muddaththir (The One Wrapping Himself Up)','Al-Qiyamah (The Resurrection)','Al-Insan (The Man)','Al-Mursalat (Those Sent Forth)','An-Naba (The Announcement)','An-Naziat (Those Who Yearn)','Abasa (He Frowned)','At-Takwir (The Folding Up)','Al-Infitar (The Cleaving)','At-Tatfif (Default in Duty)','Al-Inshiqaq (The Bursting Asunder)','Al-Buruj (The Stars)','At-Tariq (The Comer by Night)','Al-Ala (The Most High)','Al-Ghashiyah (The Overwhelming Event)','Al-Fajr (The Daybreak)','Al-Balad (The City)','Ash-Shams (The Sun)','Al-Lail (The Night)','Ad-Duha (The Brightness of the Day)','Al-Inshirah (The Expansion)','At-Tin (The Fig)','Al-Alaq (The Clot)','Al-Qadr (The Majesty)','Al-Bayyinah (The Clear Evidence)','Al-Zilzal (The Shaking)','Al-Adiyat (The Assaulters)','Al-Qariah (The Calamity)','At-Takathur (The Abundance of Wealth)','Al-Asr (The Time)','Al-Humazah (The Slanderer)','Al-Fil (The Elephant)','Al-Quraish (The Quraish)','Al-Maun (Acts of Kindness)','Al-Kauthar (The Abundance of Good)','Al-Kafirun (The Disbelievers)','An-Nasr (The Help)','Al-Lahab (The Flame)','Al-Ikhlas (The Unity)','Al-Falaq (The Dawn)','An-Nas (The Men)']
post = 0

if len(sys.argv) > 3:
	print("Too many arguments, just input 2 arguments.")
elif len(sys.argv) > 1:
	if sys.argv[1] == "-m":
		if len(sys.argv) > 2:
			if sys.argv[2].isdigit() == True:
				s_amount = int(sys.argv[2])
				while post < s_amount:
					print(random.choice(surahlist))
					post = post + 1
			else:
				print("Only Integer (Number)")
		else:
			print("Insert Amount Of Choice")
	else:
		print("Argument not found \n \n Argument List: \n -m amount :	Generate random choice more than one")
else:
	print(random.choice(surahlist))
