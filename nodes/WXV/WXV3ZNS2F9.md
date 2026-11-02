---
tag: WXV3ZNS2F9
kind: statement
role: theorem
name: Asymptotic stability of linear recurrences
msc: [39A30, 39A06]
uses: [AA7XRZ4VAG, 0YA7X86K05, X11Q0G8PNA, CHEQ235HW9, 05M5SWSZZD]
about: [AA7XRZ4VAG, X11Q0G8PNA]
sources:
  - url: https://en.wikipedia.org/wiki/Stable_polynomial
---

## Statement

Let $d \ge 1$ and let $c_0, \dots, c_{d-1}$ be complex numbers with $c_0 \ne 0$.
Consider the [[linear recurrence|AA7XRZ4VAG]]
$$x_{n+d} = c_{d-1} x_{n+d-1} + \cdots + c_1 x_{n+1} + c_0 x_n, \qquad n \ge 0,$$
and its [[characteristic polynomial|0YA7X86K05]] $\chi(z) = z^d - c_{d-1} z^{d-1} - \cdots - c_0$.
The following are equivalent.

1. Every solution $(x_n)$ satisfies $x_n \to 0$ as $n \to \infty$.
2. The zero solution is asymptotically [[stable|CHEQ235HW9]].
3. The polynomial $\chi$ is [[Schur stable|X11Q0G8PNA]], that is, every root $\lambda$ of $\chi$ satisfies $\abs{\lambda} < 1$.

## Remarks

Every solution is a finite sum of terms $p(n) \lambda^n$, where $\lambda$ is a root of $\chi$ and $p$ is a polynomial of degree less than the multiplicity of $\lambda$.
If all roots satisfy $\abs{\lambda} < 1$, each such term tends to $0$, because $\abs{\lambda}^n$ decays faster than any polynomial grows.
If some root has $\abs{\lambda} \ge 1$, then $x_n = \lambda^n$ is a solution that does not tend to $0$.
For example, $x_{n+2} = x_{n+1} - \tfrac{1}{2} x_n$ has characteristic polynomial $z^2 - z + \tfrac{1}{2}$ with roots of modulus $1/\sqrt{2}$, so all its solutions tend to $0$.
In contrast, $x_{n+2} = x_n$ has roots $\pm 1$ on the unit circle, and its solution $x_n = 1$ stays bounded but does not tend to $0$.
Suppose all roots satisfy $\abs{\lambda} \le 1$, some root lies on the unit circle, and the roots on the circle are simple.
Then the zero solution is stable but not asymptotically stable.

## Explanations

### L1 human

A linear recurrence builds each term from a fixed combination of the previous ones.
This theorem says when every such sequence dies out, whatever the starting values.
The answer is read off from one polynomial: all its roots must lie strictly inside the unit circle.
It turns a question about infinitely many sequences into a question about finitely many numbers.

### L2 human

The result is the discrete counterpart of the fact that $x' = Ax$ is asymptotically stable exactly when all eigenvalues of $A$ have negative real part.
Writing the recurrence as $X_{n+1} = C X_n$ with the companion matrix $C$, the condition says that the spectral radius of $C$ is less than $1$.
In practice one does not compute the roots; tests such as the [[Jury stability criterion|VGV9FAPCHN]] decide Schur stability from the coefficients alone.
The same criterion governs the local stability of a fixed point of a nonlinear map through its linearization.
