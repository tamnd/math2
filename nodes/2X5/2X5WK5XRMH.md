---
tag: 2X5WK5XRMH
kind: proof
name: Proof of the existence, uniqueness and least-squares property of the pseudoinverse
msc: [15A09, 15A18]
topics: [SS4EVPKT3A]
audience: ug2
proves: Q9YN0F60ZW
methods: [01XM7JEKHY, GQHHNV79PA, 0NTF6DMVAP]
uses: [0PSRCMCM5X, 000NPTMX6J, 0AR68JTMDT, 09GK5PS824, 0Q8HZTJC7G]
sources:
  - url: https://en.wikipedia.org/wiki/Moore–Penrose_inverse
    locator: Existence and uniqueness
  - url: https://en.wikipedia.org/wiki/Moore–Penrose_inverse
    locator: Linear least-squares
---

## Proof

We check the four conditions for $V \Sigma^+ U^*$ with diagonal products, prove uniqueness from the four equations alone, and then solve the least-squares problem in the singular bases.

By the [[singular value decomposition|000NPTMX6J]], $A = U \Sigma V^*$ with $U$ and $V$ [[unitary|0AR68JTMDT]], so $U^* U = U U^* = I_m$ and $V^* V = V V^* = I_n$.
The diagonal entries of $\Sigma$ are $\sigma_i > 0$ for $i \le r$ and $0$ for $i > r$, and all other entries are $0$.
Let $X = V \Sigma^+ U^*$.

*Part 1, existence.*

1. Let $E_m = \Sigma \Sigma^+$ and $E_n = \Sigma^+ \Sigma$. Both factors have nonzero entries only in positions $(i, i)$ with $i \le r$, so $E_m$ is the $m \times m$ diagonal matrix with entry $\sigma_i \cdot \sigma_i^{-1} = 1$ for $i \le r$ and $0$ otherwise, and $E_n$ is the $n \times n$ matrix of the same form.
2. The nonzero entries of $\Sigma$ lie in rows $1$ to $r$, where $E_m$ acts as the identity, so $E_m \Sigma = \Sigma$. In the same way $E_n \Sigma^+ = \Sigma^+$.
3. Using $V^* V = I_n$ and $U^* U = I_m$, we get
$$A X = U \Sigma V^* V \Sigma^+ U^* = U E_m U^*, \qquad X A = V \Sigma^+ U^* U \Sigma V^* = V E_n V^*.$$
4. Condition 1 follows from steps 3 and 2: $A X A = U E_m U^* U \Sigma V^* = U E_m \Sigma V^* = U \Sigma V^* = A$.
5. Condition 2 follows in the same way: $X A X = V E_n V^* V \Sigma^+ U^* = V E_n \Sigma^+ U^* = V \Sigma^+ U^* = X$.
6. For conditions 3 and 4, the rule $(Y Z W)^* = W^* Z^* Y^*$ from the [[transpose of a product|09GK5PS824]] gives $(U E_m U^*)^* = U E_m^* U^*$. Since $E_m$ is real and diagonal, $E_m^* = E_m$, so $A X$ is Hermitian, and the same computation shows that $X A = V E_n V^*$ is Hermitian.

*Part 2, uniqueness.*

7. Let $X$ and $Y$ both satisfy the four conditions. Conditions 1 and 3 for $Y$ give $A^* = (A Y A)^* = A^* (A Y)^* = A^* A Y$.
8. Conditions 1 and 4 for $X$ give $A^* = (A X A)^* = (X A)^* A^* = X A A^*$.
9. Conditions 2 and 3 for $X$, and then step 7, give $X = X A X = X (A X)^* = X X^* A^* = X X^* A^* A Y$.
10. Condition 3 for $X$ gives $X^* A^* = (A X)^* = A X$, so step 9 becomes $X = X A X A Y$, and condition 2 turns this into $X = X A Y$.
11. Conditions 2 and 4 for $Y$, and then step 8, give $Y = Y A Y = (Y A)^* Y = A^* Y^* Y = X A A^* Y^* Y$.
12. Condition 4 for $Y$ gives $A^* Y^* = (Y A)^* = Y A$, so step 11 becomes $Y = X A Y A Y$, and condition 2 for $Y$ turns this into $Y = X A Y$.
13. Steps 10 and 12 give $X = X A Y = Y$. So at most one matrix satisfies the conditions, and by part 1 it is $V \Sigma^+ U^*$ for every SVD of $A$.

