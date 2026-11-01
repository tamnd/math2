---
tag: ETSXVDDCYK
kind: definition
name: Canonical module
msc: [13H10, 13C14, 13D45]
defines: W5ECXPM6FW
uses: [N1QJQEGBFC, MZ02BKPHJA, NJ3APQ8BHH, 05QY1VEBYD, M2RADBFW99, 4P7GBWJ4RR, T6HCX959PJ, QCJN05GN64]
sources:
  - url: https://en.wikipedia.org/wiki/Dualizing_module
---

## Definition

Let $(R, \mathfrak{m}, k)$ be a [[Cohen–Macaulay|N1QJQEGBFC]] [[local ring|MZ02BKPHJA]] of dimension $d$ with [[residue field|NJ3APQ8BHH]] $k$.
A *canonical module* of $R$ is a [[finitely generated|05QY1VEBYD]] $R$-module $\omega_R$ such that:

1. $\omega_R$ is a maximal Cohen–Macaulay module, that is, $\operatorname{depth} \omega_R = d$, where $\operatorname{depth}$ is the [[depth|M2RADBFW99]];
2. $\omega_R$ has finite injective dimension;
3. $\dim_k \operatorname{Ext}^d_R(k, \omega_R) = 1$, where $\operatorname{Ext}$ is the [[Ext functor|4P7GBWJ4RR]].

## Remarks

A canonical module is unique up to isomorphism when it exists.
It exists if and only if $R$ is a quotient of a Gorenstein local ring; in particular every complete Cohen–Macaulay local ring has one.
Example: $R$ is [[Gorenstein|T6HCX959PJ]] if and only if $R$ itself is a canonical module; for instance $\omega_R = R$ for $R = K[\![x_1, \ldots, x_n]\!]$.
Example: for an Artinian local ring $R$, the canonical module is the [[injective hull|QCJN05GN64]] $E_R(k)$ of the residue field.
Non-example: for $R = K[x,y]/(x^2, xy, y^2)$ the module $R$ is not a canonical module, because $\operatorname{Hom}_R(k, R)$ is the socle $Kx \oplus Ky$, of dimension $2$, so clause 3 fails.
