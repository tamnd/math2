---
tag: ~d2afe9c2
kind: statement
role: theorem
name: Size-width relation for resolution
aliases: [ben-sasson-wigderson-theorem, width-size-tradeoff-resolution]
msc: ["03F20", "68Q17"]
topics: [CBAF7J051K]
audience: research
uses: [~586b5042, ~15e29404]
about: [~586b5042]
proofs: [~5c4f8fdf]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Lower bounds
history:
  first_stated: "1999"
  notes: "Eli Ben-Sasson and Avi Wigderson, Short proofs are narrow: resolution made simple, STOC 1999 and Journal of the ACM 2001."
---

## Statement

Let $F$ be an unsatisfiable CNF with $n$ variables.
Write $w(F)$ for the largest width of a clause of $F$, and $w(F \vdash \square)$ for the least width of a [[resolution refutation|~586b5042]] of $F$.
Write $S_T(F \vdash \square)$ and $S(F \vdash \square)$ for the least number of clauses of a tree-like and of a general resolution refutation of $F$.

**Theorem (Ben-Sasson and Wigderson).**

1. *Tree-like resolution.* $S_T(F \vdash \square) \ge 2^{\,w(F \vdash \square) - w(F)}$.
2. *General resolution.* If $w(F \vdash \square) \ge w(F) + 1$, then
$$S(F \vdash \square) \ge \exp\left( \frac{\bigl(w(F \vdash \square) - w(F) - 1\bigr)^2}{8 n} \right).$$

So a small refutation can be turned into a narrow one: small size implies small width.
The measures are size in clauses and width.

## Remarks

### Why each hypothesis is needed

- The term $w(F)$ is needed. Every refutation contains the axioms it uses, so the width of a refutation can be as large as $w(F)$ even when the refutation is short. The theorem bounds only the width above $w(F)$.
- The factor $n$ in part 2 is needed. Bonet and Galesi showed in 2001 that there are CNFs with polynomial-size refutations whose refutation width is of order $\sqrt n$. So the square and the factor $n$ cannot be improved in general.
- Part 1 has no factor $n$. The bound $2^{w - w(F)}$ fails for general resolution: the same examples of Bonet and Galesi have width of order $\sqrt n$ and polynomial size.

### Consequences

- *Lower bounds by width.* To prove $S(F \vdash \square) = 2^{\Omega(n)}$ for CNFs of bounded width, it is enough to prove $w(F \vdash \square) = \Omega(n)$.
- *Tseitin formulas.* On a bounded-degree expander, every refutation has width $\Omega(n)$; see [[Tseitin formulas|~4386fc47]] and [[Urquhart's theorem|~49e4d63e]].
- *Random $3$-CNFs.* For a random $3$-CNF with $\Delta n$ clauses, $\Delta$ a large constant, the refutation width is $\Omega(n)$ with probability tending to $1$. So resolution needs size $2^{\Omega(n)}$. Chvátal and Szemerédi had proved the size bound in 1988 by a different method.
- *Pigeonhole formulas.* For the pigeonhole formulas on a bipartite expander graph of bounded degree, the width bound gives an exponential size bound, and it implies [[Haken's theorem|~dd16430c]].
- *Proof search.* A refutation of least width can be found in time $n^{O(w)}$ by deriving all clauses of width at most $w$. So by part 2, a refutation of size $S$ yields an algorithm that finds a refutation in time $n^{O(\sqrt{n \log S})}$. This is the width-based search of Ben-Sasson and Wigderson; see [[automatizability|~64ace3b8]].

### Converse

A converse holds in a weaker form.
There are at most $(2n + 1)^w$ clauses of width at most $w$, so a refutation of width $w$ gives a refutation of size at most $(2n+1)^w$.
So constant width gives polynomial size, but width of order $\log n$ gives only a quasi-polynomial bound on size.

### Generalizations

- Analogous size-degree relations hold for the [[polynomial calculus|~57cdb980]], where degree plays the role of width.
- The general bound holds with $n$ replaced by the largest number of variables that occur in a refutation, by the same proof.

## History

Eli Ben-Sasson and Avi Wigderson proved the theorem in "Short proofs are narrow: resolution made simple", presented in 1999 and published in 2001.
It unified the earlier lower bounds of Haken, Urquhart, and Chvátal and Szemerédi, which had used separate counting arguments.

## Explanations

### L1 human

The width of a resolution proof is the length of its longest clause.
The theorem says that a short proof never needs very long clauses.
So if every proof of a formula needs long clauses, then every proof is long.
For example, if a formula with $10^4$ variables has clauses of width $3$ and needs refutation width $1000$, then every tree-like refutation has more than $2^{997}$ clauses.

### L2 human

We apply part 2 to a CNF of width $3$ with $n$ variables and refutation width $n/10$.

1. $w(F \vdash \square) - w(F) - 1 = n/10 - 4$.
2. For $n \ge 80$, $n/10 - 4 \ge n/20$, so the square is at least $n^2/400$.
3. So $S(F \vdash \square) \ge \exp\bigl(n^2/(400 \cdot 8 n)\bigr) = \exp(n/3200)$.

The typical use of the theorem is to prove a lower bound on width by a combinatorial argument, and then read off the size bound.
A trap: the general bound needs width larger than about $\sqrt{n}$ to give anything, while the tree-like bound works for any width above $w(F)$.

### L3 human

The theorem turns size lower bounds for resolution into a game on partial assignments, since width is controlled by local consistency.
Its proof is a restriction argument with the [[restriction lemma|~15e29404]] at its center.
Size-degree relations of the same shape hold for the polynomial calculus.
Atserias and Dalmau characterized resolution width by a game in which a prover may remember only a bounded number of variables.
