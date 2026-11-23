---
tag: AW5XA4GYGH
kind: proof
name: Proof of Seese's theorem via undecidability of grids
msc: ["03B25", "05C83", "03D05"]
topics: [E4AVTNWE9E]
audience: research
proves: RT898AFHWT
uses: [758EYCN27B, Z7TN2B35B0, QFE1AXQK2E, WP3GDNWJJW, FJ5E6FZVRJ, G6X7SZSNC5, HWC687ES0Q, BBYNPDWR5R]
methods: [0J0XBKG64S, 0ASJVEFA9J, 01XM7JEKHY]
sources:
  - url: https://en.wikipedia.org/wiki/Logic_of_graphs
    locator: Seese's theorem
  - url: https://en.wikipedia.org/wiki/Treewidth
    locator: Grid minor size
  - url: https://en.wikipedia.org/wiki/Halting_problem
    locator: Undecidability
---

## Proof

We write the run of a Turing machine into a grid, with one row per moment and one column per tape cell, and we find such grids inside every class of unbounded treewidth.
We use the notation of the [[statement|RT898AFHWT]].
Part A proves in full that MSO satisfiability in finite grids is undecidable.
Part B transfers this to every class of unbounded treewidth.
It is an outline, and the excluded grid theorem and the MSO₂-definability of grid minors are cited.

### Part A: grids and machines

The grid $G_{m,n}$ is the structure with domain $\{0, \ldots, m-1\} \times \{0, \ldots, n-1\}$ and two binary relations.
$R$ holds between $(i, j)$ and $(i, j+1)$, and $D$ holds between $(i, j)$ and $(i+1, j)$.
We call $i$ the row, read as time, and $j$ the column, read as a tape cell.

1. A [[Turing machine|758EYCN27B]] $M$ has states $Q$ with a start state $q_0$ and a halting state $q_h$, and a tape alphabet $\Gamma$ with blank $\sqcup$.
   Its transition function is $\delta \colon (Q \setminus \{q_h\}) \times \Gamma \to Q \times \Gamma \times \{\mathrm{L}, \mathrm{R}\}$.
   The tape has cells $0, 1, 2, \ldots$, and a move to the left from cell $0$ stays at cell $0$.
2. It is undecidable whether $M$ halts when started on the blank tape.
   This follows from the undecidability of the [[halting problem|Z7TN2B35B0]], because a machine can first write a fixed input and then run.
3. A configuration is a tape content, a head position and a state.
   We let a halted configuration repeat forever, so the run $c_0, c_1, c_2, \ldots$ from the blank tape is defined for all times.

### Part A: the sentence

4. "$x$ is in column $0$" is $\neg \exists y \, R(y, x)$, "$x$ is in the last column" is $\neg \exists y \, R(x, y)$, and "$x$ is in row $0$" is $\neg \exists y \, D(y, x)$.
   Write $H$ for the union of the sets $H_q$.
5. The sentence $\varphi_M$ is $\exists (C_a)_{a \in \Gamma} \, \exists (H_q)_{q \in Q} \, \Psi$, where $\Psi$ is the conjunction of the conditions in steps 6 to 10.
   The set $C_a$ is meant to hold the cells with symbol $a$, and $H_q$ the head position when the state is $q$.
6. The sets $C_a$ partition the domain, and the sets $H_q$ are pairwise disjoint.
7. Every vertex of row $0$ is in $C_\sqcup$.
   The vertex in row $0$ and column $0$ is in $H_{q_0}$, and no other vertex of row $0$ is in $H$.
8. For all $x, z$ with $D(x, z)$: if $x \notin H$ or $x \in H_{q_h}$, then $z$ lies in the same $C_a$ as $x$.
   If $x \in H_q \cap C_a$ with $q \ne q_h$ and $\delta(q, a) = (p, b, d)$, then $z \in C_b$.

### Part A: the head

9. For all $x, z$ with $D(x, z)$ and every state $p$, $z \in H_p$ holds exactly when one of four cases occurs.
   First, $x \in H_{q_h}$ and $p = q_h$.
   Second, the left neighbor $x'$ of $x$, with $R(x', x)$, lies in some $H_q \cap C_a$ with $\delta(q, a) = (p, b, \mathrm{R})$.
   Third, the right neighbor $x''$ of $x$, with $R(x, x'')$, lies in some $H_q \cap C_a$ with $\delta(q, a) = (p, b, \mathrm{L})$.
   Fourth, $x$ is in column $0$ and lies in some $H_q \cap C_a$ with $\delta(q, a) = (p, b, \mathrm{L})$.
10. No vertex of the last column is in $H$, and some vertex is in $H_{q_h}$.
11. Each condition is a finite first-order formula in $R$, $D$ and the set variables, so $\varphi_M$ is an MSO sentence, and the map $M \mapsto \varphi_M$ is computable.
12. Claim: $M$ halts on the blank tape if and only if $G_{m,n} \models \varphi_M$ for some $m, n \ge 1$.

### Part A: a halting run gives a model

