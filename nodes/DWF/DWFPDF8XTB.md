---
tag: DWFPDF8XTB
kind: statement
role: theorem
name: Riesz–Markov–Kakutani representation theorem
msc: [28C05, 28C15, "46E27"]
uses: [0FE2SB8WVJ, 0S1FJ8VEX9, 0X3WGX95FE, 07YQ1C78G0, HZNEQQBCW4, DWJF7ABPR1]
about: [HZNEQQBCW4]
sources:
  - url: https://en.wikipedia.org/wiki/Riesz%E2%80%93Markov%E2%80%93Kakutani_representation_theorem
same_as:
  wikidata: Q17098001
  wikipedia: Riesz–Markov–Kakutani representation theorem
---

## Statement

Let $X$ be a [[locally compact|0FE2SB8WVJ]] [[Hausdorff space|0S1FJ8VEX9]].
Let $C_c(X)$ be the real vector space of [[continuous functions|0X3WGX95FE]] $f \colon X \to \R$ with compact support.
Let $\Lambda \colon C_c(X) \to \R$ be a [[linear form|07YQ1C78G0]] that is positive, that is, $\Lambda f \ge 0$ whenever $f \ge 0$.
Then there is a unique measure $\mu$ on the Borel sets of $X$ with these four properties:

1. $\Lambda f = \int_X f \, d\mu$ for every $f \in C_c(X)$, where the integral is the [[Lebesgue integral|DWJF7ABPR1]].
2. $\mu(K) < \infty$ for every compact set $K \subseteq X$.
3. $\mu(E) = \inf \set{\mu(U) : U \supseteq E, \ U \text{ open}}$ for every Borel set $E$.
4. $\mu(E) = \sup \set{\mu(K) : K \subseteq E, \ K \text{ compact}}$ for every open set $E$ and for every Borel set $E$ with $\mu(E) < \infty$.

## Remarks

Clauses 2 to 4 say that $\mu$ is a [[Radon measure|HZNEQQBCW4]].
The proof sets $\mu(U) = \sup \set{\Lambda f : 0 \le f \le 1, \ \operatorname{supp} f \subseteq U}$ for open $U$, extends it to an outer measure, and checks that the Borel sets are measurable.
Urysohn's lemma for locally compact Hausdorff spaces supplies the functions $f$ that the construction needs.

Example: on $X = \R$, the Riemann integral $\Lambda f = \int_{-\infty}^{\infty} f(x) \, dx$ is positive, and the measure it gives is Lebesgue measure.
The evaluation $\Lambda f = f(0)$ gives the Dirac measure at $0$.

Let $X$ be compact Hausdorff and give $C(X)$ the sup norm.
A related form identifies the dual of $C(X)$ with the space of regular signed Borel measures on $X$, normed by total variation.

## Explanations

### L1 human

A positive linear rule that assigns a number to each continuous function always comes from integration against a measure.
So measures and positive linear functionals on continuous functions are two descriptions of the same thing.
This is often used to build measures: one writes down the functional first.

### L2 human

The theorem is the bridge between functional analysis and measure theory.
It identifies the dual of $C(X)$ for compact $X$ with a space of measures, and so gives the weak-* topology on measures that underlies weak convergence of probability measures.
Haar measure on a locally compact group is often built by constructing an invariant positive functional and then applying this theorem.
