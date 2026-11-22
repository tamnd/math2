---
tag: 0912EEEVCT
kind: statement
role: theorem
name: Injective, surjective and bijective endomorphisms
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
about: [0J7H0YBFDJ, 0B8T10CE7N]
uses: [0PTF1PTJK0, 018W3V3TCT, 0PVG1CRAJN, 0XKH881BZ7, 0SNQEF7Z53]
sources:
  - url: https://en.wikipedia.org/wiki/Rank–nullity_theorem
    locator: Reformulations and generalizations
  - url: https://en.wikipedia.org/wiki/Fredholm_alternative
    locator: Linear algebra
  - url: https://en.wikipedia.org/wiki/Shift_operator
    locator: Properties of the shift operator
  - book: isbn:9783031410253
    locator: Chapter 3
  - book: isbn:9780134860244
    locator: Section 2.4
---

## Statement

For a linear map from a finite-dimensional space to itself, being one to one, being onto and being invertible are the same thing.

Let $F$ be a field, let $V$ be a [[finite-dimensional|018W3V3TCT]] vector space over $F$, and let $T \colon V \to V$ be an [[endomorphism|0PTF1PTJK0]] of $V$.
Then the following conditions are equivalent.

1. The map $T$ is [[injective|0PVG1CRAJN]].
2. The map $T$ is [[surjective|0XKH881BZ7]].
3. The map $T$ is [[bijective|0SNQEF7Z53]], so $T$ is an automorphism of $V$.

## Remarks

### Why the hypotheses are needed

Finite dimension is necessary.
On the space of sequences, the [[right shift|N1G1WQW59J]] is injective and not surjective, and the left shift is surjective and not injective.
On $F[x]$, multiplication by $x$ is injective and not surjective, since no multiple of $x$ equals $1$.
The source and the target must have the same dimension, as the injective map $\R \to \R^2$, $x \mapsto (x, 0)$, shows.
Linearity is necessary too: the map $x \mapsto e^x$ on the one-dimensional space $\R$ is injective but misses every $y \le 0$.

### What it gives you

To prove that an endomorphism of a finite-dimensional space is invertible, it is enough to check $\ker T = \{0\}$.
For a square matrix $A$, the system $Ax = 0$ has only the solution $x = 0$ exactly when $Ax = b$ has a solution for each $b$.
One-sided inverses are two-sided: if $S \circ T = \id_V$, then $T$ is injective, so $T$ is bijective and $S = T^{-1}$.
The same equivalence holds for a linear map $T \colon V \to W$ when $\dim V = \dim W < \infty$.

### The converse

The statement is an equivalence of three conditions, so every direction holds.
For a map between finite-dimensional spaces of different dimensions, the rank-nullity theorem shows that at most one of injective and surjective can hold.

### Generalizations

A map from a finite set to itself is injective if and only if it is surjective, which is a form of the [[pigeonhole principle|0HGVCWQGY3]].
The theorem is the simplest case of the [[Fredholm alternative|4HH8C9V8JQ]]: either $T$ is surjective, or $\ker T \ne \{0\}$.

## History

The equivalence is the finite-dimensional case of the Fredholm alternative, named after Fredholm.
He proved an analogue for integral equations of the form $\lambda \varphi - K\varphi = f$, where infinite dimension needs extra hypotheses on the operator $K$.

## Explanations

### L1 human

For a linear map from a finite-dimensional space to itself, one to one and onto are the same.
If the map sends no nonzero vector to $0$, then it reaches every vector, because the dimensions match.
A map from a finite set to itself behaves in the same way.

### L2 human

To show that $T(x, y) = (x + y, \; x - y)$ on $\R^2$ is invertible, solve $T(x, y) = (0, 0)$.
This gives $x = y = 0$, so $\ker T = \{0\}$ and $T$ is injective.
By the theorem, $T$ is also surjective, with no further work.
Watch out: the shortcut fails in infinite dimension, as the shift maps show.

### L3 human

The theorem says that the ring $\End(V)$ of a finite-dimensional space is [[Dedekind-finite|GV1HKEAWVN]]: $ST = I$ implies $TS = I$.
In infinite dimension, $\End(V)$ contains the shifts $L$ and $R$ with $LR = I$ and $RL \ne I$.
In the Fredholm theory of operators on Banach spaces, the [[index|2V9Q4KHY1T]] $\dim \ker T - \dim \operatorname{coker} T$ measures the failure.
In finite dimension, the index of every endomorphism is $0$.
