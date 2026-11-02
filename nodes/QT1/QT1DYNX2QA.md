---
tag: QT1DYNX2QA
kind: definition
name: Pincherle derivative
msc: [47B47, 44A45]
defines: R0H4RXF0YZ
uses: [0SDC934R52, 0NRYHJPQG2]
sources:
  - url: https://en.wikipedia.org/wiki/Pincherle_derivative
---

## Definition

Let $K$ be a field and let $K[x]$ be the [[polynomial ring|0SDC934R52]] in one variable over $K$.
Let $T \colon K[x] \to K[x]$ be a $K$-[[linear map|0NRYHJPQG2]].
The *Pincherle derivative* of $T$ is the linear map $T'$ on $K[x]$ given by
$$T'(f) = T(x f) - x \, T(f) \qquad (f \in K[x]).$$
Writing $x$ also for the operator of multiplication by $x$, this says $T' = T x - x T$.

## Remarks

The map $T \mapsto T'$ is linear and satisfies the product rule $(ST)' = S'T + ST'$, since $STx - xST = S(Tx - xT) + (Sx - xS)T$.

Example: for $D = d/dx$, $D'(f) = (xf)' - x f' = f$, so $D' = \id$.
For the shift $E^h f(x) = f(x + h)$ with $h \in K$, $(E^h)'(f)(x) = (x + h) f(x + h) - x f(x + h) = h f(x + h)$, so $(E^h)' = h E^h$.

Operators with Pincherle derivative zero: a multiplication operator $M_q f = q f$ with $q \in K[x]$ commutes with $x$, so $M_q' = 0$.
Conversely, $T' = 0$ forces $T(x^n) = x^n T(1)$ for all $n$, so $T = M_{T(1)}$.
