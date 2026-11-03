---
tag: 31DTSY95RC
kind: definition
name: Wiener series
msc: [93C10, "93E12"]
defines: AYVZQWZ08Y
uses: [RQ3JKGWD03, 22WEM6RTW0]
sources:
  - url: https://en.wikipedia.org/wiki/Wiener_series
---

## Definition

Let $x$ be a Gaussian white noise input with zero mean and covariance $\mathbb{E}[x(t) x(t')] = K \delta(t - t')$, where $K > 0$ and $\delta$ is the Dirac delta.
For $n \ge 0$, let $k_n \colon [0, \infty)^n \to \R$ be a kernel that is symmetric in its $n$ variables, with $k_0$ a constant.
A *Volterra functional of degree $n$* is a sum of terms $\int h_j(\tau_1, \ldots, \tau_j)\, x(t - \tau_1) \cdots x(t - \tau_j)\, d\tau_1 \cdots d\tau_j$ with $j \le n$, as in a [[Volterra series|RQ3JKGWD03]].
The *Wiener functional* $G_n[k_n; x](t)$ is the unique Volterra functional of degree $n$ with the two properties below.
Its term of degree $n$ has kernel $k_n$.
It satisfies $\mathbb{E}\big[G_n[k_n; x](t)\, H(t)\big] = 0$ for every Volterra functional $H$ of degree less than $n$.
The first three are
$$G_0 = k_0, \qquad G_1(t) = \int_0^\infty k_1(\tau)\, x(t - \tau)\, d\tau,$$
$$G_2(t) = \int_0^\infty \!\! \int_0^\infty k_2(\tau_1, \tau_2)\, x(t - \tau_1) x(t - \tau_2)\, d\tau_1 d\tau_2 - K \int_0^\infty k_2(\tau, \tau)\, d\tau.$$
A *Wiener series* of a system is a representation of its output as $y(t) = \sum_{n \ge 0} G_n[k_n; x](t)$, and the $k_n$ are its *Wiener kernels*.

## Remarks

White noise is only a generalised process, so the formulas are understood in the sense of white noise analysis.
In practice they are applied to a [[Gaussian process|22WEM6RTW0]] with a short correlation time, as an approximation.
The constant in $G_2$ makes its mean zero: $\mathbb{E}[x(t - \tau_1) x(t - \tau_2)] = K \delta(\tau_1 - \tau_2)$, so the double integral has mean $K \int k_2(\tau, \tau)\, d\tau$.
Odd moments of a centred Gaussian vanish, so $G_2$ is also uncorrelated with $G_1$.

Example: let $z(t) = \int_0^\infty h(\tau)\, x(t - \tau)\, d\tau$ with $h$ square integrable, and $y = z^2$.
Its Volterra series has the single kernel $h(\tau_1) h(\tau_2)$ of degree $2$.
Its Wiener series is $y = G_0 + G_2$ with $k_0 = K \int_0^\infty h(\tau)^2\, d\tau$ and $k_2(\tau_1, \tau_2) = h(\tau_1) h(\tau_2)$.

Non-example: the functional $z(t)^2$ itself is not the Wiener functional $G_2$ with kernel $h(\tau_1) h(\tau_2)$.
Its mean $K \int h^2$ is nonzero, so it is correlated with the constant functional, which has degree $0 < 2$.

The Wiener kernels depend on the noise level $K$, unlike the Volterra kernels.
