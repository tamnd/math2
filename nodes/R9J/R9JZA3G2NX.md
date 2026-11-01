---
tag: R9JZA3G2NX
kind: statement
role: theorem
name: Thue–Siegel–Roth theorem
msc: [11J68]
uses: [0MNF0BYFQC, 0DZXAXEJQ9, 0NCJ5WXN6Z]
about: [0MNF0BYFQC]
sources:
  - url: https://en.wikipedia.org/wiki/Roth%27s_theorem
same_as:
  wikidata: Q751120
  wikipedia: Roth's theorem
---

## Statement

Let $\alpha$ be a real [[algebraic number|0MNF0BYFQC]] that is [[irrational|0DZXAXEJQ9]], and let $\varepsilon > 0$.
Then there are only finitely many [[rational numbers|0NCJ5WXN6Z]] $p/q$, with $p, q \in \Z$ and $q \ge 1$, such that
$$\abs{\alpha - \frac{p}{q}} < \frac{1}{q^{2 + \varepsilon}}.$$

## Remarks

The proof builds an auxiliary polynomial in many variables with integer coefficients that vanishes to high order at $(\alpha, \dots, \alpha)$.
Suppose there were many very good approximations with fast growing denominators.
Then this polynomial would have to vanish to high order at a rational point too, and a nonvanishing lemma (Roth's lemma) rules this out.
The proof is not effective: it gives a bound for the number of exceptional fractions, but not for their size.
The exponent $2$ cannot be lowered, because [[Dirichlet's approximation theorem|04JAY9DGB7]] gives infinitely many $p/q$ with $\abs{\alpha - p/q} < 1/q^2$.
The hypothesis that $\alpha$ is algebraic is necessary: a [[Liouville number|0PYEZM6CN9]] has, for each exponent $\mu$, infinitely many approximations with error less than $1/q^{\mu}$.
For example, $\alpha = \sqrt[3]{2}$ has only finitely many approximations with error less than $1/q^{2.01}$.
The theorem sharpens [[Liouville's theorem on Diophantine approximation|0N3WFZEFPM]], where the exponent is the degree of $\alpha$, and the later results of Thue and Siegel.

## Explanations

### L1 human

An algebraic irrational number, such as $\sqrt{2}$ or $\sqrt[3]{2}$, cannot be approximated by fractions much better than any irrational can.
Every irrational has infinitely many fractions $p/q$ within $1/q^2$, but only finitely many within $1/q^{2.001}$ when the number is algebraic.
Numbers that are approximated extremely well, like Liouville numbers, are therefore transcendental.

### L2 human

Roth's theorem implies that a [[Thue equation|3Q6CFPQZDF]] $F(x, y) = m$, with $F$ an irreducible binary form of degree at least $3$, has only finitely many integer solutions.
Its higher-dimensional generalization is the [[Schmidt subspace theorem|9TPS3W497D]].
The theorem says that the irrationality exponent of each algebraic irrational is $2$, the same as for almost all real numbers.
