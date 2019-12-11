from easyAI import TwoPlayersGame, Human_Player, AI_Player, Negamax
from flask import Flask, render_template_string, request, make_response
import time

class TicTacToe3b(TwoPlayersGame):
    """ The board positions are numbered as follows:
            7 8 9
            4 5 6
            1 2 3
    """

    def __init__(self, players):
        self.players = players
        self.board = [0 for i in range(9)]
        self.nplayer = 1  # player 1 starts.

    def possible_moves(self):
        return [i + 1 for i, e in enumerate(self.board) if e == 0]

    def make_move(self, move):
        self.board[int(move) - 1] = self.nplayer

    def unmake_move(self, move):  # optional method (speeds up the AI)
        self.board[int(move) - 1] = 0

    WIN_LINES = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # horiz.
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # vertical
        [1, 5, 9], [3, 5, 7]  # diagonal
    ]

    def lose(self, who=None):
        """ Has the opponent "three in line ?" """
        if who is None:
            who = self.nopponent
        wins = [all(
            [(self.board[c - 1] == who) for c in line]
        ) for line in self.WIN_LINES]
        return any(wins)

    def is_over(self):
        return (self.possible_moves() == []) or self.lose(1) or \
            self.lose(2)

    def show(self):
        print ('\n' + '\n'.join([
            ' '.join(
                [['.', 'O', 'X'][self.board[3 * j + i]] for i in range(3)]
            )
            for j in range(3)
        ]))

    def spot_string(self, i, j):
        return ["_", "O", "X"][self.board[3 * j + i]]

    def scoring(self):
        #if self.nplayer = 1:
        #print('ddd')
        #print(self.nplayer)
        if self.nplayer == 1:
            opp_won = self.lose(1)
            i_won = self.lose(2)
            if opp_won and not i_won:
                return 100
            if i_won and not opp_won:
                return -100
            return 0
        elif self.nplayer == 2:
            opp_won = self.lose(2)
            i_won = self.lose(1)
            if opp_won and not i_won:
                return 100
            if i_won and not opp_won:
                return -100
            return 0

    def winner(self):
        if self.lose(who=2):
            return "AI Wins"
        return "Tie"



class TicTacToe3h(TwoPlayersGame):
    """ The board positions are numbered as follows:
            7 8 9
            4 5 6
            1 2 3
    """

    def __init__(self, players):
        self.players = players
        self.board = [0 for i in range(9)]
        self.nplayer = 1  # player 1 starts.

    def possible_moves(self):
        return [i + 1 for i, e in enumerate(self.board) if e == 0]

    def make_move(self, move):
        self.board[int(move) - 1] = self.nplayer

    def unmake_move(self, move):  # optional method (speeds up the AI)
        self.board[int(move) - 1] = 0

    WIN_LINES = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # horiz.
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # vertical
        [1, 5, 9], [3, 5, 7]  # diagonal
    ]

    def lose(self, who=None):
        """ Has the opponent "three in line ?" """
        if who is None:
            who = self.nopponent
        wins = [all(
            [(self.board[c - 1] == who) for c in line]
        ) for line in self.WIN_LINES]
        return any(wins)

    def is_over(self):
        return (self.possible_moves() == []) or self.lose(1) or \
            self.lose(2)

    def show(self):
        print ('\n' + '\n'.join([
            ' '.join(
                [['.', 'O', 'X'][self.board[3 * j + i]] for i in range(3)]
            )
            for j in range(3)
        ]))

    def spot_string(self, i, j):
        return ["_", "O", "X"][self.board[3 * j + i]]

    def scoring(self):
            opp_won = self.lose(who=self.nplayer)
            i_won = self.lose()
            if opp_won and not i_won:
                return -100
            if i_won and not opp_won:
                return 100
            return 0

    def winner(self):
        if self.lose(who=1):
            return "AI Wins"
        if self.lose(who=2):
            return "HUMAN Wins"
        return "Tie"
