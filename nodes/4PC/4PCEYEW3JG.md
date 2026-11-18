---
tag: 4PCEYEW3JG
kind: statement
role: theorem
name: Haken's theorem
msc: ["03F20", "68Q17"]
topics: [CBAF7J051K]
audience: research
uses: [6JSH907W5R, RJ571F7FF0, 0HGVCWQGY3]
about: [6JSH907W5R, RJ571F7FF0]
proofs: [8D74S641EK]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Lower bounds
history:
  first_stated: "1985"
  notes: "Armin Haken, The intractability of resolution, Theoretical Computer Science, 1985. The proof given here follows Beame and Pitassi, 1996."
---

## Statement

For $n \ge 1$, let $\mathrm{PHP}^{n+1}_n$ be the [[pigeonhole formula|RJ571F7FF0]] with the variables $x_{ij}$ for pigeons $i \in \set{1, \dots, n+1}$ and holes $j \in \set{1, \dots, n}$.
It has the *pigeon clauses* $P_i = \set{x_{i1}, \dots, x_{in}}$ and the *hole clauses* $H_{i i' j} = \set{\neg x_{ij}, \neg x_{i'j}}$ for $i < i'$.

**Theorem (Haken).**
There is a constant $c > 1$ such that, for every $n \ge 1$, every [[resolution refutation|6JSH907W5R]] of $\mathrm{PHP}^{n+1}_n$ has at least $c^n$ clauses.

The proof on this site gives an explicit form.
For every $n \ge 20$, every resolution refutation of $\mathrm{PHP}^{n+1}_n$ has at least $(11/10)^{\lfloor n/20 \rfloor}$ clauses.

The system is general (dag-like) resolution, and the measure is size in clauses.
The formula has $(n+1) n$ variables and $(n+1) + n \binom{n+1}{2}$ clauses, so its size is polynomial in $n$, and the lower bound is exponential in its size to a fixed power.

## Remarks

### Why each hypothesis is needed

- The system must be resolution, or a system no stronger. [[Cutting planes|KKCX2HQP2K]] and [[Frege systems|J2BAR09TPF]] refute $\mathrm{PHP}^{n+1}_n$ in polynomial size; see [[Buss's theorem|VRX23FZV21]].
- The formula must contain all hole clauses. Without the hole clause for hole $j$ and pigeons $i, i'$, the CNF is satisfiable.
- The bound concerns $n + 1$ pigeons. For many more pigeons than holes the bounds are weaker; see the weak pigeonhole formulas in the [[pigeonhole formulas|RJ571F7FF0]] page.

### Consequences

- Resolution is not polynomially bounded. This is one step of Cook's program after the [[Cook-Reckhow theorem|YS1T29B00B]].
- Frege systems and cutting planes are exponentially stronger than resolution.
- DPLL and CDCL solvers take exponential time on $\mathrm{PHP}^{n+1}_n$, since their runs give resolution refutations.

### Converse

Resolution refutations of size $2^{O(n \log n)}$ exist.
A DPLL search that places pigeon $1$, then pigeon $2$, and so on, has at most $n$ branches per pigeon, and it gives a tree-like refutation of this size.
So the exponent $n$ in the theorem cannot be raised beyond $O(n \log n)$.

### Generalizations

- The [[size-width relation|GWDGRPAQSM]] gives exponential lower bounds for many formulas by width, including a version of the pigeonhole formulas on bipartite expander graphs.
- Exponential lower bounds for $\mathrm{PHP}^{n+1}_n$ hold in [[bounded-depth Frege|41QJ1WEMJ3]]; see [[Ajtai's theorem|Q0ERK64J78]].
- For the weak pigeonhole formulas with $m$ pigeons, Raz proved in 2004 that resolution needs size $2^{n^{\varepsilon}}$ for a constant $\varepsilon > 0$, for every $m > n$.

## History

Armin Haken proved the theorem in 1985, in "The intractability of resolution", by a counting method now called *bottleneck counting*.
It was the first exponential lower bound for general resolution.
Paul Beame and Toniann Pitassi gave a shorter proof in 1996 by random restrictions; this is the proof on this site.

## Explanations

### L1 human

The pigeonhole principle says that $n + 1$ pigeons do not fit into $n$ holes with at most one pigeon in each.
Written as clauses, it is a contradiction that every SAT solver of the resolution type must refute.
Haken's theorem says that such solvers need exponentially many steps.
For $n = 200$ the explicit bound is $(11/10)^{10}$, which is small, but the bound doubles about every $145$ new holes.

### L2 human

We read off the parameters of the explicit bound for $n = 100$.

1. $\lfloor n/20 \rfloor = 5$, so the bound is $(11/10)^5 \approx 1.61$.
2. For $n = 2000$, $\lfloor n/20 \rfloor = 100$, and $(11/10)^{100} \approx 13781$.
3. For $n = 20000$, the bound is $(11/10)^{1000}$, which has more than $40$ digits.

The typical use of the theorem is as a benchmark: a new lower bound method should reprove it.
A trap: the theorem is about resolution only, and the same formulas are easy for stronger systems.

### L3 human

The pigeonhole formulas say that there is no injection from $n + 1$ points into $n$ points, a statement about counting.
Resolution cannot count, since each line is a clause, and Haken's theorem makes this precise.
In [[bounded arithmetic|RA380RWEC0]], the formulas $\mathrm{PHP}^{n+1}_n$ are the translations of the pigeonhole principle for a new relation symbol, and lower bounds for them give independence results for weak theories.
