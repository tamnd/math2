---
tag: Z4PGTJFGYE
kind: definition
name: Character of a representation
msc: [20C15]
defines: RMWMYBY8TC
uses: [WYGRXCG2RN, 0XC1RDBY7A, 0DEBXAJ5SA, 03GSZ8RTZJ]
sources:
  - url: https://en.wikipedia.org/wiki/Character_theory
---

## Definition

Let $G$ be a group and let $F$ be a field.
Let $\rho \colon G \to GL(V)$ be a [[representation|WYGRXCG2RN]] of $G$ on a vector space $V$ over $F$ of finite [[dimension|03GSZ8RTZJ]].
The *character* of $\rho$ is the function $\chi_\rho \colon G \to F$ given by
$$\chi_\rho(g) = \tr \rho(g),$$
where $\tr$ is the [[trace|0XC1RDBY7A]] of a linear map.
The degree of $\chi_\rho$ is $\dim V$.
When $F$ has characteristic $0$, the degree equals $\chi_\rho(1)$; in characteristic $p$ the value $\chi_\rho(1)$ is only $\dim V$ modulo $p$.
A character is irreducible if $\rho$ is [[irreducible|FX3NEFYFFN]].

## Remarks

Example: let $S_3$ act on $\C^3$ by permuting coordinates.
The matrix of a permutation $\sigma$ has a $1$ on the diagonal exactly at the points fixed by $\sigma$, so $\chi(\sigma)$ is the number of fixed points of $\sigma$.
This gives $\chi(1) = 3$, $\chi(\text{transposition}) = 1$ and $\chi(\text{3-cycle}) = 0$.
Non-example: let $\Z$ act by shifting on the space of finitely supported sequences.
This space has infinite dimension, so the trace is not defined, and the representation has no character.
Every character satisfies $\chi(hgh^{-1}) = \chi(g)$, so it is constant on each [[conjugacy class|0DEBXAJ5SA]]; such functions are called class functions.
Isomorphic representations have the same character.
For a finite group over $\C$, the converse holds as well.
