---
tag: P7MWSZ837M
kind: example
name: The three-element Post chain
msc: ["06D25", "03G20"]
topics: [QYA4H5Y7VR]
audience: research
instance_of: [RD2A5Z7E2B]
uses: [G24036DJ5K, XD01Y7B6XW]
sources:
  - url: https://en.wikipedia.org/wiki/Many-valued_logic
---

## Example

Take $\mathbf{P}_3 = (\set{0, 1, 2}, \max, \min, ', 0, 2)$ with $0' = 1$, $1' = 2$ and $2' = 0$.
It generates the variety of Post algebras of order $3$, so it belongs to it; see [[the definition|G24036DJ5K]].
We compute its main features.

1. Constants. $e_0 = 0$, $e_1 = 0' = 1$ and $e_2 = 0'' = 2$.
2. Order of the negation. $x''' = x$ for each $x$, since the negation is a cycle of length $3$.
3. Complemented elements. $0$ and $2$ are complements of each other. The element $1$ has no complement: $\min(1, y) = 0$ forces $y = 0$, and then $\max(1, 0) = 1 \ne 2$.
4. Level operations. Put $D_1(x) = 2$ if $x \ge 1$ and $0$ otherwise, and $D_2(x) = 2$ if $x = 2$ and $0$ otherwise.
5. Representation. $x = (D_1(x) \land e_1) \lor (D_2(x) \land e_2)$ for each $x$. For $x = 1$: $(2 \land 1) \lor (0 \land 2) = 1$.

So $\mathbf{P}_3$ is a [[Post algebra|RD2A5Z7E2B]] of order $3$.

## Remarks

1. $D_1$ and $D_2$ are term operations, since $\mathbf{P}_3$ is [[primal|XD01Y7B6XW]].
2. $\mathbf{P}_3$ has no proper subalgebras: $0$ is a constant, and $0' = 1$, $1' = 2$.
3. $\mathbf{P}_3$ is simple: a congruence that identifies two elements $x < y$ identifies their images under every unary term operation, and some term operation sends $x$ to $0$ and $y$ to $2$.
4. The identity $x \land x' = 0$ fails at $x = 1$, since $\min(1, 2) = 1$. So the prime is not a Boolean complement.

## Explanations

### L1 human

There are three truth values: false, middle and true.
"Not" moves false to middle, middle to true, and true back to false.
Doing "not" three times returns to the start.

### L2 human

1. Compute $(1 \lor 0')' = (1 \lor 1)' = 1' = 2$.
2. Compute $D_1(1) = 2$ and $D_2(1) = 0$.
3. These two values form the decreasing chain $2 \ge 0$ that codes the element $1$.

The typical use: identities of Post algebras of order $3$ are exactly the identities of this one finite algebra.
The trap: middle is complemented by nothing, unlike in a Boolean algebra.
