---
tag: Z49V0FSFKR
kind: definition
name: L-theory
msc: [19G24, 57R67, 19J25]
defines: P5CRN7BZV0
uses: [7W52X4N3NJ, BFFA03GE3V, 0RBQS1JJCR]
sources:
  - url: https://en.wikipedia.org/wiki/L-theory
---

## Definition

Let $R$ be a [[ring with involution|7W52X4N3NJ]] $a \mapsto \bar a$ and let $\varepsilon \in \set{1, -1}$.
For a finitely generated free right $R$-module $M$, let $M^* = \Hom_R(M, R)$, made a right module by the involution.
For $\psi \colon M \to M^*$ let $\psi^* \colon M \to M^*$ be its dual, using $M^{**} \cong M$.
An *$\varepsilon$-quadratic form* is a pair $(M, \psi)$ with $\psi$ taken modulo maps of the form $\chi - \varepsilon \chi^*$.
It is *nonsingular* if $\lambda = \psi + \varepsilon \psi^* \colon M \to M^*$ is an isomorphism.
The *hyperbolic form* $H_\varepsilon(N)$ on $N \oplus N^*$ is given by $\psi(x, f)(y, g) = f(y)$.
Let $k \ge 0$.
The group $L_{2k}(R)$ is the set of nonsingular $(-1)^k$-quadratic forms on free modules modulo the relation below, with orthogonal sum.
$(M, \psi) \sim (M', \psi')$ if $(M, \psi) \oplus H_{(-1)^k}(N) \cong (M', \psi') \oplus H_{(-1)^k}(N')$ for some free modules $N, N'$.
The odd groups $L_{2k+1}(R)$ are defined in the same spirit from nonsingular $(-1)^k$-quadratic formations, or from automorphisms of hyperbolic forms.
The groups are $4$-periodic: $L_{n+4}(R) = L_n(R)$.

## Remarks

The groups in this definition are often written $L^h_n(R)$; using projective modules gives $L^p_n(R)$, and using based modules with simple isomorphisms gives $L^s_n(R)$.
For $R = \Z$ all versions agree, and $L_n(\Z) \cong \Z, 0, \Z/2, 0$ for $n \equiv 0, 1, 2, 3 \pmod 4$.
Example: the $E_8$ form is an even unimodular symmetric form on $\Z^8$ of signature $8$, and it is the symmetrization of a quadratic form; its class generates $L_0(\Z)$.
Non-example: the form $x^2$ on $\Z$ is not the symmetrization $\psi + \psi^*$ of any quadratic form, since such a symmetrization takes only even values $\lambda(x, x) = 2\psi(x)(x)$.
Ranicki defined L-groups in all degrees as cobordism groups of chain complexes with quadratic Poincaré duality, and also symmetric L-groups $L^n(R)$.
