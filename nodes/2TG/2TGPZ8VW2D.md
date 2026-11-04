---
tag: 2TGPZ8VW2D
kind: definition
name: Germ of a holomorphic function
msc: [32A10, 32B05]
defines: 7PJ8KVZZCQ
uses: [Y98MD3WVTG, 507C34W0ZT, 0ZCY0Z80B6]
sources:
  - url: https://en.wikipedia.org/wiki/Germ_(mathematics)
  - url: https://github.com/jirilebl/scv/blob/78d7d41554695c389552c301398803d4633b9208/scv.tex#L14214
    locator: scv.tex:14214
---

## Definition

Let $a \in \C^n$.
Consider pairs $(U, f)$ where $U \subseteq \C^n$ is an open [[neighbourhood|0ZCY0Z80B6]] of $a$ and $f \colon U \to \C$ is a [[holomorphic function|507C34W0ZT]].
Two pairs $(U, f)$ and $(V, g)$ are equivalent if there is an open neighbourhood $W \subseteq U \cap V$ of $a$ with $f = g$ on $W$.
A *germ of a holomorphic function* at $a$ is an equivalence class for this relation.
The germ of $(U, f)$ is written $f_a$, and the set of all germs at $a$ is written $\mathcal{O}_{n,a}$, or $\mathcal{O}_a$.

## Remarks

This is the notion of [[germ|Y98MD3WVTG]] applied to holomorphic functions.
Sums and products of representatives on a common neighbourhood make $\mathcal{O}_{n,a}$ a commutative ring, and evaluation $f_a \mapsto f(a)$ is well defined.
Example: the pairs $(\C \setminus \set{1}, 1/(1 - z))$ and $(\set{\abs{z} < 1}, \sum_{k \ge 0} z^k)$ define the same germ at $0 \in \C$, since the two functions agree on the unit disc.
Non-example: the pairs $(\C, z)$ and $(\C, z + z^2)$ do not define the same germ at $0$, since $z^2 \ne 0$ at every point $z \ne 0$ near $0$.
By the identity theorem, two holomorphic functions on a connected open set containing $a$ have the same germ at $a$ only if they are equal.
Taking Taylor series at $a$ gives an isomorphism of $\mathcal{O}_{n,a}$ onto the ring of convergent power series in $z_1 - a_1, \dots, z_n - a_n$.
The germs at all points of an open set $D$ are the stalks of the sheaf $\mathcal{O}$ of holomorphic functions on $D$.
