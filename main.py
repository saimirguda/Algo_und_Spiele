import random

import grpc
import time
import sys

sys.path.append('./netcode')

from netcode.tko_pb2 import *
from netcode.netcode_pb2 import *
from netcode.netcode_pb2_grpc import GameComStub


# settings

class field_piece:
    players_piece = None
    x_pos = None
    y_pos = None


size_of_board = None
total_stones = 8
userToken = '9583cb2887862d08ca68b99af31126d81dda7a467196e18114c5decc39e4fef8'  # TODO: Insert your user token here
gameserverAddress = 'gameserver.ist.tugraz.at:80'

# Vars
matchToken = ""

# Setup comms
channel = grpc.insecure_channel(gameserverAddress)
stub = GameComStub(channel)


# Query your userToken to be able to start a new match
def getUserToken(matr_number, secret):
    auth = AuthPacket()
    auth.matr_number = matr_number
    auth.secret = secret
    response = stub.GetUserToken(auth)
    return response.user_token


# Request a new match for Tak
def newMatch(length):
    params = GameParameter()
    request = MatchRequest(user_token=userToken,
                           game_token='tko',
                           timeout_suggestion_seconds=3600,
                           tko_game_parameters=params)
    # print(request.)
    response = stub.NewMatch(request)

    print("New Match:", response.match_token)
    print("First player?", response.beginning_player)

    global matchToken
    matchToken = response.match_token


# Helper to create the MatchIDPacket
def createMatchId():
    return MatchIDPacket(user_token=userToken,
                         match_token=matchToken)


# Let's get started
def queryGameState():
    response = stub.GetGameState(createMatchId())
    return response.tko_game_state, response.game_status


# Sleepy time
def waitMatchStarted():
    while queryGameState()[1] == GameStatus.MATCH_NOT_STARTED:
        time.sleep(1)


# Identify yourself!
def queryOpponentInfo():
    response = stub.GetOpponentInfo(createMatchId())
    print("Opponent:", response.user_pseudonym, "(" + str(response.elo.user_elo) + "),",
          "from group:", response.group_pseudonym, "(" + str(response.elo.group_elo) + ")")
    pass


# What did we agree on? 2 Timeout, keine mehr?
def queryTimeout():
    response = stub.GetTimeout(createMatchId())
    print("Negotiated timeout:", response.timeout_seconds, "sec")
    pass


# I did implement this, but I deleted it because it was not fancy enough.
def showGameState():
    state, status = queryGameState()
    # print("TODO: Implement showGameState()")

    return state, status


# Submit a turn and evaluate the turn status info. Also returns the Tak board state.
def submitTurn(turn):
    request = TurnRequest(match_id=createMatchId(),
                          tko_game_turn=turn)
    response = stub.SubmitTurn(request)
    if response.turn_status == TurnStatus.INVALID_TURN:
        print("Error: Invalid turn submitted.")
        exit(1)
    if response.turn_status == TurnStatus.MATCH_OVER:
        print("Match is over.")
        exit(0)
    if response.turn_status == TurnStatus.NOT_YOUR_TURN:
        print("This isn't the time to use that!")
    return response.tko_game_state


# Helper
def isMatchOver(game_status):
    return game_status in [GameStatus.MATCH_WON,
                           GameStatus.MATCH_LOST,
                           GameStatus.DRAW,
                           GameStatus.MATCH_ABORTED]


# Helper
def isTurnPlayable(game_status):
    return game_status == YOUR_TURN


def printField(state):
    counter = 0
    list_for_board = []
    list_for_list = []
    flag = False
    another_counter = 0
    for field in state.board:
        list_for_board.append(field)
        if counter and (counter % 5 == 4 or counter == 4) and flag:
            # print(list_for_board)
            list_for_list.append(list_for_board[another_counter:counter + 1])
            if not another_counter:
                another_counter += 5
            else:
                another_counter += 5
            flag = False
            counter += 1
            continue
        counter += 1
        flag = True
    print("GameState: ")
    for element in list_for_list:
        print(element)


def GameplayFuncion(state):

    turn = GameTurn()
    i = random.randint(0, 12579)
    i = i % 25
    while(state.board[i] != 0):
        i = random.randint(0, 12579)
        i = i % 25
        j = random.randint(0, 12579)
        #print(i)
    turn.x1 = 0
    turn.y1 = 0
    turn.x2 = i % 5
    turn.y2 = i // 5
    #state.board[i] = 1
    return turn


# Query, calculate, submit, repeat, query, calculate, submit, repeat
def autoPlay():
    status = None
    while not isMatchOver(status):
        state, status = showGameState()
        turn = GameplayFuncion(state)
        #print(state)
        if isTurnPlayable(status):
            printField(state)
            #print("TODO: Implement autoPlay()")
            submitTurn(turn)
        #time.sleep(4)
        #GameplayFuncion(state)

    return status
    #print("TODO: Implement autoPlay()")


def main():
    #userToken = getUserToken('11933108', 'Affair')
    print("UserToken here :", userToken)
    max_tries = 500
    won_rounds = 0
    lost_rounds = 0
    aborted_rouds = 0
    for counter in range(max_tries):
        print("UserToken:", userToken)
        newMatch(5)
        waitMatchStarted()
        print("Opponent found.")
        queryOpponentInfo()
        queryTimeout()
        curr_status = autoPlay()
        if curr_status == GameStatus.MATCH_WON:
            won_rounds += 1
            print("Won rounds:", won_rounds)
        elif curr_status == GameStatus.MATCH_LOST:
            lost_rounds += 1
            print("Lost rounds:", lost_rounds)
        elif curr_status == GameStatus.MATCH_ABORTED:
            aborted_rouds += 1
            print("Aborted rounds:", aborted_rouds)


if __name__ == "__main__":
    main()