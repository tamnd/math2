---
tag: GE0HX2KMMZ
kind: statement
role: theorem
name: Fabry gap theorem
msc: ["30B10", "30B40"]
uses: [0VP56B4EMX, 0660QX1VPR, PQFEA12AHA, 0M3YQJ81NB]
about: [PQFEA12AHA, 0VP56B4EMX]
sources:
  - url: https://en.wikipedia.org/wiki/Fabry_gap_theorem
same_as:
  wikidata: Q17011576
  wikipedia: Fabry gap theorem
---

## Statement

Let $(\lambda_k)_{k \ge 1}$ be a strictly increasing sequence of nonnegative integers such that $\lambda_k / k \to \infty$ as $k \to \infty$.
Let $(a_k)$ be complex numbers such that the [[power series|0VP56B4EMX]]
$$f(z) = \sum_{k=1}^{\infty} a_k z^{\lambda_k}$$
has a [[radius of convergence|0660QX1VPR]] $R$ with $0 < R < \infty$.
Then the circle $\abs{z} = R$ is a [[natural boundary|PQFEA12AHA]] of $f$.
That is, $f$ has no [[analytic continuation|0M3YQJ81NB]] to a neighbourhood of any point of this circle.

## Remarks

The condition $\lambda_k / k \to \infty$ says that the exponents that occur have density zero among the nonnegative integers.
It is weaker than the condition $\lambda_{k+1} \ge q \lambda_k$ with $q > 1$ of the [[Hadamard gap theorem|DA8M8VZZHC]], so the Fabry theorem contains the Hadamard theorem.
For example, the series $\sum_{k \ge 1} z^{k^2}$ has radius $1$, and $k^2 / k = k \to \infty$, so the unit circle is a natural boundary; the Hadamard theorem does not apply here, because $(k+1)^2 / k^2 \to 1$.
The gap condition cannot simply be dropped: the series $\sum_{k \ge 0} z^k = 1/(1-z)$ has radius $1$ and continues analytically across every point of the unit circle except $z = 1$.
The proof is harder than for the Hadamard theorem and is not sketched here.

## Explanations

### L1 human

A power series with very many missing powers cannot be extended beyond its disc of convergence at all.
Each point of the boundary circle is a singular point.
"Very many missing" means that among the first $N$ powers only a vanishing proportion appear.
The series $z + z^4 + z^9 + z^{16} + \cdots$ is an example.

### L2 human

Usually a power series has only a few singular points on its circle of convergence, and the function continues across the rest.
Gap theorems show the opposite behaviour for lacunary series.
The density condition on the exponents is the essential hypothesis, and it is much weaker than a fixed ratio between consecutive exponents.
It shows that lacunary series are a simple source of functions with a natural boundary.
