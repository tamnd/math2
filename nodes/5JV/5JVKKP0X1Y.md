---
tag: 5JVKKP0X1Y
kind: definition
name: Sheaf of modules
msc: [14F06]
defines: S33B2H3MYD
uses: [KNDXDE7K8M, TB6TM6R4MD, 0NZ8JA25WK, 082GHNPJ53]
sources:
  - url: https://en.wikipedia.org/wiki/Sheaf_of_modules
---

## Definition

Let $(X, \mathcal{O}_X)$ be a [[ringed space|KNDXDE7K8M]].
A *sheaf of $\mathcal{O}_X$-modules* is a [[sheaf|TB6TM6R4MD]] $\mathcal{F}$ of [[abelian groups|082GHNPJ53]] on $X$ with the following data and condition.

1. For each open set $U \subseteq X$, $\mathcal{F}(U)$ is a [[module|0NZ8JA25WK]] over the ring $\mathcal{O}_X(U)$.
2. For open sets $V \subseteq U$, all $a \in \mathcal{O}_X(U)$ and all $s \in \mathcal{F}(U)$, one has $(a s)|_V = (a|_V)(s|_V)$.

A morphism of $\mathcal{O}_X$-modules is a morphism of sheaves $\varphi \colon \mathcal{F} \to \mathcal{G}$ such that each $\varphi_U$ is $\mathcal{O}_X(U)$-linear.

## Remarks

The structure sheaf $\mathcal{O}_X$ is a sheaf of $\mathcal{O}_X$-modules, with each $\mathcal{O}_X(U)$ acting on itself by multiplication.
Condition 2 holds because restriction maps of $\mathcal{O}_X$ are ring homomorphisms.
On $X = \operatorname{Spec} \Z$, the constant sheaf $\underline{\Z}$ admits no structure of $\mathcal{O}_X$-module.
Its sections over $D(2)$ form the group $\Z$, and clause 1 would need a module structure over $\mathcal{O}_X(D(2)) = \Z[1/2]$.
This is impossible, since multiplication by $2$ is not invertible on $\Z$.
For each point $x \in X$, the stalk $\mathcal{F}_x$ is a module over the local ring $\mathcal{O}_{X,x}$.
The $\mathcal{O}_X$-modules form an abelian category, with tensor products $\mathcal{F} \otimes_{\mathcal{O}_X} \mathcal{G}$ and sheaves of homomorphisms.
