---
tag: C5282SWAEV
kind: proof
name: Proof that the coordinate map is a linear isomorphism
msc: [15A03]
proves: 059THXBRBB
uses: [0KCQ9Y3QKA, 04CYQHN6MC, 0XM8BZD76G, 0NRYHJPQG2, 0B8T10CE7N, 01VG2A0BHW]
sources:
  - url: https://dec41.user.srcf.net/notes/IB_M/linear_algebra_thm_proof.pdf
    locator: Section 2.1
---

## Proof

We check linearity from the uniqueness of coordinates, and then exhibit a two-sided inverse.

1. Let $\varphi \colon V \to F^n$ be the map $\varphi(v) = [v]_B$. It is well defined, because each $v \in V$ equals $a_1 b_1 + \cdots + a_n b_n$ for exactly one $(a_1, \dots, a_n) \in F^n$, since $B$ is a [[basis|0KCQ9Y3QKA]].
2. $\varphi$ is additive. Let $[v]_B = (a_1, \dots, a_n)$ and $[w]_B = (c_1, \dots, c_n)$. Then $v + w = \sum_i (a_i + c_i) b_i$.
3. By uniqueness of [[coordinates|04CYQHN6MC]], $[v + w]_B = (a_1 + c_1, \dots, a_n + c_n) = [v]_B + [w]_B$.
4. $\varphi$ is homogeneous. For $c \in F$, $cv = \sum_i (c a_i) b_i$, so by uniqueness $[cv]_B = c\,[v]_B$. Hence $\varphi$ is a [[linear map|0NRYHJPQG2]].
5. Let $\psi \colon F^n \to V$ be the map $\psi(a_1, \dots, a_n) = a_1 b_1 + \cdots + a_n b_n$ on the [[coordinate space|0XM8BZD76G]].
6. For $v \in V$ with $[v]_B = (a_1, \dots, a_n)$, the definition of coordinates gives $\psi(\varphi(v)) = \sum_i a_i b_i = v$. So $\psi \circ \varphi = \mathrm{id}_V$.
7. For $(a_1, \dots, a_n) \in F^n$, let $v = \psi(a_1, \dots, a_n) = \sum_i a_i b_i$. By uniqueness of coordinates, $[v]_B = (a_1, \dots, a_n)$. So $\varphi \circ \psi = \mathrm{id}_{F^n}$.
8. By [[the two-sided inverse criterion|01VG2A0BHW]], $\varphi$ is bijective, and its inverse is $\psi$.
9. So $\varphi$ is a bijective linear map, that is, a [[linear isomorphism|0B8T10CE7N]]. Its inverse sends $(a_1, \dots, a_n)$ to $a_1 b_1 + \cdots + a_n b_n$.

## Idea

Coordinates exist because a basis spans, and they are unique because a basis is independent. Uniqueness makes the coordinate map linear. Rebuilding a vector from its coordinates is the inverse map.
