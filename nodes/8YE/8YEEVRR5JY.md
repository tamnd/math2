---
tag: 8YEEVRR5JY
kind: proof
name: Proof of Rabin's tree theorem via parity games
msc: ["03B25", "03D05"]
topics: [E4AVTNWE9E]
audience: research
proves: PXKKP038RG
uses: [5809DBA7MW, AK66XQ59Z3, QXECDPAYTN, 3VSFM7K70Z, G6X7SZSNC5, HWC687ES0Q]
methods: [0ASJVEFA9J, 0WCP0PVET6, 01XM7JEKHY, X5HG1RNWQX]
sources:
  - url: https://en.wikipedia.org/wiki/Parity_game
    locator: Recursive algorithm for solving parity games
  - url: https://en.wikipedia.org/wiki/Parity_game
    locator: Relation with logic and automata theory
  - url: https://en.wikipedia.org/wiki/S2S_(mathematics)
    locator: Decidability of S2S
---

## Proof

We turn the emptiness question for a tree automaton into a finite parity game, and we show that the winner of such a game has a strategy that looks only at the current vertex.
We use the notation of the [[statement|PXKKP038RG]].
Part A proves positional determinacy of parity games on finite graphs in full, by Zielonka's argument.
Part B proves in full that emptiness of a parity tree automaton is decidable, and that a nonempty language contains a regular tree.
Part C gives the translation between S2S and automata in outline, and it cites complementation and the passage from Rabin conditions to parity conditions.

### Part A: games and strategies

A parity game $G = (V, V_0, V_1, E, \Omega)$ has a finite set $V$ of vertices, split into $V_0$ and $V_1$, edges $E \subseteq V \times V$, and priorities $\Omega \colon V \to \mathbb{N}$.
Every vertex has at least one successor.
A play is an infinite path $v_0 v_1 v_2 \cdots$ along $E$, where the owner of $v_k$ chooses $v_{k+1}$.
Player $0$ wins the play when the largest priority that occurs infinitely often is even, and otherwise player $1$ wins.
A strategy of player $j$ maps each finite play that ends in $V_j$ to a successor, and it is positional when it depends only on the last vertex.
$W_j(G)$ is the set of vertices from which player $j$ has a winning strategy.

### Part A: attractors and traps

1. Removing or adding a finite prefix does not change the set of priorities that occur infinitely often, so it does not change the winner.
2. The two players cannot both win from one vertex, because the play that follows both winning strategies would be won by both.
   So $W_0(G) \cap W_1(G) = \emptyset$.
3. For $X \subseteq V$ and a player $i$, let $A_0 = X$.
   Let $A_{k+1}$ be $A_k$ together with the vertices of $V_i$ that have some successor in $A_k$ and the vertices of $V_{1-i}$ whose successors all lie in $A_k$.
   The union $\operatorname{Attr}_i(X)$, the attractor, is reached after at most $|V|$ rounds.
4. The attractor strategy of player $i$ moves from each vertex of $V_i \cap (A_{k+1} \setminus A_k)$ to a successor in $A_k$.
   Along a play that follows it, the least $k$ with $v \in A_k$ drops at each step outside $X$.
   So the play reaches $X$ within $|V|$ steps from every vertex of $\operatorname{Attr}_i(X)$.
5. Let $U = V \setminus \operatorname{Attr}_i(X)$.
   A vertex of $V_i \cap U$ has all its successors in $U$, and a vertex of $V_{1-i} \cap U$ has some successor in $U$, since otherwise it would have joined the attractor.
   So player $i$ cannot leave $U$, player $1-i$ can stay in $U$, and $G[U]$ is again a game in which every vertex has a successor.

### Part A: a lemma on winning regions

