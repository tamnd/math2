---
tag: ~adaeb46b
kind: definition
name: Dual space
msc: [15A04]
defines: ~d8a7f260
uses: [~9fcf0268, ~c02afeb7]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_space
    locator: Algebraic dual space
---

## Definition

Let $F$ be a field and let $V$ be a vector space over $F$.
The *dual space* of $V$ is the vector space
$$V^* = \Hom_F(V, F)$$
of all [[linear forms|~478dba8d]] on $V$.
Its operations are pointwise: $(f + g)(v) = f(v) + g(v)$ and $(af)(v) = a f(v)$.

## Remarks

It is a special case of the [[space of linear maps|~0acf07d9]].
If $\dim V = n$ is finite, then $\dim V^* = n$, see [[the dimension of the dual space|~38adde5d]].
The elements of $F^n$ act on column vectors by the dot product, and this identifies $(F^n)^*$ with $F^n$.
For infinite-dimensional $V$, the space $V^*$ is not isomorphic to $V$.

## Explanations

### L1 human

The dual space collects all the ways to measure a vector by one linear number.
On $\R^3$, each linear form is a dot product with a fixed vector.
So, in finite dimensions, the dual space looks like the original space, but its elements play a different role.
