---
tag: NPY85FYJHF
kind: definition
name: Infinite Galois theory
msc: [12F10, "20E18"]
defines: RVR5QFFD77
uses: [0DS2F7GK05, 0XVR72M51M, F3GTF5NT4M, 02NBKVQFRQ, 0KMJ6919WS, 09EYMKMSB9]
sources:
  - url: https://en.wikipedia.org/wiki/Galois_extension
---

## Definition

Let $L/K$ be a [[Galois extension|0DS2F7GK05]], that is, an [[algebraic extension|09EYMKMSB9]] that is normal and separable, of possibly infinite degree.
*Infinite Galois theory* is the study of $L/K$ through its [[Galois group|0XVR72M51M]] $G = \Gal(L/K)$ with the [[Krull topology|F3GTF5NT4M]].
Its central statement is the Galois correspondence:

1. the maps $H \mapsto L^H$, with $L^H$ the [[fixed field|0KMJ6919WS]] of $H$, and $E \mapsto \Gal(L/E)$ are inverse bijections that reverse inclusion.
   They match the closed subgroups $H$ of $G$ with the [[intermediate fields|02NBKVQFRQ]] $E$ of $L/K$;
2. a closed subgroup $H$ is open if and only if $L^H/K$ is finite;
3. a closed subgroup $H$ is normal if and only if $L^H/K$ is Galois, and then $\Gal(L^H/K) \cong G/H$ as topological groups.

## Remarks

Example: let $K = \F_p$ and $L$ an algebraic closure of $\F_p$.
The intermediate fields are the fields $\F_{p^n}$ and the infinite unions of such fields, and $\F_{p^n}$ corresponds to the open subgroup generated topologically by $\phi^n$, where $\phi(x) = x^p$.
Non-example of the correspondence for all subgroups: the subgroup $H = \set{\phi^k : k \in \Z}$ is not closed in $\Gal(L/\F_p)$.
Its fixed field is $\F_p$, the same as for the whole group, so $H \mapsto L^H$ is not injective on all subgroups.
When $L/K$ is finite, the Krull topology is discrete, every subgroup is closed, and the theory reduces to the [[fundamental theorem of Galois theory|0T1Q8D0FW8]].
