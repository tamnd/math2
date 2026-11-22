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

We multiply one block matrix by another on both sides, compare the determinants of the two products, and then read off roots and eigenspaces.
In parts 1 and 2 all matrices have entries in the [[polynomial ring|0Q9EZS90GY]] $K[x]$, which is a commutative ring.

*Part 1.*

1. Define the $(m + n) \times (m + n)$ [[block matrices|0ASDFEQS6P]]
$$N = \begin{pmatrix} x I_m & A \\ B & I_n \end{pmatrix}, \qquad L = \begin{pmatrix} I_m & 0 \\ -B & x I_n \end{pmatrix}.$$
2. Block multiplication gives
$$NL = \begin{pmatrix} xI_m - AB & xA \\ B - B & x I_n \end{pmatrix} = \begin{pmatrix} xI_m - AB & xA \\ 0 & x I_n \end{pmatrix}.$$
3. Block multiplication in the other order gives
$$LN = \begin{pmatrix} xI_m & A \\ -xB + xB & -BA + xI_n \end{pmatrix} = \begin{pmatrix} xI_m & A \\ 0 & xI_n - BA \end{pmatrix}.$$
4. Both products are block upper triangular, so the [[determinant of a block triangular matrix|0J9TVTNB4K]] gives
$$\det(NL) = \det(xI_m - AB) \det(xI_n), \qquad \det(LN) = \det(xI_m) \det(xI_n - BA).$$
5. By the [[determinant of a triangular matrix|0K1KKMFHYH]], $\det(xI_k) = x^k$ for every $k$.
6. By the definition of the [[characteristic polynomial|039HF58KQ5]], steps 4 and 5 give $\det(NL) = x^n p_{AB}(x)$ and $\det(LN) = x^m p_{BA}(x)$.
7. The [[determinant is multiplicative|04CPJ6AF00]] over the commutative ring $K[x]$, and the two determinants commute as elements of $K[x]$, so
$$\det(NL) = \det N \det L = \det L \det N = \det(LN).$$
8. Steps 6 and 7 give $x^n p_{AB}(x) = x^m p_{BA}(x)$.

*Part 2.*

9. If $m = n$, step 8 reads $x^n p_{AB} = x^n p_{BA}$.
   The coefficient of $x^{n + k}$ on each side is the coefficient of $x^k$ in $p_{AB}$ and in $p_{BA}$, so the two polynomials have the same coefficients and $p_{AB} = p_{BA}$.

*Part 3.* Now $K = F$ is a field.

10. Let $\lambda \in F$ with $\lambda \ne 0$, and let $a \ge 0$ be the multiplicity of $\lambda$ as a root of $p_{AB}$.
    Write $p_{AB} = (x - \lambda)^a g$ with $g(\lambda) \ne 0$.
11. Then $x^n p_{AB} = (x - \lambda)^a \cdot x^n g$, and $\lambda^n g(\lambda) \ne 0$ because $\lambda \ne 0$.
    So $\lambda$ has multiplicity exactly $a$ as a root of $x^n p_{AB}$.
12. In the same way, the multiplicity of $\lambda$ in $x^m p_{BA}$ equals its multiplicity $b$ in $p_{BA}$.
13. By step 8 these two polynomials are equal, so $a = b$.
14. By the theorem that [[eigenvalues are the roots of the characteristic polynomial|053QVHF6N7]], $\lambda$ is an eigenvalue of $AB$ exactly when $a \ge 1$, and of $BA$ exactly when $b \ge 1$.
    By the definition of the [[algebraic multiplicity|0S7A0EMPF4]], $a$ and $b$ are the algebraic multiplicities, so they agree.

*Part 4.*

15. Let $\lambda \ne 0$, and let $v$ be in the [[eigenspace|0AYEPBQMAW]] $E_\lambda(AB)$.
    Then $(BA)(Bv) = B(ABv) = B(\lambda v) = \lambda\, Bv$, so $Bv \in E_\lambda(BA)$.
16. The map $v \mapsto Bv$ from $E_\lambda(AB)$ to $E_\lambda(BA)$ is linear.
    It is injective: if $Bv = 0$, then $\lambda v = ABv = A0 = 0$, and $\lambda \ne 0$ gives $v = 0$.
17. So $\dim E_\lambda(AB) \le \dim E_\lambda(BA)$.
    The same argument with $A$ and $B$ exchanged, using $v \mapsto Av$, gives the reverse inequality.
18. So the two dimensions are equal, and the injective linear map of step 16 between spaces of the same finite dimension is an isomorphism.

## Idea

Put $A$ and $B$ together into one block matrix $N$ of size $m + n$.
Multiplying $N$ by the simple matrix $L$ on the right gives a block triangular matrix with the block $xI_m - AB$, and multiplying on the left gives one with the block $xI_n - BA$.
The two products have the same determinant, because $\det N \det L = \det L \det N$ in a commutative ring.
Everything else is bookkeeping with powers of $x$.
For the eigenspaces, $B$ itself carries eigenvectors of $AB$ to eigenvectors of $BA$, and the condition $\lambda \ne 0$ stops it from sending one to zero.

## Variants

For $m = n$ over an infinite field there is a density argument.
If $A$ is invertible, then $BA = A^{-1}(AB)A$, so the two products are similar and have the same characteristic polynomial.
Each coefficient of $p_{AB} - p_{BA}$ is a polynomial in the entries of $A$ and $B$ that vanishes wherever $\det A \ne 0$, and a polynomial that vanishes off the zero set of the nonzero polynomial $\det A$ vanishes everywhere over an infinite field.

Over a field, part 4 alone already shows that $AB$ and $BA$ have the same nonzero eigenvalues, since it matches their eigenspaces.
It does not give the algebraic multiplicities, because an eigenspace can be smaller than the algebraic multiplicity; for those we need part 1.
