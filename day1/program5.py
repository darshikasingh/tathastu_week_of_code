run_player1 = int(input("ENTER THE RUN BY PLAYER 1 IN 60 BALLS: "))
run_player2 = int(input("ENTER THE RUN BY PLAYER 2 IN 60 BALLS: "))
run_player3 = int(input("ENTER THE RUN BY PLAYER 3 IN 60 BALLS: "))
strikerate1 = run_player1 * 100/60
strikerate2 = run_player2 * 100/60
strikerate3 = run_player3 * 100/60
print("STRIKE RATE OF PLAYER 1 IS", strikerate1)
print("STRIKE RATE OF PLAYER 2 IS", strikerate2)
print("STRIKE RATE OF PLAYER 3 IS", strikerate3)
print("RUNS SCORED BY PLAYER 1 IF THEY PLAYED 60 MORE BALLS IS", run_player1 *2)
print("RUNS SCORED BY PLAYER 2 IF THEY PLAYED 60 MORE BALLS IS", run_player1 *2)
print("RUNS SCORED BY PLAYER 3 IF THEY PLAYED 60 MORE BALLS IS", run_player1 *2)
print("MAX NO. OF SIXES OF PLAYER 1 =", run_player1 // 6)
print("MAX NO. OF SIXES OF PLAYER 2 =", run_player2 // 6)
print("MAX NO. OF SIXES OF PLAYER 3 =", run_player3 // 6)
