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

Haken's theorem says that resolution needs exponentially many clauses to refute the pigeonhole formulas.
For $3$ pigeons and $2$ holes the formula has $9$ clauses, and the [[pigeonhole formulas|RJ571F7FF0]] give a refutation of $19$ clauses, but the least size grows exponentially as the number of holes grows.

For $n \ge 1$, let $\mathrm{PHP}^{n+1}_n$ be the CNF in the variables $x_{ij}$, for pigeons $i \in \{1, \dots, n+1\}$ and holes $j \in \{1, \dots, n\}$.
It has the *pigeon clauses* $P_i = \{x_{i1}, \dots, x_{in}\}$ and the *hole clauses* $H_{i i' j} = \{\neg x_{ij}, \neg x_{i'j}\}$ for $i < i'$.

**Theorem (Haken).**
There is a constant $c > 1$ such that, for every $n \ge 1$, every [[resolution refutation|6JSH907W5R]] of $\mathrm{PHP}^{n+1}_n$ has at least $c^n$ clauses.

**Explicit form.**
For every $n \ge 20$, every resolution refutation of $\mathrm{PHP}^{n+1}_n$ has at least $(11/10)^{\lfloor n/20 \rfloor}$ clauses.

The proof system is general, dag-like resolution, and the measure is size, counted in clauses.

## Remarks

### The size of the input

The formula has $(n+1) n$ variables and $(n + 1) + n \binom{n+1}{2}$ clauses.
For $n = 2$ this is $3 + 2 \cdot 3 = 9$ clauses, and for $n = 4$ it is $5 + 4 \cdot 10 = 45$ clauses.
So the input has size polynomial in $n$, about $n^3$, and a lower bound of $c^n$ is exponential in a fixed root of the input size.
This is what makes the theorem a statement about the system and not about a large input.

### Why each hypothesis is needed

The proof system must be resolution or a weaker system.
[[Cutting planes|KKCX2HQP2K]] refutes $\mathrm{PHP}^{n+1}_n$ in polynomial size, and [[Frege systems|J2BAR09TPF]] prove $\neg \mathrm{PHP}^{n+1}_n$ in polynomial size by [[Buss's theorem|VRX23FZV21]].
So the same formulas are easy one level up, and the theorem says nothing there.

The formula must contain all the hole clauses.
If the hole clause for hole $j$ and pigeons $i, i'$ is missing, put $i$ and $i'$ both into hole $j$ and the other pigeons into the other holes, one each, and every remaining clause holds.

The bound is for $n + 1$ pigeons.
For many more pigeons than holes, the weak pigeonhole formulas, resolution still needs size $2^{n^{\varepsilon}}$ for a constant $\varepsilon > 0$ and every $m > n$, by a theorem of Raz from 2004, but the exponent is smaller.

### What it gives you

Resolution is not polynomially bounded, so it is one completed step of Cook's program after the [[Cook-Reckhow theorem|YS1T29B00B]].
Cutting planes and Frege systems are exponentially stronger than resolution, because they refute the same formulas in polynomial size.
SAT solvers based on DPLL or CDCL take exponential time on $\mathrm{PHP}^{n+1}_n$, since their runs give resolution refutations of at most the same size.

### The converse direction

The bound cannot be much larger.
A DPLL search that places pigeon $1$, then pigeon $2$, and so on, branches on at most $n$ holes for each pigeon, and it gives a tree-like refutation of size $2^{O(n \log n)}$.
So the least size lies between $c^n$ and $2^{O(n \log n)}$.

### Generalizations

The [[size-width relation|GWDGRPAQSM]] gives exponential lower bounds by width for the pigeonhole formulas on bipartite expander graphs of bounded degree, and the [[restriction lemma|7RX0Z6S1KZ]] transfers them to $\mathrm{PHP}^{n+1}_n$.
In [[bounded-depth Frege|41QJ1WEMJ3]], whose lines are formulas of a fixed depth, the bounds are superpolynomial by [[Ajtai's theorem|Q0ERK64J78]], and of the form $2^{n^{\varepsilon_d}}$ by the later work of two groups.

### Watch out

The theorem names one proof system and one measure.
It is easy to read "the pigeonhole principle has no short proofs" into it, and that is false: Frege proofs of polynomial size exist.
It is also easy to read the bound as one on the number of literals, which is larger by a factor of at most $2n(n+1)$, so the exponential form does not change.

## History

Armin Haken proved the theorem in 1985, in "The intractability of resolution".
His method is now called bottleneck counting.
It was the first exponential lower bound for general resolution.
Paul Beame and Toniann Pitassi gave a shorter proof by random restrictions in 1996, and the [[proof by random restrictions|8D74S641EK]] follows it.

## Explanations

### L1 human

The pigeonhole principle says that $n + 1$ pigeons do not fit into $n$ holes with at most one pigeon in each.
Written as clauses, it is a contradiction that every SAT solver of the resolution type must refute.
Haken's theorem says that such solvers need exponentially many steps.
For $n = 200$ the explicit bound is $(11/10)^{10}$, about $2.6$, which is small.
But the bound doubles about every $145$ new holes, so it soon passes every computer.

### L2 human

We read off the explicit bound for three sizes, to see how slowly it starts and how fast it grows.
For $n = 100$ we have $\lfloor n/20 \rfloor = 5$, and
$$(11/10)^5 \approx 1.61.$$
For $n = 2000$ we have $\lfloor n/20 \rfloor = 100$, and $(11/10)^{100} \approx 13781$.
For $n = 20000$ the bound is $(11/10)^{1000}$, and since $1000 \log_{10} 1.1 \approx 41.4$ it has $42$ digits.
The constants of the proof are not the best possible, and the true size is at least $2^{\Omega(n)}$ with a better constant.
The typical use of the theorem is as a benchmark: a new lower bound method for resolution should reprove it.

### L3 human

The pigeonhole formulas say that there is no injection from $n + 1$ points into $n$ points, a statement about counting.
A clause cannot count, and Haken's theorem makes this precise for proofs whose lines are clauses.
The proof idea, random restrictions that kill every wide clause, returns in the [[size-width relation|GWDGRPAQSM]] and, with switching lemmas in place of single restrictions, in the bounds for bounded-depth Frege.
In [[bounded arithmetic|RA380RWEC0]], the formulas $\mathrm{PHP}^{n+1}_n$ are the translations of the pigeonhole principle for a new relation symbol, and lower bounds for them give independence results for weak theories.
