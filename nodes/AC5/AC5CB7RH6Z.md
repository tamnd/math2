---
tag: AC5CB7RH6Z
kind: statement
role: theorem
name: Kantorovich duality
msc: [49Q22, 49N15, 60A10]
uses: [K8EBASR5VG, HTR7J0W66V, 059TJN0NZ1, 584GXXY73M]
about: [K8EBASR5VG]
sources:
  - url: https://en.wikipedia.org/wiki/Transportation_theory_(mathematics)
---

## Statement

Let $X$ and $Y$ be [[Polish spaces|584GXXY73M]], let $\mu$ be a Borel [[probability measure|059TJN0NZ1]] on $X$ and $\nu$ a Borel probability measure on $Y$.
Let $c \colon X \times Y \to [0, \infty]$ be a lower semicontinuous cost function.
Let $\Pi(\mu, \nu)$ be the set of [[couplings|HTR7J0W66V]] of $\mu$ and $\nu$, the Borel probability measures on $X \times Y$ with marginals $\mu$ and $\nu$.
Then
$$\min_{\pi \in \Pi(\mu, \nu)} \int_{X \times Y} c \, d\pi = \sup \set{ \int_X \varphi \, d\mu + \int_Y \psi \, d\nu : \varphi \in L^1(\mu), \ \psi \in L^1(\nu), \ \varphi(x) + \psi(y) \le c(x, y) \text{ for all } x, y },$$
and the minimum on the left is attained.
The supremum does not change if $\varphi$ and $\psi$ are required to be bounded and continuous.

## Remarks

The left side is the Kantorovich form of the [[optimal transport problem|K8EBASR5VG]], and the right side is its dual.
The inequality $\ge$ is easy: if $\varphi(x) + \psi(y) \le c(x, y)$ and $\pi \in \Pi(\mu, \nu)$, integrating against $\pi$ gives $\int \varphi \, d\mu + \int \psi \, d\nu \le \int c \, d\pi$.
The reverse inequality is a minimax argument.
For compact spaces and continuous $c$ it follows from a duality theorem of convex analysis, such as the Fenchel–Rockafellar theorem.
The general case follows by approximation.
Example: if $\mu = \delta_a$ is a Dirac mass, the only coupling is $\delta_a \otimes \nu$, so the left side equals $\int c(a, y) \, d\nu(y)$.
When $X = Y$ and $c$ is a metric $d$, the dual can be taken over $\psi = -\varphi$ with $\varphi$ $1$-Lipschitz, which is the [[Kantorovich–Rubinstein duality|SYXSZD8EFK]].
Lower semicontinuity of $c$ is used to show that the minimum is attained, through the weak compactness of $\Pi(\mu, \nu)$.

## Explanations

### L1 human

Think of a shipping company that moves goods from factories with distribution $\mu$ to shops with distribution $\nu$, at cost $c(x, y)$ per unit.
Instead of paying for each route, one may sell the job to a contractor who charges a loading price $\varphi(x)$ and an unloading price $\psi(y)$.
The contractor's prices are competitive if $\varphi(x) + \psi(y)$ never exceeds the direct cost $c(x, y)$.
The theorem says that the best competitive income of the contractor equals the least shipping cost.

### L2 human

Kantorovich duality is the linear-programming duality of optimal transport, extended to infinite spaces.
Under mild integrability conditions on $c$, optimal dual pairs $(\varphi, \psi)$ exist and can be chosen $c$-concave, and an optimal plan is concentrated on the set where $\varphi(x) + \psi(y) = c(x, y)$.
This is the starting point for Brenier's theorem, where the optimal $\varphi$ gives the optimal map, and for the theory of Wasserstein distances.