class TicTacToe53h(TwoPlayersGame):
    """ The board positions are numbered as follows:
            7 8 9
            4 5 6
            1 2 3
    """

    def __init__(self, players):
        self.players = players
        self.board = [0 for i in range(25)]
        self.nplayer = 1  # player 1 starts.

    def possible_moves(self):
        return [i + 1 for i, e in enumerate(self.board) if e == 0]

    def make_move(self, move):
        self.board[int(move) - 1] = self.nplayer

    def unmake_move(self, move):  # optional method (speeds up the AI)
        self.board[int(move) - 1] = 0

    WIN_LINES = [[1, 2, 3], [2, 3, 4], [3, 4, 5], [6, 7, 8], [7, 8, 9], [8, 9, 10], [11, 12, 13], [12, 13, 14],
                 [13, 14, 15], [16, 17, 18], [17, 18, 19], [18, 19, 20], [21, 22, 23], [22, 23, 24], [23, 24, 25],
                 [1, 6, 11], [6, 11, 16], [11, 16, 21], [2, 7, 12], [7, 12, 17], [12, 17, 22], [3, 8, 13], [8, 13, 18],
                 [13, 18, 23], [4, 9, 14], [9, 14, 19], [14, 19, 24], [5, 10, 15], [10, 15, 20],
                 [15, 20, 25], [1, 7, 13], [2, 8, 14], [3, 9, 15], [6, 12, 18], [7, 13, 19],
                 [8, 14, 20], [11, 17, 23], [12, 18, 24], [13, 19, 25],[15,19,23],[10,14,18],[14,18,22],[5,9,13],[9,13,17]
                 ,[13,17,21],[4,8,12],[8,12,16],[3,7,11]]


    def lose(self, who):
        """ Has the opponent "three in line ?" """
        if who is None:
            who = self.nopponent
        wins = [all(
            [(self.board[c - 1] == who) for c in line]
        ) for line in self.WIN_LINES]
        return any(wins)

    def is_over(self):
        return (self.possible_moves() == []) or self.lose(1) or \
            self.lose(2)

    def show(self):
        print ('\n' + '\n'.join([
            ' '.join(
                [['.', 'O', 'X'][self.board[5 * j + i]] for i in range(5)]
            )
            for j in range(3)
        ]))

    def spot_string(self, i, j):
        return ["_", "O", "X"][self.board[5 * j + i]]

    def scoring(self):
        opp_won = self.lose(2)
        i_won = self.lose(1)
        if opp_won and not i_won:
            return -100
        if i_won and not opp_won:
            return 1000
        return 0

    def winner(self):
        if self.lose(who=1):
            return "AI Wins"
        if self.lose(who=2):
            return "Human Wins"
        return "Tie"
