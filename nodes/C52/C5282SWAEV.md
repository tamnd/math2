---
tag: C5282SWAEV
kind: proof
name: Proof that the coordinate map is a linear isomorphism
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
proves: 059THXBRBB
methods: [0NTF6DMVAP, 01XM7JEKHY]
uses: [E2ZRZGXSNX, 0KCQ9Y3QKA, 04CYQHN6MC, 0XM8BZD76G, 0NRYHJPQG2, 0B8T10CE7N, 01VG2A0BHW]
sources:
  - url: https://dec41.user.srcf.net/notes/IB_M/linear_algebra_thm_proof.pdf
    locator: Section 2.1
  - book: isbn:9780134860244
    locator: Section 2.4
---

## Proof

We use the uniqueness of coordinates twice: once to show that the coordinate map is linear, and once to show that rebuilding a vector from its coordinates is an inverse.
Write $\varphi(v) = [v]_B$.

1. The map $\varphi \colon V \to F^n$ is well defined. Since $B$ is a [[basis|0KCQ9Y3QKA]], each $v \in V$ equals $a_1 b_1 + \dots + a_n b_n$ for exactly one $(a_1, \dots, a_n) \in F^n$, by [[unique coordinates|E2ZRZGXSNX]].
2. The map is additive. Let $[v]_B = (a_1, \dots, a_n)$ and $[w]_B = (c_1, \dots, c_n)$. By the vector space axioms,
$$v + w = (a_1 + c_1) b_1 + \dots + (a_n + c_n) b_n.$$
So $(a_1 + c_1, \dots, a_n + c_n)$ is a list of coefficients for $v + w$, and by uniqueness it is the coordinate vector, so $[v + w]_B = [v]_B + [w]_B$.
3. The map is homogeneous. For $c \in F$, the axioms give $cv = (c a_1) b_1 + \dots + (c a_n) b_n$, so by uniqueness $[cv]_B = c [v]_B$. With step 2, $\varphi$ is a [[linear map|0NRYHJPQG2]].
4. Define $\psi \colon F^n \to V$ on the [[coordinate space|0XM8BZD76G]] by $\psi(a_1, \dots, a_n) = a_1 b_1 + \dots + a_n b_n$.
5. For $v \in V$ with $[v]_B = (a_1, \dots, a_n)$, the definition of [[coordinates|04CYQHN6MC]] says $v = \sum_i a_i b_i$, so $\psi(\varphi(v)) = v$. Hence $\psi \circ \varphi = \mathrm{id}_V$.
6. For $(a_1, \dots, a_n) \in F^n$, let $v = \psi(a_1, \dots, a_n) = \sum_i a_i b_i$. Then $(a_1, \dots, a_n)$ is a list of coefficients for $v$, so by uniqueness $\varphi(v) = (a_1, \dots, a_n)$. Hence $\varphi \circ \psi = \mathrm{id}_{F^n}$.
7. A map with a two-sided inverse is [[bijective|01VG2A0BHW]], so $\varphi$ is a bijective linear map, that is, a [[linear isomorphism|0B8T10CE7N]], and its inverse is $\psi$.

## Idea

Coordinates exist because the basis spans, and they are unique because it is independent.
Uniqueness does all the work: whenever we produce some list of coefficients for a vector, it must be the coordinate vector.
So the natural list for $v + w$, the sum of the two lists, is the right one, and the inverse map is just "multiply out the combination".

## Variants

One can start from $\psi$ instead.
The map $\psi \colon F^n \to V$ is linear by the vector space axioms, it is surjective because $B$ spans, and it is injective because its kernel consists of the relations among the $b_i$, which are trivial by independence.
So $\psi$ is a linear bijection, its inverse is linear, and that inverse is $\varphi$ by the definition of coordinates.
