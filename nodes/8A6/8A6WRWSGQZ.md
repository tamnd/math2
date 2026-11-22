---
tag: 8A6WRWSGQZ
kind: proof
name: Proof of the invertibility criterion by the adjugate
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
proves: FBSAPTP1PR
methods: [01XM7JEKHY]
uses: [0528HKWZ1Z, 04CPJ6AF00, 0Z4BWARC38, 1ZK55FS2BF, 0ZZQ2E1MTE, 0EB9N0S33C]
sources:
  - url: https://en.wikipedia.org/wiki/Adjugate_matrix
    locator: Important consequence
---

## Proof

We get one direction from the product rule and the other by writing down an inverse with the adjugate.
Let $A$ be an $n \times n$ matrix over a field $F$, as in the [[theorem|FBSAPTP1PR]].

*Conditions 1 and 2.*

1. Assume that $A$ is [[invertible|0EB9N0S33C]], so $A A^{-1} = I_n$.
   By the [[product rule|04CPJ6AF00]],
$$\det A \cdot \det(A^{-1}) = \det(A A^{-1}) = \det I_n.$$
2. By the [[determinant of the identity|0Z4BWARC38]], $\det I_n = 1$.
   A factor of a product equal to $1$ cannot be $0$, so $\det A \neq 0$.
3. Conversely, assume that $\det A \neq 0$.
   By the [[adjugate identity|0528HKWZ1Z]],
$$A \operatorname{adj} A = (\operatorname{adj} A) A = (\det A) I_n.$$
4. Since $F$ is a field, $\det A$ has an inverse in $F$, and we put $B = (\det A)^{-1} \operatorname{adj} A$.
   Multiplying the identity of step 3 by $(\det A)^{-1}$ gives $AB = BA = I_n$.
   So $A$ is invertible, with inverse $B$.
5. Steps 1 to 4 prove that conditions 1 and 2 are equivalent.

*Conditions 1 and 3.*

6. By the [[criterion for invertibility by the reduced form|1ZK55FS2BF]], $A$ is invertible if and only if $Ax = 0$ has only the solution $x = 0$.
7. For the columns $c_1, \dots, c_n$ of $A$ we have $Ax = x_1 c_1 + \dots + x_n c_n$.
   So $Ax = 0$ has only $x = 0$ exactly when the columns are independent, and conditions 1 and 3 are equivalent.

*Conditions 2 and 4.*

8. The rows of $A$ are the columns of $A^{\mathsf{T}}$.
   By steps 1 to 7 for $A^{\mathsf{T}}$, they are independent if and only if $\det A^{\mathsf{T}} \neq 0$.
9. By the [[transpose rule|0ZZQ2E1MTE]], $\det A^{\mathsf{T}} = \det A$, so conditions 2 and 4 are equivalent.

Steps 5, 7 and 9 together prove that the four conditions are equivalent.

## Idea

If $A$ has an inverse, the product rule turns $A A^{-1} = I_n$ into $\det A \cdot \det A^{-1} = 1$, so $\det A$ cannot be $0$.
If $\det A$ is not $0$, the adjugate divided by $\det A$ is an explicit inverse, so nothing needs to be solved.
The two remaining conditions are about independence, and they reduce to the first two through the kernel and the transpose.

## Variants

Steps 1 to 4 divide only by $\det A$ and never by a pivot.
Over any commutative ring they therefore prove that $A$ is invertible if and only if $\det A$ is a unit, which is the [[criterion over commutative rings|03Q7RE2HXR]].
The [[proof by row reduction|EB3DSF9HPM]] needs a field, but it is the faster method in practice.
