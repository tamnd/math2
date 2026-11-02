---
tag: FE83QQS17S
kind: statement
role: theorem
name: Weierstrass division theorem
msc: [32B05, 13J07]
uses: [EVPZ7ZG1HB, 7PJ8KVZZCQ]
about: [EVPZ7ZG1HB]
sources:
  - url: https://en.wikipedia.org/wiki/Weierstrass_preparation_theorem
---

## Statement

Let $n \ge 1$, write $z' = (z_1, \dots, z_{n-1})$, and let $\mathcal{O}_n = \C\{z_1, \dots, z_n\}$ and $\mathcal{O}_{n-1} = \C\{z'\}$ be [[rings of convergent power series|EVPZ7ZG1HB]].
Let $f \in \mathcal{O}_n$ and $d \ge 0$ be such that $f(0, \dots, 0, z_n) = z_n^d\, v(z_n)$ with $v(0) \ne 0$; that is, $f$ is regular of order $d$ in $z_n$.
Then for every $g \in \mathcal{O}_n$ there are unique $q \in \mathcal{O}_n$ and $r \in \mathcal{O}_{n-1}[z_n]$ such that
$$g = q f + r \quad \text{and} \quad \deg_{z_n} r < d.$$

## Remarks

The same statement holds for [[germs of holomorphic functions|7PJ8KVZZCQ]] at $0$, since these form a ring isomorphic to $\mathcal{O}_n$.
One proof first treats a divisor $f = P$ that is a Weierstrass polynomial of degree $d$.
On a small polydisc $\abs{z'} < \varepsilon$, $\abs{z_n} < \delta$, the polynomial $P(z', \cdot)$ has its $d$ roots inside $\abs{z_n} < \delta$ for each $z'$.
The Cauchy integral
$$q(z', z_n) = \frac{1}{2\pi i} \oint_{\abs{w} = \delta} \frac{g(z', w)}{P(z', w)\,(w - z_n)}\, dw$$
defines a holomorphic $q$, and the Cauchy formula for $g$ gives
$$r = g - q P = \frac{1}{2\pi i} \oint_{\abs{w} = \delta} \frac{g(z', w)}{P(z', w)} \cdot \frac{P(z', w) - P(z', z_n)}{w - z_n}\, dw.$$
The last quotient is a polynomial in $z_n$ of degree $d - 1$, so $r$ is a polynomial in $z_n$ of degree less than $d$.
A general $f$ regular of order $d$ is a unit times a Weierstrass polynomial.
This can be shown directly through the symmetric functions of the roots of $f(z', \cdot)$, and it reduces the general case to the first one.
Example: for $n = 1$ and $f = z^d$, the theorem says $g = q z^d + r$, where $r$ is the Taylor polynomial of $g$ of degree $d - 1$.
The regularity hypothesis is needed: for $f = z_1$ in $\mathcal{O}_2$ and any $d$, the series $g = z_2^d$ is not of the form $q z_1 + r$ with $\deg_{z_2} r < d$, since setting $z_1 = 0$ would give $z_2^d = r(0, z_2)$.
Conversely, applying the theorem to $g = z_n^d$ gives the [[Weierstrass preparation theorem|49JSD49P7X]]: $f$ is a unit times the [[Weierstrass polynomial|SDCKNWSWNM]] $z_n^d - r$.
A linear change of coordinates makes any nonzero $f \in \mathcal{O}_n$ regular in $z_n$ of some order, so the hypothesis is mild.

## Explanations

### L1 human

The theorem is a division with remainder, like the division of integers or of polynomials.
One divides a power series $g$ by a power series $f$ that looks, along one axis, like $z_n^d$.
The remainder is then a polynomial in $z_n$ of degree less than $d$, with coefficients that are power series in the other variables.

### L2 human

Division is the engine behind the algebra of the ring $\mathcal{O}_n$.
It implies the preparation theorem, and with it one proves by induction on $n$ that $\mathcal{O}_n$ is Noetherian and factorial.
It also shows that $\mathcal{O}_n/(f)$ is a free module of rank $d$ over $\mathcal{O}_{n-1}$ when $f$ is regular of order $d$.
This is the algebraic form of the local parametrization of hypersurfaces.
