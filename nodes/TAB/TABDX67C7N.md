---
tag: TABDX67C7N
kind: proof
name: Proof of the block inverse formula by block elimination
msc: ["15A09"]
topics: [P8J6QR66TJ]
audience: ug2
proves: 5QTK7JWXF3
methods: [XP5SDYKJX0, TFQ1845T84, 0NTF6DMVAP]
uses: [01AXG9KZQF, 0ASDFEQS6P, CA1J41NWGS, 0TWTS88TWN, 0S4WTRE9GG]
sources:
  - url: https://en.wikipedia.org/wiki/Schur_complement
    locator: Background
---

## Proof

We check the block factorization by multiplying it out, invert its three factors, and read off parts 2 and 3 from the inverse of a product; part 4 is the same argument with the roles of $A$ and $D$ exchanged.

All products below are products of [[block matrices|01AXG9KZQF]] with compatible sizes, computed by block multiplication.
Write $E = \begin{pmatrix} I_p & 0 \\ CA^{-1} & I_q \end{pmatrix}$, $\Lambda = \begin{pmatrix} A & 0 \\ 0 & S \end{pmatrix}$ and $G = \begin{pmatrix} I_p & A^{-1}B \\ 0 & I_q \end{pmatrix}$.

**Part 1.**

1. $\Lambda G = \begin{pmatrix} A & AA^{-1}B \\ 0 & S \end{pmatrix} = \begin{pmatrix} A & B \\ 0 & S \end{pmatrix}$.
2. $E \Lambda G = \begin{pmatrix} A & B \\ CA^{-1}A & CA^{-1}B + S \end{pmatrix} = \begin{pmatrix} A & B \\ C & D \end{pmatrix} = M$, because $CA^{-1}B + S = D$ by the [[definition of $S$|CA1J41NWGS]].

**Inverses of the factors.**

3. $\begin{pmatrix} I_p & 0 \\ X & I_q \end{pmatrix}\begin{pmatrix} I_p & 0 \\ -X & I_q \end{pmatrix} = \begin{pmatrix} I_p & 0 \\ X - X & I_q \end{pmatrix} = I$, and the product in the other order is also $I$. So $E^{-1} = \begin{pmatrix} I_p & 0 \\ -CA^{-1} & I_q \end{pmatrix}$, by the [[definition of the inverse|0TWTS88TWN]].
4. In the same way, $G^{-1} = \begin{pmatrix} I_p & -A^{-1}B \\ 0 & I_q \end{pmatrix}$.

**Part 2.**

5. If $S$ is invertible, then $\Lambda$ is invertible with $\Lambda^{-1} = \operatorname{diag}(A^{-1}, S^{-1})$, by block multiplication. So $M = E \Lambda G$ is invertible, as a [[product of invertible matrices|0S4WTRE9GG]].
6. Conversely, let $M$ be invertible. Then $\Lambda = E^{-1} M G^{-1}$ is invertible, by the same rule.
7. Write $\Lambda^{-1} = \begin{pmatrix} W & X \\ Y & Z \end{pmatrix}$ in blocks of the same sizes. The lower right blocks of $\Lambda \Lambda^{-1} = I$ and $\Lambda^{-1} \Lambda = I$ give $SZ = I_q$ and $ZS = I_q$. So $S$ is invertible.

**Part 3.**

8. By part 1 and the rule for the inverse of a product, $M^{-1} = G^{-1} \Lambda^{-1} E^{-1}$.
9. $\Lambda^{-1} E^{-1} = \begin{pmatrix} A^{-1} & 0 \\ 0 & S^{-1} \end{pmatrix} \begin{pmatrix} I_p & 0 \\ -CA^{-1} & I_q \end{pmatrix} = \begin{pmatrix} A^{-1} & 0 \\ -S^{-1}CA^{-1} & S^{-1} \end{pmatrix}$.
10. $G^{-1}$ times this is $\begin{pmatrix} A^{-1} + A^{-1}BS^{-1}CA^{-1} & -A^{-1}BS^{-1} \\ -S^{-1}CA^{-1} & S^{-1} \end{pmatrix}$, because the first block row of $G^{-1}$ is $(I_p, -A^{-1}B)$ and the second is $(0, I_q)$.

**Part 4.**

11. Exchange the roles of the blocks: $M = \begin{pmatrix} I_p & BD^{-1} \\ 0 & I_q \end{pmatrix} \begin{pmatrix} T & 0 \\ 0 & D \end{pmatrix} \begin{pmatrix} I_p & 0 \\ D^{-1}C & I_q \end{pmatrix}$. Block multiplication checks this as in steps 1 and 2. The product of the last two factors is $\begin{pmatrix} T & 0 \\ C & D \end{pmatrix}$, and then the upper left block is $T + BD^{-1}C = A$.
12. The outer factors are unit block triangular, so they are invertible as in steps 3 and 4. As in steps 5 and 6, $M$ is invertible if and only if $\operatorname{diag}(T, D)$ is invertible. If $T$ is invertible, then $\operatorname{diag}(T^{-1}, D^{-1})$ is the inverse. Conversely, as in step 7, the upper left blocks of $\operatorname{diag}(T, D)\, Y = Y \operatorname{diag}(T, D) = I$ give $TW = WT = I_p$, where $W$ is the upper left block of $Y$.
13. Invert the three factors and multiply them in reverse order, as in steps 8 to 10. This gives the formula of part 4.

## Idea

Block elimination clears $C$ with a unit lower block triangular matrix and clears $B$ with a unit upper block triangular matrix.
What is left is $\operatorname{diag}(A, S)$, and the Schur complement appears because clearing $C$ subtracts $CA^{-1}B$ from $D$.
Unit block triangular matrices are inverted by changing the sign of the off diagonal block, just as $T_{ij}(c)^{-1} = T_{ij}(-c)$.
So the inverse of $M$ is a product of three easy inverses, and $M$ is invertible exactly when the middle factor is.

## Variants

One can also check part 3 directly, by multiplying $M$ with the proposed inverse and simplifying each of the four blocks with $D = S + CA^{-1}B$.
By the theorem on [[one-sided inverses|0753Y2X5K6]], one of the two products is enough.
