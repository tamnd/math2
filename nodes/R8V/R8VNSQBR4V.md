---
tag: R8VNSQBR4V
kind: proof
name: Proof of the solutions for distinct real roots
msc: [34A30]
proves: 0HJ0HDA6W7
uses: [0QDXMG46QW, 0A6PGTTP2A, 0H4KNNCHPY, 0GK68PZ6KH, 096V7H13H9, 0EVHJFTG9Z, 0EX9GFJ0B3, 0RXX2PT1MQ, 0P9BNBW2W3, 0E8HNVBCSP, 0M0TKFRX2A]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_equation_(calculus)
    locator: Distinct real roots
---

## Proof

1. Let $r \in \R$ and $e_r(x) = e^{r x}$. By the [[chain rule|0RXX2PT1MQ]] and [[the derivative of the exponential|0EX9GFJ0B3]], $e_r' = r\, e_r$. By induction on $k$, $e_r^{(k)} = r^k e_r$ for each $k \ge 0$.
2. Write $L y = y^{(n)} + a_{n-1} y^{(n-1)} + \dots + a_0 y$. By step 1, $L e_r = \left(r^n + a_{n-1} r^{n-1} + \dots + a_0\right) e_r = p(r)\, e_r$, where $p$ is the [[characteristic polynomial|0QDXMG46QW]].
3. Since $p(r_k) = 0$, each $e_{r_k}$ is a solution of the [[homogeneous equation with constant coefficients|0A6PGTTP2A]] on $\R$.
4. Claim: if $s_1, \dots, s_k$ are distinct reals, $c_1, \dots, c_k \in \R$, and $\sum_j c_j e^{s_j x} = 0$ for all $x \in \R$, then all $c_j = 0$. We argue by induction on $k$.
5. For $k = 1$, $c_1 e^{s_1 x} = 0$ and [[$e^{s_1 x} > 0$|0P9BNBW2W3]], so $c_1 = 0$.
6. Let $k \ge 2$ and assume the claim for $k - 1$ exponents. Multiply the relation by $e^{-s_k x}$. By the [[exponential of a sum|0E8HNVBCSP]], $\sum_{j < k} c_j e^{(s_j - s_k) x} + c_k = 0$ for all $x$.
7. Differentiate, using step 1 and [[linearity of differentiation|0M0TKFRX2A]]: $\sum_{j < k} c_j (s_j - s_k)\, e^{(s_j - s_k) x} = 0$ for all $x$.
8. The numbers $s_j - s_k$ for $j < k$ are distinct. By the induction hypothesis, $c_j (s_j - s_k) = 0$, and $s_j \ne s_k$ gives $c_j = 0$ for $j < k$.
9. Then $c_k e^{s_k x} = 0$, so $c_k = 0$ by step 5. This proves the claim.
10. By step 4, $e^{r_1 x}, \dots, e^{r_n x}$ are [[linearly independent|0EVHJFTG9Z]] in the space $S$ of solutions on $\R$.
11. The constant coefficients are continuous on $\R$. By [[the dimension theorem|0GK68PZ6KH]], $S$ has dimension $n$.
12. By [[the basis criterion|096V7H13H9]], $n$ linearly independent vectors in $S$ form a basis. So $\left(e^{r_1 x}, \dots, e^{r_n x}\right)$ is a [[fundamental system|0H4KNNCHPY]].
13. Each solution is a combination of a basis, so it has the form $c_1 e^{r_1 x} + \dots + c_n e^{r_n x}$. Conversely each such combination lies in the vector space $S$.

## Idea

Each root $r$ gives a solution $e^{r x}$, because differentiating $e^{r x}$ multiplies it by $r$. Exponentials with different rates cannot cancel: dividing by one of them and differentiating removes it, and induction does the rest. Then $n$ independent solutions fill the $n$-dimensional solution space.