13. Suppose $M$ reaches $q_h$ at time $T$.
    Take $m = T + 1$ and $n = T + 2$.
    Put $(i, j)$ in $C_a$ when cell $j$ holds $a$ in $c_i$, and in $H_q$ when the head of $c_i$ is at $j$ in state $q$.
14. The head moves at most one cell per step, so at time $i \le T$ it is at a cell $j \le i \le n - 2$.
    So the head is never in the last column, and conditions 6, 7 and 10 hold.
15. Conditions 8 and 9 hold because $c_{i+1}$ arises from $c_i$ by one step of $M$, or equals $c_i$ when $c_i$ is halted.
    The step changes only the cell under the head and moves the head by at most one cell, as the four cases of step 9 list.
    So $G_{m,n} \models \varphi_M$.

### Part A: a model gives a halting run

16. Conversely, suppose that sets $C_a$, $H_q$ satisfy $\Psi$ in $G_{m,n}$.
    We show by induction on $i < m$ that row $i$ agrees with $c_i$ on the columns $0, \ldots, n-1$, and that the head of $c_i$ is at a column at most $n - 2$.
17. For $i = 0$ this is condition 7 together with condition 10.
18. For the step from $i$ to $i + 1 < m$, row $i$ has exactly one vertex in $H$ by induction, at the head column $h \le n - 2$ of $c_i$, in the state of $c_i$.
    By condition 8 the symbols of row $i + 1$ are those of $c_{i+1}$ on columns $0, \ldots, n-1$.
19. Only cases of condition 9 that involve $(i, h)$ can occur, since it is the only vertex of row $i$ in $H$.
    Exactly one case occurs, for one state $p$, because $\delta$ is a function.
    It puts the single head of row $i + 1$ where $c_{i+1}$ has it, in its state, and a right move uses the column $h + 1 \le n - 1$.
    By condition 10 this position is at most $n - 2$.
20. By condition 10 some vertex lies in $H_{q_h}$, so some $c_i$ has state $q_h$, and $M$ halts.
    This proves the claim.
21. Hence the set of MSO sentences that hold in some finite grid is undecidable, since otherwise steps 11 and 12 would decide the halting problem of step 2.
    The theory of finite grids, the set of sentences true in all of them, is undecidable too, since $\varphi$ holds in some grid exactly when $\neg \varphi$ is not in it.

### Part B: grid minors

22. For every $k$ there is $w(k)$ such that every finite graph of treewidth at least $w(k)$ has the $k \times k$ grid as a [[minor|QFE1AXQK2E]].
    This is the excluded grid theorem of Robertson and Seymour (Graph Minors V), and Chekuri and Chuzhoy later showed that $w(k)$ can be taken polynomial in $k$.
    We cite it.
23. A minor of $G$ is described by sets: a set $F$ of edges whose components are the branch sets, a set of representatives with one vertex per branch set, and two edge sets that give the $R$-edges and the $D$-edges between branch sets.
    These sets are quantified in MSO₂, and this is where edge-set quantifiers are needed.
24. There is an MSO sentence $\mathrm{Grid}$ whose finite models with two binary relations are exactly the grids $G_{m,n}$.
    With step 23 it gives a computable map $\varphi \mapsto \hat{\varphi}$ such that $G \models \hat{\varphi}$ exactly when $G$ has a grid minor $G_{m,n}$, with directions chosen, in which $\varphi$ holds.
    We state steps 23 and 24 without proof.

### Part B: the transfer

25. Let $\mathcal{C}$ have unbounded treewidth.
    By step 22, for every $k$ some graph in $\mathcal{C}$ has the $k \times k$ grid as a minor, and so every $G_{m,n}$ with $m, n \le k$ as a minor.
26. Hence $\varphi$ holds in some finite grid exactly when $\hat{\varphi}$ holds in some graph of $\mathcal{C}$.
    If $\varphi$ holds in $G_{m,n}$, take a graph of $\mathcal{C}$ with a $k \times k$ grid minor for $k = \max(m, n)$.
    If $\hat{\varphi}$ holds in some graph of $\mathcal{C}$, step 24 gives a grid in which $\varphi$ holds.
27. If the MSO₂ theory of $\mathcal{C}$ were decidable, then MSO₂ satisfiability in $\mathcal{C}$ would be decidable.
    By step 26 this would decide MSO satisfiability in finite grids, which contradicts step 21.
    So a class with a decidable MSO₂ theory has bounded treewidth.

So Part A is proved in full, step 22 is cited, and steps 23 and 24 are stated in outline without proof.

## Idea

A grid can hold the run of a Turing machine: rows are moments, columns are tape cells, and monadic sets record symbols and the head.
The transition rule is a local condition on each small window, so an existential MSO sentence says "the machine halts inside this grid".
Large treewidth forces large grid minors, and MSO₂ can find a grid minor and run the same sentence inside it.

## Variants

The undecidability of grids also follows from the undecidability of the domino problem for [[Wang tiles|BBYNPDWR5R]]: a tiling of an $m \times n$ rectangle with fixed border colors is a choice of monadic sets.
Instead of minors one can use subdivisions of walls, which every graph of large treewidth also contains, and then MSO₂ only has to guess a subgraph.
