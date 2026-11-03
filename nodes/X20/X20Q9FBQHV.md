---
tag: X20Q9FBQHV
kind: statement
role: theorem
name: General solution of x'' = Ax with distinct nonpositive eigenvalues
msc: [34A30]
uses: [0BQAA2BK3Q, 0N6960W0BV, 0EB9N0S33C, 0SKYFQAFYD]
sources:
  - url: https://github.com/jirilebl/diffyqs/blob/658bcae9fb710f3fae2c9da4ca4524ce157453af/ch-systems.tex#L3484
    locator: ch-systems.tex:3484
---

## Statement

Let $A$ be a real $n \times n$ matrix with $n$ distinct real [[eigenvalues|0BQAA2BK3Q]], all negative or zero. Write them as $-\omega_1^2 > -\omega_2^2 > \cdots > -\omega_n^2$ with $\omega_i \ge 0$. Let $\vec v_1, \dots, \vec v_n$ be [[eigenvectors|0N6960W0BV]] for these eigenvalues, in the same order.

(1) If $A$ is an [[invertible matrix|0EB9N0S33C]], that is, if $\omega_1 > 0$, then the [[general solution|0SKYFQAFYD]] of $\vec x\,'' = A \vec x$ is
$$\vec x(t) = \sum_{i=1}^n \vec v_i \bigl( a_i \cos(\omega_i t) + b_i \sin(\omega_i t) \bigr),$$
where $a_i$ and $b_i$ are arbitrary constants.

(2) If $0$ is an eigenvalue, that is, $\omega_1 = 0$, and the other eigenvalues are distinct and negative, then the general solution is
$$\vec x(t) = \vec v_1 (a_1 + b_1 t) + \sum_{i=2}^n \vec v_i \bigl( a_i \cos(\omega_i t) + b_i \sin(\omega_i t) \bigr).$$

## Remarks

Each term is a solution because $\vec v_i f(t)$ solves the system when $f'' = -\omega_i^2 f$. For $\omega_i = 0$ this gives $f = a + bt$.
The $n$ eigenvectors are linearly independent, so there are $2n$ free constants, as expected for a second order system in $n$ unknowns.
This is the model of an undamped mass-spring system, where the $\omega_i$ are the natural frequencies.
