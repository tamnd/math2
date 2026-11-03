---
tag: YS3ER7BW8W
kind: statement
role: theorem
name: Osterwalder–Schrader reconstruction theorem
msc: [81T05, 81T08]
uses: [5QTZQV6TNG, G686S8SEK0, CG9JEATW3Q, 0H3YY8CPKH, 0M3YQJ81NB]
about: [5QTZQV6TNG]
sources:
  - url: https://en.wikipedia.org/wiki/Schwinger_function
---

## Statement

Let $d \ge 2$, and write points of $\R^d$ as $x = (x^0, \mathbf{x})$ with $x^0$ the Euclidean time; let $\theta(x^0, \mathbf{x}) = (-x^0, \mathbf{x})$ be time reflection.
For $n \ge 1$, let $\mathcal{S}_0(\R^{dn})$ be the space of [[Schwartz functions|CG9JEATW3Q]] on $(\R^d)^n$ that vanish with all derivatives where $x_i = x_j$ for some $i \ne j$.
Let $\mathcal{S}_+(\R^{dn})$ be its subspace of functions supported in $\set{0 < x_1^0 < \cdots < x_n^0}$.
For $f \in \mathcal{S}_+(\R^{dn})$ put $(\Theta f)(x_1, \dots, x_n) = \overline{f(\theta x_n, \dots, \theta x_1)}$.
Let $S_0 = 1$ and let $S_n$, $n \ge 1$, be continuous linear functionals on $\mathcal{S}_0(\R^{dn})$, the Schwinger functions, such that:

1. (E0′, linear growth) there are an integer $s$ and constants $\alpha, \beta$ with $\abs{S_n(f)} \le \alpha (n!)^\beta \abs{f}_{s n}$ for all $n$ and $f$.
   Here $\abs{\cdot}_k$ is the Schwartz norm of order $k$.
2. (E1, Euclidean covariance) $S_n$ is invariant under the simultaneous action of the [[Euclidean group|0H3YY8CPKH]] on all $n$ arguments;
3. (E2, reflection positivity) for every finite family $f_n \in \mathcal{S}_+(\R^{dn})$, $n \ge 0$, one has $\sum_{n, m} S_{n+m}(\Theta f_n \otimes f_m) \ge 0$;
4. (E3, symmetry) $S_n$ is invariant under permutations of its $n$ arguments.

Then there is a quantum field theory on $d$-dimensional Minkowski space that satisfies the [[Wightman axioms|5QTZQV6TNG]], except possibly the uniqueness of the vacuum.
Its Wightman functions are boundary values of analytic functions whose values at Euclidean points are the $S_n$.
The passage between them is the [[Wick rotation|G686S8SEK0]] $x^0 = i t$.
If moreover

5. (E4, cluster property) $S_{n+m}(f \otimes g_{(\lambda a)}) - S_n(f)\, S_m(g) \to 0$ as $\lambda \to \infty$ for every spacelike unit vector $a$ and all $f, g$, where $g_{(\lambda a)}$ is $g$ translated by $\lambda a$,

then the vacuum is unique.

## Remarks

Idea of the proof: reflection positivity gives a positive semidefinite inner product on vectors $(f_n)_n$ with positive time support, and the quotient by null vectors, completed, is the Hilbert space.
Euclidean time translation by $\tau \ge 0$ becomes a contraction semigroup $e^{-\tau H}$ with $H \ge 0$, which is the Hamiltonian of the relativistic theory.
The [[analytic continuation|0M3YQJ81NB]] from imaginary to real time is the delicate step, and the growth condition E0′ is what controls it.
The first paper of Osterwalder and Schrader, from 1973, had a gap in this step; their 1975 paper closed it by adding the linear growth condition.

Example: the Schwinger functions of the free scalar field of mass $m > 0$ are Gaussian, with two-point function $S_2(x, y) = G(x - y)$, the kernel of $(-\Delta + m^2)^{-1}$ on $\R^d$, and they satisfy E0′–E4.

## Explanations

### L1 human

Euclidean field theory is much easier to study than relativistic field theory, because time is just another coordinate and the integrals converge.
The theorem tells when a Euclidean theory comes from a genuine relativistic quantum field theory.
The key condition, reflection positivity, says that reflecting time turns certain sums into nonnegative numbers, and these sums become squared lengths in the Hilbert space of states.
With this theorem, a theory built in imaginary time can be rotated back to real time.

### L2 human

This theorem is the bridge used by constructive quantum field theory.
Models such as the $\phi^4$ theory in two and three dimensions are built as Euclidean measures, often as limits of lattice or cut-off models.
The moments of these measures are the Schwinger functions.
Reflection positivity is often checked at the level of lattice approximations, where it becomes a finite-dimensional positivity statement.
The converse direction, from Wightman functions to Schwinger functions, holds as well, since the Wightman functions extend analytically to the Euclidean points.
