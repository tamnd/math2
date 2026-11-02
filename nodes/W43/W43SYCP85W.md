---
tag: W43SYCP85W
kind: definition
name: Jacobi elliptic functions
msc: ["33E05"]
defines: P071B692JF
uses: [WDHHJHVP7N, RM54CPPE12, FF9ZPCZ59K, 0M3YQJ81NB]
sources:
  - url: https://en.wikipedia.org/wiki/Jacobi_elliptic_functions
---

## Definition

Let $0 < k < 1$, and let $\operatorname{am}(u) = \operatorname{am}(u, k)$ be the [[Jacobi amplitude|WDHHJHVP7N]].
For real $u$, the *Jacobi elliptic functions* with modulus $k$ are
$$\operatorname{sn} u = \sin\operatorname{am} u, \qquad \operatorname{cn} u = \cos\operatorname{am} u, \qquad \operatorname{dn} u = \sqrt{1 - k^2\sin^2\operatorname{am} u}.$$
Each of them extends by [[analytic continuation|0M3YQJ81NB]] to a meromorphic function on $\C$, still written $\operatorname{sn}$, $\operatorname{cn}$, $\operatorname{dn}$.

## Remarks

Let $K = K(k)$ and $K' = K(\sqrt{1 - k^2})$ be [[complete elliptic integrals of the first kind|RM54CPPE12]].
The extended functions are [[elliptic functions|FF9ZPCZ59K]] with these periods:
$\operatorname{sn}$ has periods $4K$ and $2iK'$; $\operatorname{cn}$ has periods $4K$ and $2K + 2iK'$; $\operatorname{dn}$ has periods $2K$ and $4iK'$.
They satisfy
$$\operatorname{sn}^2 u + \operatorname{cn}^2 u = 1, \qquad \operatorname{dn}^2 u + k^2\operatorname{sn}^2 u = 1,$$
$$\frac{d}{du}\operatorname{sn} u = \operatorname{cn} u \operatorname{dn} u, \quad \frac{d}{du}\operatorname{cn} u = -\operatorname{sn} u \operatorname{dn} u, \quad \frac{d}{du}\operatorname{dn} u = -k^2\operatorname{sn} u \operatorname{cn} u.$$
Example: at $u = K$ one has $\operatorname{am} K = \pi/2$, so $\operatorname{sn} K = 1$, $\operatorname{cn} K = 0$ and $\operatorname{dn} K = k'$, where $k' = \sqrt{1 - k^2}$.
Check of the first derivative rule: $\frac{d}{du}\sin\operatorname{am} u = \cos(\operatorname{am} u)\cdot\frac{d\operatorname{am}}{du} = \operatorname{cn} u \operatorname{dn} u$.
Non-example: $\sin$ is not one of these functions for $0 < k < 1$, since $\sin$ is entire while $\operatorname{sn}$ has poles, at $u = iK'$ for example.
Limits: for $k \to 0$ they become $\sin$, $\cos$, $1$, and the formulas with $k = 1$ give $\tanh$, $\operatorname{sech}$, $\operatorname{sech}$.
