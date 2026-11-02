---
tag: VAJPHCQBHR
kind: definition
name: Direct method in the calculus of variations
msc: [49J10, 49J45, 35A15]
defines: TE379HBTY0
uses: [PQ25NHV0KS, NN8RWPC8WG, P6KHVSTPZV, 95BSKT0S6M]
sources:
  - url: https://en.wikipedia.org/wiki/Direct_method_in_the_calculus_of_variations
---

## Definition

Let $X$ be a set with a notion of convergence of sequences, and let $J \colon X \to \R \cup \set{+\infty}$ be a functional with $\inf_X J < +\infty$.
The *direct method* is the following way to prove that $J$ has a minimiser.

1. Take a minimising sequence $(u_k)$, that is, $J(u_k) \to \inf_X J$.
2. Use *coercivity* to show that $(u_k)$ lies in a set that is sequentially compact, and extract a subsequence $u_{k_j} \to u$ in $X$.
3. Use sequential *lower semicontinuity*, $J(u) \le \liminf_j J(u_{k_j})$, to conclude that $J(u) = \inf_X J$.

The standard abstract form is this.
Let $X$ be a [[reflexive|NN8RWPC8WG]] Banach space and let $J$ be coercive, meaning $J(u) \to +\infty$ as $\norm{u} \to \infty$.
If $J$ is sequentially [[lower semicontinuous|95BSKT0S6M]] for the [[weak topology|P6KHVSTPZV]], then $J$ attains its minimum on $X$.

## Remarks

In the abstract form, coercivity makes a minimising sequence bounded, and bounded sequences in a reflexive Banach space have weakly convergent subsequences.
For integral functionals $J(u) = \int_\Omega L(x, u, \nabla u) \, dx$ of the [[calculus of variations|PQ25NHV0KS]] on $W^{1,q}(\Omega)$ with $1 < q < \infty$, weak lower semicontinuity holds when $L$ is continuous, bounded below and convex in $\nabla u$.

Example: let $\Omega \subseteq \R^n$ be bounded and open, $f \in L^2(\Omega)$, and $J(u) = \int_\Omega \big(\frac{1}{2}\abs{\nabla u}^2 - f u\big) \, dx$ on $H^1_0(\Omega)$.
By the Poincaré inequality $J(u) \ge c\norm{u}_{H^1}^2 - C\norm{u}_{H^1}$, so $J$ is coercive; it is convex and continuous, hence weakly lower semicontinuous.
So $J$ has a minimiser, which is the weak solution of $-\Delta u = f$ with $u = 0$ on $\partial\Omega$.

Non-example: $J(u) = \int_0^1 \big((u'^2 - 1)^2 + u^2\big) \, dx$ on $W^{1,4}(0, 1)$ is coercive, but its integrand is not convex in $u'$, so it is not weakly lower semicontinuous.
Indeed $\inf J = 0$, approached by sawtooth functions with slopes $\pm 1$ and small height, but no function has $J(u) = 0$, since this would need $u = 0$ and $\abs{u'} = 1$ almost everywhere.

## Explanations

### L1 human

The direct method finds a minimiser by taking a minimising sequence, extracting a convergent subsequence, and passing to the limit.
Coercivity gives the convergent subsequence and lower semicontinuity makes the limit a minimiser.
