---
tag: F46GGH7RJ5
kind: example
name: Sturm–Liouville problem as an integral equation
msc: [45C05, 34B24, 34B27]
illustrates: [6Q36P44PHZ, 7WV6B2502K]
uses: [SH6JY9RN2E, ADTYF8FG6C, DC7HMHVREP, 3JVT83K8A1]
sources:
  - url: https://en.wikipedia.org/wiki/Sturm%E2%80%93Liouville_theory
---

## Example

Consider the simplest [[Sturm–Liouville problem|7WV6B2502K]]: find $\lambda$ and a nonzero $u \in C^2[0, 1]$ with
$$-u''(x) = \lambda u(x), \quad u(0) = u(1) = 0.$$
The [[Green's function|SH6JY9RN2E]] of $-u''$ with these boundary conditions is
$$G(x, s) = \begin{cases} s(1 - x), & 0 \le s \le x \le 1, \\ x(1 - s), & 0 \le x \le s \le 1. \end{cases}$$
For continuous $f$, the unique solution of $-u'' = f$, $u(0) = u(1) = 0$ is $u(x) = \int_0^1 G(x, s) f(s) \, ds$.
Taking $f = \lambda u$, the boundary value problem becomes the homogeneous Fredholm equation of the second kind
$$u(x) = \lambda \int_0^1 G(x, s) \, u(s) \, ds.$$
Conversely, a continuous solution of this integral equation is $C^2$ and solves the boundary value problem.

Check: the kernel $G$ is continuous and [[symmetric|ADTYF8FG6C]].
For $u_n(x) = \sin(n \pi x)$, the function $v = u_n / (n^2 \pi^2)$ satisfies $-v'' = u_n$ and $v(0) = v(1) = 0$.
So $\int_0^1 G(x, s) \sin(n \pi s) \, ds = \sin(n \pi x) / (n^2 \pi^2)$, and the [[characteristic values|DC7HMHVREP]] of $G$ are $\lambda_n = n^2 \pi^2$, $n \ge 1$.
These are exactly the eigenvalues of the boundary value problem.

## Remarks

Since $G$ is symmetric, the Hilbert–Schmidt theorem gives the expansion of every function $\int_0^1 G(x, s) f(s) \, ds$ in the sine series $\sum_n c_n \sin(n \pi x)$.
The [[trace|3JVT83K8A1]] of $G$ is $\int_0^1 x(1 - x) \, dx = 1/6$.
It equals $\sum_{n \ge 1} 1/\lambda_n = \sum_{n \ge 1} 1/(n^2 \pi^2)$, which is Euler's identity $\sum_{n \ge 1} 1/n^2 = \pi^2/6$.

## Explanations

### L1 human

A differential equation with boundary conditions can be turned around.
Instead of asking which $u$ has $-u''$ proportional to $u$, one asks which $u$ is reproduced, up to a factor, by integrating against $G$.
The Green's function $G$ is a tent-shaped kernel that undoes $-d^2/dx^2$.
The two problems have the same solutions, and the integral form brings the tools of compact symmetric operators: real eigenvalues, orthogonal eigenfunctions and expansions.
