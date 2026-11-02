---
tag: MBVJ4JQXC5
kind: definition
name: Galois connection
msc: [06A15]
defines: Q5JHEPRYQ6
uses: [011C29Q1S1, 0WFF6AZPBP]
sources:
  - url: https://en.wikipedia.org/wiki/Galois_connection
---

## Definition

Let $(P, \le)$ and $(Q, \le)$ be [[partially ordered sets|011C29Q1S1]].
A (monotone) *Galois connection* between $P$ and $Q$ is a pair of maps $f \colon P \to Q$ and $g \colon Q \to P$ such that, for all $x \in P$ and $y \in Q$,
$$f(x) \le y \iff x \le g(y).$$
The map $f$ is the *lower adjoint* and $g$ is the *upper adjoint* of the connection.

## Remarks

Let $i \colon \Z \to \R$ be the inclusion and $\lfloor \cdot \rfloor \colon \R \to \Z$ the [[floor function|0YVRNEDSVG]].
Then $i(n) \le x$ if and only if $n \le \lfloor x \rfloor$, so $(i, \lfloor \cdot \rfloor)$ is a Galois connection.
On $\R$, the pair $f(x) = x + 1$, $g(y) = y$ is not a Galois connection: for $x = 0$ and $y = 1/2$, $x \le g(y)$ holds but $f(x) \le y$ fails.
In a Galois connection both maps are [[monotone|0WFF6AZPBP]], $x \le g(f(x))$ and $f(g(y)) \le y$, and $f \circ g \circ f = f$ and $g \circ f \circ g = g$.
Each adjoint determines the other: $g(y)$ is the greatest $x$ with $f(x) \le y$.
The lower adjoint preserves all existing suprema, and the upper adjoint preserves all existing infima.
An *antitone* Galois connection uses order-reversing maps with $y \le f(x)$ if and only if $x \le g(y)$; it is a monotone connection between $P$ and the dual of $Q$.

## Explanations

### L1 human

In a Galois connection, the question "is $f(x)$ below $y$?" has the same answer as "is $x$ below $g(y)$?".
So $f$ and $g$ behave like inverses as far as the order can tell.
