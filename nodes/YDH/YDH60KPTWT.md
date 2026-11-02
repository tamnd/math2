---
tag: YDH60KPTWT
kind: statement
role: theorem
name: Amitsur–Levitzki theorem
msc: [16R10, 15A24]
uses: [0310REJJY8, 0JXZKX526R, 0515A6D2Y1, 02DKV69ZH0, C0EDT81EGH, 2P3Y2FRCSZ, 0MDMZ965VE, 0F765KFC2J]
about: [C0EDT81EGH, 0JXZKX526R]
sources:
  - url: https://en.wikipedia.org/wiki/Amitsur–Levitzki_theorem
same_as:
  wikidata: Q4746948
  wikipedia: Amitsur–Levitzki theorem
---

## Statement

Let $K$ be a [[commutative ring|0310REJJY8]] with identity and let $n \ge 1$.
For $m \ge 1$, the *standard polynomial* of degree $m$ is
$$s_m(x_1, \ldots, x_m) = \sum_{\sigma \in S_m} \sgn(\sigma) \, x_{\sigma(1)} x_{\sigma(2)} \cdots x_{\sigma(m)},$$
where $S_m$ is the [[symmetric group|0515A6D2Y1]] and $\sgn$ is the [[sign of a permutation|02DKV69ZH0]].

1. For all [[matrices|0JXZKX526R]] $A_1, \ldots, A_{2n} \in M_n(K)$, one has $s_{2n}(A_1, \ldots, A_{2n}) = 0$.
2. If $K \ne 0$, then $M_n(K)$ satisfies no monic [[polynomial identity|C0EDT81EGH]] of degree less than $2n$.

## Remarks

Part 2 is the easy part.
A monic identity of degree $d < 2n$ can be replaced by a multilinear monic one of the same degree.
One evaluates it on the first $d$ matrix units of the staircase $e_{11}, e_{12}, e_{22}, e_{23}, \ldots, e_{n-1,n}, e_{nn}$.
Only the product in the staircase order is nonzero, so the identity would have to have coefficient $0$ on that monomial, and after renaming variables this contradicts monicity.
For part 1 there are several proofs: the original combinatorial one, a short proof by Rosset that works in the [[exterior algebra|0MDMZ965VE]], and proofs based on the [[Cayley–Hamilton theorem|0F765KFC2J]].

Example: for $n = 1$, part 1 says $ab - ba = 0$ for scalars $a, b$, which is commutativity.
For $n = 2$, it says that the alternating sum of the $24$ products of four $2 \times 2$ matrices in all orders is $0$.

The degree $2n$ is the best possible by part 2: $M_n(K)$ does not satisfy $s_{2n-1}$.

## Explanations

### L1 human

Matrix multiplication is not commutative, but it is not completely free either.
Take any $2n$ matrices of size $n \times n$ and multiply them in all possible orders.
Add the products, each with the sign given by the parity of its order: the result is always the zero matrix.
For $1 \times 1$ matrices this is just $ab = ba$.

### L2 human

The theorem says that $M_n(K)$ is a [[polynomial identity ring|C0EDT81EGH]] with the standard identity $s_{2n}$, and that $2n$ is the minimal degree of an identity.
This fact is the base of the theory of PI rings, since by Kaplansky's and Posner's theorems many PI rings embed in matrix rings over commutative rings or fields.
The minimal degree $2n$ of an identity is then a measure of the size of the matrices needed.
