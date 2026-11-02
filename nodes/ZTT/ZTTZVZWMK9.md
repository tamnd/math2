---
tag: ZTTZVZWMK9
kind: conjecture
name: Zariski's multiplicity conjecture
msc: [32S05, 32S15, 14B05]
uses: [EVPZ7ZG1HB, VZXF7RNFKS, 0QT00PB5G2]
about: [42V5XGZS4F, JX20MNDDXT]
sources:
  - url: https://en.wikipedia.org/wiki/Singularity_theory
history:
  posed_by: "Oscar Zariski"
  first_stated: "1971"
---

## Statement

Let $f, g \in \C\{z_0, \dots, z_n\}$ be [[convergent power series|EVPZ7ZG1HB]] without repeated factors, with $f(0) = g(0) = 0$.
The *multiplicity* $\operatorname{mult}_0 f$ is the least degree of a nonzero homogeneous term in the power series expansion of $f$.
Suppose that there is a [[homeomorphism|0QT00PB5G2]] $\phi$ between neighbourhoods of $0$ in $\C^{n+1}$ with $\phi(0) = 0$.
Suppose that $\phi$ maps the [[germ|VZXF7RNFKS]] of $f^{-1}(0)$ at $0$ onto the germ of $g^{-1}(0)$ at $0$.
Then $\operatorname{mult}_0 f = \operatorname{mult}_0 g$.

## Remarks

Zariski asked this question in his 1971 paper "Some open questions in the theory of singularities".
It is open in general.
It holds for plane curves, $n = 1$, where the embedded topological type determines the Puiseux characteristics of the branches and hence the multiplicity.
The multiplicity of $f$ equals the [[multiplicity of the local ring|JX20MNDDXT]] $\C\{z_0, \dots, z_n\} / (f)$, so the conjecture asks whether this algebraic invariant is determined by the embedded topology.
The Milnor number, by contrast, is known to be a topological invariant in this sense.

## Explanations

### L1 human

The multiplicity of a hypersurface at a point counts how many sheets meet there: a smooth point has multiplicity $1$, two crossing lines have multiplicity $2$.
Zariski asked whether this number can be read off from the shape of the hypersurface near the point, as seen by topology, without using its algebra.
For curves in the plane the answer is yes, but in higher dimensions the question is still unanswered.
