---
tag: P84GBDM0QR
kind: definition
name: Cartan–Eilenberg resolution
msc: [18G10, 18G35]
defines: SX8V8GR5ZG
uses: [Y9CZ3MTNF1, WQ82C0M3QB, N80ABTQHEQ, YXMXAGVC1Q, HK2AA1YSQ2, 2J4JJJYP22, HTK9WQZJ1G]
sources:
  - url: https://en.wikipedia.org/wiki/Cartan%E2%80%93Eilenberg_resolution
---

## Definition

Let $\mathcal{A}$ be an [[abelian category|Y9CZ3MTNF1]] and let $C_\bullet$ be a [[chain complex|WQ82C0M3QB]] in $\mathcal{A}$.
A *Cartan–Eilenberg resolution* of $C_\bullet$ is a [[double complex|N80ABTQHEQ]] $P_{\bullet,\bullet}$ of [[projective objects|YXMXAGVC1Q]] with $P_{p,q} = 0$ for $q < 0$.
Its horizontal differential is $d^h \colon P_{p,q} \to P_{p-1,q}$ and its vertical differential is $d^v \colon P_{p,q} \to P_{p,q-1}$.
It comes with a [[chain map|HTK9WQZJ1G]] $\varepsilon \colon P_{\bullet,0} \to C_\bullet$ with $\varepsilon \circ d^v = 0$ on $P_{\bullet,1}$.
These data must satisfy, for every $p$:

1. if $C_p = 0$, then $P_{p,q} = 0$ for all $q$;
2. the maps induced by $\varepsilon$ on boundaries, $B_p(P_{\bullet,\bullet}, d^h) \to B_p(C)$, form a [[projective resolution|HK2AA1YSQ2]] of $B_p(C)$;
3. the maps induced by $\varepsilon$ on [[homology|2J4JJJYP22]], $H_p(P_{\bullet,\bullet}, d^h) \to H_p(C)$, form a projective resolution of $H_p(C)$.

Here $B_p(P_{\bullet,\bullet}, d^h)$ and $H_p(P_{\bullet,\bullet}, d^h)$ are the complexes, with vertical differential, of horizontal boundaries and horizontal homology in column $p$.

## Remarks

It follows that each column $P_{p,\bullet} \to C_p$ and the cycles $Z_p(P_{\bullet,\bullet}, d^h) \to Z_p(C)$ are projective resolutions too.
If $\mathcal{A}$ has [[enough projectives|J2TX4TDPCX]], every chain complex has a Cartan–Eilenberg resolution.
It is built with the [[horseshoe lemma|VNMBSYX9PY]] applied to $0 \to B_p \to Z_p \to H_p \to 0$ and $0 \to Z_p \to C_p \to B_{p-1} \to 0$.
Example: let $C$ be a module $M$ in degree $0$, and place a projective resolution $Q_\bullet \to M$ in column $0$.
This is a Cartan–Eilenberg resolution: the boundaries are $0$, resolved by $0$.
The horizontal homology of column $0$ is $Q_\bullet$, which resolves $H_0(C) = M$.
Non-example: over $\Z$, let $C$ be $\Z \xrightarrow{\cdot 2} \Z$ in degrees $1$ and $0$, and let $P = C$ placed in row $0$.
Clause 3 fails in degree $0$: the horizontal homology there is $\Z/2\Z$ alone.
It is not projective, so it is not a projective resolution of $H_0(C) = \Z/2\Z$.
Injective Cartan–Eilenberg resolutions of cochain complexes are defined dually.
