---
tag: 14Z5TDHRV2
kind: example
name: The density axiom on the rational and the integer time lines
msc: ["03B44"]
topics: [CQM9SRN8PM]
audience: grad
instance_of: [8XB117FKKV]
uses: [8XB117FKKV, 2W4S2H4VYA, NGHWZ9Y7ZV]
sources:
  - url: https://en.wikipedia.org/wiki/Temporal_logic
    locator: Temporal operators
  - book: isbn:9780521527149
    locator: Blackburn, de Rijke and Venema, Modal Logic, chapter 3
---

## Example

We compare the [[temporal frames|8XB117FKKV]] $(\mathbb{Q}, <)$ and $(\mathbb{Z}, <)$ with the density formula
$$\delta = Fp \to FFp.$$
A frame $(T, <)$ is dense when for all $t < u$ there is $z$ with $t < z < u$.
We show that $\delta$ is valid on a frame exactly when the frame is dense.

1. Let $(T, <)$ be dense, let $V$ be any valuation, and let $Fp$ be true at $t$.
2. By the clause for $F$, there is $u$ with $t < u$ and $p$ true at $u$.
3. By density there is $z$ with $t < z < u$. Then $Fp$ is true at $z$, because $z < u$.
4. So $FFp$ is true at $t$, because $t < z$. Hence $\delta$ is true at every point under every valuation.
5. Let $(T, <)$ be not dense. Then there are $t < u$ with no point strictly between them.
6. Put $V(p) = \set{u}$. Then $Fp$ is true at $t$, because $t < u$.
7. $FFp$ at $t$ needs $z$ with $t < z$ and $Fp$ at $z$. $Fp$ at $z$ needs $z < u$, since $u$ is the only $p$-point.
8. No such $z$ exists, so $FFp$ is false at $t$, and $\delta$ fails at $t$.
9. The rationals are a [[dense linear order|2W4S2H4VYA]]: for $t < u$ the point $z = (t + u)/2$ lies strictly between. So $\delta$ is valid on $(\mathbb{Q}, <)$.
10. The integers are not dense: nothing lies strictly between $0$ and $1$. Steps 5 to 8 with $t = 0$, $u = 1$ refute $\delta$ on $(\mathbb{Z}, <)$.

## Remarks

The example shows how a property of time becomes a modal axiom: density corresponds to $Fp \to FFp$.
The same proof works for $(\mathbb{R}, <)$, which is dense.
On $(\mathbb{Z}, <)$ the opposite property holds: every point has an immediate successor.
That property makes "next" definable with until, as in [[since and until on the integers|FJEN3XBRP1]].
The validity of $\delta$ needs all valuations: on $\mathbb{Z}$ with $p$ true everywhere, $\delta$ is true at every point.

## Explanations

### L1 human

Think of time as made of instants, like the fractions or like the whole numbers.
"It will be the case that it will rain" follows from "it will rain" when time has no gaps.
With fractions, between now and the rainy instant there is always a middle instant, and from there the rain is still ahead.
With whole numbers, if it rains tomorrow, there is no instant between today and tomorrow.

### L2 human

1. Take $T = \mathbb{Q}$, $t = 0$, and $p$ true only at $u = \tfrac{1}{2}$.
2. $Fp$ holds at $0$.
3. The point $z = \tfrac{1}{4}$ satisfies $0 < z < \tfrac{1}{2}$, so $Fp$ holds at $\tfrac{1}{4}$ and $FFp$ holds at $0$.
4. Now take $T = \mathbb{Z}$, $t = 0$, and $p$ true only at $1$. No $z$ works, so $FFp$ fails at $0$.

The typical use is the axiomatization of the tense logic of $\mathbb{Q}$, which contains $\delta$.
A trap: $\delta$ is the converse of the transitivity axiom $FFp \to Fp$, and the two are often swapped.
