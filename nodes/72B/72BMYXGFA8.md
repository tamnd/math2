---
tag: 72BMYXGFA8
kind: statement
role: theorem
name: Ehrenfeucht-Fraïssé theorem
aliases: [ehrenfeucht-fraisse-theorem]
msc: ["03C07", "03C13"]
topics: [N64R1MGDBN]
audience: grad
about: [2RE7YAZK8R, FVEVRE5XNZ, P3B1V182N4]
uses: [2RE7YAZK8R, 1DVRN1T2Z0, FVEVRE5XNZ, MQ2KK8P8NT, P3B1V182N4, WDVVEYD6AT, 983GZBQYT4]
sources:
  - url: https://en.wikipedia.org/wiki/Ehrenfeucht%E2%80%93Fra%C3%AFss%C3%A9_game
    locator: Equivalence and inexpressibility
  - book: isbn:9780521587136
    locator: Chapter 3
---

## Statement

Let $L$ be a finite [[signature|WDVVEYD6AT]] with relation symbols only.
Let $\mathcal{A}$ and $\mathcal{B}$ be $L$-[[structures|983GZBQYT4]], let $\bar a \in A^k$ and $\bar b \in B^k$, and let $n \ge 0$.
The following are equivalent.

1. Duplicator has a winning strategy in the [[Ehrenfeucht-Fraïssé game|2RE7YAZK8R]] $G_n(\mathcal{A}, \bar a, \mathcal{B}, \bar b)$ with $n$ rounds, starting from the pairs $a_i \mapsto b_i$.
2. $(\mathcal{A}, \bar a) \equiv_n (\mathcal{B}, \bar b)$: for every formula $\varphi(x_1, \dots, x_k)$ of [[quantifier rank|FVEVRE5XNZ]] at most $n$, $\mathcal{A} \models \varphi(\bar a)$ if and only if $\mathcal{B} \models \varphi(\bar b)$.

For $k = 0$: Duplicator wins $G_n(\mathcal{A}, \mathcal{B})$ if and only if $\mathcal{A} \equiv_n \mathcal{B}$.
So $\mathcal{A}$ and $\mathcal{B}$ are [[elementarily equivalent|P3B1V182N4]] if and only if Duplicator wins $G_n(\mathcal{A}, \mathcal{B})$ for every $n$.
The implication from 1 to 2 holds for every relational signature, finite or not.

## Remarks

### Why each hypothesis is needed

Finiteness of $L$ is needed for 2 to imply 1.
Let $L = \set{P_0, P_1, \dots}$ with unary $P_i$.
Let $\mathcal{B} = \N$ with $m \in P_i$ iff $i < m$, and let $\mathcal{A} = \N \cup \set{\infty}$ with $\infty$ in every $P_i$.
A rank $1$ sentence mentions only $P_0, \dots, P_{N-1}$ for some $N$, and for those, $N \in \N$ looks like $\infty$.
So $\mathcal{A} \equiv_1 \mathcal{B}$.
But Spoiler wins $G_1$ by picking $\infty$, since each answer $m$ fails $P_m$.

The absence of function symbols is needed.
Let $L = \set{f}$ with $f$ unary, and let the game ask that the chosen elements generate isomorphic substructures.
Let $\mathcal{B}$ be the disjoint union of $f$-cycles of every finite length, and let $\mathcal{A}$ be $\mathcal{B}$ plus a copy of $(\Z, x \mapsto x + 1)$.
A quantifier-free formula $\theta(x)$ only compares $f^i(x)$ and $f^j(x)$ for $i, j \le N$, and a cycle longer than $N$ looks like $\Z$ for those.
So $\mathcal{A} \equiv_1 \mathcal{B}$.
But Spoiler wins $G_1$ by picking a point of $\Z$, which generates an infinite substructure.

### Consequences

- A property $P$ is not first-order definable if for each $n$ there are $\mathcal{A}_n$ with $P$ and $\mathcal{B}_n$ without $P$ on which Duplicator wins $G_n$; see [[non-definability by games|VT2PSXKM50]].
- $(\Z, <) \equiv (\Z + \Z, <)$, by [[this example|JPE6BXFX3F]].
- Finite linear orders with at least $2^n - 1$ elements are $n$-equivalent, by the [[games on linear orders|ZZPXVVZARC]].
- Each class of $\equiv_n$ is defined by one sentence of rank $n$, the Hintikka formula of any of its members.

### Converse

The theorem is an equivalence.
Winning every finite game is weaker than winning the infinite game: $(\Z, <)$ and $(\Z + \Z, <)$ are elementarily equivalent but [[not partially isomorphic|4TAA50T7QB]].
The infinite game corresponds to the infinitary logic $L_{\infty\omega}$, by [[Karp's theorem|KAWWZ2DF0G]].

### Generalizations

- Constant symbols can be allowed: they count as pairs chosen before the game starts.
- Function symbols can be handled by unnested formulas or by replacing each function by its graph, at the cost of changing the quantifier rank.
- The pebble game with $k$ pebbles characterizes the logic with $k$ variables, and games with set moves characterize monadic second-order logic.

## History

Roland Fraïssé gave the characterization of elementary equivalence by systems of partial isomorphisms in his thesis, published in 1954.
Andrzej Ehrenfeucht formulated it as a game in a paper of 1961 on the completeness of theories.

## Explanations

### L1 human

Duplicator can survive $n$ rounds of the game exactly when no sentence with $n$ nested quantifiers tells the two structures apart.
Each round answers one quantifier.
If a sentence with an "exists" is true on one side, Spoiler picks the witness there, and Duplicator must find a witness on the other side.

### L2 human

We use the theorem to show that the orders $(\Z, <)$ and $(\Q, <)$ agree on sentences of rank $2$.

1. Round 1: whatever Spoiler picks, Duplicator picks any element on the other side. Neither order has endpoints.
2. Round 2: Spoiler picks an element below, equal to or above the first one. Duplicator picks an element in the same position on the other side, which exists for the same reason.
3. The two pairs are ordered the same way, so Duplicator wins $G_2$.
4. By the theorem, $(\Z, <) \equiv_2 (\Q, <)$, although density, of rank $3$, separates them.

A trap is to use only the direction from games to sentences when the signature is infinite, and then to expect the other direction as well.

### L3 human

The theorem is a completeness result for a proof method: every difference of rank $n$ is witnessed by a winning strategy for Spoiler in $n$ rounds, and conversely.
It holds in finite model theory without change, while the compactness theorem fails there, so games are the standard tool for inexpressibility on finite structures.
