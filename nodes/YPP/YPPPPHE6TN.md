---
tag: YPPPPHE6TN
kind: definition
name: Subfactor
msc: [46L37]
defines: 9RWS7TZHXH
uses: [PSFWQVZ0FS, 1VC7EJ1ZBZ]
sources:
  - url: https://en.wikipedia.org/wiki/Subfactor
---

## Definition

A *factor* is a [[von Neumann algebra|PSFWQVZ0FS]] $M$ whose center $M \cap M'$ is $\C I$, where $M'$ is the [[commutant|1VC7EJ1ZBZ]].
A *subfactor* of a factor $M$ is a von Neumann subalgebra $N \subseteq M$ that is itself a factor and contains the identity of $M$.
One often writes the subfactor as the inclusion $N \subseteq M$.

If $M$ is of type $\mathrm{II}_1$ with faithful normal tracial state $\tau$, let $L^2(M)$ be the Hilbert space completion of $M$ for $\langle x, y \rangle = \tau(y^* x)$.
The *Jones index* of $N \subseteq M$ is
$$[M : N] = \dim_N L^2(M) \in [1, \infty],$$
the Murray–von Neumann dimension of $L^2(M)$ as a module over $N$ acting by left multiplication.

## Remarks

Example: let $N$ be a $\mathrm{II}_1$ factor and $k \ge 1$.
Then $N \otimes I_k$, the matrices $\operatorname{diag}(x, \dots, x)$ with $x \in N$, is a subfactor of $M = N \otimes M_k(\C)$, the $k \times k$ matrices over $N$.
Both are factors with the same unit, and $L^2(M)$ is the direct sum of $k^2$ copies of $L^2(N)$ as an $N$-module, so $[M:N] = k^2$.

Non-example: the diagonal matrices $D_2 \subseteq M_2(\C)$ form a unital von Neumann subalgebra of the factor $M_2(\C)$.
But $D_2$ is commutative and two-dimensional, so its center is $D_2 \ne \C I$, and $D_2$ is not a factor.

Another example: if a finite group $G$ acts on a $\mathrm{II}_1$ factor $M$ by outer automorphisms, the fixed-point algebra $M^G$ is a subfactor with $[M : M^G] = \abs{G}$.
The index is $1$ exactly when $N = M$.