6. Let $\sigma$ be a positional strategy of player $j$ that wins from every vertex of $W_j(G)$, and let $v \in W_j(G)$.
   If $v \in V_j$, then $\sigma(v) \in W_j(G)$.
   If $v \in V_{1-j}$, then every successor of $v$ lies in $W_j(G)$.
   Indeed, for such a successor $u$, every play from $u$ that follows $\sigma$ becomes, with $v$ in front, a play from $v$ that follows $\sigma$.
   Player $j$ wins it, and step 1 removes $v$ again.

**Claim.** $V = W_0(G) \cup W_1(G)$, and each player $j$ has one positional strategy that wins from every vertex of $W_j(G)$.

We prove the claim by [[induction|0ASJVEFA9J]] on $|V|$, and the empty game is the base case.

### Part A: the induction, first case

7. Let $d$ be the largest priority in $G$, let $i = d \bmod 2$, let $N = \{ v : \Omega(v) = d \}$, and let $A = \operatorname{Attr}_i(N)$.
   By step 5, $G' = G[V \setminus A]$ is a game, and it has fewer vertices because $N \ne \emptyset$.
8. By induction $V \setminus A = W'_0 \cup W'_1$ with $W'_j = W_j(G')$.
   There are positional strategies $\sigma'_0$ and $\sigma'_1$ that win in $G'$ from every vertex of $W'_0$ and $W'_1$ respectively.
9. Case 1 is $W'_{1-i} = \emptyset$.
   Let player $i$ follow $\sigma'_i$ on $V \setminus A$, the attractor strategy on $A \setminus N$, and any successor on $N$.
10. Take a play that follows this strategy.
    If it visits $A$ infinitely often, then by step 4 it visits $N$ infinitely often.
    So $d$ is the largest priority that occurs infinitely often, and player $i$ wins.
11. Otherwise the play stays in $V \setminus A$ from some point on.
    That tail is a play of $G'$ that follows $\sigma'_i$ from a vertex of $W'_i = V \setminus A$, so player $i$ wins it, and by step 1 the whole play.
    Hence $W_i(G) = V$, with a positional strategy.

### Part A: the induction, second case

