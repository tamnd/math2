---
tag: WR4X7MMTH2
kind: statement
role: theorem
name: Kolmogorov extension theorem
msc: [60G05, 28A35, 60A10]
uses: [059TJN0NZ1, 584GXXY73M, 6HVCTJGB61, 3N66TM3TSQ]
about: [059TJN0NZ1, 0QH5ENKZM1]
sources:
  - url: https://en.wikipedia.org/wiki/Kolmogorov_extension_theorem
same_as:
  wikidata: Q3526996
  wikipedia: Kolmogorov extension theorem
---

## Statement

Let $T$ be a nonempty index set, and for each $t \in T$ let $E_t$ be a [[Polish space|584GXXY73M]] with its Borel σ-algebra.
For $J \subseteq T$ let $E_J = \prod_{t \in J} E_t$ with the [[product σ-algebra|6HVCTJGB61]], and for $K \subseteq J$ let $\pi^J_K \colon E_J \to E_K$ be the restriction of coordinates.
For each finite nonempty $J \subseteq T$ let $\mu_J$ be a [[probability measure|059TJN0NZ1]] on $E_J$.
Assume the family is consistent: for all finite nonempty $K \subseteq J \subseteq T$, the [[pushforward|3N66TM3TSQ]] of $\mu_J$ under $\pi^J_K$ equals $\mu_K$.
Then there is a unique probability measure $\mu$ on $E_T$ such that, for every finite nonempty $J \subseteq T$, the pushforward of $\mu$ under $\pi^T_J$ equals $\mu_J$.

## Remarks

The measure $\mu$ is first defined on cylinder sets, where consistency makes it well defined and finitely additive.
The key step is countable additivity on the algebra of cylinder sets.
It uses inner regularity: each $\mu_J$ is approximated from inside by compact sets, and a decreasing sequence of nonempty compact cylinders has nonempty intersection.
[[Carathéodory's extension theorem|Q8EXG7EKYW]] then extends $\mu$ to the product σ-algebra, and uniqueness holds because cylinder sets form a π-system.

Example: let $T = [0, \infty)$, $E_t = \R$, and let $\mu_J$ be the centred Gaussian measure on $\R^J$ with covariance $\min(s, t)$ for $s, t \in J$.
These measures are consistent, so there is a [[stochastic process|0QH5ENKZM1]] $(X_t)_{t \ge 0}$ with these finite-dimensional laws.
This is the first step in the construction of Brownian motion; the continuity of paths needs a further argument.

A topological assumption on the factors is needed.
For arbitrary measurable spaces in place of Polish spaces, consistent families exist that have no extension.
No such assumption is needed when the $\mu_J$ are products, as for the [[infinite product measure|2HWVFHM13R]].
It is not needed either when they are built from kernels, as in the [[Ionescu-Tulcea theorem|94ASD187AQ]].

## Explanations

### L1 human

To describe a random process, such as the position of a particle at every time, it is enough to say how it behaves at finitely many times at once.
If these finite descriptions do not contradict each other, the theorem gives a single probability measure on the whole space of paths that matches all of them.
So a process can be built from its finite-dimensional distributions.

### L2 human

The theorem is the standard existence result for stochastic processes with prescribed finite-dimensional distributions: Gaussian processes, Markov processes from transition functions, and sequences of independent variables.
The resulting σ-algebra only contains events that depend on countably many coordinates.
So for uncountable $T$, sets such as "the path is continuous" are not measurable, and one has to pass to a modification, for instance with the [[Kolmogorov continuity theorem|V1HAJNC5RK]].
