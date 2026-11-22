---
tag: WBARMR8ZPK
kind: proof
name: Proof that the eigenvalues are the roots of the characteristic polynomial
msc: ["15A18"]
topics: [6R1D6QPY3S]
audience: ug1
proves: 053QVHF6N7
methods: [0NTF6DMVAP, TFQ1845T84, 0J0XBKG64S]
uses: [0ZND7NQ970, 0BZ81AJNWF, 039HF58KQ5, 0YYMY95FWS, 016PE4VZ8Q, 0125QVNCFQ, 0BJBYCGMWE, 02YFME3RGW, 0912EEEVCT, 059THXBRBB, 05Q1B7MH0M, 03Q7RE2HXR, 0TWTS88TWN, 0TYMASG33Y, 0KJVQV3E0F]
sources:
  - url: https://en.wikipedia.org/wiki/Characteristic_polynomial
    locator: Motivation
---

## Proof

We show that both conditions of part 1 say that the map $\lambda \id_V - T$ is not injective, and then part 2 follows from the bound on the number of roots of a polynomial.

*Setting up.*

1. Let $n = \dim V \ge 1$ and fix a basis $B = (b_1, \dots, b_n)$ of $V$.
   Let $A = [T]_B$ be the [[matrix of T|0YYMY95FWS]].
   By the [[definition|0BZ81AJNWF]] and the [[invariance under change of basis|0TYMASG33Y]], $p_T(t) = p_A(t) = \det(t I_n - A)$.
2. Let $S = \lambda \id_V - T$ and $M = \lambda I_n - A$.
   Since $S(b_j) = \lambda b_j - T(b_j)$, column $j$ of $[S]_B$ is column $j$ of $M$, so $[S]_B = M$.

*The value of the polynomial at $\lambda$.*

3. Let $\operatorname{ev}_\lambda \colon F[t] \to F$ be the [[evaluation homomorphism|0125QVNCFQ]] at $\lambda$.
   It maps each entry of $t I_n - A$ to the entry of $M$ in the same place.
4. By the [[Leibniz formula|016PE4VZ8Q]], $p_A(t)$ is a sum of products of entries of $t I_n - A$, with signs $\pm 1$.
5. A ring homomorphism keeps sums, products and the signs $\pm 1$.
   So by step 4 and the Leibniz formula for $M$, $p_T(\lambda) = \operatorname{ev}_\lambda(p_A) = \det M$.

*Eigenvalues and injectivity.*

6. By the definition of an [[eigenvalue|0ZND7NQ970]], $\lambda$ is an eigenvalue of $T$ if and only if $S(v) = 0$ for some $v \ne 0$.
7. That is, $\lambda$ is an eigenvalue if and only if the [[kernel|02YFME3RGW]] of $S$ is not $\{0\}$.
   By the [[kernel criterion|0BJBYCGMWE]], this holds if and only if $S$ is not injective.

*If $S$ is not injective, then $\det M = 0$.*

8. Take $v \ne 0$ with $S(v) = 0$, and suppose that $M$ is [[invertible|0TWTS88TWN]] with inverse $N$.
9. By the definition of the matrix of a linear map, $[S(v)]_B = M [v]_B$, so
$$[v]_B = N M [v]_B = N [S(v)]_B = N \cdot 0 = 0.$$
10. The map $v \mapsto [v]_B$ is injective, by the [[isomorphism with the coordinate space|059THXBRBB]], so $v = 0$.
    This contradicts the choice of $v$, so $M$ is not invertible.
11. By the [[determinant criterion for invertibility|03Q7RE2HXR]] over a field, $\det M = 0$.

*If $S$ is injective, then $\det M \ne 0$.*

12. Since $V$ has finite dimension, an injective endomorphism is [[bijective|0912EEEVCT]].
    Let $R \colon V \to V$ be the inverse map of $S$.
13. The map $R$ is linear.
    For $u, w \in V$ and $a, c \in F$, linearity of $S$ gives $S(a R(u) + c R(w)) = a u + c w$, and applying $R$ gives $a R(u) + c R(w) = R(a u + c w)$.
14. The matrix of $\id_V$ in $B$ is $I_n$.
    By the rule for the [[matrix of a composition|05Q1B7MH0M]], $M [R]_B = [S \circ R]_B = I_n$ and $[R]_B M = [R \circ S]_B = I_n$.
15. So $M$ is invertible, and by the determinant criterion $\det M$ is a unit of $F$, so $\det M \ne 0$.

*Conclusion of part 1.*

16. By steps 7, 11 and 15, $\lambda$ is an eigenvalue of $T$ if and only if $\det M = 0$.
    By step 5, this holds if and only if $p_T(\lambda) = 0$.

*Part 2.*

17. By the definition of the [[characteristic polynomial|039HF58KQ5]], $p_T = p_A$ is monic of degree $n$, so $p_T \ne 0$.
18. A nonzero polynomial over a field has at most as many roots as its degree, by the [[root bound|0KJVQV3E0F]].
    So $p_T$ has at most $n$ roots in $F$.
19. By part 1, the eigenvalues of $T$ are exactly the roots of $p_T$ in $F$, so $T$ has at most $n$ eigenvalues.

The matrix form follows by applying parts 1 and 2 to the map $x \mapsto Ax$ on $F^n$, whose matrix in the standard basis is $A$.

## Idea

The scalar $\lambda$ is an eigenvalue exactly when $\lambda \id_V - T$ sends some nonzero vector to $0$.
In finite dimension this happens exactly when the matrix $\lambda I - A$ is not invertible, and a square matrix over a field is not invertible exactly when its determinant is $0$.
That determinant is the characteristic polynomial evaluated at $\lambda$, which is the content of step 5.
The bound on the number of eigenvalues then comes from the bound on the number of roots of a polynomial.

## Variants

Part 2 has a proof without determinants.
Eigenvectors for distinct eigenvalues are [[linearly independent|0HNMFG8F8K]], and an independent list in $V$ has at most $n$ vectors, so there are at most $n$ distinct eigenvalues.
Many textbooks skip step 5 for matrices and simply put $t = \lambda$ into $\det(tI - A)$.
That move is correct, but its justification is that evaluation at $\lambda$ is a ring homomorphism $F[t] \to F$, which commutes with the Leibniz formula.