class TicTacToe53b(TwoPlayersGame):
    """ The board positions are numbered as follows:
            7 8 9
            4 5 6
            1 2 3
    """

    def __init__(self, players):
        self.players = players
        self.board = [0 for i in range(25)]
        self.nplayer = 1  # player 1 starts.

    def possible_moves(self):
        return [i + 1 for i, e in enumerate(self.board) if e == 0]

    def make_move(self, move):
        self.board[int(move) - 1] = self.nplayer

    def unmake_move(self, move):  # optional method (speeds up the AI)
        self.board[int(move) - 1] = 0

    WIN_LINES =  [[1, 2, 3], [2, 3, 4], [3, 4, 5], [6, 7, 8], [7, 8, 9], [8, 9, 10], [11, 12, 13], [12, 13, 14],
                 [13, 14, 15], [16, 17, 18], [17, 18, 19], [18, 19, 20], [21, 22, 23], [22, 23, 24], [23, 24, 25],
                 [1, 6, 11], [6, 11, 16], [11, 16, 21], [2, 7, 12], [7, 12, 17], [12, 17, 22], [3, 8, 13], [8, 13, 18],
                 [13, 18, 23], [4, 9, 14], [9, 14, 19], [14, 19, 24], [5, 10, 15], [10, 15, 20],
                 [15, 20, 25], [1, 7, 13], [2, 8, 14], [3, 9, 15], [6, 12, 18], [7, 13, 19],
                 [8, 14, 20], [11, 17, 23], [12, 18, 24], [13, 19, 25],[15,19,23],[10,14,18],[14,18,22],[5,9,13],[9,13,17]
                 ,[13,17,21],[4,8,12],[8,12,16],[3,7,11]]
    def lose(self, who=None):
        """ Has the opponent "three in line ?" """
        if who is None:
            who = self.nopponent
        wins = [all(
            [(self.board[c - 1] == who) for c in line]
        ) for line in self.WIN_LINES]
        return any(wins)

    def is_over(self):
        return (self.possible_moves() == []) or self.lose(1) or \
            self.lose(2)

    def show(self):
        print ('\n' + '\n'.join([
            ' '.join(
                [['.', 'O', 'X'][self.board[5 * j + i]] for i in range(3)]
            )
            for j in range(3)
        ]))

    def spot_string(self, i, j):
        return ["_", "O", "X"][self.board[5 * j + i]]

    def scoring(self):
        opp_won = self.lose(who=self.nplayer)
        i_won = self.lose()
        if opp_won and not i_won:
            return -100
        if i_won and not opp_won:
            return 1000
        return 0

    def winner(self):
        if self.lose(who=1):
            return "X Wins"
        if self.lose(who=2):
            return "O Wins"
        return "Tie"

    
class TicTacToe5h(TwoPlayersGame):
    """ The board positions are numbered as follows:
            7 8 9
            4 5 6
            1 2 3
    """

    def __init__(self, players):
        self.players = players
        self.board = [0 for i in range(25)]
        self.nplayer = 1  # player 1 starts.

    def possible_moves(self):
        return [i + 1 for i, e in enumerate(self.board) if e == 0]

    def make_move(self, move):
        self.board[int(move) - 1] = self.nplayer

    def unmake_move(self, move):  # optional method (speeds up the AI)
        self.board[int(move) - 1] = 0

    WIN_LINES = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20],
                 [21, 22, 23, 24, 25], [1, 6, 11, 16, 21], [2, 7, 12, 17, 22], [3, 8, 13, 18, 23],
                 [4, 9, 14, 19, 24], [5, 10, 15, 20, 25], [1, 7, 13, 19, 25],[5,9,13,17,21]]


    def lose(self, who=None):
        """ Has the opponent "three in line ?" """
        if who is None:
            who = self.nopponent
        wins = [all(
            [(self.board[c - 1] == who) for c in line]
        ) for line in self.WIN_LINES]
        return any(wins)

    def is_over(self):
        return (self.possible_moves() == []) or self.lose(1) or \
            self.lose(2)

    def show(self):
        print ('\n' + '\n'.join([
            ' '.join(
                [['.', 'O', 'X'][self.board[5 * j + i]] for i in range(5)]
            )
            for j in range(3)
        ]))

    def spot_string(self, i, j):
        return ["_", "O", "X"][self.board[5 * j + i]]

    def scoring(self):
            opp_won = self.lose(who=self.nplayer)
            i_won = self.lose()
            if opp_won and not i_won:
                return -100
            if i_won and not opp_won:
                return 1000
            return 0
        #else:
            #opp_won = self.lose(1)
            #i_won = self.lose(who=self.nplayer)
            #if opp_won and not i_won:
            #    return 100
            #if i_won and not opp_won:
            #    return -100
            #return 0

    def winner(self):
        if self.lose(who=1):
            return "AI Wins"
        if self.lose(who=2):
            return "Human Wins"
        return "Tie"

