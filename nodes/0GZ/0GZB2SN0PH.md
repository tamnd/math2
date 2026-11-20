---
tag: 0GZB2SN0PH
kind: example
name: Spaces of functions and sequences
msc: ["15A03", "46E99"]
topics: [MVH97H8B2J]
audience: ug1
instance_of: [000AYPA9AJ]
uses: [05EGHEQZAW, 0X3WGX95FE, 0K57YG3BB8, 0G9EKM0E15]
sources:
  - url: https://en.wikipedia.org/wiki/Function_space
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Examples_of_vector_spaces
    locator: Function spaces
  - book: isbn:9783031410253
    locator: Section 1B
same_as:
  wikidata: Q934367
  wikipedia: Function space
---

## Example

Let $F$ be a field and let $S$ be a set.
Let $F^S$ be the set of all functions $f \colon S \to F$, with the pointwise operations
$$(f + g)(s) = f(s) + g(s), \qquad (af)(s) = a\, f(s)$$
for $f, g \in F^S$, $a \in F$ and $s \in S$.
We check the axioms of the [[definition|05EGHEQZAW]] at each point $s$.

1. Axiom 1: $((f + g) + h)(s) = (f(s) + g(s)) + h(s) = f(s) + (g(s) + h(s)) = (f + (g + h))(s)$, by associativity in $F$.
2. Axiom 2: $(f + g)(s) = f(s) + g(s) = g(s) + f(s) = (g + f)(s)$.
3. Axiom 3: the zero function $0(s) = 0$ satisfies $(f + 0)(s) = f(s)$.
4. Axiom 4: the function $(-f)(s) = -f(s)$ satisfies $(f + (-f))(s) = 0$.
5. Axioms 5 to 8: each one is an identity in $F$ at each point; for example $((a + b)f)(s) = (a + b) f(s) = a f(s) + b f(s)$.

So $F^S$ is a [[vector space|000AYPA9AJ]] over $F$.
The same proof works for functions $S \to V$ with values in a vector space $V$.

Special cases:

- For $S = \set{1, \dots, n}$, the space $F^S$ is the [[coordinate space|~9949dfd5]] $F^n$.
- For $S = \N$, the space $F^{\N}$ is the space of all [[sequences|0G9EKM0E15]] $(a_0, a_1, a_2, \dots)$ in $F$.
- The finitely supported functions, which are $0$ at all but finitely many points, form a subspace $F^{(S)}$ of $F^S$.
- The [[continuous functions|0X3WGX95FE]] $[0, 1] \to \R$ form a subspace $C[0, 1]$ of $\R^{[0, 1]}$, because sums and scalar multiples of continuous functions are continuous, and $0$ is continuous.
- The [[differentiable functions|0K57YG3BB8]] $\R \to \R$ form a subspace, because $(f + ag)' = f' + a g'$.

As a numerical check, take $f(s) = s^2$ and $g(s) = \sin s$ in $C[0, 1]$; then $(2f - g)(1) = 2 - \sin 1$.

## Remarks

The functions $\delta_s$ with $\delta_s(s) = 1$ and $\delta_s(t) = 0$ for $t \ne s$ form a [[basis|0KCQ9Y3QKA]] of $F^{(S)}$.
They are not a basis of $F^S$ when $S$ is infinite: the constant function $1$ is not a finite linear combination of them.
If $S$ is infinite, then $F^S$ is infinite-dimensional, because $\delta_s$ for $s \in S$ is an independent family.
The functions $f$ with $f(0) = 1$ do not form a subspace, because they do not contain the zero function.
The [[sequence spaces|XYTN19EPF2]] of analysis, such as the bounded sequences, are subspaces of $\R^{\N}$; their norms and Schauder bases belong to functional analysis.

## Explanations

### L1 human

We add two functions by adding their values at each point.
We scale a function by scaling its values.
With these rules, functions behave like vectors, and the zero function is the zero vector.
A sequence is a function on $\N$, so sequences are vectors too.

### L2 human

To show that a set of functions is a vector space, we usually do not check all eight axioms.
We show that it is a [[subspace|00YC1D652K]] of $F^S$: it contains $0$ and is closed under sums and scalar multiples.
For example, the solutions of $y'' + y = 0$ form a subspace of the differentiable functions, because $(y_1 + a y_2)'' + (y_1 + a y_2) = 0$.
A trap: a function space with the pointwise operations is different from a function space with composition as its operation.

### L3 human

The space $F^S$ is the product of copies of $F$ indexed by $S$, and $F^{(S)}$ is the direct sum.
The space $F^{(S)}$ is the free vector space on $S$, and its dual is $F^S$.
For infinite $S$, the dimension of $F^S$ is $\abs{F}^{\abs{S}}$, by the Erdős-Kaplansky theorem, so it is strictly larger than $\abs{S}$.
