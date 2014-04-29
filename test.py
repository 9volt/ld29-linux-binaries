import re

find_links_re = re.compile(r"<p class='links'>(.*)</p>")

s = """
d='compo2'><p><a href='?action=default'>Back to Rate Entries</a></p><h3>A failed journey to the middle of the Earth - Balint197 - <i>48 Hour Compo Entry</i></h3><p class='links'><a href="http://db.orangedox.com/bZcMKpypwYCqswdpmp/LD-Default-1.0.0.0.exe" target='_blank'>Windows</a></p><p>Game description:
<br/>
<br/>It is a 1v1 local multiplayer game. Try to get a friend playing! 
<br/>
<br/>Player 1: arrows to move, shift to shoot
<br/>Player 2: &quot;w&quot; &quot;a&quot; &quot;d&quot; to move , &quot;v&quot; to shoot
<br/>
<br/>You die if you get shot 3 times, or if you fall into lava! Enjoy :)
<br/>
<br/>Story: You were two explorers going down to the core of the Earth, but you start shooting each other, because you cant agree whether the uncrackable pistacchios should be cracked or thrown away! :D You also have jetpacks because why not? :D
<br/>
<br/>I used Game Maker Studio (I only have Standard)
<br/>
<br/>Hi everyone!
<br/>
<br/>So this is my first Ludum Dare game! I was really excited about what I could do in 48 hours, but it turned out I only had less than a day... oh well. On the first day when I couldn't really get into making the game i was trying to figure out the idea for it. At first I was thinking about a game where you are a giant worm-thing eating people, but i turned it down, because i knew that there was another game about it( i cant remember its name though) :D I was thinking about a mining game like Super Motherload, but i thought that a lot of people would be making a game like that. I was also thinking about making a bank-tunnel drilling simulator, but i though it would be boring. I always like to bring something new to my games, and i couldn't think of any with this theme :( So i made a generic 1v1 local MP game! I hope you enjoy, try to get a friend to play with!
<br/>
<br/>What went good:
<br/>
<br/>*graphics are better than expected and as usual, but it still looks awful IMO :D
<br/>
<br/>*solid code 
<br/>
<br/>*gameplay: the bullet hit, screenshake part was new for me
<br/>
<br/>What went wrong:
<br/>
<br/>*i couldn't find a good idea with the theme
<br/>
<br/>*not enough encouragement to fight (in gameplay)
<br/>
<br/>What I learned:
<br/>
<br/>Next time I will be making a more interesting game even if I don't like the theme. I could have made one of my ideas with a little tweak to the gameplay. I will definitely attend the next LD48, because I enjoyed it despite my idea.
<br/>
<br/>Still, I hope you enjoy the game, I would be happy if you would comment any suggestions!
<br/>
<br/>Greetings from Hungary! :D
<br/>Balint, 17</p><table><tr><td colspan=4 align=center><a href='http://www.ludumdare.com/compo/wp-content/compo2/342546/34465-shot0.png' target='_blank'><img src='http://www.ludumdare.com/compo/wp-content/compo2/thumb/8e267f338161b7f6c7ed53a9933c277d.jpg'></a><tr><td><a href='http://www.ludumdare.com/compo/wp-content/compo2/342546/34465-shot1.png' target='_blank'><img src='http://www.ludumdare.com/compo/wp-content/compo2/thumb/fef0b28471d90b4b03aac8207a219612.jpg'></a></table><p><a href='http://www.ludumdare.com/compo/?category_name=ld-29&author_name=balint197' target='_blank'>View Balint197's journal.</a> | <a href="../author/balint197/" target='_blank'>View all entries by Balint197</a></p><meta name="twitter:card" content="summary" /><meta name="twitter:site" content="@ludumdare" /><meta name="twitter:title" content="A failed journey to the middle of the Earth" /><meta name="twitter:description" content="Game description:



It is a 1v1 local multiplayer game. Try to get a friend playing! 



Player 1: arrows to move, shift to shoot

Player 2: &quot;w&quot; &quot;a&quot; &quot;d&quot; to move , &quot;" /><meta name="twitter:image" content="http://www.ludumdare.com/compo/wp-content/compo2/342546/34465-shot0.png" /><script>var Elm = document.getElementsByTagName("title")[0];Elm.innerHTML = "A failed journey to the middle of the Earth by Balint197 | " + Elm.innerHTML;</script><h3>Rate this 48 Hour Compo Entry</h3><p><i>If you can't run this entry, please leave a comment saying so and explaining why.  Do not score unrunnable entries.</i></p>more stuff</a>
"""

print(find_links_re.findall(s))
