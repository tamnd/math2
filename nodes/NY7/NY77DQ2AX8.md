---
tag: NY77DQ2AX8
kind: statement
role: theorem
name: Kodaira vanishing theorem
msc: [14F17, 32L20]
uses: [A4H4CZ2V35, EXKGG9X6J0, RRK8P6TXG2, W05VYY4HBR, PQ6Q143ARJ]
about: [RRK8P6TXG2, PQ6Q143ARJ]
sources:
  - url: https://en.wikipedia.org/wiki/Kodaira_vanishing_theorem
same_as:
  wikidata: Q2518048
  wikipedia: Kodaira vanishing theorem
---

## Statement

Let $X$ be a [[smooth|EXKGG9X6J0]] [[projective variety|A4H4CZ2V35]] of dimension $n$ over a field of characteristic $0$, with [[canonical bundle|W05VYY4HBR]] $\omega_X$.
Let $L$ be an [[ample line bundle|RRK8P6TXG2]] on $X$.
Then
$$H^i(X, \omega_X \otimes L) = 0 \quad \text{for all } i > 0,$$
where $H^i$ is [[sheaf cohomology|PQ6Q143ARJ]].
Equivalently, by Serre duality, $H^i(X, L^{-1}) = 0$ for all $i < n$.

## Remarks

Kodaira's proof over $\C$ uses a Hermitian metric on $L$ with positive curvature and the Bochner–Kodaira–Nakano identity, which shows that harmonic forms representing the classes must vanish.
Deligne and Illusie gave an algebraic proof by reduction to positive characteristic, using a lifting of $X$ modulo $p^2$.

Example: on $X = \mathbb{P}^n_\C$ with $L = \mathcal{O}(d)$, $d > 0$, one has $\omega_X \otimes L = \mathcal{O}(d - n - 1)$, and indeed $H^i(\mathbb{P}^n, \mathcal{O}(m)) = 0$ for $0 < i < n$ and all $m$, and for $i = n$ when $m > -n-1$.

The ampleness hypothesis cannot be dropped: for a curve $X$ of genus $g \ge 1$ and $L = \mathcal{O}_X$, $H^1(X, \omega_X) \cong \C \ne 0$.
The characteristic hypothesis is also needed: Raynaud gave counterexamples in positive characteristic.

## Explanations

### L1 human

The Kodaira vanishing theorem says that certain cohomology groups of a positive line bundle, twisted by the canonical bundle, are all zero.
When cohomology vanishes, global sections are easy to count, because the Euler characteristic, which Riemann–Roch computes, equals the dimension of the space of sections.
So the theorem turns an existence question into a numerical computation.

### L2 human

The theorem is a key input of the Kodaira embedding theorem and of the theory of adjoint linear systems $\abs{K_X + L}$.
Its generalizations, the Nakano vanishing theorem for higher differential forms and the Kawamata–Viehweg vanishing theorem for nef and big bundles, are basic tools of the minimal model program.
It fails in positive characteristic, which makes it a test case for methods there.
