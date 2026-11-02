---
tag: 9QQN0QH2YT
kind: definition
name: Nemytskii operator
msc: [47H30, 45G10]
defines: W8G3AZ0DNG
uses: [P15VQS5DJ9, YYNCJSR0PJ, SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Nemytskii_operator
---

## Definition

Let $(\Omega, \mathcal{A}, m)$ be a $\sigma$-finite [[measure space|P15VQS5DJ9]] and let $g \colon \Omega \times \R \to \R$ be a *Carathéodory function*:

1. for every $u \in \R$, the map $x \mapsto g(x, u)$ is [[measurable|YYNCJSR0PJ]];
2. for almost every $x \in \Omega$, the map $u \mapsto g(x, u)$ is continuous.

The *Nemytskii operator* of $g$ sends each measurable function $u \colon \Omega \to \R$ to the function $N_g u \colon \Omega \to \R$ given by
$$(N_g u)(x) = g\bigl(x, u(x)\bigr).$$
Under the two conditions, $N_g u$ is again measurable.

## Remarks

A theorem of Krasnosel'skii describes the [[$L^p$ spaces|SASP14MA1Z]] case.
Let $\Omega \subseteq \R^m$ be measurable with Lebesgue measure, and let $1 \le p, q < \infty$.
Then $N_g$ maps $L^p(\Omega)$ into $L^q(\Omega)$ if and only if there are $a \in L^q(\Omega)$ and $b \ge 0$ with $\abs{g(x, u)} \le a(x) + b \abs{u}^{p/q}$ for almost every $x$ and all $u$.
In that case $N_g \colon L^p(\Omega) \to L^q(\Omega)$ is continuous and maps bounded sets to bounded sets.

Example: $\Omega = [0, 1]$ with Lebesgue measure and $g(x, u) = u^2$.
Both conditions hold, and $\abs{g(x, u)} \le \abs{u}^{4/2}$, so $N_g$ maps $L^4[0, 1]$ into $L^2[0, 1]$; indeed $\int_0^1 (u^2)^2 = \int_0^1 u^4 < \infty$.

Non-example: the map $u \mapsto \bigl(x \mapsto \int_0^1 u(t)\, dt\bigr)$ is not a Nemytskii operator.
The value at $x$ depends on all values of $u$, not only on $u(x)$.

Other names are superposition operator and, for $g$ independent of $x$, composition operator.
