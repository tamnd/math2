---
tag: C6EC4SBEMC
kind: definition
name: Potential operator of a Markov process
msc: [60J45, 60J35]
defines: 595AZJAZNA
uses: [2AVNDP8BJP, 46436KE7NT, 22735FGJV6, J5YNNKSB9P, VPA41PWRR1]
sources:
  - url: https://en.wikipedia.org/wiki/Markov_kernel
---

## Definition

Let $(E, \mathcal{E})$ be a measurable space and let $(P_t)_{t \ge 0}$ be a sub-Markov transition semigroup on $E$.
So the $P_t$ are kernels as for [[Markov kernels|2AVNDP8BJP]] but with $P_t(x, E) \le 1$, and $P_s P_t = P_{s+t}$.
Assume that $(t, x) \mapsto P_t(x, A)$ is measurable on $[0, \infty) \times E$ for each $A \in \mathcal{E}$.
The *potential operator* (or potential kernel) of $(P_t)$ is the kernel $U$ given by
$$U(x, A) = \int_0^\infty P_t(x, A) \, dt \in [0, \infty], \qquad x \in E, \ A \in \mathcal{E}.$$
For measurable $f \colon E \to [0, \infty]$ it acts by $U f(x) = \int_0^\infty P_t f(x) \, dt$.

## Remarks

If $(X_t)$ is a Markov process with semigroup $(P_t)$ and law $P^x$ when started at $x$, then $U f(x) = E^x \int_0^\infty f(X_t) \, dt$.
So $U(x, A)$ is the expected total time that the process spends in $A$.
For each measurable $f \ge 0$, the function $U f$ is [[excessive|46436KE7NT]].
Example: for [[Brownian motion|22735FGJV6]] in $\R^3$, the Gaussian integral $\int_0^\infty (2\pi t)^{-3/2} e^{-r^2/2t} \, dt = 1/(2\pi r)$ gives
$$U(x, A) = \int_A \frac{dy}{2\pi \abs{x - y}}.$$
Non-example of finiteness: for Brownian motion in $\R^2$, $U(x, A) = \infty$ for every nonempty open $A$, so $U$ is not a useful kernel there; the process is recurrent.
$U$ is the limit as $\alpha \downarrow 0$ of the [[resolvent|J5YNNKSB9P]] $U_\alpha = \int_0^\infty e^{-\alpha t} P_t \, dt$.
When $L$ is the [[infinitesimal generator|VPA41PWRR1]] and $U f$ is finite and in the domain of $L$, one has $-L U f = f$.
In discrete time the analogue is $U = \sum_{n \ge 0} P^n$, the Green kernel of a Markov chain.
