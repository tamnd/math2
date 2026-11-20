---
tag: 7EPP1D7MGF
kind: example
name: Sentences that count elements
aliases: [quantifier-rank-of-counting-sentences]
msc: ["03C07", "03C13"]
topics: [N64R1MGDBN]
audience: ug2
instance_of: [FVEVRE5XNZ]
uses: [FVEVRE5XNZ, MQ2KK8P8NT, DKFGQTRYZE, 0FRXBVVR03, 070R982G4B]
sources:
  - url: https://en.wikipedia.org/wiki/Quantifier_rank
    locator: Examples
  - book: isbn:9780521587136
    locator: Chapter 3
---

## Example

For $n \ge 1$ let
$$\sigma_{\ge n} = \exists x_1 \cdots \exists x_n \bigwedge_{1 \le i < j \le n} \neg(x_i = x_j).$$
This [[sentence|DKFGQTRYZE]] says "there are at least $n$ elements".

1. The quantifiers $\exists x_1, \dots, \exists x_n$ are nested, so the [[quantifier rank|FVEVRE5XNZ]] of $\sigma_{\ge n}$ is $n$.
2. In the empty signature, no sentence of rank $n - 1$ says the same thing on [[finite sets|070R982G4B]]. Sets with $n - 1$ and $n$ elements satisfy the same sentences of rank $n - 1$, by [[the game on finite sets|X98C7KEQRV]], and $\sigma_{\ge n}$ separates them.
3. In the signature $\set{<}$, on [[linear orders|0FRXBVVR03]], fewer nested quantifiers suffice. The sentence $\exists x \, (\exists y \, (y < x) \wedge \exists y \, (x < y))$ has rank $2$ and says "there are at least $3$ elements".
4. One more quantifier doubles the count. Let $\beta(x) = \exists y \, (y < x \wedge \exists z \, (z < y) \wedge \exists z \, (y < z \wedge z < x))$, which says "at least $3$ elements lie below $x$". It has rank $2$.
5. With the mirror formula $\alpha(x)$ for "at least $3$ elements above $x$", the sentence $\exists x \, (\beta(x) \wedge \alpha(x))$ has rank $3$ and says "there are at least $7$ elements".

## Remarks

In step 4, $\beta(x)$ holds when some $y < x$ has a point below it and a point between it and $x$; then three points lie below $x$.
Conversely, if three points $u < v < w$ lie below $x$, take $y = v$.

In general, rank $k$ suffices for "at least $2^k - 1$ elements" in linear orders.
This bound is sharp: the [[games on linear orders|ZZPXVVZARC]] show that finite orders with at least $2^k - 1$ elements all satisfy the same sentences of rank $k$.
So the same counting statement costs rank $n$ for bare sets and only about $\log_2 n$ for orders, because the order lets one locate points by halving.

## Explanations

### L1 human

To say "there are at least $5$ things" in a bare set, a sentence must name $5$ different things one after another.
Nothing shorter works, because a set with $4$ things and a set with $5$ things look the same until all $5$ are named.
In an ordered set a sentence can name a middle point and then count on each side, so it needs far fewer nested steps.

### L2 human

We check that the rank $2$ sentence $\tau = \exists x \, (\exists y \, (y < x) \wedge \exists y \, (x < y))$ separates $\set{1, 2}$ from $\set{1, 2, 3}$ under $<$.

1. In $\set{1, 2, 3}$ take $x = 2$; then $y = 1$ lies below and $y = 3$ lies above, so $\tau$ holds.
2. In $\set{1, 2}$, the point $x = 1$ has nothing below and $x = 2$ has nothing above, so $\tau$ fails.
3. The rank of $\tau$ is $2$: the outer $\exists x$ adds $1$ to the larger rank of two formulas of rank $1$.

The typical use of these sentences is to give Spoiler's strategy in a game: each nested quantifier is one round.
A trap is to expect $\sigma_{\ge n}$ to be the shortest way to count in every signature; the signature can make counting much cheaper.
