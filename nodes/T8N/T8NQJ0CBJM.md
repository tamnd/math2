---
tag: T8NQJ0CBJM
kind: definition
name: Neville theta functions
msc: ["33E05"]
defines: TZ1N0HAGW7
uses: [2F5CYQJVAF, YSAZVCZAZC, RM54CPPE12]
sources:
  - url: https://en.wikipedia.org/wiki/Neville_theta_functions
---

## Definition

Let $0 < k < 1$, $k' = \sqrt{1 - k^2}$, let $K = K(k)$ be the [[complete elliptic integral of the first kind|RM54CPPE12]], and let $q$ be the [[nome|YSAZVCZAZC]] of $k$.
For complex $\zeta$ let
$$\vartheta_1(\zeta) = 2\sum_{n \ge 0} (-1)^n q^{(n + 1/2)^2}\sin((2n + 1)\zeta), \qquad \vartheta_2(\zeta) = 2\sum_{n \ge 0} q^{(n + 1/2)^2}\cos((2n + 1)\zeta),$$
$$\vartheta_3(\zeta) = 1 + 2\sum_{n \ge 1} q^{n^2}\cos(2n\zeta), \qquad \vartheta_4(\zeta) = 1 + 2\sum_{n \ge 1} (-1)^n q^{n^2}\cos(2n\zeta)$$
be the four Jacobi [[theta functions|2F5CYQJVAF]] with nome $q$.
With $\zeta = \pi u/(2K)$, the *Neville theta functions* of $u \in \C$ are
$$\theta_s(u) = \sqrt{\frac{\pi}{2kk'K}}\,\vartheta_1(\zeta), \quad \theta_c(u) = \sqrt{\frac{\pi}{2kK}}\,\vartheta_2(\zeta), \quad \theta_d(u) = \sqrt{\frac{\pi}{2K}}\,\vartheta_3(\zeta), \quad \theta_n(u) = \sqrt{\frac{\pi}{2k'K}}\,\vartheta_4(\zeta).$$

## Remarks

The constants are chosen so that $\theta_c(0) = \theta_d(0) = \theta_n(0) = 1$ and $\theta_s'(0) = 1$.
Check of $\theta_d(0) = 1$: Jacobi's formula $\vartheta_3(0)^2 = 2K/\pi$ gives $\theta_d(0) = \sqrt{\pi/(2K)}\cdot\sqrt{2K/\pi} = 1$.
Similarly $\vartheta_2(0)^2 = 2kK/\pi$ and $\vartheta_4(0)^2 = 2k'K/\pi$ give $\theta_c(0) = \theta_n(0) = 1$.
The [[Jacobi elliptic functions|P071B692JF]] are
$$\operatorname{sn} u = \frac{\theta_s(u)}{\theta_n(u)}, \qquad \operatorname{cn} u = \frac{\theta_c(u)}{\theta_n(u)}, \qquad \operatorname{dn} u = \frac{\theta_d(u)}{\theta_n(u)}.$$
Non-example: $\vartheta_3(\pi u/(2K))$ itself is not $\theta_d(u)$, since its value at $u = 0$ is $\sqrt{2K/\pi} > 1$; the factor $\sqrt{\pi/(2K)}$ is needed.
The function $\theta_d$ is even with period $2K$, and $\theta_s$ is odd with $\theta_s(u + 2K) = -\theta_s(u)$.
