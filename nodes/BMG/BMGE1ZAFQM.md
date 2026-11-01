---
tag: BMGE1ZAFQM
kind: definition
name: Galois theory
msc: [12F10]
defines: WNQDKQYZ2R
uses: [0WQ1A8SHTZ, 0DS2F7GK05, 0XVR72M51M, 0KMJ6919WS, 02NBKVQFRQ, R3625YKQC0]
sources:
  - url: https://en.wikipedia.org/wiki/Galois_theory
---

## Definition

Let $L/K$ be a [[field extension|0WQ1A8SHTZ]], and let $\Aut(L/K)$ be the group of field automorphisms of $L$ that fix every element of $K$.
*Galois theory* is the study of field extensions $L/K$ through the groups $\Aut(L/K)$ and the [[Galois connection between subgroups and subfields|R3625YKQC0]].
Its basic objects are:

1. the [[Galois extensions|0DS2F7GK05]], that is, the algebraic extensions that are normal and separable;
2. their [[Galois groups|0XVR72M51M]] $\Gal(L/K) = \Aut(L/K)$;
3. the maps $H \mapsto L^H$, from subgroups of $\Gal(L/K)$ to their [[fixed fields|0KMJ6919WS]], and $E \mapsto \Gal(L/E)$, from [[intermediate fields|02NBKVQFRQ]] to subgroups.

## Remarks

Example: for $L = \Q(i)$ over $\Q$, the group $\Gal(L/\Q)$ has two elements, the identity and complex conjugation, and the fixed field of the whole group is $\Q$.
Non-example of a Galois extension: $\Q(\sqrt[3]{2})/\Q$ is separable but not normal, since $x^3 - 2$ has only one root in it.
Its automorphism group is trivial, so the base field $\Q$ is not the fixed field of any subgroup.
The Galois group of a separable polynomial $f \in K[x]$ is the Galois group of a splitting field of $f$ over $K$.
