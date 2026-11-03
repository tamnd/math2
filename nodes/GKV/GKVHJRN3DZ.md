---
tag: GKVHJRN3DZ
kind: statement
role: theorem
name: Integral flow theorem
msc: [90C35, 05C21, 90B10]
uses: [ZSNXTW5E2K, EXMR7RYRTP, 9P19SEYN1R, 4HMR4KQ01T, 0JP0ZF57PN, E6GYGZDBS7, 08WCB90WND]
about: [EXMR7RYRTP]
sources:
  - url: https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_flowapplications_intro.ptx#L6
    locator: source/s_flowapplications_intro.ptx:6
---

## Statement

Let $N = (V, A, c, s, t)$ be a [[flow network|ZSNXTW5E2K]] in which every capacity $c(a)$ is a nonnegative integer.
Then there is a maximum $s$–$t$ flow $f$ such that $f(a)$ is an integer for every edge $a \in A$.
In particular, the maximum value of a flow is an integer.

## Remarks

Run the [[Ford–Fulkerson method|9P19SEYN1R]] from the zero flow.
By induction, every flow it produces is integral, since each augmentation adds or removes the least residual capacity of a path, which is an integer.
Each augmentation raises the value by at least $1$, and the value is bounded by the capacity of the cut $(\set{s}, V \setminus \set{s})$, so the method stops.
At the end there is no augmenting path, and the proof of the [[max-flow min-cut theorem|4HMR4KQ01T]] shows that the flow is maximum.

Example: let $G$ be a bipartite graph with sides $X$ and $Y$.
Add a source with an edge to every vertex of $X$ and a sink with an edge from every vertex of $Y$.
Direct the edges of $G$ from $X$ to $Y$, and give all edges capacity $1$.
An integral maximum flow uses each edge $0$ or $1$ times, and its edges between $X$ and $Y$ form a maximum matching.

Integrality of the capacities is needed: with capacities $1/2$ on all edges of a single path from $s$ to $t$, every maximum flow has value $1/2$.
The theorem does not say that every maximum flow is integral.
Take edges $s a$, $s b$, $a v$, $b v$, $v t$, all of capacity $1$.
Sending $1/2$ along $s, a, v$ and $1/2$ along $s, b, v$, then $1$ along $v t$, gives a maximum flow that is not integral.

## Explanations

### L1 human

If every pipe carries a whole number of units, the best flow can be chosen to send whole units on every pipe.
One never needs to split a unit into fractions to reach the maximum.
This matters when the units are indivisible, such as people, trucks or pairs in a matching.

### L2 human

The theorem turns maximum flow into a tool for combinatorics.
Bipartite matching, [[Kőnig's theorem|0JP0ZF57PN]], [[Menger's theorem|E6GYGZDBS7]] on disjoint paths and [[Hall's theorem|08WCB90WND]] all follow by building networks with capacities $0$ and $1$.
From the point of view of linear programming, it holds because the constraint matrix of a flow problem, the incidence matrix of a directed graph, is totally unimodular.
So every vertex of the flow polytope is integral when the capacities are integers.
The same holds for minimum-cost flows with integral data.
