---
tag: VGRDQ0QJN0
kind: proof
name: Proof that the determinant is multilinear in the rows
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
proves: 0PPG793642
methods: [41JZ39GE3F]
uses: [0C3CFHDN6R, 0443XNARDV]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: As an alternating multilinear form
---

## Proof

We turn the determinant into a function of row $i$ alone and read off the [[statement|0PPG793642]] from property 1 of the definition.

1. For $k \ne i$, let $r_k$ be row $k$ of $A$.
   By hypothesis, $r_k$ is also row $k$ of $B$ and of $C$.
2. By property 1 of the [[definition of the determinant|0C3CFHDN6R]], $\det$ is a [[multilinear function|0443XNARDV]] of the $n$ rows.
3. For a row $x \in K^n$, let $M(x)$ be the matrix with row $i$ equal to $x$ and row $k$ equal to $r_k$ for each $k \ne i$.
   Put $\varphi(x) = \det M(x)$.
4. The map $\varphi$ is linear, because it is $\det$ with all rows except row $i$ held fixed, and step 2 says exactly that this is linear.
   So $\varphi(sa + tb) = s \varphi(a) + t \varphi(b)$ for all rows $a, b$ and all $s, t \in K$.
5. By step 1, $M(a) = A$, $M(b) = B$ and $M(c) = C$.
   So $\varphi(a) = \det A$, $\varphi(b) = \det B$ and $\varphi(c) = \det C$.
6. Since $c = sa + tb$, steps 4 and 5 give
$$\det C = \varphi(sa + tb) = s \varphi(a) + t \varphi(b) = s \det A + t \det B.$$

This is the claim.

## Idea

The statement is property 1 of the definition, written out.
"Multilinear" means linear in each row while the other rows are held fixed.
The three matrices share every row except row $i$, so they are three values of one function of row $i$, and that function is linear.
The only work is to name that function, which is the map $\varphi$ of step 3.

## Variants

If the Leibniz sum is taken as the definition, the proof is a direct count.
Each product $a_{1 \sigma(1)} a_{2 \sigma(2)} \cdots a_{n \sigma(n)}$ contains exactly one entry of row $i$, namely $a_{i \sigma(i)}$.
So each term is a linear function of row $i$, and a sum of linear functions is linear.
The proof of the [[existence and uniqueness theorem|1C8RRWHD45]] uses the same count when it checks that the Leibniz sum is multilinear.
