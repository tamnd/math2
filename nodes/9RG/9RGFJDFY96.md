---
tag: 9RGFJDFY96
kind: definition
name: Cyclic homology
msc: ["16E40", 19D55]
defines: 676K167XS8
uses: [3CTW1P4HBP, S5H153HFWC, F0HQXQ0HCD, WQ82C0M3QB]
sources:
  - url: https://en.wikipedia.org/wiki/Cyclic_homology
---

## Definition

Let $k$ be a field of characteristic $0$ and let $A$ be an [[associative algebra|3CTW1P4HBP]] over $k$ with identity.
Tensor products are over $k$.
For $n \ge 0$ let $t \colon A^{\otimes (n+1)} \to A^{\otimes (n+1)}$ be the cyclic operator
$$t(a_0 \otimes a_1 \otimes \cdots \otimes a_n) = (-1)^n \, a_n \otimes a_0 \otimes \cdots \otimes a_{n-1},$$
and let $C^\lambda_n(A) = A^{\otimes (n+1)} / \im(1 - t)$.
The Hochschild boundary $b$ of the complex $C_\bullet(A, A)$ of [[Hochschild homology|S5H153HFWC]] maps $\im(1 - t)$ into $\im(1 - t)$, so it induces a boundary on $C^\lambda_\bullet(A)$.
The *cyclic homology* of $A$ is $HC_n(A) = H_n(C^\lambda_\bullet(A), b)$, the homology of this Connes complex.

## Remarks

Example: in degree $0$, $C^\lambda_0(A) = A$ and $b(a_0 \otimes a_1) = a_0 a_1 - a_1 a_0$, so $HC_0(A) = A/[A, A] = HH_0(A)$.
Example: for $A = k$, the space $C^\lambda_n(k)$ is $k$ for $n$ even and $0$ for $n$ odd, since then $t = -1$ and $1 - t = 2$ is invertible.
The boundary vanishes on it, so $HC_n(k) = k$ for even $n \ge 0$ and $HC_n(k) = 0$ for odd $n$.
Over a general ground ring, cyclic homology is defined from Connes' bicomplex instead, and the two definitions agree when $k$ contains $\Q$.
There is a long exact sequence of Connes relating the two theories:
$$\cdots \to HH_n(A) \to HC_n(A) \to HC_{n-2}(A) \to HH_{n-1}(A) \to \cdots.$$
