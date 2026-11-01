---
tag: VT98YJJJ47
kind: definition
name: Grunsky matrix
msc: [30C50, 30C55]
defines: XKRR37N916
uses: [R91E83SDBD, 0X3XD2ATB0, 0X2FY491PF]
sources:
  - url: https://en.wikipedia.org/wiki/Grunsky_matrix
---

## Definition

Let $\Delta = \set{z \in \C : \abs{z} > 1}$.
Let $g$ be an injective meromorphic function on $\Delta \cup \set{\infty}$ with a simple pole at $\infty$ and [[Laurent expansion|0X3XD2ATB0]]
$$g(z) = z + b_0 + \sum_{n=1}^{\infty} b_n z^{-n}, \qquad \abs{z} > 1.$$
The function $Q(z, \zeta) = \dfrac{g(z) - g(\zeta)}{z - \zeta}$ for $z \ne \zeta$, with $Q(z, z) = g'(z)$, is holomorphic and nowhere zero on $\Delta \times \Delta$ and tends to $1$ as $z, \zeta \to \infty$.
So it has a holomorphic [[logarithm|0X2FY491PF]] with value $0$ at $(\infty, \infty)$, with an expansion
$$\log \frac{g(z) - g(\zeta)}{z - \zeta} = -\sum_{m, n \ge 1} c_{mn}\, z^{-m} \zeta^{-n}, \qquad \abs{z}, \abs{\zeta} > 1.$$
The numbers $c_{mn}$ are the *Grunsky coefficients* of $g$, and the infinite matrix $(c_{mn})_{m, n \ge 1}$ is the *Grunsky matrix* of $g$.

## Remarks

The Grunsky matrix is symmetric: $c_{mn} = c_{nm}$, because $Q(z, \zeta) = Q(\zeta, z)$.
The coefficients are polynomials in $b_1, b_2, \ldots$; for example $c_{11} = b_1$.
The Grunsky inequalities say that for every finite sequence $\lambda_1, \ldots, \lambda_N \in \C$,
$$\Bigl| \sum_{m, n = 1}^{N} \sqrt{mn}\, c_{mn} \lambda_m \lambda_n \Bigr| \le \sum_{n=1}^{N} \abs{\lambda_n}^2.$$
Example: $g(z) = z + 1/z$ is injective on $\Delta$, since $g(z) = g(w)$ with $z \ne w$ forces $zw = 1$.
Here $Q(z, \zeta) = 1 - 1/(z\zeta)$, so $\log Q = -\sum_{n \ge 1} \frac{1}{n} (z\zeta)^{-n}$, and $c_{nn} = 1/n$ while $c_{mn} = 0$ for $m \ne n$.
The weighted matrix $(\sqrt{mn}\, c_{mn})$ is the identity, so the Grunsky inequalities reduce to $\abs{\sum_n \lambda_n^2} \le \sum_n \abs{\lambda_n}^2$, with equality for real $\lambda_n$.
Non-example: $g(z) = z + 2/z$ is not injective on $\Delta$, since $g(i\sqrt{2}) = g(-i\sqrt{2}) = 0$.
Then $Q(z, \zeta) = 1 - 2/(z\zeta)$ vanishes at points of $\Delta \times \Delta$, and no holomorphic logarithm exists there.
Sign and normalisation conventions differ between authors; some use $\log\frac{g(z) - g(\zeta)}{z - \zeta}$ with a plus sign or with the factors $\sqrt{mn}$ built in.
