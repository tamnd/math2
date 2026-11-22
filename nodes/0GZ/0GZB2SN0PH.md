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
$$(f + g)(s) = f(s) + g(s), \qquad (af)(s) = a\, f(s) \qquad (f, g \in F^S,\ a \in F,\ s \in S).$$
For example, with $f(s) = s^2$ and $g(s) = \sin s$ in $\mathbb{R}^{\mathbb{R}}$, the function $2f - g$ has the value $2 - \sin 1$ at $s = 1$.
Two functions are equal when they agree at every point, so we check each axiom of the [[definition|05EGHEQZAW]] at an arbitrary point $s$.

1. Axiom 1: $((f + g) + h)(s) = (f(s) + g(s)) + h(s) = f(s) + (g(s) + h(s)) = (f + (g + h))(s)$, by associativity in $F$.
2. Axiom 2: $(f + g)(s) = f(s) + g(s) = g(s) + f(s) = (g + f)(s)$, by commutativity in $F$.
3. Axiom 3: the zero function, with $0(s) = 0$ for all $s$, satisfies $(f + 0)(s) = f(s)$.
4. Axiom 4: the function $-f$, with $(-f)(s) = -f(s)$, satisfies $(f + (-f))(s) = 0$.
5. Axioms 5 to 8: each is an identity of $F$ at the point $s$; for example $((a + b)f)(s) = (a + b) f(s) = a f(s) + b f(s) = (af + bf)(s)$.

So $F^S$ is a [[vector space|000AYPA9AJ]] over $F$.
The same proof works for functions $S \to V$ with values in any vector space $V$.

## Remarks

### One construction, many spaces

Different choices of $S$ give the familiar spaces.
For $S = \{1, \dots, n\}$, a function is a list of $n$ values, so $F^S$ is the [[coordinate space|713F6AM1X1]] $F^n$.
For $S = \mathbb{N}$, a function is a [[sequence|0G9EKM0E15]] $(a_0, a_1, a_2, \dots)$, so $F^{\mathbb{N}}$ is the space of all sequences in $F$.
The [[sequence spaces|XYTN19EPF2]] of analysis, such as the bounded sequences, are subspaces of $\mathbb{R}^{\mathbb{N}}$.

### Subspaces of functions

Many useful spaces are [[subspaces|00YC1D652K]] of $F^S$, and for them we check only that $0$ is in the set and that sums and multiples stay in it.
The [[continuous functions|0X3WGX95FE]] $[0, 1] \to \mathbb{R}$ form the subspace $C[0, 1]$, because sums and multiples of continuous functions are continuous.
The [[differentiable functions|0K57YG3BB8]] $\mathbb{R} \to \mathbb{R}$ form a subspace, because $(f + ag)' = f' + a g'$.
The finitely supported functions, which vanish at all but finitely many points, form a subspace $F^{(S)}$.
In contrast, the functions with $f(0) = 1$ are not a subspace, because the zero function has $f(0) = 0$.

### A basis, and where it stops working

For each $s \in S$, let $\delta_s$ be the function with $\delta_s(s) = 1$ and $\delta_s(t) = 0$ for $t \ne s$.
The functions $\delta_s$ form a [[basis|0KCQ9Y3QKA]] of $F^{(S)}$, since a finitely supported $f$ equals $\sum_s f(s) \delta_s$, a finite sum.
Watch out: they are not a basis of $F^S$ when $S$ is infinite.
The constant function $1$ is nonzero at infinitely many points, while a finite combination of the $\delta_s$ is nonzero at only finitely many.
Still, the $\delta_s$ are independent, so $F^S$ is infinite-dimensional whenever $S$ is infinite.

## Explanations

### L1 human

You add two functions by adding their values at each point, and you scale a function by scaling its values.
For example, if $f(x) = x$ and $g(x) = x^2$, then $(f + g)(3) = 3 + 9 = 12$.
With these rules, functions behave like vectors, and the zero function is the zero vector.
A sequence is a function on the numbers $0, 1, 2, \dots$, so sequences are vectors too.

### L2 human

Here is a typical use: the sequences $(a_0, a_1, a_2, \dots)$ of real numbers with $a_{k + 2} = a_{k + 1} + a_k$ for all $k$ form a vector space.
They sit inside $\mathbb{R}^{\mathbb{N}}$, so it is enough to check the subspace conditions.
The zero sequence satisfies $0 = 0 + 0$.
If $a$ and $b$ satisfy the rule and $c \in \mathbb{R}$, then
$$(a + cb)_{k + 2} = a_{k + 2} + c b_{k + 2} = (a_{k + 1} + a_k) + c(b_{k + 1} + b_k) = (a + cb)_{k + 1} + (a + cb)_k.$$
So the solutions form a subspace, and a solution is fixed by its first two terms $a_0$ and $a_1$.
For example, $(1, 0, 1, 1, 2, \dots)$ and $(0, 1, 1, 2, 3, \dots)$ add to $(1, 1, 2, 3, 5, \dots)$, which again satisfies the rule.
Watch out: the rule $a_{k + 2} = a_{k + 1} + a_k + 1$ gives a set without the zero sequence, so it is not a subspace.

### L3 human

The space $F^S$ is the product of copies of $F$ indexed by $S$, and $F^{(S)}$ is their direct sum.
The space $F^{(S)}$ is the free vector space on $S$, and its dual space is $F^S$.
For infinite $S$, the dimension of $F^S$ is $|F|^{|S|}$ by the [[Erdős-Kaplansky theorem|S5ET1HG2ZX]], so it is strictly larger than $|S|$.
In analysis one adds a norm to subspaces of $F^S$, and then bases in the sense of infinite sums, such as Schauder bases, take the place of the finite combinations used here.
