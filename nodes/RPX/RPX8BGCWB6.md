---
tag: RPX8BGCWB6
kind: proof
name: Proof that the minimal polynomial divides every polynomial vanishing at the element
msc: [12F05]
proves: 06K7SARZKR
uses: [0WQ1A8SHTZ, 0NPW1DWECM, 0GK1WB9R98, 0MES3KS0ZC, 04GNK7K4VP, 0BDX4MBKT4, 0125QVNCFQ]
methods: [0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Minimal_polynomial_(field_theory)
    locator: Properties
---

## Proof

1. Let $L/K$ be a [[field extension|0WQ1A8SHTZ]], let $a \in L$ be [[algebraic|0NPW1DWECM]] over $K$, and let $m_a$ be its [[minimal polynomial|0GK1WB9R98]]. Let $f \in K[x]$ with $f(a) = 0$.
2. The polynomial $m_a$ is [[monic|0BDX4MBKT4]]. By [[polynomial division|0MES3KS0ZC]], there are $q, r \in K[x]$ with $f = q m_a + r$ and $\deg r < \deg m_a$.
3. [[Evaluation at $a$|0125QVNCFQ]] is a ring homomorphism. So $f(a) = q(a) m_a(a) + r(a)$, and $0 = q(a) \cdot 0 + r(a)$. Hence $r(a) = 0$.
4. Suppose that $r \ne 0$, and let $c \ne 0$ be its leading coefficient. Then $c^{-1} r$ is monic, vanishes at $a$, and has degree less than $\deg m_a$.
5. This contradicts the minimality of $\deg m_a$. So $r = 0$.
6. Then $f = q m_a$, so $m_a$ [[divides|04GNK7K4VP]] $f$ in $K[x]$.

## Idea

Divide $f$ by $m_a$. The remainder also vanishes at $a$ and has smaller degree than $m_a$. Since $m_a$ has the least degree among monic polynomials with root $a$, the remainder must be zero.
