---
tag: XZCSJCXK5C
kind: example
name: The module of the Jordan block J₂(0) is F[x]/(x²)
msc: ["15A21", "13C05"]
topics: [GEBYZKYV3D]
audience: grad
instance_of: [KGVTFBZX59]
illustrates: [R5X8SNHBGG]
uses: [KGVTFBZX59, R5X8SNHBGG, 0PBFS92AJP, 0ACX5QT8TE]
sources:
  - url: https://en.wikipedia.org/wiki/Structure_theorem_for_finitely_generated_modules_over_a_principal_ideal_domain
    locator: Corollaries
---

## Example

Let $F$ be a field, and let $N$ be the [[Jordan block|0PBFS92AJP]]
$$N = J_2(0) = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \qquad N e_1 = 0, \quad N e_2 = e_1.$$
We show that the [[module|KGVTFBZX59]] $F^2_N$, with $x$ acting as $N$, is isomorphic to $F[x]/(x^2)$.

1. Define $\psi \colon F[x] \to F^2$ by $\psi(f) = f(N) e_2$. It is a homomorphism of $F[x]$-modules, since $\psi(gf) = g(N) f(N) e_2 = g \cdot \psi(f)$.
2. We have $\psi(1) = e_2$ and $\psi(x) = N e_2 = e_1$, so $\psi$ is surjective.
3. Also $\psi(x^2) = N e_1 = 0$, so $(x^2) \subseteq \ker \psi$.
4. Write any $f$ as $a + bx + x^2 g$. Then $\psi(f) = a e_2 + b e_1$, which is $0$ only if $a = b = 0$, so $\ker \psi = (x^2)$.
5. Hence $F^2_N \cong F[x]/(x^2)$, a cyclic module with generator $e_2$.
6. The submodules of $F[x]/(x^2)$ are $0$, $(x)/(x^2)$ and the whole module, and $\psi$ sends them to $0$, the line $F e_1$ and $F^2$.
7. These are exactly the [[$N$-invariant subspaces|0ACX5QT8TE]] of $F^2$, as the [[dictionary theorem|R5X8SNHBGG]] says. Indeed, $N(a, b) = (b, 0)$ is a multiple of $(a, b)$ only if $b = 0$, so $F e_1$ is the only invariant line.

## Remarks

### A cyclic module that does not split

The only nonzero proper submodule is $F e_1$, so $F^2_N$ is not a direct sum of two nonzero submodules.
A scalar matrix such as $0 \cdot I_2$ has the same characteristic polynomial $x^2$, but its module $(F[x]/(x))^2$ splits, so the two matrices are not similar.

### Longer blocks

For $J_k(0)$ the same map $f \mapsto f(J_k(0)) e_k$ gives $F^k_{J_k(0)} \cong F[x]/(x^k)$, with generator $e_k$.
For $J_k(\lambda)$ it gives $F[x]/((x - \lambda)^k)$.
The submodules then form a chain $0 \subset F e_1 \subset F e_1 + F e_2 \subset \cdots \subset F^k$, which is the image of the chain of ideals $(x^k) \subset (x^{k-1}) \subset \cdots \subset (1)$ under the map $f \mapsto f(J_k(0)) e_k$.

## Explanations

### L1 human

The matrix $N$ sends the second basis vector to the first, and the first to zero.
Think of $x$ as "apply $N$".
Then the second basis vector plays the role of $1$, the first plays the role of $x$, and $x$ squared is zero.
So the plane with this map behaves like the polynomials in which $x$ squared counts as zero.

### L2 human

Here is a typical computation: find $(3 + 2x + 5x^2) \cdot (1, 1)$ in $\mathbb{Q}^2_N$.
We have $N(1, 1) = (1, 0)$ and $N^2 = 0$, so the result is $3(1, 1) + 2(1, 0) + 0 = (5, 3)$.
Check it in $\mathbb{Q}[x]/(x^2)$, where $(1, 1) = e_1 + e_2$ corresponds to $1 + x$.
There $(3 + 2x + 5x^2)(1 + x) \equiv (3 + 2x)(1 + x) = 3 + 5x + 2x^2 \equiv 3 + 5x$, and $3 + 5x$ corresponds to $3 e_2 + 5 e_1 = (5, 3)$.
The typical use of the isomorphism is to read off invariant subspaces from ideals.
Watch out: the generator is $e_2$, the vector that $N$ does not kill, so matching $e_1$ with $1$ gives the wrong answer.
