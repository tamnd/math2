---
tag: 05HYGWFG63
kind: statement
role: theorem
name: Inner automorphism group is isomorphic to G modulo its centre
msc: [20F28]
uses: [0H47DMFN3S, 0S7Y9Q990Q, 0CXXJNG5B6]
sources:
  - url: https://en.wikipedia.org/wiki/Inner_automorphism
    locator: Inner and outer automorphism groups
---

## Statement

Let $G$ be a [[group|G5S1M9]] with [[centre|0DZ93493VN]] $Z(G)$.
Then the map $gZ(G) \mapsto c_g$, where $c_g(x) = gxg^{-1}$, is an [[isomorphism|08MG7H8JW5]] from $G/Z(G)$ to $\operatorname{Inn}(G)$.

## Remarks

The map $g \mapsto c_g$ is a surjective homomorphism from $G$ to $\operatorname{Inn}(G)$. Its kernel is $Z(G)$, because $c_g$ is the identity exactly when $g$ commutes with each element.
The [[first isomorphism theorem|0CXXJNG5B6]] then gives the result.
For example, the symmetric group $S_3$ has trivial centre, so $\operatorname{Inn}(S_3) \cong S_3$.

## Explanations

### L1 human

Two elements give the same conjugation exactly when they differ by an element of the centre.
So the inner automorphisms are counted by the cosets of the centre.
A group with a big centre has few inner automorphisms.
