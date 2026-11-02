---
tag: P8CAK0FHGJ
kind: statement
role: theorem
name: Jentzsch's theorem on positive kernels
msc: [45C05, 47B65]
uses: [ZM5G144PZG, 4NSACSWRJZ, 9V7YQA85PC, VADXDK3TKM, 62NS7PV1M9, MF77N00SK8]
about: [ZM5G144PZG]
sources:
  - url: https://en.wikipedia.org/wiki/Krein%E2%80%93Rutman_theorem
---

## Statement

Let $a < b$ and let $K \colon [a, b] \times [a, b] \to \R$ be a [[continuous kernel|ZM5G144PZG]] with $K(x, y) > 0$ for all $x, y \in [a, b]$.
Let $T_K$ be the integral operator $(T_K \varphi)(x) = \int_a^b K(x, y) \varphi(y) \, dy$, and let $r$ be its [[spectral radius|9V7YQA85PC]].
Then:

1. $r > 0$, and $r$ is an eigenvalue of $T_K$ with an [[eigenfunction|4NSACSWRJZ]] $u$ that is continuous and satisfies $u(x) > 0$ for all $x \in [a, b]$;
2. the eigenspace of $r$ is spanned by $u$;
3. every other eigenvalue $\mu$ of $T_K$, real or complex, satisfies $\abs{\mu} < r$.

## Remarks

The operator $T_K$ is compact on $C[a, b]$ by the [[compactness of integral operators|MF77N00SK8]], and it maps the cone of nonnegative functions into itself.
Since $K$ has a positive minimum on the square, $T_K$ sends every nonnegative function that is not identically $0$ to a strictly positive function.
So it maps the cone minus $0$ into the interior of the cone.
The strong form of the [[Krein–Rutman theorem|VADXDK3TKM]] then gives all three parts.

Example: for $K(x, y) = 1 + xy$ on $[0, 1]$, $T_K$ has rank $2$ and maps into the span of $1$ and $x$.
Its matrix in this basis is $\begin{pmatrix} 1 & 1/2 \\ 1/2 & 1/3 \end{pmatrix}$, with eigenvalues $\frac{4 \pm \sqrt{13}}{6}$.
The larger one, $r = \frac{4 + \sqrt{13}}{6}$, has the eigenfunction $u(x) = 1 + 2(r - 1) x = 1 + \frac{\sqrt{13} - 2}{3} x$, which is positive on $[0, 1]$.
The other eigenvalues, $\frac{4 - \sqrt{13}}{6}$ and $0$, have modulus less than $r$.

Strict positivity matters.
Take $K(x, y) = 1$ when $y \le x$ and $0$ otherwise, which is nonnegative but neither continuous nor positive.
Its operator is the Volterra operator, whose spectral radius is $0$ and which has no eigenvalue at all.

## Explanations

### L1 human

If every point influences every other point positively, the integral operator has a dominant mode.
This mode is a positive function, it is unique up to scaling, and it grows faster under repeated application than every other mode.
This is the integral version of the [[Perron–Frobenius theorem|62NS7PV1M9]] for matrices with positive entries.

### L2 human

The theorem explains the long-time behaviour of models with a positive integral operator, such as population models structured by size.
After many steps, the state lines up with the positive eigenfunction $u$ and grows by the factor $r$ per step.
It is a special case of the Krein–Rutman theorem for strongly positive compact operators on ordered Banach spaces.
