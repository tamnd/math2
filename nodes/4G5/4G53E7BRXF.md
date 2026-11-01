---
tag: 4G53E7BRXF
kind: statement
role: theorem
name: Doob's martingale inequality
msc: [60G42, "60E15"]
uses: [EQ055QMACW, 0CDVK9RQBH, 0DCT0QZVQ1, 05PWWHYBX5]
about: [6M852B4RA8]
sources:
  - url: https://en.wikipedia.org/wiki/Doob%27s_martingale_inequality
same_as:
  wikidata: Q1242402
  wikipedia: Doob's martingale inequality
---

## Statement

Let $n \ge 0$, let $(X_k)_{0 \le k \le n}$ be a [[submartingale|EQ055QMACW]] with respect to a [[filtration|HNK1Y62G7V]] $(\mathcal{F}_k)_{0 \le k \le n}$, and let $\lambda > 0$.
Then
$$\lambda\, P\Bigl(\max_{0 \le k \le n} X_k \ge \lambda\Bigr) \le E\Bigl[X_n \mathbf{1}\bigl\{\max_{0 \le k \le n} X_k \ge \lambda\bigr\}\Bigr] \le E[X_n^+],$$
where $X_n^+ = \max(X_n, 0)$.

## Remarks

Let $\tau$ be the first $k \le n$ with $X_k \ge \lambda$, and split the event $A = \{\max_k X_k \ge \lambda\}$ into the disjoint events $\{\tau = k\}$.
Since $\{\tau = k\} \in \mathcal{F}_k$, the submartingale property gives $E[X_n \mathbf{1}\{\tau = k\}] \ge E[X_k \mathbf{1}\{\tau = k\}] \ge \lambda P(\tau = k)$.
Summing over $k$ gives the first inequality, and $X_n \mathbf{1}_A \le X_n^+$ gives the second.
If $(M_k)$ is a [[martingale|0CDVK9RQBH]], then $\abs{M_k}$ is a submartingale, so $P(\max_{k \le n} \abs{M_k} \ge \lambda) \le E[\abs{M_n}]/\lambda$.
For $M_k$ a sum of independent centred square-integrable variables, applying this to the submartingale $M_k^2$ gives [[Kolmogorov's inequality|D9B4HE4B4Q]].
The inequality is stronger than [[Markov's inequality|05PWWHYBX5]] for $X_n$ alone: it controls the whole path up to time $n$ by the last value.
For a non-negative submartingale and $p > 1$, it implies Doob's $L^p$ inequality $E[\max_{k \le n} X_k^p] \le \bigl(\tfrac{p}{p-1}\bigr)^p E[X_n^p]$.

## Explanations

### L1 human

For a process that tends to increase, the chance that it ever climbs above a level $\lambda$ before time $n$ is controlled by its final value alone.
The bound is the same as the Markov bound for the single variable $X_n$.
So looking at the maximum over the whole path costs nothing extra.

### L2 human

The inequality is the basic maximal inequality of martingale theory.
It gives Kolmogorov's inequality, which is a step in the strong law of large numbers and the three-series theorem.
Its $L^p$ form is used to prove $L^p$ convergence of martingales and to define the norm on spaces of continuous martingales.
In continuous time it holds for right-continuous submartingales, with the maximum replaced by the supremum over $[0, t]$.
