---
tag: FRNXHYX2SH
kind: statement
role: theorem
name: Duminil-Copin–Smirnov theorem
msc: [82B41, 05A16]
uses: [P671RWPDJJ, E2BVEB570S]
about: [P671RWPDJJ]
sources:
  - url: https://en.wikipedia.org/wiki/Connective_constant
---

## Statement

Let $\mathbb H$ be the hexagonal lattice, the infinite planar graph in which every vertex has degree $3$ and every face is a regular hexagon.
Then the [[connective constant|P671RWPDJJ]] of $\mathbb H$ is
$$\mu(\mathbb H) = \sqrt{2 + \sqrt 2}.$$

## Remarks

Bernard Nienhuis predicted this value in 1982 with the [[Coulomb gas method|X02M521M51]].
Hugo Duminil-Copin and Stanislav Smirnov proved it in a paper published in 2012.

Idea of the proof: let $x_c = 1/\sqrt{2 + \sqrt 2}$, and let $Z(x) = \sum_{\gamma} x^{\abs{\gamma}}$ be the generating function of [[self-avoiding walks|E2BVEB570S]] from a fixed point, where $\abs{\gamma}$ is the length of $\gamma$.
The radius of convergence of $Z$ is $1/\mu$, so the claim is that $Z(x) < \infty$ for $x < x_c$ and $Z(x_c) = \infty$.
The proof uses a parafermionic observable, a sum over walks in a domain weighted by $x_c^{\abs{\gamma}}$ and by a complex phase given by the winding of $\gamma$.
At $x = x_c$ this observable satisfies a discrete form of half of the Cauchy–Riemann equations, around every vertex.
Summing these relations over a trapezoidal domain gives a linear identity between walks ending on the different sides, from which both bounds follow.

Example of the statement at work: since $c_n \ge \mu^n$ for all $n$, the number of self-avoiding walks of $n$ steps from a vertex of $\mathbb H$ is at least $(2 + \sqrt 2)^{n/2} \approx 1.848^n$.

## Explanations

### L1 human

On a honeycomb grid, count the paths of $n$ steps that never visit a point twice.
Each step offers at most $2$ new directions, so the count is at most about $2^n$, and in fact it grows like $\mu^n$ with $\mu$ about $1.848$.
The theorem says that $\mu$ is exactly $\sqrt{2 + \sqrt 2}$, a rare case of an exact value.

### L2 human

The connective constant is not universal: it depends on the lattice, unlike critical exponents.
The hexagonal lattice is special because of a discrete holomorphic structure at $x_c$, the same kind of structure that appears in Smirnov's proof of [[Cardy's formula|AKRJ7MDNMW]].
The theorem was a first rigorous confirmation of the Coulomb gas predictions for the self-avoiding walk.
The critical exponents of the self-avoiding walk in the plane, such as the growth $c_n \approx \mu^n n^{11/32}$, are still not proved.
