---
tag: 2WW2DQYK7P
kind: proof
name: Proof that AB and BA have the same nonzero eigenvalues
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug2
proves: MCXV71BY74
methods: [XP5SDYKJX0, 0NTF6DMVAP]
uses: [0Q9EZS90GY, 039HF58KQ5, 0ASDFEQS6P, 04CPJ6AF00, 0J9TVTNB4K, 0K1KKMFHYH, 0S7A0EMPF4, 053QVHF6N7, 0AYEPBQMAW]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_polynomial
    locator: Characteristic polynomial of a product of two matrices
---

## Proof

All matrices in parts 1 and 2 have entries in the [[polynomial ring|0Q9EZS90GY]] $K[x]$, which is a commutative ring.

Part 1.

1. Define the $(m + n) \times (m + n)$ [[block matrices|0ASDFEQS6P]]
$$N = \begin{pmatrix} x I_m & A \\ B & I_n \end{pmatrix}, \qquad L = \begin{pmatrix} I_m & 0 \\ -B & x I_n \end{pmatrix}.$$
2. Block multiplication gives
$$NL = \begin{pmatrix} xI_m - AB & xA \\ B - B & x I_n \end{pmatrix} = \begin{pmatrix} xI_m - AB & xA \\ 0 & x I_n \end{pmatrix}.$$
3. Block multiplication gives
$$LN = \begin{pmatrix} xI_m & A \\ -xB + xB & -BA + xI_n \end{pmatrix} = \begin{pmatrix} xI_m & A \\ 0 & xI_n - BA \end{pmatrix}.$$
4. By the [[determinant of a block triangular matrix|0J9TVTNB4K]], $\det(NL) = \det(xI_m - AB) \det(xI_n)$ and $\det(LN) = \det(xI_m) \det(xI_n - BA)$.
5. By the [[determinant of a triangular matrix|0K1KKMFHYH]], $\det(xI_k) = x^k$ for every $k$.
6. By the definition of the [[characteristic polynomial|039HF58KQ5]], steps 4 and 5 give $\det(NL) = x^n p_{AB}(x)$ and $\det(LN) = x^m p_{BA}(x)$.
7. The [[determinant is multiplicative|04CPJ6AF00]] over the commutative ring $K[x]$. So $\det(NL) = \det N \det L = \det L \det N = \det(LN)$.
8. Steps 6 and 7 give $x^n p_{AB}(x) = x^m p_{BA}(x)$.

Part 2.

9. If $m = n$, step 8 reads $x^n p_{AB} = x^n p_{BA}$. Both sides are polynomials, and the coefficient of $x^{n + k}$ on each side is the coefficient of $x^k$ in $p_{AB}$ and in $p_{BA}$. So $p_{AB} = p_{BA}$.

Part 3.
Now $K = F$ is a field.

10. Let $\lambda \in F$ with $\lambda \ne 0$, and let $a$ be the multiplicity of $\lambda$ as a root of $p_{AB}$, with $a = 0$ if it is not a root. Write $p_{AB} = (x - \lambda)^a g$ with $g(\lambda) \ne 0$.
11. Then $x^n p_{AB} = (x - \lambda)^a \cdot x^n g$, and $\lambda^n g(\lambda) \ne 0$. So $\lambda$ has multiplicity exactly $a$ in $x^n p_{AB}$.
12. In the same way, the multiplicity of $\lambda$ in $x^m p_{BA}$ equals its multiplicity $b$ in $p_{BA}$.
13. By step 8, these two polynomials are equal, so $a = b$.
14. By the theorem that [[eigenvalues are the roots of the characteristic polynomial|053QVHF6N7]], $\lambda$ is an eigenvalue of $AB$ if and only if $a \ge 1$, and of $BA$ if and only if $b \ge 1$. By the definition of the [[algebraic multiplicity|0S7A0EMPF4]], $a$ and $b$ are the algebraic multiplicities.

Part 4.

15. Let $\lambda \ne 0$, and let $v \in E_\lambda(AB)$, the [[eigenspace|0AYEPBQMAW]] of $AB$. Then $BA(Bv) = B(ABv) = \lambda Bv$. So $Bv \in E_\lambda(BA)$.
16. The map $v \mapsto Bv$ from $E_\lambda(AB)$ to $E_\lambda(BA)$ is linear. It is injective: if $Bv = 0$, then $\lambda v = ABv = 0$, and $\lambda \ne 0$ gives $v = 0$.
17. So $\dim E_\lambda(AB) \le \dim E_\lambda(BA)$. Exchanging the roles of $A$ and $B$ gives the reverse inequality.
18. So the dimensions are equal, and the injective map of step 16 is an isomorphism.

## Idea

Put $A$ and $B$ into one block matrix $N$ of size $m + n$.
Multiplying $N$ by a simple matrix $L$ on the right and on the left produces two block triangular matrices.
One has the block $xI_m - AB$ and the other has the block $xI_n - BA$.
Both products have the same determinant, because determinants commute.
For the eigenspaces, the matrix $B$ carries eigenvectors of $AB$ to eigenvectors of $BA$.

## Variants

- For $m = n$ and $F$ infinite, a density argument works. If $A$ is invertible, then $BA = A^{-1}(AB)A$, so the two products are similar. Both sides of $p_{AB} = p_{BA}$ are polynomial in the entries of $A$, and $\det A \ne 0$ holds on a dense set.
- Over a field, part 3 also follows from part 4 for the existence of eigenvalues. Part 4 alone does not give the algebraic multiplicities.
