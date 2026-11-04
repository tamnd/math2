---
tag: RCMSYW1KBX
kind: proof
name: Proof of the Archimedean property in an Archimedean ordered field
msc: [12J15]
proves: 0A74SX55QP
uses: [0HQARMKEV5, 010JCV9J4E]
sources:
  - url: https://en.wikipedia.org/wiki/Archimedean_property
    locator: Ordered fields
---

## Proof

1. Let $F$ be an [[Archimedean ordered field|0HQARMKEV5]] and let $x \in F$.
2. First, $0 \le 1$ in $F$. The order is total, so $0 \le 1$ or $1 \le 0$.
3. If $1 \le 0$, add $-1$ to both sides, using the first axiom of an [[ordered field|010JCV9J4E]]. This gives $0 \le -1$.
4. Then the second axiom gives $0 \le (-1)(-1) = 1$. So $0 \le 1$ in both cases.
5. In a field $1 \ne 0$. Hence $0 < 1$.
6. Apply the definition of an Archimedean field with $y = 1$. It gives a natural number $n$ with $n \cdot 1 > x$.
7. Here $n \cdot 1 = 1 + \dots + 1$, with $n$ terms, is the element $n$ of $F$. So $x < n$.

## Idea

The definition says that copies of any positive $y$ add up past any $x$. Taking $y = 1$, which is positive in each ordered field, gives the claim.
