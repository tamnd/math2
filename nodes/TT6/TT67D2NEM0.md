---
tag: TT67D2NEM0
kind: definition
name: Communication complexity
msc: [68Q11, 68Q17]
defines: 4DJPQPQA4A
uses: [0XHDTE5YMZ]
sources:
  - url: https://en.wikipedia.org/wiki/Communication_complexity
---

## Definition

Let $X$ and $Y$ be finite sets and let $f \colon X \times Y \to \set{0, 1}$ be a [[function|0XHDTE5YMZ]].
A *deterministic protocol* for $f$ is a rooted binary tree with these labels.

1. Each internal node is owned by Alice or by Bob.
2. An internal node owned by Alice carries a map $a \colon X \to \set{0, 1}$, and one owned by Bob carries a map $b \colon Y \to \set{0, 1}$.
3. Each leaf carries an output in $\set{0, 1}$.

On input $(x, y)$, the run starts at the root.
At each internal node it applies the map of the node to $x$ or to $y$.
It goes to the left child if the value is $0$, and to the right child if it is $1$.
The protocol *computes* $f$ if for every $(x, y)$ the run ends at a leaf whose label is $f(x, y)$.
The *cost* of the protocol is the depth of the tree, the number of bits sent in the worst case.
The *deterministic communication complexity* $D(f)$ is the least cost of a protocol that computes $f$.

## Remarks

Every $f$ has $D(f) \le \lceil \log_2 \abs{X} \rceil + 1$: Alice sends $x$ and Bob sends $f(x, y)$.

Example: let $X = Y = \set{0,1}^n$ and let $\mathrm{EQ}(x, y) = 1$ exactly when $x = y$.
Then $D(\mathrm{EQ}) = n + 1$.
The lower bound holds because the inputs $(x, x)$ must reach $2^n$ distinct leaves labeled $1$, and the protocol also needs leaves labeled $0$.

Non-example: a "protocol" in which a leaf label depends on $x$ itself is not allowed by clause 3.
The output must be determined by the bits sent, which both players see.

Randomized complexity allows random bits and errors of probability at most $1/3$.
For $\mathrm{EQ}$ it is $O(\log n)$ with private randomness and $O(1)$ with shared randomness.
