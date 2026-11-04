---
tag: WF7HV1W1BH
kind: proof
name: Proof that every element of a finite field of order q satisfies x^q = x
msc: ["12E20"]
proves: 0QWR8WTZEW
uses: [08RTDHX1SK, 05THZKR9AN, 0ZEPNS9BXK, 0KJVQV3E0F, 0DPF6WRZW6]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_field
    locator: Multiplicative structure
---

## Proof

1. Let $F$ be a [[finite field|08RTDHX1SK]] with $q$ elements. Let $F^\times$ be its [[group of units|05THZKR9AN]].
2. In a field, every nonzero element is a unit. So $F^\times = F \setminus \set{0}$, and $F^\times$ is a group of order $q - 1$.
3. Let $a \in F$ with $a \neq 0$. Then [[$a^{q-1} = 1$|0ZEPNS9BXK]], since $a$ lies in the finite group $F^\times$ of order $q - 1$.
4. Multiplying by $a$ gives $a^q = a$.
5. For $a = 0$ we have $a^q = 0 = a$, since $q \ge 1$. So $a^q = a$ for every $a \in F$.
6. Let $f = x^q - x$ and $g = \prod_{a \in F} (x - a)$ in $F[x]$. Both are monic of [[degree|0DPF6WRZW6]] $q$.
7. So the leading terms cancel in $h = f - g$, and $h$ is $0$ or has degree less than $q$.
8. Every $a \in F$ is a root of $f$ by step 5. It is also a root of $g$, because $g$ has the factor $x - a$. So every $a \in F$ is a root of $h$.
9. Thus $h$ has $q$ distinct roots in $F$. A nonzero polynomial of degree less than $q$ has [[fewer than $q$ roots|0KJVQV3E0F]]. So $h = 0$.
10. Hence $x^q - x = \prod_{a \in F} (x - a)$ in $F[x]$.

## Idea

The nonzero elements form a group of order $q - 1$, so Lagrange's theorem gives $a^{q-1} = 1$ for them. Then all $q$ elements are roots of $x^q - x$. A monic polynomial of degree $q$ with $q$ known distinct roots is the product of the linear factors, because the difference would have too many roots.
