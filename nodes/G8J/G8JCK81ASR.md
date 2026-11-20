---
tag: G8JCK81ASR
kind: example
name: The three-element chain with order-reversing negation is not a Post algebra
msc: ["06D25", "06D30"]
topics: [QYA4H5Y7VR]
audience: research
not_instance_of:
  - target: RD2A5Z7E2B
    note: the identity x''' = x of the three-element Post chain fails at 0
uses: [G24036DJ5K, P7MWSZ837M, 5Q53XWV0QN]
sources:
  - url: https://en.wikipedia.org/wiki/Many-valued_logic
---

## Example

Take $K = (\set{0, 1, 2}, \max, \min, ', 0, 2)$ with $x' = 2 - x$.
It has the same signature as [[the Post chain $\mathbf{P}_3$|P7MWSZ837M]].

1. The identity $x''' = x$ holds in $\mathbf{P}_3$, since its negation is a cycle of length $3$.
2. So $x''' = x$ holds in every Post algebra of order $3$; see [[the definition|G24036DJ5K]].
3. In $K$, $0' = 2$, $0'' = 0$ and $0''' = 2 \ne 0$.

So $K$ is not a [[Post algebra|RD2A5Z7E2B]] of order $3$.

## Remarks

1. $K$ satisfies $x'' = x$ and $(x \lor y)' = x' \land y'$, so it is a [[De Morgan algebra|5Q53XWV0QN]].
2. It also satisfies $x \land x' \le y \lor y'$, so it is the three-element Kleene algebra, the algebra of strong Kleene logic.
3. $K$ is not a Post algebra of any order $n \ge 2$. A finite Post algebra of order $n$ is a power $\mathbf{P}_n^k$, so it has $n^k$ elements, and $3 = n^k$ forces $n = 3$ and $k = 1$. But $K \not\cong \mathbf{P}_3$, since $0'' = 0$ in $K$ and $0'' = 2$ in $\mathbf{P}_3$.
4. The two negations differ in their order behavior: $x \mapsto 2 - x$ reverses the order, and the cyclic negation does not.

## Explanations

### L1 human

This algebra uses the "mirror" negation: false and true swap, and middle stays.
Post's negation instead moves every value one step up and wraps around.
The two negations give different laws.

### L2 human

1. In $K$, apply the negation three times to $0$: $0 \mapsto 2 \mapsto 0 \mapsto 2$.
2. In $\mathbf{P}_3$, the same gives $0 \mapsto 1 \mapsto 2 \mapsto 0$.
3. The law $x''' = x$ separates the two algebras.

The typical use: the example shows that the name "negation" covers very different operations in many-valued logic.
The trap: the same lattice can carry several negations, and the variety depends on the choice.