class TicTacToe5b(TwoPlayersGame):
    """ The board positions are numbered as follows:
            7 8 9
            4 5 6
            1 2 3
    """

    def __init__(self, players):
        self.players = players
        self.board = [0 for i in range(25)]
        self.nplayer = 1  # player 1 starts.

    def possible_moves(self):
        return [i + 1 for i, e in enumerate(self.board) if e == 0]

    def make_move(self, move):
        self.board[int(move) - 1] = self.nplayer

    def unmake_move(self, move):  # optional method (speeds up the AI)
        self.board[int(move) - 1] = 0

    WIN_LINES = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20],
                 [21, 22, 23, 24, 25], [1, 6, 11, 16, 21], [2, 7, 12, 17, 22], [3, 8, 13, 18, 23],
                 [4, 9, 14, 19, 24], [5, 10, 15, 20, 25], [1, 7, 13, 19, 25],[5,9,13,17,21]]

    def lose(self, who=None):
        """ Has the opponent "three in line ?" """
        if who is None:
            who = self.nopponent
        wins = [all(
            [(self.board[c - 1] == who) for c in line]
        ) for line in self.WIN_LINES]
        return any(wins)

    def is_over(self):
        return (self.possible_moves() == []) or self.lose(1) or \
            self.lose(2)

    def show(self):
        print ('\n' + '\n'.join([
            ' '.join(
                [['.', 'O', 'X'][self.board[5 * j + i]] for i in range(3)]
            )
            for j in range(3)
        ]))

    def spot_string(self, i, j):
        return ["_", "O", "X"][self.board[5 * j + i]]

    def scoring(self):
            opp_won = self.lose(who=self.nplayer)
            i_won = self.lose()
            if opp_won and not i_won:
                return 1000
            if i_won and not opp_won:
                return -100
            return 0

    def winner(self):
        if self.lose(who=2) or self.lose(who=1):
            return "AI Wins"
        
        return "Tie"


app = Flask(__name__)
ai_algo = Negamax(6)
ai_tup = Negamax(6)

@app.route('/bot3/', methods=['GET','POST'])
def play_game():
        TEXT = '''
<!doctype html>
<html>
  <head><title>Tic Tac Toe</title></head>
  <body>
    <h1>Tic Tac Toe</h1>
    <h2>{{msg}}</h2>
    <form action="" method="POST">
      <table>
        {% for j in range(2, -1, -1) %}
        <tr>
          {% for i in range(0, 3) %}
          <td>
            <button style="height:40px;width:40px" type="submit" name="choice" value="{{j*3+i+1}}"
             {{"disabled" if ttt.spot_string(i, j)!="_"}}>
              {{ttt.spot_string(i, j)}}
            </button>
          </td>
          {% endfor %}
        </tr>
        {% endfor %}
      </table>
      <button type="submit" name="reset">Start Over</button>
      <button style="height:20px;width:100px" type="submit" name = "lala">Сделать ход</button>
    </form>
  </body>
</html>
'''
        msg = ''
        ttt = TicTacToe3b([AI_Player(ai_tup), AI_Player(ai_algo)])
        resp = make_response(render_template_string(TEXT, ttt=ttt, msg=msg))
        c = ",".join(map(str, ttt.board))
        resp.set_cookie("game_board", c)
        game_cookie = request.cookies.get('game_board')
        if game_cookie and len(ttt.board)==len(game_cookie.split(",")):
            ttt.board = [int(x) for x in game_cookie.split(",")]
        if "lala" in request.form:
            #ttt.play_move(request.form["choice"])
            if not ttt.is_over():
                print('ggg')
                print(ttt.nplayer)
                ai_move = ttt.get_move()
                ttt.play_move(ai_move)
                #time.sleep(2)
            if not ttt.is_over():
                print('ggg')
                print(ttt.nplayer)
                ai_move = ttt.get_move()
                ttt.play_move(ai_move)
                #time.sleep(2)
        if "reset" in request.form:
            ttt.board = [0 for i in range(9)]
            resp.set_cookie('game_board', '', expires=0)
        if ttt.is_over():
            msg = ttt.winner()
        else:
            msg = "play move"
        resp = make_response(render_template_string(TEXT, ttt=ttt, msg=msg))
        c = ",".join(map(str, ttt.board))
        resp.set_cookie("game_board", c)
        return resp



