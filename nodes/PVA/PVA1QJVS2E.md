---
tag: PVA1QJVS2E
kind: statement
role: theorem
name: Grauert's solution of the Levi problem for manifolds
msc: ["32E40", 32Q28, 32U10]
uses: [JSGWAN2RJV, FGSKR6ZS3Q, HMCD0JBFST, 6BJB149MDK]
about: [47CVS9RJ9D, HMCD0JBFST]
sources:
  - url: https://en.wikipedia.org/wiki/Stein_manifold
---

## Statement

Let $X$ be a [[complex manifold|JSGWAN2RJV]] that is second countable.
Then $X$ is a [[Stein manifold|HMCD0JBFST]] if and only if $X$ has a smooth strictly [[plurisubharmonic exhaustion function|FGSKR6ZS3Q]].

## Remarks

The direction from Stein to the exhaustion function is easy.
A Stein manifold has a proper holomorphic embedding $F \colon X \to \C^N$, and then $\varphi = \abs{F}^2$ is smooth, strictly plurisubharmonic, and an exhaustion because $F$ is proper.
Grauert proved the converse in 1958.
His proof enlarges the sublevel sets $\set{\varphi < c}$ step by step and uses a finiteness theorem for cohomology on strongly pseudoconvex domains.
A later proof by Hörmander uses $L^2$ estimates for $\bar\partial$.
Example: the unit ball $B \subseteq \C^n$ is Stein, since $-\log(1 - \abs{z}^2)$ is a smooth strictly plurisubharmonic exhaustion function.
Strictness is needed: on a compact complex manifold $X$ of positive dimension, every constant is a smooth plurisubharmonic exhaustion function, yet $X$ is not Stein.

## Explanations

### L1 human

A Stein manifold is a complex manifold with very many global holomorphic functions.
The theorem says that this is the same as having a function that behaves like $\abs{z}^2$ on $\C^n$.
Such a function grows to infinity at the ends of the manifold and is strictly convex in the complex sense.
So a question about the existence of holomorphic functions is reduced to the existence of one real function with a convexity property.

### L2 human

For domains in $\C^n$ the theorem gives back [[Oka's solution of the Levi problem|6BJB149MDK]], after one smooths a continuous plurisubharmonic exhaustion and adds $\abs{z}^2$ to make it strict.
The function $\varphi$ is a Morse function after a small perturbation, and the strict plurisubharmonicity bounds the indices of its critical points by $\dim_\C X$.
This gives the result of Andreotti and Frankel that a Stein manifold of complex dimension $n$ has the homotopy type of a CW complex of real dimension at most $n$.
The Andreotti–Grauert theorem generalizes the theorem to $q$-convex manifolds.
