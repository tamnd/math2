---
tag: S09YBRBTY2
kind: definition
name: Dimensional regularization
msc: [81T15, 81T18]
defines: N3M811M8HA
uses: [0H5SYBSED9, 0M3YQJ81NB, 0ZZ7ZYDR8W, BS6HVNMTWC]
sources:
  - url: https://en.wikipedia.org/wiki/Dimensional_regularization
---

## Definition

Let $f \colon (0, \infty) \to \C$ be a continuous function.
Let $U \subseteq \C$ be a nonempty connected open set of values of $d$ such that $\int_0^\infty r^{d-1} \abs{f(r^2)} \, dr$ converges for $d \in U$.
For $d \in U$, put
$$\int d^dk \, f(k^2) = \frac{2\pi^{d/2}}{\Gamma(d/2)} \int_0^\infty r^{d-1} f(r^2) \, dr,$$
where $\Gamma$ is the [[gamma function|0H5SYBSED9]].
For a positive integer $d$, this is the integral of $k \mapsto f(\abs{k}^2)$ over $\R^d$.
The *dimensionally regularized* value of the integral is defined by [[analytic continuation|0M3YQJ81NB]] in $d$.
It is the continuation of this function of $d$ from $U$ to a larger domain of $\C$, when it exists.
Integrals of [[Feynman diagrams|BS6HVNMTWC]] are reduced to this form by Feynman parameters and shifts of the loop momenta.

## Remarks

Example: for $\Delta > 0$ and an integer $n \ge 1$, the integral of $f(r^2) = (r^2 + \Delta)^{-n}$ converges for $0 < \operatorname{Re} d < 2n$.
A beta-function computation gives
$$\int \frac{d^dk}{(2\pi)^d} \frac{1}{(k^2 + \Delta)^n} = \frac{\Gamma(n - d/2)}{(4\pi)^{d/2}\,\Gamma(n)} \, \Delta^{d/2 - n}.$$
The right side is a [[meromorphic function|0ZZ7ZYDR8W]] of $d$, and it gives the continuation to all of $\C$ minus the poles $d = 2n, 2n + 2, \dots$.
For $n = 2$ and $d = 4 - 2\varepsilon$, it equals $\frac{1}{16\pi^2}\left(\frac{1}{\varepsilon} - \gamma - \log\frac{\Delta}{4\pi} + O(\varepsilon)\right)$, where $\gamma$ is the Euler–Mascheroni constant.
The logarithmic divergence in four dimensions has become the pole $1/\varepsilon$.

Non-example: for $f(r^2) = r^{-2}$, the integral converges for no $d$, since it needs $\operatorname{Re} d < 2$ at infinity and $\operatorname{Re} d > 2$ at $0$.
So the defining condition fails; by convention such scaleless integrals are set equal to $0$ in dimensional regularization.
