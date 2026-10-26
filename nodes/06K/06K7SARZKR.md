---
tag: 06K7SARZKR
kind: statement
role: proposition
name: The minimal polynomial divides every polynomial vanishing at the element
msc: [12F05]
uses: [0GK1WB9R98, 0MES3KS0ZC, 04GNK7K4VP]
sources:
  - url: https://en.wikipedia.org/wiki/Minimal_polynomial_(field_theory)
    locator: Properties
---

## Statement

Let $L/K$ be a [[field extension|0WQ1A8SHTZ]], let $a \in L$ be algebraic over $K$, and let $m_a$ be its [[minimal polynomial|0GK1WB9R98]].
For every $f \in K[x]$ with $f(a) = 0$, the polynomial $m_a$ [[divides|04GNK7K4VP]] $f$ in $K[x]$.

## Remarks

The proof: [[polynomial division|0MES3KS0ZC]] gives $f = q m_a + r$ with $\deg r < \deg m_a$. Then $r(a) = 0$, so $r = 0$ by the minimality of $\deg m_a$.
Equivalently, the kernel of the evaluation map $K[x] \to L$, $f \mapsto f(a)$, is the ideal $(m_a)$.
If $a$ is a root of $f$ and $f$ is monic and irreducible over $K$, then $f = m_a$.

## Explanations

### L1 human

Every polynomial equation that the element satisfies comes from the minimal polynomial.
It is a multiple of the minimal polynomial.
