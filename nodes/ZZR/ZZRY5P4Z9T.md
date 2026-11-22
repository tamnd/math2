---
tag: ZZRY5P4Z9T
kind: proof
name: Proof of linear systems of ODEs by eigenvectors
msc: ["34A30", "15A18"]
topics: [K0FNC6CWZN]
audience: ug2
proves: DH7CQXQYJX
uses: [0VJF99CZ0Z, 0B5H4208Z9, 04R3CY41VJ, 0EX9GFJ0B3, 003QDZ4T16, 0CRMGPAH83, ACDFDABVQK, 0HNMFG8F8K, 0WF5AQYTW6]
methods: [0NTF6DMVAP]
sources:
  - url: https://github.com/jirilebl/diffyqs/blob/658bcae9fb710f3fae2c9da4ca4524ce157453af/ch-systems.tex#L4365
    locator: ch-systems.tex:4365
  - book: isbn:9780321982384
    locator: Section 5.7
---

## Proof

We first solve the scalar equation $f' = \lambda f$, then we uncouple the system with the eigenbasis, and last we use conjugation to get real solutions.
We use the notation of the statement, and we take derivatives of vector functions entry by entry.

**A lemma on scalar functions.**

1. Let $\lambda = \alpha + i \beta \in \mathbb C$.
   By [[Euler's formula|04R3CY41VJ]], $e^{\lambda t} = e^{\alpha t} \cos \beta t + i\, e^{\alpha t} \sin \beta t$.
2. The product rule and the fact that [[the exponential function is its own derivative|0EX9GFJ0B3]] give the derivative $e^{\alpha t} (\alpha \cos \beta t - \beta \sin \beta t) + i\, e^{\alpha t} (\alpha \sin \beta t + \beta \cos \beta t)$.
3. Multiplying out $(\alpha + i \beta) e^{\alpha t} (\cos \beta t + i \sin \beta t)$ gives the same result.
   So $(e^{\lambda t})' = \lambda e^{\lambda t}$.
4. Let $f : \mathbb R \to \mathbb C$ be differentiable with $f' = \lambda f$.
   By step 3 for $-\lambda$ and the product rule, $(e^{-\lambda t} f)' = -\lambda e^{-\lambda t} f + e^{-\lambda t} \lambda f = 0$.
5. The real and imaginary parts of $e^{-\lambda t} f$ have derivative $0$, so they are constant, because [[a function with zero derivative is constant|003QDZ4T16]] on $\mathbb R$.
   So $e^{-\lambda t} f(t) = c$ for a constant $c \in \mathbb C$, and $f(t) = c\, e^{\lambda t}$ with $c = f(0)$.

**Part 1.**

6. Let $A v = \lambda v$ and $x(t) = e^{\lambda t} v$.
   By step 3, $x'(t) = \lambda e^{\lambda t} v = e^{\lambda t} A v = A (e^{\lambda t} v) = A x(t)$, so $x$ is a solution.

**Part 2.**

7. The columns of $P$ form a basis of $\mathbb C^n$, so $P$ is invertible by the [[invertible matrix theorem|ACDFDABVQK]].
   Column $j$ of $A P$ is $A v_j = \lambda_j v_j$, so $A P = P D$ with $D = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$.
8. Let $x$ be a solution, and put $y(t) = P^{-1} x(t)$.
   Since $P^{-1}$ is a constant matrix, $y' = P^{-1} x' = P^{-1} A x = P^{-1} A P\, y = D y$.
9. So $y_j' = \lambda_j y_j$ for each $j$.
   By step 5, $y_j(t) = c_j e^{\lambda_j t}$ with $c_j = y_j(0)$, that is, $c = P^{-1} x(0)$.
10. Then $x(t) = P y(t) = \sum_j c_j e^{\lambda_j t} v_j$, so every solution has the stated form.
11. Conversely, every such combination is a solution, by part 1 and because both $x \mapsto x'$ and $x \mapsto A x$ are linear.
12. Suppose that $\sum_j c_j e^{\lambda_j t} v_j = 0$ for all $t$.
    At $t = 0$ this gives $\sum_j c_j v_j = 0$, so all $c_j = 0$, because the $v_j$ are [[linearly independent|0CRMGPAH83]].
    So the solutions $e^{\lambda_j t} v_j$ are independent.
13. By step 9, the coefficients of a solution are $P^{-1} x(0)$, so two solutions with the same value at $0$ are equal.
    If $P$ and $x(0)$ are real, then $P^{-1}$ is real, and so is $c$.

**Part 3, the real solutions.**

14. Let $x$ be a solution, and conjugate each entry of $x'(t) = A x(t)$.
    Since $A$ is real, $\bar x'(t) = A \bar x(t)$, so $\bar x$ is a solution.
15. By linearity, $\operatorname{Re} x = \frac12 (x + \bar x)$ and $\operatorname{Im} x = \frac{1}{2i} (x - \bar x)$ are solutions, and they are real.
16. Apply this to $x(t) = e^{\lambda t} v$, which is a solution by part 1.
    Steps 1 and 3 give $e^{\lambda t} v = e^{\alpha t} (\cos \beta t + i \sin \beta t)(a + i b)$.
    Its real part is $e^{\alpha t} (a \cos \beta t - b \sin \beta t)$, and its imaginary part is $e^{\alpha t} (a \sin \beta t + b \cos \beta t)$.

**Part 3, the real basis.**

17. Since $A$ is real, $A v = \lambda v$ holds exactly when $A \bar v = \bar \lambda \bar v$.
    So conjugation maps the eigenspace $E_\lambda$ onto $E_{\bar\lambda}$.
    It maps a basis of $E_\lambda$ to a basis of $E_{\bar\lambda}$, because it turns a dependence relation into a conjugate one.
18. For a real eigenvalue $\mu$, the matrix $A - \mu I$ is real.
    Row reduction to the [[reduced row echelon form|0WF5AQYTW6]] uses only real numbers, and the special solutions read off from it are real vectors that span the null space over $\mathbb C$.
    So $E_\mu$ has a basis of real vectors.
19. The dimensions of the eigenspaces add up to $n$, because $A$ has a basis of eigenvectors.
    [[Eigenvectors with distinct eigenvalues are linearly independent|0HNMFG8F8K]], so the union of bases of the eigenspaces is independent, and it is a basis of $\mathbb C^n$.
20. For each pair $\lambda$, $\bar\lambda$ with $\beta > 0$, choose a basis of $E_\lambda$, and take its conjugate as the basis of $E_{\bar\lambda}$, by step 17.
    For each real eigenvalue, choose a real basis, by step 18.
    By step 19, all these vectors together form a basis $v_1, \dots, v_n$ of $\mathbb C^n$.
21. In this basis, replace each pair $v = a + i b$, $\bar v = a - i b$ by the real pair $a$, $b$.
    Since $a = \frac12 (v + \bar v)$, $b = \frac{1}{2i} (v - \bar v)$, $v = a + i b$ and $\bar v = a - i b$, the new list spans the same space.
    So it is a basis $w_1, \dots, w_n$ of $\mathbb C^n$ made of real vectors.
22. Now make one real solution $z_j$ for each $w_j$.
    For a real eigenvector $w_j$ with the eigenvalue $\mu$, put $z_j(t) = e^{\mu t} w_j$.
    For a pair $a$, $b$ from step 21, take the real part and the imaginary part of $e^{\lambda t} v$ from step 16.
    In each case $z_j(0) = w_j$.
23. Suppose that $\sum_j d_j z_j = 0$ with real $d_j$.
    At $t = 0$ this gives $\sum_j d_j w_j = 0$, so all $d_j = 0$, and the $z_j$ are independent over $\mathbb R$.
24. Let $x$ be a real solution.
    The $n$ real vectors $w_j$ are independent over $\mathbb R$, so they form a basis of $\mathbb R^n$, and $x(0) = \sum_j d_j w_j$ with real $d_j$.
25. The real solution $z = \sum_j d_j z_j$ has $z(0) = x(0)$, so $x = z$ by step 13.
    So every real solution is a real combination of $z_1, \dots, z_n$, and the proof is complete.

## Idea

An eigenvector direction is invariant, so on it the system reduces to the scalar equation $f' = \lambda f$, whose solutions are $c\, e^{\lambda t}$.
An eigenbasis uncouples the system completely, because the substitution $x = P y$ turns $x' = A x$ into $n$ scalar equations $y_j' = \lambda_j y_j$.
For a real matrix, conjugation maps solutions to solutions, so the real and imaginary parts of a complex solution are real solutions.

## Variants

With the [[matrix exponential|020M04FN1H]], every solution is $x(t) = e^{t A} x(0)$.
For $A = P D P^{-1}$, the series gives $e^{t A} = P e^{t D} P^{-1}$, and $e^{t D}$ is diagonal with the entries $e^{\lambda_j t}$.
This gives part 2 at once, but it needs the theory of the matrix exponential.

Another proof of part 2 uses the uniqueness theorem for initial value problems from ODE theory.
The combination $\sum_j c_j e^{\lambda_j t} v_j$ with $c = P^{-1} x(0)$ is a solution with the same initial value as $x$, so it equals $x$.
