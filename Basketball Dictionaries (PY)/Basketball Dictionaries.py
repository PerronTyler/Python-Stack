# kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}
# jason = {"name": "Jason Tatum", "age":24, "position": "small forward", "team": "Boston Celtics"}
# kyrie = {"name": "Kyrie Irving", "age":32,"position": "Point Guard", "team": "Brooklyn Nets"}
# damian = {"name": "Damian Lillard", "age":33,"position": "Point Guard", "team": "Portland Trailblazers"}
# joel = {"name": "Joel Embiid", "age":32,"position": "Power Foward", "team": "Philidelphia 76ers"}
# demar = {"name": "DeMar DeRozan","age": 32,"position": "Shooting Guard","team": "Chicago Bulls"}
players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33,
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32,
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

kevin = players[0]
jason = players[1]
kyrie = players[2]
damian = players[3]
joel = players[4]
demar = players[5]

class Player:
    def __init__(self, Player):
        self.name = Player["name"]
        self.age = Player["age"]
        self.position = Player["position"]
        self.team = Player["team"]

player_kevin = Player(kevin)
player_jason = Player(jason)
player_kyrie = Player(kyrie)
player_damian = Player(damian)
player_joel = Player(joel)
player_demar = Player(demar)

print(player_kevin)
print(kevin)
print(player_damian.name)