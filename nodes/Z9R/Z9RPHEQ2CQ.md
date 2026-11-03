---
tag: Z9RPHEQ2CQ
kind: definition
name: Steinberg group
msc: [19C09, 19C20]
defines: 590VZSQ83X
uses: [0B1261B5ED, 5N139ECTM1, 0JGEQXQ4AC, 01REXW3WWE, E5JXB0E324, X9HEQ29Q49]
sources:
  - url: https://en.wikipedia.org/wiki/Steinberg_group_(K-theory)
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] with identity, and let $n \ge 3$.
The *Steinberg group* $St_n(R)$ is the group given by the following [[presentation|0JGEQXQ4AC]].
The generators are $x_{ij}(r)$, for $1 \le i, j \le n$ with $i \ne j$ and $r \in R$.
The defining relations are the [[Steinberg relations|5N139ECTM1]].
The map $x_{ij}(r) \mapsto x_{ij}(r)$ gives homomorphisms $St_n(R) \to St_{n+1}(R)$.
The *stable Steinberg group* $St(R)$ is the [[direct limit|X9HEQ29Q49]] of the groups $St_n(R)$ along these maps.

## Remarks

The [[elementary matrices|01REXW3WWE]] satisfy the Steinberg relations, so there is a unique homomorphism $\phi_n \colon St_n(R) \to GL_n(R)$ with $\phi_n(x_{ij}(r)) = e_{ij}(r)$.
Its image is the [[elementary subgroup|E5JXB0E324]] $E_n(R)$.
In the limit one gets $\phi \colon St(R) \to E(R)$, which is onto, and its kernel is $K_2(R)$.

Example: for $R = \Z$, the element $w = x_{12}(1) \, x_{21}(-1) \, x_{12}(1)$ of $St(\Z)$ maps to $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, a matrix of order $4$.
So $w^4$ lies in the kernel of $\phi$; it is the generator of $K_2(\Z) \cong \Z/2\Z$, so $w^4 \ne 1$ in $St(\Z)$.

Non-example: for $n = 2$ there are no three distinct indices, so only clause 1 of the Steinberg relations has content.
The same presentation then gives the free product of two copies of the additive group of $R$, with no relation between $x_{12}(r)$ and $x_{21}(s)$.
This is far from $E_2(R)$, which is why the definition takes $n \ge 3$.

Kervaire and Steinberg showed that $\phi \colon St(R) \to E(R)$ is a universal central extension, so $K_2(R)$ is the center of $St(R)$.
