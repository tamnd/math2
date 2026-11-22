---
tag: BDT6XBCRDJ
kind: proof
name: Proof of the diagonalization of a quadratic form by Lagrange's method
msc: ["11E04", "15A63"]
topics: [6TSCEW8QMK]
audience: ug1
proves: 0Z3FEWZ8HA
methods: [0ASJVEFA9J, 0WCP0PVET6, 01XM7JEKHY]
uses: [0HZNE5QZDJ, VN9AG8JKYT, XNCV97HTZ8, 0VTQTPQGAV]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Equivalence of forms
  - url: https://en.wikipedia.org/wiki/Completing_the_square
    locator: lead section
---

## Proof

We write $Q$ as a polynomial in coordinates and remove one variable at a time by completing the square, with induction on the number of variables.
Let $F$ be a field with $2 \ne 0$ in $F$, fix a [[basis|0VTQTPQGAV]] $(e_1, \dots, e_n)$ of $V$, and write $v = \sum_i x_i e_i$.

1. By [[the correspondence theorem|VN9AG8JKYT]], part 4, $Q(v) = \sum_{i \le j} c_{ij} x_i x_j$ for some $c_{ij} \in F$.
   So $Q$ is a homogeneous polynomial of degree $2$ in $x_1, \dots, x_n$.
2. An invertible linear change of variables $x = Py$ is the same as the new basis $e'_j = \sum_i P_{ij} e_i$, because $\sum_i x_i e_i = \sum_j y_j e'_j$.
   So it suffices to find an invertible change of variables after which the polynomial has no cross terms.
3. A composite of invertible changes of variables is invertible, so we may apply several changes one after the other.
4. We prove by induction on $n$ that each polynomial $q = \sum_{i \le j} c_{ij} x_i x_j$ becomes $\sum_i a_i y_i^2$ after an invertible change of variables.
   For $n = 0$ there is nothing to prove, and for $n = 1$ the polynomial $q = c_{11} x_1^2$ is already diagonal.
5. Let $n \ge 2$ and assume the claim for $n - 1$ variables.
   Three cases cover all polynomials.
6. Case A: all $c_{ij}$ are $0$.
   Then $q = \sum_i 0 \cdot x_i^2$, and the identity change of variables works.
7. Case B: some diagonal coefficient is nonzero.
   After renumbering the variables, $a = c_{11} \ne 0$, and we collect the terms that contain $x_1$ as $q = a x_1^2 + x_1 L + q'$, where $L$ is linear and $q'$ is quadratic in $x_2, \dots, x_n$.
8. [[Complete the square|XNCV97HTZ8]], which needs $2a \ne 0$:
   $$a x_1^2 + x_1 L = a \Bigl( x_1 + \frac{L}{2a} \Bigr)^2 - \frac{L^2}{4a}.$$
9. Put $y_1 = x_1 + \frac{L}{2a}$ and $y_i = x_i$ for $i \ge 2$.
   This change is invertible, with inverse $x_1 = y_1 - \frac{L}{2a}$, because $L$ does not contain $x_1$.
10. Then $q = a y_1^2 + q''$ with $q'' = q' - \frac{L^2}{4a}$, a quadratic polynomial in $y_2, \dots, y_n$ only.
    By the induction hypothesis, an invertible change of $y_2, \dots, y_n$ makes $q''$ diagonal, and it leaves $y_1$ alone, so $q$ becomes diagonal.
11. Case C: all $c_{ii}$ are $0$, but some $c_{ij} \ne 0$ with $i < j$.
    After renumbering, $c_{12} \ne 0$.
12. Put $x_1 = s + t$ and $x_2 = s - t$, and keep $x_3, \dots, x_n$.
    The inverse is $s = \tfrac{1}{2}(x_1 + x_2)$ and $t = \tfrac{1}{2}(x_1 - x_2)$, so the change is invertible.
13. The term $c_{12} x_1 x_2$ becomes $c_{12}(s^2 - t^2)$.
    The other terms are $c_{1k} x_1 x_k$, $c_{2k} x_2 x_k$ and $c_{kl} x_k x_l$ with $k, l \ge 3$, and none of them produces $s^2$.
14. So the new coefficient of $s^2$ is $c_{12} \ne 0$, the new polynomial is in Case B, and steps 7 to 10 make it diagonal.
15. This completes the induction.
    By step 2, the final change of variables gives a basis in which $Q = \sum_i a_i y_i^2$.

## Idea

Take all terms that contain the first variable and fold them into one square, as in school algebra.
What is left involves one variable fewer, so induction finishes the job.
If no square term is left, the substitution $x_1 = s + t$, $x_2 = s - t$ makes one, because $x_1 x_2 = s^2 - t^2$.
Both moves divide by $2$, and that is why the characteristic must not be $2$.

## Variants

[[The proof by an orthogonal basis|PP93XQZ6WR]] is the same argument without coordinates: Case B is the choice of a vector $e_1$ with $Q(e_1) \ne 0$, and the rest of the form lives on the hyperplane orthogonal to $e_1$.

In matrix form, Case B is a symmetric row and column reduction.
Subtract multiples of row $1$ from the other rows to clear column $1$ below the pivot, then do the same column operations to clear row $1$.
Each pair of operations replaces $A$ by $E^{\mathsf{T}} A E$ for an elementary matrix $E$.

Case C on an example: $Q = xy + yz$ has no square terms.
With $x = s + t$ and $y = s - t$ it becomes $s^2 - t^2 + sz - tz$.
Completing both squares, $s^2 + sz = (s + \tfrac{z}{2})^2 - \tfrac{z^2}{4}$ and $-t^2 - tz = -(t + \tfrac{z}{2})^2 + \tfrac{z^2}{4}$, so
$$Q = \Bigl(s + \frac{z}{2}\Bigr)^2 - \Bigl(t + \frac{z}{2}\Bigr)^2.$$
