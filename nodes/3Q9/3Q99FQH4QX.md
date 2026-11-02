---
tag: 3Q99FQH4QX
kind: definition
name: Quasitriangular Hopf algebra
msc: [16T05, 16T25, 81R50]
defines: NCRPWS9W5R
uses: [7XFYP0N84H, 0BF2DE2SYK]
sources:
  - url: https://en.wikipedia.org/wiki/Quasitriangular_Hopf_algebra
---

## Definition

Let $k$ be a field and let $H$ be a [[Hopf algebra|7XFYP0N84H]] over $k$ with coproduct $\Delta$.
Let $\tau \colon H \otimes H \to H \otimes H$ be the flip $a \otimes b \mapsto b \otimes a$, and let $\Delta^{\mathrm{op}} = \tau \circ \Delta$.
For $R = \sum_i a_i \otimes b_i$ in the [[tensor product|0BF2DE2SYK]] $H \otimes H$, put $R_{12} = \sum_i a_i \otimes b_i \otimes 1$, $R_{13} = \sum_i a_i \otimes 1 \otimes b_i$ and $R_{23} = \sum_i 1 \otimes a_i \otimes b_i$.
The pair $(H, R)$ is a *quasitriangular Hopf algebra* if $R$ is invertible in $H \otimes H$ and:

1. $R \, \Delta(x) \, R^{-1} = \Delta^{\mathrm{op}}(x)$ for all $x \in H$.
2. $(\Delta \otimes \id)(R) = R_{13} R_{23}$.
3. $(\id \otimes \Delta)(R) = R_{13} R_{12}$.

The element $R$ is the *universal R-matrix*.

## Remarks

Example: let $H = k[G]$ be the group algebra of a group $G$, with $\Delta(g) = g \otimes g$, and let $R = 1 \otimes 1$.
Then $\Delta^{\mathrm{op}} = \Delta$, so clause 1 holds, and both sides of clauses 2 and 3 equal $1 \otimes 1 \otimes 1$.
Non-example: let $G$ be a finite non-abelian group and let $H = k^G$ be the dual Hopf algebra of functions on $G$.
Since $k^G$ is commutative, $R \, \Delta(x) \, R^{-1} = \Delta(x)$ for every invertible $R$, so clause 1 would force $\Delta = \Delta^{\mathrm{op}}$.
This fails because $k^G$ is not cocommutative, so no $R$ makes $k^G$ quasitriangular.
The axioms imply $(\varepsilon \otimes \id)(R) = 1 = (\id \otimes \varepsilon)(R)$ for the counit $\varepsilon$.
They also imply the Yang–Baxter equation $R_{12} R_{13} R_{23} = R_{23} R_{13} R_{12}$.
A *triangular* Hopf algebra is a quasitriangular one with $R_{21} R = 1$, where $R_{21} = \tau(R)$.
