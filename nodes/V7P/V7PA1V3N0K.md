---
tag: V7PA1V3N0K
kind: statement
role: theorem
name: Maximal ergodic theorem
msc: [37A30, 28D05]
uses: [556WBDAHNP, 0NFPJVJJHX, X7GTF3D98F, 8TD2KCVH5N]
about: [8TD2KCVH5N, 556WBDAHNP]
sources:
  - url: https://en.wikipedia.org/wiki/Maximal_ergodic_theorem
same_as:
  wikidata: Q6795637
  wikipedia: Maximal ergodic theorem
---

## Statement

Let $(X, \mathcal{A}, \mu)$ be a [[probability space|0NFPJVJJHX]], let $T \colon X \to X$ be a [[measure-preserving transformation|556WBDAHNP]], and let $f \colon X \to \R$ be [[integrable|X7GTF3D98F]].
For $n \ge 1$ let $S_n f = \sum_{k=0}^{n-1} f \circ T^k$ be the [[Birkhoff sums|8TD2KCVH5N]] of $f$, and let
$$E = \set{x \in X : \sup_{n \ge 1} S_n f(x) > 0}.$$
Then
$$\int_E f \, d\mu \ge 0.$$

## Remarks

Proof idea, after Garsia: let $F_N = \max(0, S_1 f, \dots, S_N f)$.
For $1 \le n \le N$ one has $S_n f \le f + F_N \circ T$, so $F_N \le f + F_N \circ T$ on the set $E_N = \set{F_N > 0}$.
Integrating over $E_N$ and using $F_N \ge 0$ and the invariance of $\mu$ gives $\int_{E_N} f \, d\mu \ge \int_X F_N \, d\mu - \int_X F_N \circ T \, d\mu = 0$.
The sets $E_N$ increase to $E$, and dominated convergence finishes the proof.

Applied to $f - \lambda$ for a real number $\lambda > 0$, it gives the maximal inequality
$$\lambda \, \mu\left(\set{x : \sup_{n \ge 1} \tfrac{1}{n} S_n f(x) > \lambda}\right) \le \int_X \abs{f} \, d\mu.$$
The inequality $\int_E f \, d\mu \ge 0$ holds, with the same proof, for a measure-preserving map of any measure space and any integrable $f$.

Example: if $f \ge 0$ is not almost everywhere $0$, then $E = \set{x : f(T^k(x)) > 0 \text{ for some } k \ge 0}$, and the conclusion $\int_E f \, d\mu \ge 0$ is clear; the content of the theorem lies in functions of both signs.

## Explanations

### L1 human

Consider the points from which the running total of $f$ along the orbit becomes positive at some time.
The theorem says that, on this set, the function $f$ has a nonnegative integral.
In other words, the points where the running sum ever gets ahead cannot, on average, be points where $f$ is negative.

### L2 human

This is the key lemma in the standard proof of Birkhoff's pointwise ergodic theorem.
Through the maximal inequality, it controls the supremum of all Birkhoff averages at once.
This control is what is needed to pass from a dense class of functions to all integrable functions.
It plays the same role as the Hardy–Littlewood maximal inequality in the proof of the Lebesgue differentiation theorem.