12. Case 2 is $W'_{1-i} \ne \emptyset$.
    Let $B = \operatorname{Attr}_{1-i}(W'_{1-i})$, computed in $G$.
13. A play of $G$ that starts in $W'_{1-i}$ and follows $\sigma'_{1-i}$ stays in $W'_{1-i}$.
    Player $1-i$ stays there by step 6 applied in $G'$.
    A vertex of $V_i \cap W'_{1-i}$ has all its $G$-successors in $V \setminus A$ by step 5, so they are $G'$-successors, and they lie in $W'_{1-i}$ by step 6.
14. So such a play is a play of $G'$ that follows $\sigma'_{1-i}$, and player $1-i$ wins it.
15. Let $\tau$ be the attractor strategy of player $1-i$ on $B \setminus W'_{1-i}$ and $\sigma'_{1-i}$ on $W'_{1-i}$.
    By steps 4, 14 and 1, $\tau$ wins from every vertex of $B$.
16. By step 5 with the roles exchanged, $G'' = G[V \setminus B]$ is a game in which player $1-i$ cannot leave $V \setminus B$.
    It has fewer vertices than $G$ because $W'_{1-i} \ne \emptyset$.
17. By induction $V \setminus B = W''_0 \cup W''_1$, with positional strategies $\sigma''_0$ and $\sigma''_1$ that win in $G''$ from $W''_0$ and from $W''_1$.

### Part A: the end of the induction

18. Player $i$ wins from $W''_i$ with $\sigma''_i$.
    Player $i$ never leaves $V \setminus B$ when following $\sigma''_i$, and player $1-i$ cannot leave it by step 16.
    So every such play is a play of $G''$ that follows $\sigma''_i$, and player $i$ wins it.
19. Player $1-i$ wins from $W''_{1-i} \cup B$ with the positional strategy that is $\tau$ on $B$ and $\sigma''_{1-i}$ on $V \setminus B$.
    A play that enters $B$ follows $\tau$ from then on, and it is won by steps 15 and 1.
    A play that never enters $B$ is a play of $G''$ that follows $\sigma''_{1-i}$ from a vertex of $W''_{1-i}$, and it is won too.
20. The sets $W''_i$ and $W''_{1-i} \cup B$ cover $V$, and by step 2 they are exactly $W_i(G)$ and $W_{1-i}(G)$.
    This completes the induction and proves the claim.

### Part B: the emptiness game

Let $A = (Q, \Sigma, q_{\mathrm{in}}, \Delta, \Omega)$ be a parity tree automaton.
The emptiness game $G_A$ is played between Automaton, player $0$, and Pathfinder, player $1$.

21. The vertices of Automaton are the states $q \in Q$ and a sink $\bot$.
    The vertices of Pathfinder are the transitions $\delta = (q, a, q_0, q_1) \in \Delta$.
22. There are edges from $q$ to every transition whose first component is $q$, from $(q, a, q_0, q_1)$ to $q_0$ and to $q_1$, from a state without transitions to $\bot$, and from $\bot$ to itself.
23. The priorities are $\Omega(q)$ on a state $q$, $0$ on transitions, and $1$ on $\bot$.
    A play that never reaches $\bot$ visits states infinitely often, so its largest priority seen infinitely often is the largest $\Omega(q)$ over the states $q$ that it visits infinitely often.
    A play that reaches $\bot$ is lost by Automaton.
24. We claim that $L(A) \ne \emptyset$ if and only if $q_{\mathrm{in}} \in W_0(G_A)$.

### Part B: from an accepted tree to a winning strategy

25. Suppose $t \in L(A)$ with an accepting run $\rho$.
    Automaton plays with a current node $w$, starting at $w = \varepsilon$, and he keeps the current state equal to $\rho(w)$.
    At $\rho(w)$ he picks $(\rho(w), t(w), \rho(w0), \rho(w1)) \in \Delta$.
    If Pathfinder then picks $\rho(wc)$, the new current node is $wc$, and if $\rho(w0) = \rho(w1)$ the node $w0$ is taken.
26. The nodes $w$ form a path of the tree, and the states of the play are the states of $\rho$ along it.
    The path is good, so Automaton wins, and hence $q_{\mathrm{in}} \in W_0(G_A)$.

### Part B: from a positional strategy to a regular tree

27. Conversely, let $q_{\mathrm{in}} \in W_0(G_A)$.
    By Part A there is a positional strategy $\sigma$ of Automaton that wins from every vertex of $W_0(G_A)$.
28. For $q \in W_0(G_A) \cap Q$, step 6 gives $\sigma(q) \in W_0(G_A)$, so $\sigma(q) \ne \bot$, and we write $\sigma(q) = (q, a_q, q^0, q^1)$.
    By step 6 again, $q^0, q^1 \in W_0(G_A)$.
29. Define $\rho(\varepsilon) = q_{\mathrm{in}}$, and for each node $w$ with $\rho(w) = q$ put $t(w) = a_q$, $\rho(w0) = q^0$ and $\rho(w1) = q^1$.
    By step 28 and induction on $|w|$, every $\rho(w)$ lies in $W_0(G_A)$, so this defines a tree $t$ and a run $\rho$ of $A$ on $t$.
30. Along a path $\varepsilon, w_1, w_2, \ldots$, the sequence $\rho(\varepsilon), \sigma(\rho(\varepsilon)), \rho(w_1), \sigma(\rho(w_1)), \ldots$ is a play that follows $\sigma$ from $q_{\mathrm{in}}$.
    Automaton wins it, so by step 23 the path is good.
    Hence $\rho$ is accepting and $t \in L(A)$.
31. In step 29 the subtree of $t$ at $w$ is determined by $\rho(w)$, since the same rules build it from that state.
    So $t$ has at most $|Q|$ distinct subtrees, and it is regular.

### Part B: deciding emptiness

32. There are finitely many positional strategies $\sigma$ of Automaton.
    For a fixed $\sigma$, delete the edges from the vertices of Automaton that $\sigma$ does not use, and the plays that follow $\sigma$ are the infinite paths of the remaining graph $H_\sigma$.
33. The strategy $\sigma$ loses from $q_{\mathrm{in}}$ exactly when $H_\sigma$ has a closed walk, reachable from $q_{\mathrm{in}}$, with odd largest priority.
    Such a walk, repeated forever after a path to it, is a losing play.
    Conversely, a losing play visits only vertices seen infinitely often from some point on, and between two later visits to a vertex of the top such priority lies such a walk.
34. A finite graph search checks this condition.
    By step 24 and Part A, $L(A) \ne \emptyset$ exactly when some positional $\sigma$ passes the test, so emptiness is decidable.
    The recursion of Part A is also an algorithm, since attractors are computed by finite iteration.

### Part C: from S2S to automata, in outline

35. Every Rabin tree automaton can be turned effectively into a parity tree automaton with the same language, by recording the order of the latest visits to states.
    We cite this translation and do not prove it, and with it Part B proves part 3 of the theorem for Rabin automata.
36. First-order variables are replaced by set variables restricted to singletons, as in the [[proof of Büchi's theorem|5809DBA7MW]].
    The tracks of $X_1, \ldots, X_m$ form a $\{0,1\}^m$-tree.
37. "$X$ is a singleton" uses states $s$ (the element lies in this subtree) and $n$ (it does not), with $\Omega(s) = 1$ and $\Omega(n) = 0$.
    In state $s$, label $1$ sends $n$ to both children, and label $0$ sends $s$ to one child and $n$ to the other.
    State $n$ needs label $0$ and sends $n$ to both children, and priority $1$ forbids an infinite chain of $s$.
    Similar automata handle $X \subseteq Y$ and $s_c(x) = y$.
38. Disjunction is the union of automata.
    An existential quantifier is a projection, where the automaton guesses the erased track, as in Part A of the [[proof of Büchi's theorem|5809DBA7MW]].

### Part C: complement, the converse and decidability

39. Negation needs complementation of parity tree automata, and we cite it.
    Rabin proved it in 1969, Gurevich and Harrington gave a proof by games in 1982, and Emerson and Jutla and Mostowski gave proofs from positional determinacy of parity games on infinite graphs in 1991.
    Part A covers only finite graphs, because the acceptance game of one automaton on one infinite tree is infinite.
40. For the converse, guess sets $X_{q_1}, \ldots, X_{q_n}$ for the run, as in the [[Büchi-Elgot-Trakhtenbrot theorem|AK66XQ59Z3]].
    "Every path is good" quantifies over paths $P$ and says, for each odd $p$, that if $p$ occurs infinitely often on $P$, then so does a larger priority.
    "Infinitely often on $P$" is definable, since the prefix order of the tree is S2S-definable.
41. For a sentence $\varphi$, steps 36 to 39 build an automaton over the one-letter alphabet of zero tracks, since $\varphi$ has no free variables.
    Its language is the one tree over that alphabet if $\varphi$ is true, and it is empty otherwise.
    Step 34 decides which case holds, and this proves part 4.

So Parts A and B are proved in full, steps 35 and 39 are cited, and steps 36 to 40 are an outline.

## Idea

Acceptance and emptiness of tree automata are games.
To decide emptiness, Automaton chooses transitions and Pathfinder chooses directions, and the game is finite because only states matter.
A winning strategy of Automaton becomes an accepting run, and positional determinacy makes it depend only on the state, so the tree it builds is regular.
Positional determinacy itself follows by induction on the size of the game: the player who likes the top priority attracts the play to it, and the rest of the game is smaller.

## Variants

Rabin's original proof of complementation was a direct and long induction on automata.
Gurevich and Harrington used games with a latest appearance record as finite memory, and the parity condition with positional strategies gives the shortest proof.
Muchnik's theorem, with a proof by Walukiewicz, extends the method: decidability of the MSO theory passes from a structure to its tree-like iteration.
