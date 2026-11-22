---
tag: JP2G9QMQDE
kind: proof
name: Proof that an endomorphism is cyclic if and only if its minimal and characteristic polynomials are equal
msc: ["15A21", "15A18"]
topics: [GEBYZKYV3D]
audience: ug2
proves: RK1QVMYW7H
methods: [0NTF6DMVAP]
uses: [5VYBJYPYMW, QPE5Y86Y8V, 0J5EMJRRFM, 03NDVCSHSB, 03GSZ8RTZJ]
sources:
  - url: https://en.wikipedia.org/wiki/Cyclic_subspace
    locator: Companion matrix
---

## Proof

We prove each direction with the [[lemma on cyclic subspaces|5VYBJYPYMW]], and for the second direction we also use a vector whose annihilator is the minimal polynomial.

1. Assume that $T$ is cyclic, with a cyclic vector $v$, so that $Z(v; T) = V$.
2. By part 6 of the lemma on cyclic subspaces, the restriction of $T$ to $Z(v; T)$ has minimal polynomial and characteristic polynomial both equal to $m_v$. This restriction is $T$ itself, because $Z(v; T) = V$.
3. So $m_T = m_v = \chi_T$.
4. Conversely, assume that $m_T = \chi_T$. Then $\deg m_T = \deg \chi_T = n$.
5. By the [[lemma on a vector of maximal annihilator|QPE5Y86Y8V]], there is a vector $v \in V$ with $m_v = m_T$.
6. By part 3 of the lemma on cyclic subspaces, $\dim Z(v; T) = \deg m_v = n = \dim V$.
7. A subspace of $V$ whose [[dimension|03GSZ8RTZJ]] is $\dim V$ is $V$ itself, so $Z(v; T) = V$ and $T$ is cyclic.
8. Finally, let $v$ be any cyclic vector. Part 5 of the lemma on cyclic subspaces gives the matrix $C(m_v)$ in the basis $v, Tv, \dots, T^{n-1} v$, and $m_v = \chi_T$ by step 3.

## Idea

A cyclic vector gives a basis in which $T$ is a companion matrix, and a companion matrix has equal minimal and characteristic polynomials.
For the other direction, pick a vector that needs the whole minimal polynomial to be killed.
It generates a cyclic subspace of dimension $\deg m_T$, and when $m_T = \chi_T$ that dimension is $n$, so the subspace is everything.

## Variants

The [[cyclic decomposition theorem|R3Z20J19BR]] gives a second proof.
It writes $V = Z(v_1; T) \oplus \cdots \oplus Z(v_r; T)$ with annihilators $d_1 \mid \cdots \mid d_r$, all nonconstant, and then $\chi_T = d_1 \cdots d_r$ and $m_T = d_r$.
So $m_T = \chi_T$ holds exactly when $r = 1$, that is, when $T$ is cyclic.
