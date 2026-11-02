---
tag: 4READX002Z
kind: statement
role: theorem
name: Stein factorization
msc: [14A15]
uses: [JXRKH6P1Z4, ND6XEY68P4, 9537RKBZPP, N9C4X7XKE4]
about: [9537RKBZPP]
sources:
  - url: https://en.wikipedia.org/wiki/Stein_factorization
same_as:
  wikidata: Q7606788
  wikipedia: Stein factorization
---

## Statement

Let $Y$ be a locally [[Noetherian scheme|ND6XEY68P4]] and let $f \colon X \to Y$ be a [[proper morphism|9537RKBZPP]].
Then $f = g \circ f'$ for [[morphisms|JXRKH6P1Z4]] $f' \colon X \to Y'$ and $g \colon Y' \to Y$ with the following properties.

1. $g$ is a [[finite morphism|N9C4X7XKE4]].
2. $f'$ is proper, and the map $\mathcal{O}_{Y'} \to f'_* \mathcal{O}_X$ is an isomorphism.
3. Every fibre of $f'$ is nonempty and connected.

One may take $Y'$ to be the relative spectrum over $Y$ of the sheaf of $\mathcal{O}_Y$-algebras $f_* \mathcal{O}_X$.

## Remarks

The sheaf $f_* \mathcal{O}_X$ is coherent because $f$ is proper, so $g$ is finite.
Clause 3 follows from clause 2 by Zariski's connectedness theorem, which in turn rests on the theorem on formal functions.
For example, if $f$ is finite, then $f$ is affine and $X$ is the relative spectrum of $f_* \mathcal{O}_X$.
So $Y' = X$, $f'$ is the identity and $g = f$.
At the other extreme, for $X$ proper and connected over $k$ with $\mathcal{O}(X) = k$, the map $X \to \operatorname{Spec} k$ already has $Y' = Y$.
The properness hypothesis is necessary: for a non-proper $f$, the sheaf $f_* \mathcal{O}_X$ need not be coherent.
For $\mathbb{A}^1_k \to \operatorname{Spec} k$, the algebra $f_* \mathcal{O}_X = k[t]$ is not finite over $k$.

## Explanations

### L1 human

Every proper map splits into two simpler maps.
The first has connected fibres, so it only collapses connected pieces.
The second is finite, so each point of the target has finitely many preimages.
One can picture it as first squashing each connected part of each fibre to a point, and then mapping the result finitely onto the target.

### L2 human

The Stein factorization reduces many questions about proper morphisms to two cases: finite morphisms and morphisms with connected fibres.
It is used in the study of contractions in birational geometry.
The contractions of the minimal model program are by definition proper morphisms $f$ with $f_* \mathcal{O}_X = \mathcal{O}_Y$, exactly the maps $f'$ of the factorization.
The name comes from the analogous result of Karl Stein for proper holomorphic maps of complex spaces.
