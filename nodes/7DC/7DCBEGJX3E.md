---
tag: 7DCBEGJX3E
kind: definition
name: Dixon elliptic functions
msc: ["33E05"]
defines: PPW3GYXH0P
uses: [0NT64JV96A, FF9ZPCZ59K, 0M3YQJ81NB]
sources:
  - url: https://en.wikipedia.org/wiki/Dixon_elliptic_functions
---

## Definition

Consider the system of [[ordinary differential equations|0NT64JV96A]]
$$\operatorname{sm}'(z) = \operatorname{cm}(z)^2, \qquad \operatorname{cm}'(z) = -\operatorname{sm}(z)^2,$$
with initial values $\operatorname{sm}(0) = 0$ and $\operatorname{cm}(0) = 1$.
The *Dixon elliptic functions* $\operatorname{sm}$ and $\operatorname{cm}$ are its unique solution near $z = 0$, continued by [[analytic continuation|0M3YQJ81NB]] to meromorphic functions on $\C$.

## Remarks

The derivative of $\operatorname{sm}^3 + \operatorname{cm}^3$ is $3\operatorname{sm}^2\operatorname{cm}^2 - 3\operatorname{cm}^2\operatorname{sm}^2 = 0$, so $\operatorname{sm}^3 + \operatorname{cm}^3 = 1$ everywhere: the point $(\operatorname{cm} z, \operatorname{sm} z)$ lies on the Fermat cubic $x^3 + y^3 = 1$.
Hence $\operatorname{sm}' = (1 - \operatorname{sm}^3)^{2/3}$ near $0$, and $\operatorname{sm}$ is the inverse of $x \mapsto \int_0^x dt/(1 - t^3)^{2/3}$ near $0$.
Both functions are [[elliptic|FF9ZPCZ59K]], with real period
$$\pi_3 = 3\int_0^1 \frac{dt}{(1 - t^3)^{2/3}} = B(1/3, 1/3) \approx 5.29992.$$
Let $\omega = e^{2\pi i/3}$.
Example: $f(z) = \omega^{-1}\operatorname{sm}(\omega z)$ and $g(z) = \operatorname{cm}(\omega z)$ satisfy $f' = g^2$, $g' = -\omega^3 f^2 = -f^2$, $f(0) = 0$, $g(0) = 1$; by uniqueness $\operatorname{sm}(\omega z) = \omega\operatorname{sm}(z)$ and $\operatorname{cm}(\omega z) = \operatorname{cm}(z)$.
So $\omega\pi_3$ is also a period, and the period lattice contains $\pi_3(\Z + \Z\omega)$.
Non-example: $\sin$ and $\cos$ satisfy $\sin' = \cos$, not $\cos^2$, and $\sin^3 + \cos^3$ is not constant (it is $1$ at $0$ and $2^{-1/2}$ at $\pi/4$).
