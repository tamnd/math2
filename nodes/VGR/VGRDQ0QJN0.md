---
tag: VGRDQ0QJN0
kind: proof
name: Proof that the determinant is multilinear in the rows
msc: [15A15]
proves: 0PPG793642
uses: [0C3CFHDN6R, 0443XNARDV]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: As an alternating multilinear form
---

## Proof

1. Let $r_k$ be row $k$ of $A$ for $k \ne i$. By hypothesis, $r_k$ is also row $k$ of $B$ and of $C$.
2. By property 1 of the [[definition of the determinant|0C3CFHDN6R]], $\det$ is a [[multilinear function|0443XNARDV]] of the $n$ rows.
3. For a row $x \in K^n$, let $M(x)$ have row $i$ equal to $x$ and row $k$ equal to $r_k$ for $k \ne i$. Put $\varphi(x) = \det M(x)$. By step 2, $\varphi$ is linear.
4. Linearity of $\varphi$ means $\varphi(sa + tb) = s \varphi(a) + t \varphi(b)$ for all rows $a, b$ and all $s, t \in K$.
5. By step 1, $\varphi(a) = \det A$, $\varphi(b) = \det B$ and $\varphi(c) = \det C$.
6. Since $c = sa + tb$, step 4 gives $\det C = \varphi(sa + tb) = s \det A + t \det B$.

## Idea

This is property 1 of the definition, unpacked. Multilinear means linear in each row when the other rows are held fixed. The three matrices share all rows except row $i$, so linearity in row $i$ is exactly the claim.