@app.route("/human3/", methods=['GET', 'POST'])
def play_game2():

    TEXT = '''
<!doctype html>
<html>
  <head><title>Tic Tac Toe</title></head>
  <body>
    <h1>Tic Tac Toe</h1>
    <h2>{{msg}}</h2>
    <form action="" method="POST">
      <table>
        {% for j in range(2, -1, -1) %}
        <tr>
          {% for i in range(0, 3) %}
          <td>
            <button style="height:60px;width:60px" type="submit" name="choice" value="{{j*3+i+1}}"
             {{"disabled" if ttt.spot_string(i, j)!="_"}}>
              {{ttt.spot_string(i, j)}}
            </button>
          </td>
          {% endfor %}
        </tr>
        {% endfor %}
      </table>
      <button type="submit" name="reset">Start Over</button>
    </form>
  </body>
</html>
'''
    msg = ''
    ttt = TicTacToe3h([Human_Player(), AI_Player(ai_algo)])
    resp = make_response(render_template_string(TEXT, ttt=ttt, msg=msg))
    c = ",".join(map(str, ttt.board))
    resp.set_cookie("game_board", c)
    while not(ttt.is_over()):
        #ttt = TicTacToe([AI_Player(ai_algo), AI_Player(ai_tup)])
        game_cookie = request.cookies.get('game_board')
        if game_cookie and len(ttt.board)==len(game_cookie.split(",")):
            ttt.board = [int(x) for x in game_cookie.split(",")]
        if "choice" in request.form:
            ttt.play_move(request.form["choice"])
            if not ttt.is_over():
                print('ggg')
                print(ttt.nplayer)
                ai_move = ttt.get_move()
                ttt.play_move(ai_move)
                print('ggg')
                print(ttt.nplayer)
                #ai_move = ttt.get_move()
                #ttt.play_move(request.form["choice"])
                #ttt.play_move(ai_move)
        if "reset" in request.form:
            resp.set_cookie('game_board', '', expires=0)
            ttt.board = [0 for i in range(9)]
        if ttt.is_over():
            msg = ttt.winner()
        else:
            msg = "play move"
        resp = make_response(render_template_string(TEXT, ttt=ttt, msg=msg))
        c = ",".join(map(str, ttt.board))
        resp.set_cookie("game_board", c)
        return resp
    
@app.route("/human53/", methods=['GET', 'POST'])
def play_game3():
    TEXT = '''
<!doctype html>
<html>
  <head><title>Tic Tac Toe</title></head>
  <body>
    <h1>Tic Tac Toe</h1>
    <h2>{{msg}}</h2>
    <form action="" method="POST">
      <table>
        {% for j in range(4, -1, -1) %}
        <tr>
          {% for i in range(0, 5) %}
          <td>
            <button  style="height:40px;width:40px" type="submit" name="choice" value="{{j*5+i+1}}"
             {{"disabled" if ttt.spot_string(i, j)!="_"}}>
              {{ttt.spot_string(i, j)}}
            </button>
          </td>
          {% endfor %}
        </tr>
        {% endfor %}
      </table>
      <button type="submit" name="reset">Start Over</button>
    </form>
  </body>
</html>
'''
    msg = ''
    ttt = TicTacToe53h([ Human_Player(), AI_Player(ai_algo)])
    resp = make_response(render_template_string(TEXT, ttt=ttt, msg=msg))
    c = ",".join(map(str, ttt.board))
    resp.set_cookie("game_board", c)
    while not(ttt.is_over()):
        #ttt = TicTacToe([AI_Player(ai_tup), AI_Player(ai_algo)])
        game_cookie = request.cookies.get('game_board')
        if game_cookie and len(ttt.board)==len(game_cookie.split(",")):
            ttt.board = [int(x) for x in game_cookie.split(",")]
        if "choice" in request.form:
            ttt.play_move(request.form["choice"])
            if not ttt.is_over():
                print('ggg')
                print(ttt.nplayer)
                ai_move = ttt.get_move()
                ttt.play_move(ai_move)
                print('ggg')
                print(ttt.nplayer)
                #ai_move = ttt.get_move()
                #ttt.play_move(request.form["choice"])
                #ttt.play_move(ai_move)
        if "reset" in request.form:
            ttt.board = [0 for i in range(25)]
            resp.set_cookie('game_board', '', expires=0)
        if ttt.is_over():
            msg = ttt.winner()
        else:
            msg = "play move"
        resp = make_response(render_template_string(TEXT, ttt=ttt, msg=msg))
        c = ",".join(map(str, ttt.board))
        resp.set_cookie("game_board", c)
        return resp
