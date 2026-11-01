---
tag: YHSSQ67GDS
kind: statement
role: theorem
name: Doob decomposition theorem
msc: [60G42]
uses: [0CDVK9RQBH, EQ055QMACW, YRNFE016FF, HNK1Y62G7V, 0YAMJRK04E]
about: [0D0GBNDKDH, 6M852B4RA8]
sources:
  - url: https://en.wikipedia.org/wiki/Doob_decomposition_theorem
same_as:
  wikidata: Q1242398
  wikipedia: Doob decomposition theorem
---

## Statement

Let $(X_n)_{n \ge 0}$ be a sequence of real random variables, [[adapted|YRNFE016FF]] to a [[filtration|HNK1Y62G7V]] $(\mathcal{F}_n)_{n \ge 0}$, with $E[\abs{X_n}] < \infty$ for all $n$.
Then there are a [[martingale|0CDVK9RQBH]] $(M_n)_{n \ge 0}$ and a sequence $(A_n)_{n \ge 0}$ of integrable random variables with $A_0 = 0$ and $A_n$ $\mathcal{F}_{n-1}$-measurable for $n \ge 1$, such that
$$X_n = M_n + A_n \quad \text{for all } n \ge 0.$$
This decomposition is unique up to equality almost surely.
Explicitly,
$$A_n = \sum_{k=1}^{n} \bigl(E[X_k \mid \mathcal{F}_{k-1}] - X_{k-1}\bigr).$$
Moreover, $(A_n)$ is almost surely non-decreasing if and only if $(X_n)$ is a [[submartingale|EQ055QMACW]].

## Remarks

Existence: with $A_n$ as above, $M_n = X_n - A_n$ satisfies $E[M_n - M_{n-1} \mid \mathcal{F}_{n-1}] = E[X_n \mid \mathcal{F}_{n-1}] - X_{n-1} - (A_n - A_{n-1}) = 0$.
Uniqueness: if $M_n + A_n = M'_n + A'_n$, then $M - M'$ is a martingale that is predictable, so $M_n - M'_n = E[M_n - M'_n \mid \mathcal{F}_{n-1}] = M_{n-1} - M'_{n-1}$, and it is constant equal to $0$.
Example: for the simple symmetric random walk $S_n$, $S_n^2 = (S_n^2 - n) + n$, so $A_n = n$.
A sequence $(A_n)$ with $A_n$ $\mathcal{F}_{n-1}$-measurable is called predictable.
Without the predictability of $A$ the decomposition is not unique: $X_n = 0 + X_n$ is another split into a martingale and an adapted process.

## Explanations

### L1 human

Any random process with finite means splits into a fair-game part and a trend part.
The trend is the part you can predict one step ahead, and the fair game is the surprise.
For a submartingale the trend only goes up.

### L2 human

The predictable part $A$ of $M^2$ for a square-integrable martingale $M$ is the predictable quadratic variation $\langle M \rangle$, a basic tool for martingale central limit theorems and stochastic integration.
The decomposition is the discrete-time model for the [[Doob–Meyer decomposition theorem|SX7ZPP72EM]], whose continuous-time proof is much harder.
It is also the discrete form of the split of a [[semimartingale|MZNFPJJMY9]] into a local martingale and a finite variation part.
