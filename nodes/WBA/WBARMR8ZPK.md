---
tag: WBARMR8ZPK
kind: proof
name: Proof that the eigenvalues are the roots of the characteristic polynomial
msc: [15A18]
proves: 053QVHF6N7
uses: [0ZND7NQ970, 0BZ81AJNWF, 039HF58KQ5, 0YYMY95FWS, 016PE4VZ8Q, 0125QVNCFQ, 0BJBYCGMWE, 02YFME3RGW, 0912EEEVCT, 059THXBRBB, 05Q1B7MH0M, 03Q7RE2HXR, 0TWTS88TWN, 0TYMASG33Y]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_polynomial
    locator: Motivation
---

## Proof

We show that both conditions say that the map $\lambda \id_V - T$ is not injective.

1. Let $n = \dim V$. The [[characteristic polynomial of $T$|0BZ81AJNWF]] needs $n \ge 1$, so let $n \ge 1$. Fix a basis $B = (b_1, \dots, b_n)$ of $V$.
2. Let $A = [T]_B$ be the [[matrix of $T$|0YYMY95FWS]]. By the definition and the [[invariance under change of basis|0TYMASG33Y]], $p_T(t) = p_A(t) = \det(t I_n - A)$.
3. Let $S = \lambda \id_V - T$ and $M = \lambda I_n - A$. Since $S(b_j) = \lambda b_j - T(b_j)$, column $j$ of $[S]_B$ is column $j$ of $M$. So $[S]_B = M$.
4. Let $\operatorname{ev}_\lambda \colon F[t] \to F$ be the [[evaluation homomorphism|0125QVNCFQ]] at $\lambda$. It maps each entry of $t I_n - A$ to the same entry of $M$.
5. By the [[Leibniz formula|016PE4VZ8Q]], $p_A(t)$ is a sum of products of entries of $t I_n - A$, with signs $\pm 1$.
6. A ring homomorphism preserves sums, products and signs. So by step 5 and the Leibniz formula for $M$, $p_T(\lambda) = \operatorname{ev}_\lambda(p_A) = \det M$.
7. By the definition of an [[eigenvalue|0ZND7NQ970]], $\lambda$ is an eigenvalue of $T$ if and only if $S(v) = 0$ for some $v \ne 0$.
8. So $\lambda$ is an eigenvalue if and only if the [[kernel|02YFME3RGW]] of $S$ is not $\set{0}$. By the [[kernel criterion|0BJBYCGMWE]], this holds if and only if $S$ is not injective.
9. Suppose $S$ is not injective. Take $v \ne 0$ with $S(v) = 0$, and suppose that $M$ is [[invertible|0TWTS88TWN]] with inverse $N$.
10. By the definition of the matrix of a linear map, $[S(v)]_B = M [v]_B$. So $[v]_B = N M [v]_B = N [S(v)]_B = 0$.
11. The map $v \mapsto [v]_B$ is injective, by the [[isomorphism with the coordinate space|059THXBRBB]]. So $v = 0$, which contradicts step 9. Hence $M$ is not invertible.
12. By the [[determinant criterion for invertibility|03Q7RE2HXR]] over a field, $\det M = 0$.
13. Now suppose $S$ is injective. Since $V$ is finite-dimensional, $S$ is [[bijective|0912EEEVCT]]. Let $R \colon V \to V$ be its inverse map.
14. The map $R$ is linear: for $u, w \in V$ and $a, c \in F$, $S(a R(u) + c R(w)) = a u + c w$. Applying $R$ gives $a R(u) + c R(w) = R(a u + c w)$.
15. The matrix of $\id_V$ in $B$ is $I_n$, since $\id_V(b_j) = b_j$. By the rule for the [[matrix of a composition|05Q1B7MH0M]], $M [R]_B = [S \circ R]_B = I_n$ and $[R]_B M = [R \circ S]_B = I_n$.
16. So $M$ is invertible. By the determinant criterion, $\det M$ is a unit of $F$, so $\det M \ne 0$.
17. By steps 8, 12 and 16, $\lambda$ is an eigenvalue of $T$ if and only if $\det M = 0$.
18. By step 6, this holds if and only if $p_T(\lambda) = 0$.

## Idea

The scalar $\lambda$ is an eigenvalue exactly when $\lambda \id_V - T$ kills a nonzero vector. In finite dimensions this happens exactly when the matrix $\lambda I - A$ is not invertible, that is, when its determinant is $0$. That determinant is the characteristic polynomial evaluated at $\lambda$.
