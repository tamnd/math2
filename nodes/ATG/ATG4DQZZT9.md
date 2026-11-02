---
tag: ATG4DQZZT9
kind: definition
name: Bartle–Dunford–Schwartz integral
msc: [46G10, 28B05]
defines: RMWW2X86TT
uses: [PS28BSAJKJ, 06GZ956657, 7WMBX7M4P6, YYNCJSR0PJ]
sources:
  - url: https://en.wikipedia.org/wiki/Vector_measure
---

## Definition

Let $(\Omega, \Sigma)$ be a measurable space, let $E$ be a real [[Banach space|06GZ956657]], and let $\mu \colon \Sigma \to E$ be a countably additive [[vector measure|PS28BSAJKJ]].
A set $N \in \Sigma$ is $\mu$-null if $\mu(A) = 0$ for every $A \in \Sigma$ with $A \subseteq N$.

1. For a [[simple function|7WMBX7M4P6]] $s = \sum_{i=1}^{k} a_i \mathbf{1}_{A_i}$ with $a_i \in \R$ and $A_i \in \Sigma$, and for $B \in \Sigma$, put $\int_B s \, d\mu = \sum_{i=1}^{k} a_i \, \mu(A_i \cap B)$.
2. A [[measurable|YYNCJSR0PJ]] $f \colon \Omega \to \R$ is $\mu$-integrable if there are simple functions $s_n \to f$, pointwise outside a $\mu$-null set, such that $\int_B s_n \, d\mu$ converges in $E$ for every $B \in \Sigma$.
3. For such $f$, the *Bartle–Dunford–Schwartz integral* is $\int_B f \, d\mu = \lim_{n \to \infty} \int_B s_n \, d\mu$ for $B \in \Sigma$.

The limit in clause 3 does not depend on the choice of the sequence $(s_n)$.

## Remarks

Example: every bounded measurable $f$ is $\mu$-integrable.
Take simple $s_n$ with $\abs{s_n - f} \le 1/n$ everywhere.
For a simple $s$ with $\abs{s} \le c$ one has $\norm{\int_B s \, d\mu} \le c \, \norm{\mu}(\Omega)$.
Here $\norm{\mu}(\Omega)$ is the supremum of $\norm{\sum_i a_i \mu(A_i)}$ over finite measurable partitions $(A_i)$ of $\Omega$ and reals $\abs{a_i} \le 1$; it is finite when $\mu$ is countably additive.
Apply this to $s = s_n - s_m$.
So $\int_B s_n \, d\mu$ is a Cauchy sequence in $E$.

Non-example: let $\mu$ be Lebesgue measure on $(0, 1]$, viewed as a vector measure with values in $\R$, and $f(x) = 1/x$.
For a real-valued finite measure, integrability in the sense of clause 2 is the same as Lebesgue integrability.
Since $\int_0^1 dx / x = \infty$, no sequence as in clause 2 exists, and $f$ is not $\mu$-integrable.

When $E = \R$ and $\mu$ is a finite signed measure, the integral is the Lebesgue integral against $\mu$.
For each continuous linear functional $x^*$ on $E$, $x^* \big( \int_B f \, d\mu \big) = \int_B f \, d(x^* \circ \mu)$.