@app.route("/bot53/", methods=['GET', 'POST'])
def play_game4():

        TEXT = '''
    <!doctype html>
    <html>
      <head><title>Tic Tac Toe</title></head>
      <body>
        <h1>Tic Tac Toe</h1>
        <h2>{{msg}}</h2>
        <form action="" method="POST">
          <table>
            {% for j in range(4, -1, -1) %}
            <tr>
              {% for i in range(0, 5) %}
              <td>
                <button style="height:40px;width:40px" type="submit" name="choice" value="{{j*5+i+1}}"
                 {{"disabled" if ttt.spot_string(i, j)!="_"}}>
                  {{ttt.spot_string(i, j)}}
                </button>
              </td>
              {% endfor %}
            </tr>
            {% endfor %}
          </table>
          <button type="submit" name="reset">Start Over</button>
          <button style="height:20px;width:100px" type="submit" name = "lala">Сделать ход</button>
        </form>
      </body>
    </html>
    '''
        msg = ''
        ttt = TicTacToe53b([AI_Player(ai_tup), AI_Player(ai_algo)])
        resp = make_response(render_template_string(TEXT, ttt=ttt, msg=msg))
        c = ",".join(map(str, ttt.board))
        resp.set_cookie("game_board", c)
        game_cookie = request.cookies.get('game_board')
        if game_cookie and len(ttt.board)==len(game_cookie.split(",")):
            ttt.board = [int(x) for x in game_cookie.split(",")]
        if "lala" in request.form:
            #ttt.play_move(request.form["choice"])
            if not ttt.is_over():
                print('ggg')
                print(ttt.nplayer)
                ai_move = ttt.get_move()
                ttt.play_move(ai_move)
                #time.sleep(2)
            if not ttt.is_over():
                print('ggg')
                print(ttt.nplayer)
                ai_move = ttt.get_move()
                ttt.play_move(ai_move)
                #time.sleep(2)
        if "reset" in request.form:
            ttt.board = [0 for i in range(25)]
            resp.set_cookie('game_board', '', expires=0)
        if ttt.is_over():
            msg = ttt.winner()
        else:
            msg = "play move"
        resp = make_response(render_template_string(TEXT, ttt=ttt, msg=msg))
        c = ",".join(map(str, ttt.board))
        resp.set_cookie("game_board", c)
        return resp    