*Part 3, projections.*

14. Write $E_m = \sum_{i \le r} e_i e_i^{\mathsf{T}}$ with the standard basis vectors $e_i$. Since $U e_i = u_i$, step 3 gives $A A^+ = \sum_{i \le r} u_i u_i^*$, and in the same way $A^+ A = \sum_{i \le r} v_i v_i^*$.
15. Let $y \in \C^m$ and $p = \sum_{i \le r} (u_i^* y) u_i = A A^+ y$. The vectors $u_1, \dots, u_r$ are an orthonormal basis of the column space of $A$ by the SVD theorem, so $p$ lies in the column space.
16. For $j \le r$, orthonormality gives $u_j^* (y - p) = u_j^* y - u_j^* y = 0$. So $y - p$ is orthogonal to the column space, and $p$ is the [[orthogonal projection|0Q8HZTJC7G]] of $y$ onto it. The same argument with the orthonormal basis $v_1, \dots, v_r$ of the column space of $A^*$ handles $A^+ A$.

*Part 4, least squares.*

17. A unitary matrix keeps lengths: $\norm{U z}^2 = z^* U^* U z = \norm{z}^2$ for every $z$, and the same holds for $U^*$, $V$ and $V^*$.
18. Let $x \in \C^n$, $y = V^* x$ and $c = U^* b$. Since $U U^* = I_m$ and $x = V y$, we have $Ax - b = U(\Sigma y - c)$, so step 17 gives $\norm{Ax - b} = \norm{\Sigma y - c}$ and $\norm{x} = \norm{y}$.
19. The entries of $\Sigma y$ are $\sigma_i y_i$ for $i \le r$ and $0$ for $i > r$, so
$$\norm{\Sigma y - c}^2 = \sum_{i=1}^r \abs{\sigma_i y_i - c_i}^2 + \sum_{i=r+1}^m \abs{c_i}^2.$$
20. The second sum does not depend on $x$, and the first sum is at least $0$ with equality exactly when $y_i = c_i / \sigma_i$ for all $i \le r$. So $x$ minimizes $\norm{Ax - b}$ if and only if this holds, and $y_{r+1}, \dots, y_n$ are free.
21. For a minimizer, step 18 gives $\norm{x}^2 = \norm{y}^2 = \sum_{i \le r} \abs{c_i / \sigma_i}^2 + \sum_{i > r} \abs{y_i}^2$, which is smallest exactly when $y_i = 0$ for all $i > r$.
22. So exactly one minimizer has least norm, the one with $y = \Sigma^+ c$, and it is $x = V \Sigma^+ U^* b = A^+ b$ by step 13.

*Part 5, reality.*

23. If $A$ is real, the SVD theorem gives real orthogonal $U$ and $V$. Then $V$, $\Sigma^+$ and $U^* = U^{\mathsf{T}}$ are real, so $A^+ = V \Sigma^+ U^{\mathsf{T}}$ is real.

This proves all five parts of the theorem.

## Idea

In the singular bases, $A$ becomes the diagonal matrix $\Sigma$, and the natural inverse of a diagonal matrix inverts its nonzero entries and keeps its zeros.
Then each Penrose condition is a product of diagonal matrices, which we can read off.
Uniqueness is a different kind of argument: we never look inside the matrices, and we only push the four equations and the rule $(XY)^* = Y^* X^*$ around until both candidates equal $X A Y$.
For least squares, the unitary changes of coordinates keep every length, so the problem splits into one scalar problem $\sigma_i y_i \approx c_i$ for each coordinate, and the coordinates that $A$ kills are set to zero.

## Variants

Existence can also come from a rank factorization $A = F G$, where $F$ is $m \times r$ with independent columns and $G$ is $r \times n$ with independent rows.
Then $F^* F$ and $G G^*$ are invertible, and the matrix $G^* (G G^*)^{-1} (F^* F)^{-1} F^*$ satisfies the four conditions, which one checks by direct multiplication.

Part 4 also follows from the normal equations.
The least-squares solutions form a set $x_0 + \operatorname{Nul}(A)$, and the shortest of them is the one that lies in the column space of $A^*$, as in the [[minimum-norm solution theorem|QM2Y84VDX8]].
