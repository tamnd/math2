---
tag: Z2N8MPD8DH
kind: statement
role: theorem
name: Lumer–Phillips theorem
msc: [47D06, 47B44]
uses: [06GZ956657, BCJHNHKQFG, 3S7HJ5GQRF, XPWE94BV6N, 60HSWZBTK9]
about: [3S7HJ5GQRF, XPWE94BV6N]
sources:
  - url: https://en.wikipedia.org/wiki/Lumer%E2%80%93Phillips_theorem
same_as:
  wikidata: Q1602819
  wikipedia: Lumer–Phillips theorem
---

## Statement

Let $X$ be a real or complex [[Banach space|06GZ956657]] and let $A$ be a [[densely defined|BCJHNHKQFG]] linear operator in $X$ with domain $D(A)$.
Then the following are equivalent.

1. $A$ is the [[generator|60HSWZBTK9]] of a [[contraction semigroup|XPWE94BV6N]] on $X$.
2. $A$ is [[dissipative|3S7HJ5GQRF]], and there is $\lambda_0 > 0$ such that $\lambda_0 I - A$ maps $D(A)$ onto $X$.

## Remarks

If $A$ generates a contraction semigroup $T(t)$, then for $\lambda > 0$ the resolvent is the Laplace transform $(\lambda I - A)^{-1}x = \int_0^\infty e^{-\lambda t} T(t)x \, dt$.
This gives surjectivity of $\lambda I - A$ and the bound $\norm{(\lambda I - A)^{-1}} \le 1/\lambda$, which is dissipativity.
Conversely, dissipativity and one surjective $\lambda_0 I - A$ give $\norm{(\lambda I - A)^{-1}} \le 1/\lambda$ for all $\lambda > 0$, and the [[Hille–Yosida theorem|5YR4GJKPCV]] then produces the semigroup.

Example: on $L^2(0, 1)$, let $Af = f''$ with domain $H^2(0, 1) \cap H^1_0(0, 1)$.
It is dissipative since $\ip{Af}{f} = -\int_0^1 \abs{f'}^2 \, dx$, and $I - A$ is onto because the boundary problem $f - f'' = g$, $f(0) = f(1) = 0$ has a solution for every $g \in L^2(0, 1)$.
So $A$ generates the heat semigroup with Dirichlet boundary conditions, and it is a contraction semigroup.

The range condition cannot be dropped.
The operator $f \mapsto f''$ on smooth functions with compact support in $(0, 1)$ is densely defined and dissipative, but it is not closed, so it is not a generator.

## Explanations

### L1 human

The theorem tells when the equation $u' = Au$ has solutions that never grow in norm.
Two things are needed.
The operator must lose energy, which is dissipativity.
And the equation $\lambda u - Au = g$ must be solvable for every right side $g$, which rules out an operator with too small a domain.

### L2 human

The Hille–Yosida theorem asks for the resolvent bound $\norm{(\lambda - A)^{-1}} \le 1/\lambda$ for every $\lambda > 0$.
The Lumer–Phillips theorem replaces this bound by dissipativity, which is often a one-line integration by parts, plus solvability for one $\lambda_0$.
For a second-order elliptic operator with Dirichlet conditions, the solvability usually comes from the Lax–Milgram theorem.
For a self-adjoint operator $A \le 0$ on a Hilbert space, both conditions hold, and the semigroup is $e^{tA}$ given by the spectral theorem.
