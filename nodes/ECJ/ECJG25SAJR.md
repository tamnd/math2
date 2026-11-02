---
tag: ECJG25SAJR
kind: statement
role: theorem
name: Hartogs's theorem on separate holomorphicity
msc: [32A10]
uses: [507C34W0ZT, 0NAHXR1FRH, NBFNXA2WFM]
about: [507C34W0ZT]
sources:
  - url: https://en.wikipedia.org/wiki/Hartogs%27s_theorem_on_separate_holomorphicity
same_as:
  wikidata: Q1050932
  wikipedia: Hartogs's theorem on separate holomorphicity
---

## Statement

Let $D \subseteq \C^n$ be an open set and let $f \colon D \to \C$ be a function.
Suppose that $f$ is holomorphic in each variable separately.
That is, for each $j$ and each choice of the other coordinates, the function $z_j \mapsto f(z_1, \dots, z_n)$ is [[holomorphic|0NAHXR1FRH]] where it is defined.
Then $f$ is a [[holomorphic function|507C34W0ZT]] on $D$; in particular, $f$ is continuous.

## Remarks

If $f$ is also assumed continuous, the result is easier: it is [[Osgood's lemma|NBFNXA2WFM]].
The same easy argument works if $f$ is only assumed locally bounded.
In that case the iterated Cauchy formula on small polydiscs gives the power series of $f$.
Hartogs's proof first finds, by a Baire category argument, small polydiscs on which $f$ is bounded.
It then uses [[Hartogs's lemma for subharmonic functions|ZENZT8596D]] on the power series in one variable to get holomorphy at every point.
No such result holds for real variables.
The function $g(x, y) = xy/(x^2 + y^2)$ with $g(0, 0) = 0$ is real analytic in each variable separately, yet it is not continuous at the origin.
Example: $f(z_1, z_2) = e^{z_1 z_2}$ is entire in $z_1$ for each fixed $z_2$ and in $z_2$ for each fixed $z_1$, so it is holomorphic on $\C^2$.

## Explanations

### L1 human

To check that a function of several complex variables is holomorphic, it is enough to check it one variable at a time.
No continuity needs to be assumed; it comes for free.
This is special to complex variables: the same statement fails for real smooth or analytic functions.

### L2 human

The theorem shows that the definition of holomorphy in several variables is very robust.
Complex differentiability, holomorphy in each variable, local power series expansion, and the Cauchy–Riemann equations for $C^1$ functions all give the same class of functions.
In practice one often uses the easier Osgood version, since continuity is usually known.
The full theorem is a striking early result of the theory, and its proof introduced methods that reappear in the study of plurisubharmonic functions.
