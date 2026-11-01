---
tag: BGXEC1SVQV
kind: definition
name: Regular chain
msc: [13P15, 13P10, 68W30]
defines: 1ZA98AGKGK
uses: [04C5ZBG1WT, 0SDC934R52, 0V5GYWR8R8, 096Z9MP2ME, 16J9DM8V57, 0NNRDW10RZ, 0076HWHGHQ]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_chain
---

## Definition

Let $k$ be a [[field|04C5ZBG1WT]] and let $S = k[x_1, \ldots, x_n]$ be the [[polynomial ring|0SDC934R52]] with the variables ordered $x_1 < x_2 < \cdots < x_n$.
Let $p \in S \setminus k$.
Its *main variable* $\operatorname{mvar}(p)$ is the largest variable that occurs in $p$.
Its *initial* $\operatorname{init}(p)$ is the [[leading coefficient|0V5GYWR8R8]] of $p$ as a polynomial in $\operatorname{mvar}(p)$.
A *triangular set* is a finite set $T$ of elements of $S \setminus k$ with pairwise distinct main variables.
For a triangular set $T$ with product of initials $h_T$, the *saturated ideal* is the [[ideal quotient|16J9DM8V57]] $\operatorname{sat}(T) = (T) : h_T^\infty = \set{ f \in S : h_T^m f \in (T) \text{ for some } m \ge 0 }$.
A triangular set $T$ is a *regular chain* if either $T = \emptyset$, or $T = T' \cup \set{t}$ where:

1. $\operatorname{mvar}(t)$ is larger than the main variable of every element of $T'$.
2. $T'$ is a regular chain.
3. $\operatorname{init}(t)$ is not a [[zero divisor|0NNRDW10RZ]] in the [[quotient ring|0076HWHGHQ]] $S/\operatorname{sat}(T')$.

## Remarks

For $T = \emptyset$, the saturated ideal is $(0)$, so a set $\set{t}$ with one element is always a regular chain.

Example: in $k[x, y]$ with $x < y$, let $T = \set{x^2 - 1, \; xy - 1}$.
Here $T' = \set{x^2 - 1}$ has initial $1$, so $\operatorname{sat}(T') = (x^2 - 1)$.
The initial of $t = xy - 1$ is $x$, and $x$ is a unit in $k[x, y]/(x^2 - 1)$, because $x \cdot x = 1$ there; so it is not a zero divisor, and $T$ is a regular chain.

Non-example: $T = \set{x^2 - x, \; xy - 1}$ fails clause 3.
Here $\operatorname{sat}(\set{x^2 - x}) = (x^2 - x)$, and $x \cdot (x - 1) = 0$ in $k[x, y]/(x^2 - x)$ with $x - 1 \ne 0$, so the initial $x$ is a zero divisor.
