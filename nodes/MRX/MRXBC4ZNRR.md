---
tag: MRXBC4ZNRR
kind: statement
role: theorem
name: Doob's martingale convergence theorems
msc: [60G42, 60G44]
uses: [EQ055QMACW, 0CDVK9RQBH, KYW1PV0SX5, 0AAXWGT5TD, 0YAMJRK04E]
about: [0D0GBNDKDH, 6M852B4RA8]
sources:
  - url: https://en.wikipedia.org/wiki/Doob%27s_martingale_convergence_theorems
same_as:
  wikidata: Q1765521
  wikipedia: Doob's martingale convergence theorems
---

## Statement

Let $(X_n)_{n \ge 0}$ be a sequence of real random variables, adapted to a [[filtration|HNK1Y62G7V]] $(\mathcal{F}_n)_{n \ge 0}$.
A family $(Y_i)$ of random variables is uniformly integrable if $\sup_i E\bigl[\abs{Y_i} \mathbf{1}\{\abs{Y_i} > K\}\bigr] \to 0$ as $K \to \infty$.

1. If $(X_n)$ is a [[submartingale|EQ055QMACW]] and $\sup_n E[X_n^+] < \infty$, then $X_n$ converges [[almost surely|0AAXWGT5TD]] to a random variable $X_\infty$ with $E[\abs{X_\infty}] < \infty$.
2. If $(X_n)$ is a non-negative [[supermartingale|KYW1PV0SX5]], then $X_n$ converges almost surely to a random variable $X_\infty$ with $E[X_\infty] \le E[X_0]$.
3. Let $(X_n)$ be a [[martingale|0CDVK9RQBH]].
These are equivalent: $(X_n)$ is uniformly integrable; $X_n$ converges almost surely and in $L^1$; $X_n = E[X \mid \mathcal{F}_n]$ for an integrable $X$.
In this case $X_n = E[X_\infty \mid \mathcal{F}_n]$ for all $n$, where $X_\infty$ is the limit.

## Remarks

The proof of part 1 uses [[Doob's upcrossing inequality|10HFW1GRV2]].
The bound on $E[X_n^+]$ makes the number of upcrossings of each rational interval finite almost surely, so the limit exists in $[-\infty, \infty]$.
Fatou's lemma shows that the limit is finite and integrable.
Part 2 follows from part 1 applied to $-X_n$, and part 3 uses that uniform integrability upgrades almost sure convergence to $L^1$ convergence.
Example: for independent $\xi_i$ with $P(\xi_i = 0) = P(\xi_i = 2) = 1/2$, the product $M_n = \xi_1 \cdots \xi_n$ is a non-negative martingale with $E[M_n] = 1$.
It converges almost surely to $0$ but not in $L^1$, so it is not uniformly integrable, which shows that part 3 needs its hypothesis.
The bound in part 1 is needed: the simple symmetric random walk is a martingale with $E[\abs{S_n}] \to \infty$, and it does not converge.
The same statements hold in continuous time for submartingales with right-continuous paths.

## Explanations

### L1 human

A fair or favourable game whose size stays under control must settle down to a limit.
A gambler who keeps playing fair games with a fortune that cannot go negative ends up with a fortune that stops changing.
But the limit may lose mass: the expected value can drop in the limit unless the process is uniformly integrable.

### L2 human

These theorems are the main reason martingales are useful in analysis and probability.
They give short proofs of the strong law of large numbers, of [[Lévy's upward theorem|W01FD2A8NK]] and of Kolmogorov's zero–one law.
They also give almost sure convergence of likelihood ratios, of branching process normalisations and of the Radon–Nikodym derivatives on finer and finer partitions.
The $L^p$ version, for $p > 1$, says that a martingale bounded in $L^p$ converges almost surely and in $L^p$, by [[Doob's martingale inequality|4G53E7BRXF]].
