---
tag: XZFYB2PBPD
kind: statement
role: theorem
name: Fenchel–Moreau theorem
msc: [52A41, 46N10, 26B25]
uses: [T7V2VPY61S, 07Q7CNM5WF, RN4G8SGP6P, 03J5RAKB30, 4A82S5FVRT, 0GSZ7B0CGR, 8BJ5M76FSX]
about: [T7V2VPY61S]
sources:
  - url: https://en.wikipedia.org/wiki/Fenchel–Moreau_theorem
same_as:
  wikidata: Q5443005
  wikipedia: Fenchel–Moreau theorem
---

## Statement

Let $X$ be a real [[normed space|03J5RAKB30]] with [[continuous dual space|4A82S5FVRT]] $X^*$.
Let $f \colon X \to [-\infty, +\infty]$ be a function with values in the [[extended real line|0GSZ7B0CGR]], with [[Fenchel conjugate|T7V2VPY61S]] $f^* \colon X^* \to [-\infty, +\infty]$.
Define the biconjugate $f^{**} \colon X \to [-\infty, +\infty]$ by $f^{**}(x) = \sup_{y \in X^*} \big(y(x) - f^*(y)\big)$.
Then $f^{**} = f$ if and only if one of the following holds:

1. $f$ is proper, [[convex|07Q7CNM5WF]] and lower [[semicontinuous|RN4G8SGP6P]], where proper means that $f$ never takes the value $-\infty$ and is not identically $+\infty$;
2. $f$ is identically $+\infty$;
3. $f$ is identically $-\infty$.

## Remarks

For every $f$, the function $f^{**}$ is a supremum of continuous affine functions, so it is convex and lower semicontinuous, and the Fenchel–Young inequality gives $f^{**} \le f$.
If $f$ takes the value $-\infty$ somewhere, then $f^*$ is identically $+\infty$ and $f^{**}$ is identically $-\infty$, so $f^{**} = f$ forces case 3.
Otherwise $f^{**} = f$ forces $f$ to be convex and lower semicontinuous, which is case 1 or case 2.
For the "if" direction, take $x_0$ and a real $r < f(x_0)$.
The point $(x_0, r)$ lies outside the closed convex [[epigraph|8BJ5M76FSX]] of $f$, and the Hahn–Banach separation theorem gives a continuous affine minorant of $f$ with value above $r$ at $x_0$.
Every such minorant is below $f^{**}$, so $f^{**}(x_0) \ge f(x_0)$.

Example: $f(x) = \abs{x}$ on $\R$ has $f^* = 0$ on $[-1, 1]$ and $+\infty$ elsewhere, and $f^{**}(x) = \sup_{\abs{y} \le 1} xy = \abs{x}$.
Lower semicontinuity is necessary: for $f = 0$ on $(0, 1)$ and $f = +\infty$ elsewhere on $\R$, the function is convex and proper, but $f^{**}$ is $0$ on the closed interval $[0, 1]$.
Convexity is necessary: for $f(x) = \min\big((x - 1)^2, (x + 1)^2\big)$, the biconjugate is $0$ on $[-1, 1]$ and agrees with $f$ outside.

## Explanations

### L1 human

Taking the conjugate twice returns the function you started with, as long as the function is convex and has no gaps in its graph from below.
In general, the double conjugate is the largest convex, lower semicontinuous function that stays below $f$.
So a convex closed function is completely described by the family of lines that lie below it.

### L2 human

The theorem is the basis of duality in convex optimization.
A primal problem and its dual are related through conjugates, and the theorem says that dualizing twice gives back the primal problem.
It also shows that $f \mapsto f^*$ is a bijection between proper convex lower semicontinuous functions on $X$ and on the dual side, when $X$ is reflexive.
It extends the involution property of the classical Legendre transformation to nonsmooth functions.
The same statement holds in every Hausdorff locally convex space.
