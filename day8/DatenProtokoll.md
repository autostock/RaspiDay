* Arduino serial line usage

sS // set No. of Servo in [0, 6]; 0 is pseudo servo (used for setting of all servos)

tT // set Time t[S] (in ms)

pP // set Position p[S] in [30, 990]

x  // execute all servos

g  // go for one servo S

wT // wait

 

r  // get/read all Positions and remaining Time -> P1 T1 P2 T2 P3 T3 P4 T4 P5 T5 P6 T6

* examples

  // set servo 1 to position 500 in time 1000 and go. And back to Position 0.

  s1 p500 t1000 g

  s1 p0 t1000 g

  // set every servo to position 500 in time 2000 ms and execute

  s1 t2000 p500 s2 t2000 p500 s3 t2000 p500 s4 t2000 p500 s5 t2000 p500 s6 t2000 p500 x

  // as shortcut for above commands use pseudo servo 0

  s0 t2000 p500 x

  // set all servo positions to 0 and execute

  s0 p0 x

  // wait for 1000 ms (Warning!! all Arduino communication is blocked for this time)

  w1000