---
tag: B2GEEB0VT2
kind: definition
name: Differential graded Lie algebra
msc: [17B70, 17B55, 55P62]
defines: D5XH66A8RP
uses: [04C5ZBG1WT, 000AYPA9AJ, WQ82C0M3QB, 5JJYBJ6A8K]
sources:
  - url: https://en.wikipedia.org/wiki/Differential_graded_Lie_algebra
---

## Definition

Let $F$ be a [[field|04C5ZBG1WT]] of characteristic $0$.
Let $L = \bigoplus_{i \in \Z} L^i$ be a $\Z$-graded [[vector space|000AYPA9AJ]] over $F$, and write $\abs{x} = i$ when $x \in L^i$ is homogeneous.
A *differential graded Lie algebra* structure on $L$ is a pair $([\cdot, \cdot], d)$.
Here $[\cdot, \cdot] \colon L \times L \to L$ is bilinear and $d \colon L \to L$ is linear.
The conditions are, for all homogeneous $x, y, z \in L$:

1. $[L^i, L^j] \subseteq L^{i + j}$ for all $i, j$;
2. $[x, y] = -(-1)^{\abs{x}\abs{y}} [y, x]$;
3. $[x, [y, z]\,] = [\,[x, y], z] + (-1)^{\abs{x}\abs{y}} [y, [x, z]\,]$;
4. $d(L^i) \subseteq L^{i + 1}$ for all $i$, and $d \circ d = 0$;
5. $d[x, y] = [dx, y] + (-1)^{\abs{x}} [x, dy]$.

## Remarks

Example: a [[Lie algebra|5JJYBJ6A8K]] $\mathfrak{g}$ placed in degree $0$, with $L^i = 0$ for $i \ne 0$ and $d = 0$.
All signs are $+1$, so clauses 2 and 3 become antisymmetry and the Jacobi identity, and clauses 4 and 5 hold because both sides are $0$.

Example: for a smooth manifold $M$ and a Lie algebra $\mathfrak{g}$, the forms $\Omega^\bullet(M) \otimes \mathfrak{g}$ with $[\alpha \otimes a, \beta \otimes b] = (\alpha \wedge \beta) \otimes [a, b]$ and $d$ the exterior derivative form a differential graded Lie algebra.

Non-example: take $L = L^0 = \mathfrak{g}$ as above, but with $d = \id$.
This fails clause 4, because $d$ does not raise the degree and $d \circ d = \id \ne 0$ when $\mathfrak{g} \ne 0$.

By clause 4, $(L, d)$ is a cochain complex, and by clause 5 its cohomology $H(L)$ inherits a graded Lie bracket.
Some authors use a lower grading in which $d$ lowers the degree by one.
