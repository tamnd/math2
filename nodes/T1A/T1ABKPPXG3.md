---
tag: T1ABKPPXG3
kind: proof
name: Proof of linear recurrences by linear algebra
msc: ["39A06", "15A03"]
topics: [K0FNC6CWZN]
audience: ug1
proves: K00NJY6C33
uses: [081THG13JZ, 05BDYVQQ0T, 0XSJ25Z9M4, 0BJBYCGMWE, 0VJBSK15SN, 0B5H4208Z9, 5T4DY28JSK, 0P84B554AS, ACDFDABVQK, 0TNR9BQ871]
methods: [0NTF6DMVAP, 0ASJVEFA9J, DD2P85Y8E9]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_recurrence_with_constant_coefficients
    locator: lead section
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_recurrence_rigorous.ptx#L37
    locator: source/s_recurrence_rigorous.ptx:37
---

## Proof

We show that the first $k$ terms give an isomorphism from $S$ onto $K^k$, then that the state vector moves by $M$, and then we diagonalize $M$ with the Vandermonde matrix.
We use the notation of the statement, and we write $K^{\mathbb N}$ for the vector space of all sequences in $K$, with termwise addition and scalar multiplication.

**Part 1.**

1. $S$ is a subspace of $K^{\mathbb N}$.
   The zero sequence satisfies the [[recurrence|081THG13JZ]], and each side of the recurrence is linear in the sequence, so $u + w$ and $a u$ lie in $S$ when $u, w \in S$ and $a \in K$.
2. The map $\Phi \colon S \to K^k$, $\Phi(u) = (u_0, \dots, u_{k-1})$, is linear, because the operations on sequences are termwise.
3. $\Phi$ is injective.
   Let $\Phi(u) = 0$; we show $u_m = 0$ for all $m$ by strong induction on $m$.
   For $m < k$ this is $\Phi(u) = 0$.
   For $m \ge k$, the recurrence with $n = m - k$ writes $u_m$ as a combination of $u_{m-k}, \dots, u_{m-1}$, which are $0$ by the induction hypothesis.
   So the kernel of $\Phi$ is $\{0\}$, and $\Phi$ is injective by [[injectivity and the kernel|0BJBYCGMWE]].
4. $\Phi$ is surjective.
   Given $b = (b_0, \dots, b_{k-1}) \in K^k$, put $u_m = b_m$ for $m < k$, and define $u_m$ for $m \ge k$ by the recurrence, one term after the other.
   This sequence lies in $S$, and $\Phi(u) = b$.
5. So $\Phi$ is a [[linear isomorphism|0XSJ25Z9M4]] from $S$ onto $K^k$.
   By the [[classification of vector spaces by dimension|0VJBSK15SN]], $\dim S = k$, which is part 1.

**Part 2.**

6. Let $u \in S$ and $n \ge 0$.
   Rows $1$ to $k - 1$ of $M$ each pick the next entry of $U_n$, so the first $k - 1$ entries of $M U_n$ are $u_{n+1}, \dots, u_{n+k-1}$.
7. The last row of $M$ gives the last entry $c_0 u_n + \dots + c_{k-1} u_{n+k-1}$, which is $u_{n+k}$ by the recurrence.
8. So $M U_n = (u_{n+1}, \dots, u_{n+k})^{\mathsf T} = U_{n+1}$.
   Induction on $n$ then gives $U_n = M^n U_0$, since
$$U_{n+1} = M U_n = M M^n U_0 = M^{n+1} U_0.$$

**Part 3.**

9. Let $r$ be a root of $p$, and let $v = (1, r, \dots, r^{k-1})^{\mathsf T}$.
   The first $k - 1$ entries of $M v$ are $r, r^2, \dots, r^{k-1}$, and the last entry is $c_0 + c_1 r + \dots + c_{k-1} r^{k-1}$.
10. The equation $p(r) = 0$ says that $r^k = c_0 + c_1 r + \dots + c_{k-1} r^{k-1}$.
    So $M v = (r, r^2, \dots, r^k)^{\mathsf T} = r v$, and $v \ne 0$ because its first entry is $1$.
    Hence $v$ is an [[eigenvector|0B5H4208Z9]] of $M$ for the eigenvalue $r$.
