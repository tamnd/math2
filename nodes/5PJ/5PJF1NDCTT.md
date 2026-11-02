---
tag: 5PJF1NDCTT
kind: statement
role: theorem
name: Fukushima correspondence between Dirichlet forms and processes
msc: [60J46, 31C25, 60J25]
uses: [MH20Q2N1AH, Z7T669BQ9B, HZNEQQBCW4, 0FE2SB8WVJ, XPWE94BV6N, EK58S2872F]
about: [MH20Q2N1AH, Z7T669BQ9B]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet_form
---

## Statement

Let $X$ be a [[locally compact|0FE2SB8WVJ]] separable metric space and let $m$ be a positive [[Radon measure|HZNEQQBCW4]] on $X$ with full support.
Let $(\mathcal{E}, \mathcal{F})$ be a regular [[Dirichlet form|MH20Q2N1AH]] on $L^2(X, m)$, and let $(T_t)_{t \ge 0}$ be the strongly continuous symmetric Markovian [[contraction semigroup|XPWE94BV6N]] on $L^2(X, m)$ associated with it.
Then there is an $m$-symmetric [[Hunt process|Z7T669BQ9B]] $M$ on $X$ whose transition function $(p_t)_{t \ge 0}$ satisfies, for every $t > 0$ and every bounded Borel function $f \in L^2(X, m)$:
$$p_t f = T_t f \quad m\text{-almost everywhere}.$$
Such a process is unique up to equivalence.
That is, two $m$-symmetric Hunt processes with this property have the same transition functions outside a set of zero capacity for $\mathcal{E}$.
This exceptional set can be chosen so that neither process enters it.

## Remarks

The process is built from the semigroup, but the semigroup only acts on classes of functions defined almost everywhere.
The difficulty is to choose good pointwise versions, and this is done with the capacity of $\mathcal{E}$.
Every element of $\mathcal{F}$ has a quasi-continuous version, which is continuous outside open sets of small capacity.
Regularity of the form provides enough continuous functions in $\mathcal{F}$ to separate points and to build the process on $X$ itself.
Moreover $p_t f$ is a quasi-continuous version of $T_t f$.
Example: the form $\tfrac12 \int_{\R^n} \nabla u \cdot \nabla v \, dx$ on $W^{1,2}(\R^n)$ corresponds to Brownian motion on $\R^n$.
Ma and Röckner extended the correspondence to quasi-regular Dirichlet forms, which include forms on infinite-dimensional spaces.

## Explanations

### L1 human

A Dirichlet form is an energy for functions, and a Hunt process is a random motion that may jump or be killed.
The theorem says that every regular energy of this kind comes from a random motion.
Heat flow defined by the energy is the same as averaging over the random paths of the process.
So questions about the energy can be answered with random paths, and conversely.

### L2 human

The theorem is a central result of the monograph of Fukushima, Oshima and Takeda on Dirichlet forms.
Together with the [[Beurling–Deny formula|EK58S2872F]], it gives a meaning to the three parts of the form.
The local part, the jumping measure and the killing measure describe the continuous motion, the jumps and the killing of the process.
A regular Dirichlet form has the local property exactly when the process is a diffusion, that is, has continuous paths up to its lifetime.
A nearly Borel set has zero capacity if and only if the process, started from $m$-almost every point, never hits it, which gives a probabilistic meaning to capacity.
