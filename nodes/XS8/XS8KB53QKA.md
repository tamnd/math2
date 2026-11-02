---
tag: XS8KB53QKA
kind: definition
name: Shilov boundary
msc: [46J20, 46J10]
defines: JHQNT58FEH
uses: [M7JVFJ3MMX, VWNSHKJT92]
sources:
  - url: https://en.wikipedia.org/wiki/Shilov_boundary
---

## Definition

Let $A$ be a commutative complex [[Banach algebra|9KYWN94QDN]] with unit, and let $\Delta(A)$ be its [[character space|M7JVFJ3MMX]], a compact Hausdorff space.
For $a \in A$, let $\hat a$ be its [[Gelfand transform|VWNSHKJT92]].
A *boundary* for $A$ is a subset $F \subseteq \Delta(A)$ such that, for every $a \in A$,
$$\max_{\varphi \in \Delta(A)} \abs{\hat a(\varphi)} = \sup_{\varphi \in F} \abs{\hat a(\varphi)}.$$
The *Shilov boundary* $\partial A$ is the smallest closed boundary for $A$: a closed boundary contained in every closed boundary.

## Remarks

The existence of a smallest closed boundary is a theorem of Shilov: the intersection of all closed boundaries is again a boundary.

Example: the disc algebra $A(\mathbb{D})$ of continuous functions on the closed unit disc $\overline{\mathbb{D}}$ that are holomorphic in the open disc, with the sup norm.
Its character space is $\overline{\mathbb{D}}$, through the evaluations at points.
By the maximum modulus principle, the unit circle $\mathbb{T}$ is a closed boundary.
No proper closed subset $F \subsetneq \mathbb{T}$ is a boundary.
Indeed, let $\zeta \in \mathbb{T} \setminus F$; the function $f(z) = (1 + \overline{\zeta} z) / 2$ satisfies $\abs{f} < 1$ on $\overline{\mathbb{D}} \setminus \set{\zeta}$ and $f(\zeta) = 1$.
So its supremum on the compact set $F$ is less than $1$.
Hence $\partial A(\mathbb{D}) = \mathbb{T}$.

Non-example: for the disc algebra, the circle $\set{\abs{z} = 1/2}$ is closed but not a boundary, since $f(z) = z$ has maximum modulus $1/2$ there and $1$ on $\overline{\mathbb{D}}$.

For $A = C(X)$ with $X$ compact Hausdorff, the Shilov boundary is all of $X$.
Indeed, if $F \subsetneq X$ is closed and $x \notin F$, Urysohn's lemma gives $f \in C(X)$ with $f(x) = 1$ and $f = 0$ on $F$, so $F$ is not a boundary.
