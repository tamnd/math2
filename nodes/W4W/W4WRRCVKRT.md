---
tag: W4WRRCVKRT
kind: proof
name: Proof that a one-sided inverse of a square matrix is two-sided
msc: [15A09]
proves: 0753Y2X5K6
uses: [0TWTS88TWN, 076JGP6R3T, 073E4XC016, 06DW9BAWB1, 0CCQV3884B, 0RXD6EZYBK, 0NRYHJPQG2, 02YFME3RGW, 0JB228DCWB, 0W4FSW1TVB, 0QK7FPE6VE, 0WGAXEK99E, 0V7ZD6P7RK, 0EPTJA5QV4]
sources:
  - url: https://en.wikipedia.org/wiki/Invertible_matrix
    locator: Properties
---

## Proof

We use the [[rank–nullity theorem|0W4FSW1TVB]] to build a right inverse, and then show that it equals $B$.

1. Assume $BA = I_n$, where $I_n$ is the [[identity matrix|06DW9BAWB1]]. Define $T \colon F^n \to F^n$ by $T(x) = Ax$, the [[matrix–vector product|0CCQV3884B]].
2. By [[distributivity|0RXD6EZYBK]], $A(x + y) = Ax + Ay$. Entry by entry, $A(cx) = c(Ax)$ for $c \in F$, since $F$ is commutative. So $T$ is a [[linear map|0NRYHJPQG2]].
3. Let $x \in \ker T$, the [[kernel|02YFME3RGW]] of $T$, so $Ax = 0$. View $x$ as an $n \times 1$ matrix. By [[associativity|073E4XC016]], $x = I_n x = (BA)x = B(Ax) = B0 = 0$.
4. So $\ker T = \set{0}$, and $\dim \ker T = 0$, since the empty family is a basis of $\set{0}$.
5. By the rank–nullity theorem and the [[dimension of the coordinate space|0QK7FPE6VE]], $\dim \im T = n - 0 = n$, where $\im T$ is the [[image|0JB228DCWB]] of $T$.
6. The image $\im T$ is a [[linear subspace|0EPTJA5QV4]] of $F^n$ of dimension $n = \dim F^n$. By [[a subspace of full dimension is the whole space|0WGAXEK99E]], $\im T = F^n$.
7. Let $e_1, \dots, e_n$ be the [[standard basis|0V7ZD6P7RK]] of $F^n$. By step 6, for each $j$ there is $c_j \in F^n$ with $A c_j = e_j$.
8. Let $C$ be the $n \times n$ matrix with columns $c_1, \dots, c_n$. By the definition of the [[product|076JGP6R3T]], column $j$ of $AC$ is $A c_j = e_j$.
9. Column $j$ of $I_n$ is also $e_j$. So $AC = I_n$.
10. By associativity, $B = B I_n = B(AC) = (BA)C = I_n C = C$.
11. By steps 9 and 10, $AB = AC = I_n$. Together with $BA = I_n$, this shows that $A$ is [[invertible|0TWTS88TWN]] with $A^{-1} = B$.
12. Now assume instead $AB = I_n$. Apply steps 1 to 11 to the pair $(B, A)$ in place of $(A, B)$. The hypothesis there reads $AB = I_n$, which holds.
13. Step 11 for this pair gives $BA = I_n$. So $AB = BA = I_n$. Hence $B$ is invertible with $B^{-1} = A$, and $A$ is invertible with $A^{-1} = B$.

## Idea

A left inverse forces $x \mapsto Ax$ to be injective. For a square matrix, rank–nullity turns injective into surjective, so $A$ also has a right inverse $C$. A left inverse and a right inverse of the same matrix are always equal, because $B = B(AC) = (BA)C = C$.
