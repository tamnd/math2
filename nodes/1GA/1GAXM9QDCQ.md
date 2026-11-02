---
tag: 1GAXM9QDCQ
kind: definition
name: Approximate point spectrum
msc: [47A10]
defines: N44162Y9XS
uses: [BMKATJ802A, 7FNVA0Q6YQ, YVH149HCAG]
sources:
  - url: https://en.wikipedia.org/wiki/Spectrum_(functional_analysis)
    locator: Approximate point spectrum
---

## Definition

Let $X$ be a complex Banach space with identity map $I$, and let $T \colon X \to X$ be a bounded operator.
The *approximate point spectrum* of $T$ is the set $\sigma_{ap}(T)$ of $\lambda \in \C$ for which there is a sequence $(x_n)$ in $X$ with
$$\norm{x_n} = 1 \text{ for all } n \quad \text{and} \quad \norm{(T - \lambda I) x_n} \to 0.$$

## Remarks

Equivalently, $\lambda \in \sigma_{ap}(T)$ if and only if $T - \lambda I$ is not bounded below, that is, there is no $c > 0$ with $\norm{(T - \lambda I)x} \ge c \norm{x}$ for all $x$.
It satisfies $\sigma_p(T) \cup \sigma_c(T) \subseteq \sigma_{ap}(T) \subseteq \sigma(T)$, with the [[point spectrum|7FNVA0Q6YQ]], the [[continuous spectrum|YVH149HCAG]] and the [[spectrum|BMKATJ802A]].
It is closed, and it contains the boundary of $\sigma(T)$, so it is nonempty when $X \ne \set{0}$.

Example: for $D(x_n) = (x_n / n)$ on $\ell^2$, the unit vectors $e_n$ satisfy $\norm{D e_n} = 1/n \to 0$, so $0 \in \sigma_{ap}(D)$.

Non-example: for the right shift $S$ on $\ell^2$, $\norm{Sx} = \norm{x}$ for all $x$, so $S$ is bounded below and $0 \notin \sigma_{ap}(S)$, although $0 \in \sigma(S)$.
More generally $\norm{(S - \lambda I)x} \ge (1 - \abs{\lambda}) \norm{x}$, so $\sigma_{ap}(S)$ is the unit circle.

For a normal operator on a Hilbert space, $\sigma_{ap}(T) = \sigma(T)$.
