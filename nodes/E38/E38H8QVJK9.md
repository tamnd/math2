---
tag: E38H8QVJK9
kind: definition
name: Berezin integral
msc: [58C50, 15A75, 81T60]
defines: CYWSMK47CN
uses: [0MDMZ965VE, 6JZW4JC68Z, NH5HWBPWS9, Z0SB9HQBAJ]
sources:
  - url: https://en.wikipedia.org/wiki/Berezin_integral
---

## Definition

Let $n \ge 1$ and let $\Lambda_n = \Lambda[\theta_1, \dots, \theta_n]$ be the real [[exterior algebra|0MDMZ965VE]] on anticommuting generators $\theta_1, \dots, \theta_n$, so that $\theta_i \theta_j = -\theta_j \theta_i$.
Every $f \in \Lambda_n$ has a unique expansion $f = \sum_{I} a_I \theta_I$, where $I = \set{i_1 < \dots < i_k}$ runs over subsets of $\set{1, \dots, n}$, $\theta_I = \theta_{i_1} \cdots \theta_{i_k}$ and $a_I \in \R$.
The *Berezin integral* is the linear map $\Lambda_n \to \R$,
$$\int f \, d^n\theta = a_{\set{1, \dots, n}},$$
the coefficient of $\theta_1 \theta_2 \cdots \theta_n$.
The same definition applies with coefficients in any commutative ring, for instance $a_I \in C^\infty(U)$.

## Remarks

The order of the symbols $d\theta_i$ in the notation varies between authors and changes the result by a sign.
For $n = 1$: $\int (a + b\theta)\, d\theta = b$.

The integral kills derivatives: for each $i$, $\int \frac{\partial f}{\partial \theta_i}\, d^n\theta = 0$, where $\partial / \partial\theta_i$ is the odd derivation with $\partial \theta_j / \partial \theta_i = \delta_{ij}$, since a derivative has no top term.
Every monomial other than $\theta_1 \cdots \theta_n$ is, up to sign, such a derivative, so this property fixes the functional up to a constant factor.
Under a linear substitution $\theta = A\eta$ with $A$ an invertible real $n \times n$ matrix, $\theta_1 \cdots \theta_n = \det(A)\, \eta_1 \cdots \eta_n$, so $\int f(A\eta)\, d^n\eta = \det(A) \int f(\theta)\, d^n\theta$; for ordinary integrals the factor would be $\abs{\det A}^{-1}$.

Example: for $n = 2$ and $a \in \R$, $e^{a\theta_1\theta_2} = 1 + a\theta_1\theta_2$, so $\int e^{a\theta_1\theta_2}\, d^2\theta = a$.
This is the [[Pfaffian|NH5HWBPWS9]] of the antisymmetric matrix with entries $A_{12} = a$, $A_{21} = -a$, and in general the Gaussian integral $\int \exp(\frac{1}{2} \sum_{i,j} A_{ij}\theta_i\theta_j)\, d^n\theta$ equals $\operatorname{Pf}(A)$ up to a sign fixed by the conventions.

Non-example: the map $f \mapsto a_\emptyset$, which takes the constant term, is linear but is not the Berezin integral.
For $n = 1$ it gives $1$ on $\partial(\theta)/\partial\theta = 1$, so it does not kill derivatives.

On a [[supermanifold|Z0SB9HQBAJ]] of dimension $p|q$, consider a compactly supported function on a superdomain.
Its integral is the Berezin integral in the odd variables followed by the ordinary integral in the even ones.