@app.route("/human5/", methods=['GET', 'POST'])
def play_game5():
    TEXT = '''
<!doctype html>
<html>
  <head><title>Tic Tac Toe</title></head>
  <body>
    <h1>Tic Tac Toe</h1>
    <h2>{{msg}}</h2>
    <form action="" method="POST">
      <table>
        {% for j in range(4, -1, -1) %}
        <tr>
          {% for i in range(0, 5) %}
          <td>
            <button  style="height:40px;width:40px" type="submit" name="choice" value="{{j*5+i+1}}"
             {{"disabled" if ttt.spot_string(i, j)!="_"}}>
              {{ttt.spot_string(i, j)}}
            </button>
          </td>
          {% endfor %}
        </tr>
        {% endfor %}
      </table>
      <button type="submit" name="reset">Start Over</button>
    </form>
  </body>
</html>
'''
    msg = ''
    ttt = TicTacToe5h([ Human_Player(), AI_Player(ai_algo)])
    resp = make_response(render_template_string(TEXT, ttt=ttt, msg=msg))
    c = ",".join(map(str, ttt.board))
    resp.set_cookie("game_board", c)
    while not(ttt.is_over()):
        #ttt = TicTacToe([AI_Player(ai_tup), AI_Player(ai_algo)])
        game_cookie = request.cookies.get('game_board')
        if game_cookie and len(ttt.board)==len(game_cookie.split(",")):
            ttt.board = [int(x) for x in game_cookie.split(",")]
        if "choice" in request.form:
            ttt.play_move(request.form["choice"])
            if not ttt.is_over():
                print('ggg')
                print(ttt.nplayer)
                ai_move = ttt.get_move()
                ttt.play_move(ai_move)
                print('ggg')
                print(ttt.nplayer)
                #ai_move = ttt.get_move()
                #ttt.play_move(request.form["choice"])
                #ttt.play_move(ai_move)
        if "reset" in request.form:
            ttt.board = [0 for i in range(25)]
            resp.set_cookie('game_board', '', expires=0)
        if ttt.is_over():
            msg = ttt.winner()
        else:
            msg = "play move"
        resp = make_response(render_template_string(TEXT, ttt=ttt, msg=msg))
        c = ",".join(map(str, ttt.board))
        resp.set_cookie("game_board", c)
        return resp

@app.route("/bot5/", methods=['GET', 'POST'])
def play_game6():
        TEXT = '''
<!doctype html>
<html>
  <head><title>Tic Tac Toe</title></head>
  <body>
    <h1>Tic Tac Toe</h1>
    <h2>{{msg}}</h2>
    <form action="" method="POST">
      <table>
        {% for j in range(4, -1, -1) %}
        <tr>
          {% for i in range(0, 5) %}
          <td>
            <button style="height:40px;width:40px" type="submit" name="choice" value="{{j*5+i+1}}"
             {{"disabled" if ttt.spot_string(i, j)!="_"}}>
              {{ttt.spot_string(i, j)}}
            </button>
          </td>
          {% endfor %}
        </tr>
        {% endfor %}
      </table>
      <button type="submit" name="reset">Start Over</button>
      <button style="height:20px;width:100px" type="submit" name = "lala">Сделать ход</button>
    </form>
  </body>
</html>
'''
        ttt = TicTacToe5b([AI_Player(ai_tup), AI_Player(ai_algo)])
        msg = ''
        resp = make_response(render_template_string(TEXT, ttt=ttt, msg=msg))
        c = ",".join(map(str, ttt.board))
        resp.set_cookie("game_board", c)
        
        game_cookie = request.cookies.get('game_board')
        if game_cookie and len(ttt.board)==len(game_cookie.split(",")):
            ttt.board = [int(x) for x in game_cookie.split(",")]
        if "lala" in request.form:
            #ttt.play_move(request.form["choice"])
            if not ttt.is_over():
                print('ggg')
                print(ttt.nplayer)
                ai_move = ttt.get_move()
                ttt.play_move(ai_move)
                #time.sleep(2)
            if not ttt.is_over():
                print('ggg')
                print(ttt.nplayer)
                ai_move = ttt.get_move()
                ttt.play_move(ai_move)
                #time.sleep(2)
        if "reset" in request.form:
            resp.set_cookie('game_board', '', expires=0)
            ttt.board = [0 for i in range(25)]
        if ttt.is_over():
            msg = ttt.winner()
        else:
            msg = "play move"
        resp = make_response(render_template_string(TEXT, ttt=ttt, msg=msg))
        c = ",".join(map(str, ttt.board))
        resp.set_cookie("game_board", c)
        return resp
if __name__ == "__main__":
    app.run(threaded=True, port=5000)
