param n := 20;


var Q[{1 .. n}] integer >=1 <=n;
minimize dist_lexic

subto ReinesCloitree:
forall <i> in {1..n-1}:
    forall <j> in {i+1..n}:
        vabs(Q[i] - Q[j]) >=1 and vabs(Q[i] - Q[j] - i + j) >=1 and vabs(Q[i] - Q[j] - j + i) >=1;
