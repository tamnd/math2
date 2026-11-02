---
tag: 6WTHKQG40F
kind: definition
name: Contiguity of measures
msc: ["62E20", 60B10]
defines: DQGJMP9WHC
uses: [059TJN0NZ1, 2G173YJC54, 04WSW8T3SY, 07RXBVTVZB]
sources:
  - url: https://en.wikipedia.org/wiki/Contiguity_(probability_theory)
---

## Definition

For each $n \ge 1$, let $(\Omega_n, \mathcal{F}_n)$ be a measurable space, with $\mathcal{F}_n$ a [[sigma-algebra|04WSW8T3SY]], and let $P_n$ and $Q_n$ be [[probability measures|059TJN0NZ1]] on it.
The sequence $(Q_n)$ is *contiguous with respect to* $(P_n)$, written $Q_n \triangleleft P_n$, if for every sequence of events $A_n \in \mathcal{F}_n$,
$$P_n(A_n) \to 0 \implies Q_n(A_n) \to 0.$$
The sequences are *mutually contiguous*, written $P_n \triangleleft \triangleright Q_n$, if $Q_n \triangleleft P_n$ and $P_n \triangleleft Q_n$.

## Remarks

Contiguity is the asymptotic analogue of [[absolute continuity|2G173YJC54]]; for constant sequences $P_n = P$ and $Q_n = Q$ it is the same as $Q \ll P$.
If $Q_n \triangleleft P_n$, then every sequence of statistics that tends to $0$ in $P_n$-probability also tends to $0$ in $Q_n$-probability.

Example: let $P_n = \mathcal{N}(0, 1)^{\otimes n}$ and $Q_n = \mathcal{N}(h/\sqrt{n}, 1)^{\otimes n}$, products of [[normal distributions|07RXBVTVZB]], for a fixed $h \in \R$.
Under $P_n$, the log-likelihood ratio $\log(dQ_n/dP_n) = h n^{-1/2}\sum_i X_i - h^2/2$ has the law $\mathcal{N}(-h^2/2, h^2)$ for every $n$.
By Le Cam's first lemma, a limit law $L$ of $\log(dQ_n/dP_n)$ under $P_n$ with $E e^{L} = 1$ implies $Q_n \triangleleft P_n$, and here $E e^{L} = e^{-h^2/2 + h^2/2} = 1$; by symmetry the sequences are mutually contiguous.

Non-example: let $P_n = \mathcal{N}(0, 1)^{\otimes n}$ and $Q_n = \mathcal{N}(1, 1)^{\otimes n}$, and let $A_n = \set{\bar{x}_n > 1/2}$, with $\bar{x}_n$ the mean of the coordinates.
Then $P_n(A_n) = P(Z > \sqrt{n}/2) \to 0$ but $Q_n(A_n) = P(Z > -\sqrt{n}/2) \to 1$ for $Z$ standard normal, so $Q_n$ is not contiguous with respect to $P_n$.
