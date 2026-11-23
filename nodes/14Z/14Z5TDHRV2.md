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

We compare the [[temporal frames|8XB117FKKV]] $(\mathbb{Q}, <)$ and $(\mathbb{Z}, <)$ on the density formula below.
$$\delta = Fp \to FFp$$
A frame $(T, <)$ is dense when for all $t < u$ there is a $z$ with $t < z < u$.
We show that $\delta$ is valid on a frame exactly when the frame is dense, and then apply this to the two time lines.

1. Let $(T, <)$ be dense, let $V$ be any valuation, and let $Fp$ be true at $t$.
   By the clause for $F$, there is a $u$ with $t < u$ and $p$ true at $u$.
2. By density there is a $z$ with $t < z < u$.
   Then $Fp$ is true at $z$, because $z < u$, and so $FFp$ is true at $t$, because $t < z$.
   Hence $\delta$ is true at every point under every valuation.
3. Now let $(T, <)$ be not dense, so there are $t < u$ with no point strictly between them.
   Put $V(p) = \{u\}$, so that $Fp$ is true at $t$.
4. $FFp$ at $t$ needs a $z$ with $t < z$ and $Fp$ at $z$, and $Fp$ at $z$ needs $z < u$, since $u$ is the only $p$-point.
   No such $z$ exists, so $FFp$ is false at $t$ and $\delta$ fails at $t$.
5. The rationals are a [[dense linear order|2W4S2H4VYA]], because for $t < u$ the midpoint $z = (t + u)/2$ lies strictly between them.
   So $\delta$ is valid on $(\mathbb{Q}, <)$.
6. The integers are not dense, because nothing lies strictly between $0$ and $1$.
   Steps 3 and 4 with $t = 0$ and $u = 1$ refute $\delta$ on $(\mathbb{Z}, <)$.

## Remarks

The example shows how a property of time becomes a modal axiom: density corresponds to $Fp \to FFp$.
The same proof works for the real line $(\mathbb{R}, <)$, which is dense.
On $(\mathbb{Z}, <)$ the opposite holds, since every point has an immediate successor, and that is what makes "next" definable with until in [[since and until on the integers|FJEN3XBRP1]].

Validity needs every valuation.
On $\mathbb{Z}$ with $p$ true everywhere, $\delta$ is true at every point, because $FFp$ only needs two later points.
So one model where $\delta$ holds tells you nothing about the frame, and the refutation in step 4 needs the valuation that puts $p$ at a single point.

## Explanations

### L1 human

Think of time as made of instants, either like the fractions or like the whole numbers.
"It will be the case that it will rain" follows from "it will rain" when time has no gaps.
With fractions, between now and the rainy instant there is always a middle instant, and from there the rain is still ahead.
With whole numbers, if it rains tomorrow, there is no instant between today and tomorrow.

### L2 human

Take $T = \mathbb{Q}$, $t = 0$, and $p$ true only at $u = \tfrac{1}{2}$.
Then $Fp$ holds at $0$.
The point $z = \tfrac{1}{4}$ lies between them:
$$0 < \tfrac{1}{4} < \tfrac{1}{2}.$$
So $Fp$ holds at $\tfrac{1}{4}$, and $FFp$ holds at $0$.
Now take $T = \mathbb{Z}$, $t = 0$, and $p$ true only at $1$; no $z$ works, so $FFp$ fails at $0$.
The typical use is the axiomatization of the tense logic of $\mathbb{Q}$, which contains $\delta$.
Watch out: $\delta$ is the converse of the transitivity axiom $FFp \to Fp$, and the two are easy to swap.
