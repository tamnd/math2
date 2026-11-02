---
tag: GJM3PAVV96
kind: definition
name: Curve complex
msc: [57K20, 20F65, 30F60]
defines: KHEJ0FVZXT
uses: [VGJJVBZ1MQ, V8GZ0W1ZZ5, NJ787GZS1N]
sources:
  - url: https://en.wikipedia.org/wiki/Curve_complex
---

## Definition

Let $S$ be a compact connected orientable [[surface|VGJJVBZ1MQ]] of [[genus|NJ787GZS1N]] $g$ with $n$ boundary components, and assume $3g - 3 + n \ge 2$.
A simple closed curve in $S$ is *essential* when it bounds no disc in $S$.
It must also not cobound an annulus with a component of $\partial S$.
The *curve complex* $\mathcal{C}(S)$ is the [[simplicial complex|V8GZ0W1ZZ5]] such that:

1. its vertices are the isotopy classes of essential simple closed curves in $S$;
2. a set of $k + 1$ distinct vertices spans a $k$-simplex if and only if the classes have pairwise disjoint representatives.

## Remarks

A maximal set of pairwise disjoint, pairwise non-isotopic essential curves has $3g - 3 + n$ elements, a pants decomposition, so $\mathcal{C}(S)$ has dimension $3g - 4 + n$.
The [[mapping class group|JV5NYG913V]] acts on $\mathcal{C}(S)$, and under the hypothesis $3g - 3 + n \ge 2$ the complex is connected and has infinite diameter.

Example: for the sphere with $5$ boundary circles, $g = 0$ and $n = 5$, so $3g - 3 + n = 2$ and $\mathcal{C}(S)$ is a graph.
Each essential curve cuts off two of the boundary circles from the other three, and two such curves are joined by an edge when they can be made disjoint.

Non-example of clause 2: on a closed surface of genus $2$, let curves $a$ and $b$ meet transversally in one point.
Their algebraic intersection number is $\pm 1$, so they have no disjoint representatives.
So $a$ and $b$ are not joined by an edge.

For the torus, the once-punctured torus and the four-holed sphere, the definition gives a complex without edges.
For them one joins curves of minimal intersection by edges instead, and the result is the Farey graph.

## Explanations

### L1 human

The vertices are loops on the surface that cannot be shrunk away, counted up to sliding.
Simplices record which loops can coexist without crossings.
The condition on $g$ and $n$ excludes small surfaces where no two different loops are disjoint.
