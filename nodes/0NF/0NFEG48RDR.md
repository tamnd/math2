---
tag: 0NFEG48RDR
kind: statement
role: proposition
name: The minimal polynomial is irreducible
msc: [12F05]
uses: [0GK1WB9R98, 00X2A9G9W3]
sources:
  - url: https://en.wikipedia.org/wiki/Minimal_polynomial_(field_theory)
    locator: Irreducibility
---

## Statement

Let $L/K$ be a [[field extension|0WQ1A8SHTZ]] and let $a \in L$ be algebraic over $K$.
Then the [[minimal polynomial|0GK1WB9R98]] $m_a$ of $a$ over $K$ is [[irreducible|00X2A9G9W3]] over $K$.

## Remarks

The proof: if $m_a = g h$ with $g, h \in K[x]$ of smaller degree, then $g(a) h(a) = 0$ in the field $L$. So $g(a) = 0$ or $h(a) = 0$, and this contradicts the minimality of $\deg m_a$.
Conversely, a monic irreducible polynomial $f \in K[x]$ with $f(a) = 0$ is the minimal polynomial of $a$.
For example, $x^3 - 2$ is irreducible over $\mathbb{Q}$, so it is the minimal polynomial of $\sqrt[3]{2}$ over $\mathbb{Q}$.

## Explanations

### L1 human

The minimal polynomial cannot be factored over the base field.
If it could, one of the factors would already vanish at the element, and that factor would be a smaller polynomial.
