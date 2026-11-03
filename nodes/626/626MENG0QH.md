---
tag: 626MENG0QH
kind: statement
role: theorem
name: Choquet-Bruhat–Geroch theorem on maximal developments
msc: ["83C05", "35Q75", "35L70"]
uses: [SB7BVCZJ3F, PZGHVCQB13, R8KDE9QYNP, PPB51F8QVK, 0Z1Y7JHGBR]
about: [SB7BVCZJ3F]
sources:
  - url: https://en.wikipedia.org/wiki/Initial_value_formulation_(general_relativity)
---

## Statement

Let $(\Sigma, h, K)$ be a smooth vacuum initial data set, as in the [[initial value formulation of general relativity|SB7BVCZJ3F]].
Then there is a development $(M, g, \iota)$ of $(\Sigma, h, K)$ with the following property.
For every development $(M', g', \iota')$ of the same data, there is an isometric embedding $\psi \colon M' \to M$ with $\psi \circ \iota' = \iota$.
This *maximal globally hyperbolic development* is unique up to an isometry that commutes with the embeddings of $\Sigma$.

## Remarks

Every development is a [[globally hyperbolic|PZGHVCQB13]] spacetime, because $\iota(\Sigma)$ is a [[Cauchy surface|R8KDE9QYNP]].
Local existence was proved by Choquet-Bruhat in 1952 with the [[harmonic coordinate condition|PPB51F8QVK]], which turns the vacuum equations into a system of quasilinear wave equations.
Local uniqueness says that two developments are isometric near $\Sigma$, by a [[diffeomorphism|0Z1Y7JHGBR]] that fixes the data.
Choquet-Bruhat and Geroch then obtained the maximal development in 1969, by gluing all developments together with Zorn's lemma.
Sbierski later gave a proof that avoids Zorn's lemma.
Example: for the data $(\R^3, \delta, 0)$ the maximal development is Minkowski space.
The maximal development may still be extendible as a smooth spacetime beyond a Cauchy horizon, for example for Taub–NUT data; the extension is then no longer determined by the data.

## Explanations

### L1 human

Given the state of space at one instant, Einstein's equations determine a unique largest spacetime that grows out of it.
Any other spacetime grown from the same data is just a piece of this largest one.

### L2 human

The theorem makes general relativity a deterministic theory in the same sense as other hyperbolic equations.
It gives the object on which global questions are asked: the [[nonlinear stability of Minkowski space|PH4Z47SCK6]] concerns the maximal development of data near $(\R^3, \delta, 0)$.
The [[strong cosmic censorship conjecture|C663A9H5DM]] asks whether, for generic data, the maximal development is inextendible.
