---
tag: 0TJ1V9DDPC
kind: statement
role: theorem
name: Third isomorphism theorem
msc: [20A05]
uses: [0CXXJNG5B6, 0YYWCNTPWR]
sources:
  - url: https://en.wikipedia.org/wiki/Isomorphism_theorems
    locator: Theorem C (groups)
---

## Statement

Let $G$ be a [[group|G5S1M9]], and let $N$ and $K$ be [[normal subgroups|0CB0DX5BVV]] of $G$ with $N \subseteq K$.
Then $K/N$ is a normal subgroup of $G/N$, and the map $(gN)(K/N) \mapsto gK$ is an [[isomorphism|08MG7H8JW5]] from $(G/N)/(K/N)$ to $G/K$.

## Remarks

The proof applies the [[first isomorphism theorem|0CXXJNG5B6]] to the surjective homomorphism $G/N \to G/K$, $gN \mapsto gK$, whose kernel is $K/N$.
For example, $(\mathbb{Z}/12\mathbb{Z})/(4\mathbb{Z}/12\mathbb{Z}) \cong \mathbb{Z}/4\mathbb{Z}$.
For finite groups, it gives $[G : K] = [G/N : K/N]$.

## Explanations

### L1 human

If you divide by $N$ and then by the image of $K$, you get the same result as dividing by $K$ in one step.
It looks like cancelling fractions: $(G/N)/(K/N) = G/K$.
The theorem makes this cancellation precise.