11. The vectors of step 9 for $r_1, \dots, r_k$ are the columns of the [[Vandermonde matrix|5T4DY28JSK]] $V$.
    Step 10, applied to each column, gives $M V = V D$.
12. By the [[Vandermonde determinant|0P84B554AS]], $\det V = \prod_{i < j} (r_j - r_i)$, which is not $0$ because the roots are distinct.
    So $V$ is invertible by the [[invertible matrix theorem|ACDFDABVQK]], and $M = V D V^{-1}$.
13. The sequence $(r_j^n)_{n \ge 0}$ lies in $S$, because
$$r_j^{n+k} - c_{k-1} r_j^{n+k-1} - \dots - c_0 r_j^n = r_j^n\, p(r_j) = 0.$$
    Its image under $\Phi$ is column $j$ of $V$.
14. The columns of the invertible matrix $V$ form a basis of $K^k$.
    The inverse isomorphism $\Phi^{-1}$ sends this basis to a basis of $S$, so the sequences $(r_j^n)$ form a basis of $S$.
15. By step 8 and the formula for [[powers of a diagonalizable matrix|0TNR9BQ871]], $U_n = M^n U_0 = V D^n V^{-1} U_0$.
    Put $a = V^{-1} U_0$.
16. The first row of $V$ is $(1, \dots, 1)$, and $D^n = \operatorname{diag}(r_1^n, \dots, r_k^n)$.
    So the first entry of $V D^n a$ is $u_n = a_1 r_1^n + \dots + a_k r_k^n$, which proves part 3.

**Part 4.**

17. The Fibonacci recurrence is the case $K = \mathbb R$, $k = 2$ and $c_0 = c_1 = 1$.
    Then $p(x) = x^2 - x - 1$, whose roots are $\varphi$ and $\psi$ by the quadratic formula.
18. The roots are distinct, since $\varphi - \psi = \sqrt 5 \ne 0$.
    By part 3, $F_n = a \varphi^n + b \psi^n$, where $(a, b)$ solves $V (a, b)^{\mathsf T} = (F_0, F_1)^{\mathsf T}$.
19. This system is $a + b = 0$ and $a \varphi + b \psi = 1$.
    The first equation gives $b = -a$, and then the second gives $a (\varphi - \psi) = 1$.
20. So $a = 1/\sqrt 5$ and $b = -1/\sqrt 5$, which gives $F_n = (\varphi^n - \psi^n)/\sqrt 5$.
    This is Binet's formula, and the proof of all four parts is complete.

## Idea

A solution of the recurrence is fixed by its first $k$ terms, so the solutions form a copy of $K^k$.
The window of $k$ consecutive terms slides forward by one fixed matrix $M$ at each step, so every solution is an orbit $M^n U_0$.
When $p$ has distinct roots, the vectors $(1, r, \dots, r^{k-1})$ are eigenvectors of $M$, and together they form an eigenbasis.
In that basis $M^n$ is diagonal with entries $r_j^n$, and reading off the first coordinate gives the closed form.

## Variants

Part 3 also has a proof without matrices.
Each $(r_j^n)$ lies in $S$ by step 13, and their starting vectors are the columns of $V$, which are independent because $\det V \ne 0$.
So the $k$ sequences are independent in $S$, and they form a basis because $\dim S = k$.

A third proof uses generating functions.
For $u \in S$, the series $\sum_n u_n z^n$ equals $q(z) / (1 - c_{k-1} z - \dots - c_0 z^k)$ for a polynomial $q$ of degree less than $k$.
The denominator is $\prod_j (1 - r_j z)$, and partial fractions turn the quotient into $\sum_j a_j / (1 - r_j z)$, whose coefficients are $\sum_j a_j r_j^n$.

Once Binet's formula is known, it also follows by induction on $n$, from $\varphi^2 = \varphi + 1$ and $\psi^2 = \psi + 1$.
