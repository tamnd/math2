---
tag: 2ZKWZ0A4MT
kind: statement
role: theorem
name: Schwartz kernel theorem
msc: [46F05, 46A11]
uses: [XC6XPMC2FQ, 0KPHENZ5S7]
sources:
  - url: https://en.wikipedia.org/wiki/Schwartz_kernel_theorem
same_as:
  wikidata: Q1276318
  wikipedia: Schwartz kernel theorem
---

## Statement

Let $X \subseteq \R^m$ and $Y \subseteq \R^n$ be open sets.
Let $\mathcal{D}(X)$ be the space of test functions on $X$, and let $\mathcal{D}'(X)$ be the space of distributions on $X$.
For $\varphi \in \mathcal{D}(X)$ and $\psi \in \mathcal{D}(Y)$, let $(\varphi \otimes \psi)(x, y) = \varphi(x) \psi(y)$.

1. Each $K \in \mathcal{D}'(X \times Y)$ defines a linear map $A_K \colon \mathcal{D}(Y) \to \mathcal{D}'(X)$ by $\langle A_K \psi, \varphi \rangle = \langle K, \varphi \otimes \psi \rangle$. It is sequentially continuous: if $\psi_j \to 0$ in $\mathcal{D}(Y)$, then $\langle A_K \psi_j, \varphi \rangle \to 0$ for every $\varphi \in \mathcal{D}(X)$.
2. Conversely, for each linear map $A \colon \mathcal{D}(Y) \to \mathcal{D}'(X)$ that is sequentially continuous in this sense, there is exactly one $K \in \mathcal{D}'(X \times Y)$ with $A = A_K$.

The distribution $K$ is the *Schwartz kernel* of $A$.

## Remarks

The hard part is the existence of $K$ in part 2.
One proof expands test functions in Fourier series on large cubes and controls the coefficients.
Another uses that the spaces of test functions are [[nuclear spaces|XC6XPMC2FQ]], so that continuous bilinear forms on $\mathcal{D}(X) \times \mathcal{D}(Y)$ extend to $\mathcal{D}(X \times Y)$.

Example: the identity map of $\mathcal{D}(\R)$, viewed as a map into $\mathcal{D}'(\R)$, has kernel $\delta(x - y)$.
Indeed $\langle \delta(x - y), \varphi \otimes \psi \rangle = \int \varphi(x) \psi(x)\, dx$.
The operator $\psi \mapsto \psi'$ has kernel $\delta'(x - y)$, the derivative in $x$ of the [[Dirac delta|0KPHENZ5S7]] on the diagonal.

## Explanations

### L1 human

A matrix is the same as a linear map between spaces of columns.
The kernel theorem says that the same holds for very general linear maps on functions: each one is "integration against a kernel" $K(x, y)$.
The price is that $K$ may be a distribution rather than a function, like the delta function for the identity map.

### L2 human

The theorem lets one describe operators such as differential operators, pseudodifferential operators and Fourier integral operators through their kernels.
Properties of the operator then become properties of $K$, for example the singular support or the wave front set of $K$.
Function kernels are not enough: the identity operator of $L^2(\R)$ is not an integral operator with a function kernel, so one really needs distributions.
