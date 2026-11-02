---
tag: V3MP0RJ2NX
kind: definition
name: Mapping cone
msc: [18G35, 18G80]
defines: 6CXPGB13WD
uses: [B2VP96NJSK, WQ82C0M3QB, HTK9WQZJ1G, BZEJKTQ76T, C9JEC2WQKV]
sources:
  - url: https://en.wikipedia.org/wiki/Mapping_cone_(homological_algebra)
---

## Definition

Let $\mathcal{A}$ be an [[additive category|B2VP96NJSK]] and let $f \colon C_\bullet \to D_\bullet$ be a [[chain map|HTK9WQZJ1G]] of [[chain complexes|WQ82C0M3QB]] in $\mathcal{A}$, with differentials $d^C$ and $d^D$.
The *mapping cone* of $f$ is the chain complex $\mathrm{cone}(f)$ with
$$\mathrm{cone}(f)_n = C_{n-1} \oplus D_n,$$
the [[biproduct|BZEJKTQ76T]], and with differential $\mathrm{cone}(f)_n \to \mathrm{cone}(f)_{n-1}$ given in matrix form by
$$d(c, y) = \left(-d^C_{n-1}(c),\ f_{n-1}(c) + d^D_n(y)\right).$$

## Remarks

The condition $d^2 = 0$ holds: $d^2(c, y) = \left(d^C d^C c,\ -f d^C c + d^D f c + d^D d^D y\right) = (0, 0)$, because $f$ is a chain map.
The inclusion $D_\bullet \to \mathrm{cone}(f)$ and the projection $\mathrm{cone}(f) \to C[-1]_\bullet$, where $C[-1]_n = C_{n-1}$ with differential $-d^C$, form a degreewise split short exact sequence of complexes.
In an abelian category, its long exact homology sequence has connecting maps equal to $H_{n-1}(f)$ up to sign.
So $f$ is a [[quasi-isomorphism|C9JEC2WQKV]] if and only if $\mathrm{cone}(f)$ has zero homology.
Sign conventions differ between texts; they give isomorphic complexes.

Example: let $C_\bullet = D_\bullet = \Z$ in degree $0$ and let $f_0$ be multiplication by $2$.
Then $\mathrm{cone}(f)_1 = \Z$, $\mathrm{cone}(f)_0 = \Z$, and the differential is $c \mapsto 2c$, so $H_0(\mathrm{cone}(f)) = \Z/2\Z \ne 0$ and $f$ is not a quasi-isomorphism.

Non-example: dropping the sign, $d(c, y) = (d^C c, f c + d^D y)$, does not give a complex in general.
For $C_\bullet = D_\bullet$ with $C_1 = C_0 = \Z$, $d_1 = 1_{\Z}$, and $f$ the identity, the element $(c, 0)$ in degree $2$ goes to $(c, c)$ and then to $(0, 2c) \ne 0$.
