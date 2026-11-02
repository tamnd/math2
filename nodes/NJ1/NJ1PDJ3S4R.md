---
tag: NJ1PDJ3S4R
kind: statement
role: theorem
name: Oseledets theorem
msc: [37H15, 37A30, 37D25]
uses: [0NFPJVJJHX, 556WBDAHNP, AZRPHS478B, 06EKW1AKXF, RARTMA0ZEC, 833XVEEZCJ, J6NMBX3E55]
about: [NJ1FJSNK6A]
sources:
  - url: https://en.wikipedia.org/wiki/Oseledets_theorem
same_as:
  wikidata: Q7106480
  wikipedia: Oseledets theorem
---

## Statement

Let $(X, \mathcal{B}, \mu)$ be a [[probability space|0NFPJVJJHX]] and let $T \colon X \to X$ be an [[ergodic|AZRPHS478B]] [[measure-preserving transformation|556WBDAHNP]].
Let $A \colon X \to GL(d, \R)$ be a measurable map, and let $\norm{\cdot}$ be the [[operator norm|06EKW1AKXF]].
Assume that $\log^+ \norm{A}$ and $\log^+ \norm{A^{-1}}$ are integrable, where $\log^+ t = \max(\log t, 0)$.
For $n \ge 1$ let $A^{(n)}(x) = A(T^{n-1}x) \cdots A(Tx) \, A(x)$.
Then there are an integer $k$ with $1 \le k \le d$ and real numbers $\lambda_1 > \lambda_2 > \cdots > \lambda_k$ with the following property.
For [[almost every|RARTMA0ZEC]] $x \in X$ there is a chain of linear subspaces
$$\R^d = V_1(x) \supsetneq V_2(x) \supsetneq \cdots \supsetneq V_k(x) \supsetneq V_{k+1}(x) = \set{0}$$
such that, for each $i = 1, \dots, k$:

1. $A(x) V_i(x) = V_i(Tx)$.
2. For every $v \in V_i(x) \setminus V_{i+1}(x)$,
$$\lim_{n \to \infty} \frac{1}{n} \log \norm{A^{(n)}(x) v} = \lambda_i.$$
3. The dimension $\dim V_i(x) - \dim V_{i+1}(x)$ does not depend on $x$.

## Remarks

The numbers $\lambda_i$ are the [[Lyapunov exponents|NJ1FJSNK6A]] of the cocycle $A$, and the dimensions in clause 3 are their multiplicities.
The largest one is $\lambda_1 = \lim_{n} \frac{1}{n} \log \norm{A^{(n)}(x)}$ for almost every $x$, which already follows from [[Kingman's subadditive ergodic theorem|833XVEEZCJ]], since $\log \norm{A^{(n)}}$ is subadditive along orbits.
Applying the same argument to exterior powers gives the sums $\lambda_1 + \cdots + \lambda_j$ with multiplicity, and linear algebra then builds the subspaces.
Without ergodicity the theorem still holds, but $k$, the $\lambda_i$ and the multiplicities become $T$-invariant functions of $x$.
Example: if $A$ is a constant diagonal matrix $\mathrm{diag}(e^{a_1}, \dots, e^{a_d})$ with $a_1 > \cdots > a_d$, then $\lambda_i = a_i$ and $V_i$ is spanned by the last $d - i + 1$ coordinate vectors.
If $T$ is invertible, the filtration refines to a splitting $\R^d = E_1(x) \oplus \cdots \oplus E_k(x)$ into subspaces on which the growth rate is $\lambda_i$ both forward and backward in time.

## Explanations

### L1 human

Multiply many random matrices together, each chosen by a stationary random process.
The theorem says that the product grows at a few well-defined exponential rates, the Lyapunov exponents.
Each vector grows at one of these rates, and which rate it gets depends only on which of a nested family of subspaces it belongs to.
This is the law of large numbers for products of matrices.

### L2 human

The main use is in smooth ergodic theory: take $A(x) = Df(x)$, the derivative of a diffeomorphism $f$ preserving a measure.
Then the Lyapunov exponents measure how fast nearby orbits separate in each direction, and positive exponents signal chaos.
Pesin theory builds stable and unstable manifolds from the Oseledets subspaces, and Ruelle's inequality bounds the entropy by the sum of the positive exponents.
For $d = 1$ the theorem reduces to [[Birkhoff's ergodic theorem|J6NMBX3E55]] applied to $\log \abs{A}$.
