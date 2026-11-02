---
tag: 8GSKDNZ4TK
kind: statement
role: theorem
name: Legendre's relation
msc: ["33E05"]
uses: [RM54CPPE12, VS2PSX14C8]
about: [RM54CPPE12, VS2PSX14C8]
sources:
  - url: https://en.wikipedia.org/wiki/Legendre%27s_relation
same_as:
  wikidata: Q6517885
  wikipedia: Legendre's relation
---

## Statement

Let $0 < k < 1$ and $k' = \sqrt{1 - k^2}$.
Let $K = K(k)$ and $K' = K(k')$ be [[complete elliptic integrals of the first kind|RM54CPPE12]], and let $E = E(k)$ and $E' = E(k')$ be [[complete elliptic integrals of the second kind|VS2PSX14C8]].
Then
$$E K' + E' K - K K' = \frac{\pi}{2}.$$

## Remarks

Proof idea: differentiation under the integral sign gives $\frac{dE}{dk} = \frac{E - K}{k}$ and $\frac{dK}{dk} = \frac{E - k'^2 K}{k k'^2}$.
With these rules, and the same rules for $E'$ and $K'$ via $dk'/dk = -k/k'$, the derivative of the left side in $k$ is $0$, so the left side is constant.
To find the constant, let $k \to 0$: then $K, E \to \pi/2$ and $E' \to 1$, while $K'$ grows only like $\log(4/k)$ and $E - K = O(k^2)$, so $(E - K)K' \to 0$ and the left side tends to $\pi/2$.
Example: at $k = 1/\sqrt{2}$ one has $k = k'$, so $K = K'$ and $E = E'$, and the relation becomes $2EK - K^2 = \pi/2$.
There is a parallel form for the periods $\omega_1, \omega_2$ and quasi-periods $\eta_1, \eta_2$ of the [[Weierstrass zeta function|QATW7046PD]]: $\eta_1\omega_2 - \eta_2\omega_1 = 2\pi i$ when $\operatorname{Im}(\omega_2/\omega_1) > 0$.

## Explanations

### L1 human

The four complete elliptic integrals $K, E, K', E'$ are transcendental functions of $k$, and none of them has a simple closed form.
Yet this particular combination of them is always exactly $\pi/2$, whatever the modulus.
It is one of the few exact links between these integrals and the number $\pi$.

### L2 human

Legendre's relation is the key identity behind the Gauss–Legendre algorithm for $\pi$, also called the Brent–Salamin algorithm.
That algorithm combines it with the [[arithmetic–geometric mean|E0V3N93DX8]] formula for $K$ and a similar formula for $E$.
For an elliptic curve it is the same fact as the quasi-period relation for the Weierstrass zeta function, read for a curve with real periods.
It is also used to compute $E$ from $K$ at special moduli, for example at $k = 1/\sqrt 2$, where it gives $E(1/\sqrt2) = \frac{\pi/2 + K^2}{2K}$ with $K = K(1/\sqrt2)$, a value tied to the [[lemniscate constant|V5A2S8QYQQ]].
