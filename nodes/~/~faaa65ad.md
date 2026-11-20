---
tag: ~faaa65ad
kind: example
name: The interior algebra of up-sets of a finite preorder
msc: ["06E25", "03B45"]
topics: [QYA4H5Y7VR]
audience: research
instance_of: [BDEX7HET71]
uses: [7X1HGZ6FK0, 0VABYWJWH9, ETCE287E2R, ATP1JK3V27]
sources:
  - url: https://en.wikipedia.org/wiki/Interior_algebra
    locator: Relationships to other areas of mathematics
  - url: https://en.wikipedia.org/wiki/Alexandrov_topology
    locator: lead section
---

## Example

Let $W = \set{0, 1, 2}$ with the [[preorder|0VABYWJWH9]] $0 \le 1$, $0 \le 2$, and $w \le w$ for each $w$.
Let $B$ be the power set of $W$, and let $Ix = \set{w : v \in x \text{ for every } v \ge w}$.
So $Ix$ is the largest [[up-set|ETCE287E2R]] inside $x$.
We check the four axioms of an [[interior algebra|7X1HGZ6FK0]] and compute the open elements.

1. $IW = W$, since every $v$ lies in $W$.
2. $Ix \subseteq x$, since $w \ge w$ gives $w \in x$ for $w \in Ix$.
3. $Ix$ is an up-set: if $w \in Ix$ and $w \le w'$, then every $v \ge w'$ satisfies $v \ge w$, so $v \in x$.
   An up-set $u$ has $Iu = u$, so $IIx = Ix$.
4. $w \in I(x \cap y)$ iff all $v \ge w$ lie in $x$ and in $y$, iff $w \in Ix \cap Iy$.
5. The open elements are the up-sets: $\emptyset$, $\set{1}$, $\set{2}$, $\set{1, 2}$, $W$.
6. Heyting negation: $\neg \set{1} = I\set{0, 2} = \set{2}$, since $0 \le 1$ and $1 \notin \set{0, 2}$.
7. So $\set{1} \lor \neg \set{1} = \set{1, 2} \ne W$, and $\neg \neg \set{1} = I\set{0, 1} = \set{1}$.

So $(B, I)$ is an interior algebra whose open elements form a five-element Heyting algebra.

## Remarks

1. This is the [[Alexandrov topology|ATP1JK3V27]] of the preorder: the open sets are exactly the up-sets.
2. The open elements form the lattice $0 < \set{1}, \set{2} < \set{1, 2} < 1$; it is [[the five-element Heyting algebra that is not a BL-algebra|~32d5d900]].
3. In it, $\set{1} \Rightarrow \set{2} = \set{2}$ and $\set{2} \Rightarrow \set{1} = \set{1}$, so $(p \to q) \lor (q \to p)$ fails.
4. If the preorder is a chain $0 \le 1 \le 2$, the open elements form a four-element chain, and the Gödel-Dummett law holds.
5. Every finite interior algebra arises in this way from a finite preorder.

## Explanations

### L1 human

Think of the points $1$ and $2$ as two possible futures of the present $0$.
A statement is "settled" at a point if it stays true at every later point.
The settled statements are the up-sets: if true now, then true later.
"It will be like future $1$" is settled only at $1$.
So at the present $0$, neither it nor its negation is settled.

### L2 human

1. Compute $I\set{1, 2}$: the point $0$ has $1, 2 \ge 0$ in the set, but $0 \notin \set{1, 2}$.
2. So $0 \notin I\set{1, 2}$, while $1$ and $2$ are in it.
3. So $I\set{1, 2} = \set{1, 2}$.
4. Compute $\set{1} \Rightarrow \set{2} = I(\set{0, 2} \cup \set{2}) = I\set{0, 2} = \set{2}$.

The typical use: finite preorders give all finite S4 countermodels, and their up-sets give the intuitionistic Kripke models.
The trap: $I$ keeps a point only if all points above it are in the set, not just the point itself.
