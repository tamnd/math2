---
tag: REWYZ8N7EN
kind: statement
role: lemma
name: The kernel of a linear map is a subspace
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
about: [0S23E6YE83]
uses: [02YFME3RGW, 0EPTJA5QV4]
sources:
  - url: https://en.wikipedia.org/wiki/Kernel_(linear_algebra)
    locator: Properties
  - book: isbn:9780134860244
    locator: Section 2.1
  - book: isbn:9783031410253
    locator: Chapter 3
---

## Statement

The lemma says that the vectors sent to zero form a subspace, and that two vectors have the same image exactly when they differ by such a vector.
Let $F$ be a field, let $V$ and $W$ be vector spaces over $F$, and let $T \colon V \to W$ be a linear map.
Then the [[kernel|02YFME3RGW]] $\ker T$ is a [[linear subspace|0EPTJA5QV4]] of $V$.
Also, for $u, v \in V$, we have $T(u) = T(v)$ if and only if $u - v \in \ker T$.

## Remarks

### Why the hypotheses are needed

Linearity is needed.
For the non-linear map $f(x, y) = xy$ on $\R^2$, the zero set $\{f = 0\}$ is the union of the two axes.
It contains $(1, 0)$ and $(0, 1)$, but not their sum $(1, 1)$, since $f(1, 1) = 1$.

The value $0$ is needed as well.
The set $\{v : T(v) = w\}$ with $w \ne 0$ [[is not a subspace|HSXSS57MS3]], because it does not contain $0$.

### A worked use

For $T(x, y) = x - 2y$ from $\R^2$ to $\R$, the kernel is the line $x = 2y$.
The lemma says we only need one vector in the kernel to describe it, for example $(2, 1)$, and then every multiple of it lies in the kernel too.
The second part answers a different question: which vectors have the same image as $(3, 0)$?
Since $T(3, 0) = 3$, they are the vectors $(3, 0) + t(2, 1)$, and indeed $T(3 + 2t, \; t) = 3 + 2t - 2t = 3$.

### What it gives you

The solution set of a homogeneous system $Ax = 0$ is a subspace of $F^n$, the [[null space|0PHDYNR24D]].
If $T(v_0) = w$, then the solution set of $T(v) = w$ is $v_0 + \ker T$, by the second part, and this is the [[structure of the solution set|PDH3HKXWAZ]] for linear systems.
When $V$ is finite-dimensional, the kernel has a dimension, the [[nullity|0APCFW7639]].

### The converse and generalizations

Every subspace $U$ of $V$ is a kernel: it is the kernel of the quotient map $V \to V/U$ onto the [[quotient space|0BR3FY5Q8M]].
The kernel of a homomorphism of modules is a submodule, and the kernel of a [[group homomorphism|0JYTG5K9Y4]] is a normal subgroup, with the same proof.

## Explanations

### L1 human

The vectors sent to zero by a linear map form a subspace.
The zero vector is one of them, and sums and multiples of them are again sent to zero.
For example, if $T(u) = 0$ and $T(v) = 0$, then $T(u + v) = 0 + 0 = 0$.

### L2 human

Here is a typical use: show that the matrices $X \in M_2(\R)$ with $X + X^{\mathsf T} = 0$ form a subspace.
The map $X \mapsto X + X^{\mathsf T}$ is linear, because the transpose is linear and sums of linear maps are linear.
The set in question is its kernel, so the lemma says it is a subspace, with no closure checks needed.
These are the skew-symmetric matrices $\begin{pmatrix} 0 & b \\ -b & 0 \end{pmatrix}$, a subspace of dimension $1$.
Watch out: the lemma needs a linear map, and the zero set of a non-linear map such as $xy$ is usually not a subspace.
