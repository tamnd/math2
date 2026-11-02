---
tag: 4XR88RPJ4K
kind: definition
name: Bohr compactification
msc: [22C05, 43A60, 22B05]
defines: G852FHZ3W1
uses: [92700QAB5Y, EVHCE5VR6Y, 9J5PQMG3HJ, FMW57WNPDB]
sources:
  - url: https://en.wikipedia.org/wiki/Bohr_compactification
---

## Definition

Let $G$ be a [[topological group|92700QAB5Y]].
A *Bohr compactification* of $G$ is a pair $(bG, b)$ of a compact Hausdorff group $bG$ and a [[continuous homomorphism|9J5PQMG3HJ]] $b \colon G \to bG$ with this property.
For every compact Hausdorff group $K$ and every continuous homomorphism $f \colon G \to K$, there is exactly one continuous homomorphism $\tilde{f} \colon bG \to K$ with $f = \tilde{f} \circ b$.

## Remarks

The Bohr compactification exists for every topological group, and it is unique up to a unique isomorphism compatible with the maps from $G$.
Example: if $G$ is a [[compact|EVHCE5VR6Y]] Hausdorff group, then $(G, \id_G)$ is a Bohr compactification, since each $f$ factors as $f = f \circ \id_G$ and the factor must be $f$.
Non-example: $(\mathbb{T}, x \mapsto e^{2\pi i x})$ is not a Bohr compactification of $\R$.
The continuous homomorphism $x \mapsto e^{2\pi i \sqrt{2} x}$ from $\R$ to $\mathbb{T}$ does not factor through $x \mapsto e^{2\pi i x}$.
A factor $\tilde f$ would give $e^{2\pi i \sqrt{2}} = \tilde f(e^{2\pi i}) = \tilde f(1) = 1$, which is false.
If $G$ is a locally compact abelian group, $bG$ is the [[Pontryagin dual|FMW57WNPDB]] of the group $\widehat{G}$ with the discrete topology, and $b(x)$ is evaluation at $x$.
The map $b$ need not be injective, and its image is dense in $bG$.
