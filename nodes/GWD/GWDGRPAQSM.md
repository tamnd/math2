---
tag: GWDGRPAQSM
kind: statement
role: theorem
name: Size-width relation for resolution
aliases: [ben-sasson-wigderson-theorem, width-size-tradeoff-resolution]
msc: ["03F20", "68Q17"]
topics: [CBAF7J051K]
audience: research
uses: [6JSH907W5R, 7RX0Z6S1KZ]
about: [6JSH907W5R]
proofs: [9BVKW1XJZK]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Lower bounds
history:
  first_stated: "1999"
  notes: "Eli Ben-Sasson and Avi Wigderson, Short proofs are narrow: resolution made simple, STOC 1999 and Journal of the ACM 2001."
---

## Statement

The size-width relation says that a short resolution refutation can always be made narrow, so a formula that forces wide clauses forces long refutations.
For example, if every refutation of a $3$-CNF must contain a clause with $100$ literals, then every tree-like refutation has at least $2^{97}$ clauses.

Let $F$ be an unsatisfiable CNF with $n$ variables.
Write $w(F)$ for the largest width of a clause of $F$, and $w(F \vdash \square)$ for the least width of a [[resolution refutation|6JSH907W5R]] of $F$.
Write $S_T(F \vdash \square)$ and $S(F \vdash \square)$ for the least number of clauses of a tree-like and of a general resolution refutation of $F$.

**Theorem (Ben-Sasson and Wigderson).**

1. *Tree-like resolution.*
   $$S_T(F \vdash \square) \ge 2^{\,w(F \vdash \square) - w(F)}.$$
2. *General resolution.* Let $S = S(F \vdash \square)$.
   Then
   $$w(F \vdash \square) \le w(F) + 1 + 2\sqrt{2 n \ln S},$$
   so the width is at most $w(F) + O(\sqrt{n \log S})$.
   Equivalently, if $w(F \vdash \square) \ge w(F) + 1$, then
   $$S(F \vdash \square) \ge \exp\left( \frac{\bigl(w(F \vdash \square) - w(F) - 1\bigr)^2}{8 n} \right).$$

The proof systems are tree-like and general resolution, and the measures are size in clauses and width.

## Remarks

### Why each term is there

The term $w(F)$ cannot be dropped.
A refutation contains the axioms that it uses, so its width can be as large as $w(F)$ even when it is short, and the theorem bounds only the width above $w(F)$.
The factor $n$ in part 2 cannot be dropped either.
Bonet and Galesi showed in 2001 that there are CNFs of bounded width with polynomial-size refutations whose refutation width is of order $\sqrt n$.
So the square root and the factor $n$ are the right shape in general.
The same examples show that the tree-like bound $2^{w - w(F)}$ fails for general resolution, since $2^{\sqrt n}$ is not polynomial.

### What it gives you

To prove $S(F \vdash \square) = 2^{\Omega(n)}$ for a CNF of bounded width, it is enough to prove $w(F \vdash \square) = \Omega(n)$.
Width is a local quantity, so such a bound is often a short combinatorial argument.
On a bounded-degree expander every refutation of the [[Tseitin formulas|JXTCC6KXNG]] has linear width, which gives [[Urquhart's theorem|HF1GHVRDSD]].
For a random $3$-CNF with $\Delta n$ clauses, $\Delta$ a large constant, the refutation width is $\Omega(n)$ with probability tending to $1$, so resolution needs size $2^{\Omega(n)}$; Chvátal and Szemerédi had proved this size bound in 1988 by another method.
For the pigeonhole formulas on a bipartite expander of bounded degree, the width bound gives an exponential size bound, and it implies [[Haken's theorem|4PCEYEW3JG]].

### Proof search by width

All clauses of width at most $w$ can be derived in time $n^{O(w)}$, so a refutation of least width can be found in that time.
For a CNF of bounded width with a refutation of size $S$, part 2 turns this into a search in time $n^{O(\sqrt{n \log S})}$.
This is the width-based search of Ben-Sasson and Wigderson; it is a weak form of [[automatizability|WBECDG163W]].

### The converse

A converse holds in a weaker form.
There are at most $(2n + 1)^w$ clauses of width at most $w$, so a refutation of width $w$ gives a refutation of size at most $(2n+1)^w$.
Check for $w = 1$: the empty clause and the $2n$ literals give $2n + 1$ clauses.
So constant width gives polynomial size, but width of order $\log n$ gives only a quasi-polynomial bound on size.

### Watch out

The general bound gives nothing until the width passes about $\sqrt{n}$.
For example, with $n = 10^4$ variables, $w(F) = 3$ and refutation width $50$, the exponent is $46^2/(8 \cdot 10^4) \approx 0.26$, so the bound is $S \ge 1.3$.
The tree-like bound for the same numbers is $2^{47}$.
So a width bound of order $\sqrt n$ or less proves a lot for tree-like resolution and almost nothing for general resolution.

### Generalizations

Impagliazzo, Pudlák and Sgall proved a size-degree relation of the same shape for the [[polynomial calculus|ZERBQSTZB5]], with degree in the role of width.
The general bound also holds with $n$ replaced by the number of variables that occur in the refutation, by the same proof.

## History

Eli Ben-Sasson and Avi Wigderson proved the theorem in "Short proofs are narrow: resolution made simple", presented in 1999 and published in 2001.
It unified the earlier exponential lower bounds for resolution of Haken, Urquhart, and Chvátal and Szemerédi, which had used separate counting arguments.

## Explanations

### L1 human

The width of a resolution proof is the number of letters in its longest clause.
The theorem says that a short proof never needs very long clauses.
So if every proof of a formula needs long clauses, then every proof is long.
For example, if a formula has clauses of $3$ letters and every proof needs a clause of $1000$ letters, then every tree-like proof has more than $2^{997}$ clauses.

### L2 human

We apply part 2 to a CNF of width $3$ with $n$ variables and refutation width $n/10$.
First compute the gap above $w(F) + 1$:
$$w(F \vdash \square) - w(F) - 1 = \frac{n}{10} - 4.$$
For $n \ge 80$ we have $n/10 - 4 \ge n/20$, so the square is at least $n^2/400$.
So the size bound is
$$S(F \vdash \square) \ge \exp\left(\frac{n^2}{400 \cdot 8 n}\right) = \exp\left(\frac{n}{3200}\right).$$
Check at $n = 32000$: the bound is $e^{10} \approx 22026$, and it grows by a factor $e$ for every $3200$ more variables.
The typical use of the theorem is exactly this: prove a linear lower bound on width by a combinatorial argument, and read off an exponential size bound.

### L3 human

The theorem turns size lower bounds for resolution into a question about local consistency, since width is controlled by what a refutation can know about small sets of variables.
Its proof is a restriction argument, with the [[restriction lemma|7RX0Z6S1KZ]] at its center.
Atserias and Dalmau characterized resolution width by a game in which a prover may remember only a bounded number of variables.
The same idea, a measure of local complexity that small proofs keep small, gives the size-degree relation for the polynomial calculus.
