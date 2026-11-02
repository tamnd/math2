---
tag: TA0NREQMPX
kind: definition
name: Degree of a projective variety
msc: [14C17, 14N05]
defines: 1XG9GSHZ3N
uses: [A4H4CZ2V35, ZT9A6JK8QF, RMH4FBCFDA, 36X2WTHYCB]
sources:
  - url: https://en.wikipedia.org/wiki/Degree_of_an_algebraic_variety
---

## Definition

Let $k$ be an algebraically closed field and let $X \subseteq \mathbb{P}^n_k$ be a [[projective variety|A4H4CZ2V35]] of [[dimension|36X2WTHYCB]] $d$.
Let $I(X) \subseteq S = k[x_0, \dots, x_n]$ be its homogeneous ideal, and let $P_X$ be the [[Hilbert polynomial|RMH4FBCFDA]] of the graded ring $S/I(X)$.
Then $P_X$ has degree $d$ and leading coefficient $e/d!$ for a positive integer $e$.
The *degree* of $X$ is $\deg X = e$.

## Remarks

Equivalently, $\deg X$ is the number of points of $X \cap L$ for a general linear subspace $L \subseteq \mathbb{P}^n$ of dimension $n - d$.

Example: let $X = V(f) \subseteq \mathbb{P}^2$ with $f$ an irreducible homogeneous polynomial of degree $e$.
The exact sequence $0 \to S(-e) \to S \to S/(f) \to 0$ gives $P_X(t) = \binom{t+2}{2} - \binom{t-e+2}{2} = et - e(e-3)/2$.
Here $d = 1$ and the leading coefficient is $e$, so $\deg X = e$.

Non-example of the geometric form: the conic $X = V(xz - y^2)$ has degree $2$.
The line $y = 0$ meets it in the two points $[1:0:0]$ and $[0:0:1]$.
The tangent line $x = 0$ meets it only in $[0:0:1]$.
The tangent line is not general, so it does not compute the degree; it counts the point with multiplicity $2$.

The degree depends on the embedding: $\mathbb{P}^1$ embedded as a line has degree $1$, and embedded as the conic above it has degree $2$.
For a hypersurface $V(f)$ with $f$ irreducible, the degree of the variety is the degree of $f$.
