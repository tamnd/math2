---
tag: GTA8ZFGZ3N
kind: statement
role: theorem
name: Universal coefficient theorem
msc: [55U20, 18G15, 55N10]
uses: [0CMD0BCH8T, WQ82C0M3QB, 2J4JJJYP22, F0HQXQ0HCD, DDQRERAQCV, 4P7GBWJ4RR, M0Q5CFJ7ZH, 6N7BC70CX0, 0CQHFPGJ45]
about: [M0Q5CFJ7ZH, 6N7BC70CX0]
sources:
  - url: https://en.wikipedia.org/wiki/Universal_coefficient_theorem
same_as:
  wikidata: Q2495664
  wikipedia: Universal coefficient theorem
---

## Statement

Let $R$ be a [[principal ideal domain|0CMD0BCH8T]], let $C_\bullet$ be a [[chain complex|WQ82C0M3QB]] of free $R$-modules, and let $M$ be an $R$-module.
Then for every $n$ there are natural short exact sequences
$$0 \to H_n(C) \otimes_R M \to H_n(C \otimes_R M) \to \operatorname{Tor}_1^R(H_{n-1}(C), M) \to 0,$$
$$0 \to \operatorname{Ext}^1_R(H_{n-1}(C), M) \to H^n(\Hom_R(C, M)) \to \Hom_R(H_n(C), M) \to 0,$$
and both split, though not naturally.
In particular, for a [[topological space|0CQHFPGJ45]] $X$ and an abelian group $G$, applied to the singular chain complex of $X$:
$$H_n(X; G) \cong (H_n(X) \otimes G) \oplus \operatorname{Tor}_1^\Z(H_{n-1}(X), G), \qquad H^n(X; G) \cong \Hom(H_n(X), G) \oplus \operatorname{Ext}^1_\Z(H_{n-1}(X), G).$$

## Remarks

Here $H_n(X)$ is [[singular homology|M0Q5CFJ7ZH]] with integer coefficients and $H^n(X; G)$ is [[singular cohomology|6N7BC70CX0]]; [[Tor|DDQRERAQCV]] and [[Ext|4P7GBWJ4RR]] are the derived functors of $\otimes$ and $\Hom$.
For the proof, the cycles $Z_n$ and boundaries $B_n$ of $C$ are free, since submodules of free modules over a principal ideal domain are free.
So $0 \to Z_\bullet \to C_\bullet \to B_{\bullet-1} \to 0$ splits in each degree.
Apply $- \otimes M$ or $\Hom(-, M)$ and take the long exact sequence; its connecting maps are induced by the inclusions $B_n \to Z_n$.
Their kernels and cokernels are the Tor and Ext terms.
Example: for the real projective plane $P$, $H_0(P) = \Z$, $H_1(P) = \Z/2\Z$, $H_2(P) = 0$.
So $H^1(P; \Z) \cong \Hom(\Z/2\Z, \Z) \oplus \operatorname{Ext}^1(\Z, \Z) = 0$ and $H^2(P; \Z) \cong \Hom(0, \Z) \oplus \operatorname{Ext}^1(\Z/2\Z, \Z) \cong \Z/2\Z$.
This shows that cohomology is not simply the dual of homology: the torsion of $H_1$ moves up to $H^2$.

## Explanations

### L1 human

Homology with integer coefficients determines homology and cohomology with any other coefficients.
The answer is almost the naive one, the tensor product or the dual, plus a correction that comes from torsion.
For the projective plane, the integer homology in degree one is $\Z/2\Z$, and this torsion reappears in integer cohomology one degree higher.

### L2 human

The homology part of the theorem is a special case of the [[Künneth theorem|77K0BZQ4MK]], with the second complex a module in degree $0$.
It is used constantly, for example to compute cohomology from homology.
It also shows that a map inducing isomorphisms on integral homology induces isomorphisms on homology and cohomology with all coefficients.
Over a field $k$, it gives $H^n(X; k) \cong \Hom_k(H_n(X; k), k)$.
