---
tag: G4QVDEXYTV
kind: definition
name: Gabor frame
msc: [42C15, 94A12]
defines: M9WHY8E2PM
uses: [3DHNP5NEWH, SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Gabor_transform
---

## Definition

For $x, \omega \in \R$ and $g \in L^2(\R)$, let $T_x g(t) = g(t - x)$ and $M_\omega g(t) = e^{2\pi i \omega t} g(t)$.
Let $g \in L^2(\R)$ be nonzero and let $a, b > 0$.
The *Gabor system* $\mathcal{G}(g, a, b)$ is the family $(M_{bn} T_{ak} g)_{k, n \in \Z}$.
It is a *Gabor frame* if it is a frame of $L^2(\R)$: there are constants $0 < A \le B < \infty$ with
$$A \norm{f}^2 \le \sum_{k, n \in \Z} \abs{\ip{f}{M_{bn} T_{ak} g}}^2 \le B \norm{f}^2 \quad \text{for all } f \in L^2(\R).$$

## Remarks

The coefficients $\ip{f}{M_{bn} T_{ak} g}$ are the values $V_g f(ak, bn)$ of the [[short-time Fourier transform|3DHNP5NEWH]] on the lattice $a\Z \times b\Z$.
If $\mathcal{G}(g, a, b)$ is a frame, then $ab \le 1$; for $ab = 1$ it is a frame only if it is a Riesz basis.
For the Gaussian $g(t) = e^{-\pi t^2}$, the system $\mathcal{G}(g, a, b)$ is a frame exactly when $ab < 1$, a result of Lyubarskii and of Seip.

Example: let $g = 1_{[0, 1)}$ and $a = b = 1$.
The translates $T_k g$ are the indicators of the intervals $[k, k+1)$, which tile $\R$.
On each such interval the functions $e^{2\pi i n t}$, $n \in \Z$, form an orthonormal basis of $L^2([k, k+1))$.
So $\mathcal{G}(g, 1, 1)$ is an orthonormal basis of $L^2(\R)$, hence a Gabor frame with $A = B = 1$.

Non-example: with $g = 1_{[0, 1)}$, $a = 2$ and $b = 1$, every function in the system vanishes on $[1, 2)$.
So a nonzero $f$ supported in $[1, 2)$ has all coefficients $0$, and the lower frame bound fails.
