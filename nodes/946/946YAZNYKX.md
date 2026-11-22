---
tag: 946YAZNYKX
kind: concept
name: Exact sequence of vector spaces
msc: ["15A03", "18G35"]
topics: [QHKTJ89V6S]
audience: grad
specializes: [JB7ZBFBA9C]
uses: [0NRYHJPQG2, 0S23E6YE83, 0WSFKKT6FF, 0BR3FY5Q8M]
sources:
  - url: https://en.wikipedia.org/wiki/Exact_sequence
    locator: Definition
  - book: isbn:9783031410253
    locator: Section 3E
---

## Summary

An exact sequence is a chain of linear maps in which each map kills exactly what the map before it produces.
It is a compact way to say that one space is built from a subspace and a quotient, and to keep track of kernels and images along a chain.
A sequence of vector spaces and [[linear maps|0NRYHJPQG2]]
$$V_0 \xrightarrow{f_0} V_1 \xrightarrow{f_1} V_2 \to \cdots \xrightarrow{f_{n-1}} V_n$$
is *exact at* $V_i$, for $0 < i < n$, when the [[image|0WSFKKT6FF]] of the incoming map equals the [[kernel|0S23E6YE83]] of the outgoing map, $\operatorname{im} f_{i-1} = \ker f_i$.
The sequence is *exact* when it is exact at every inner space.
A *short exact sequence* is an exact sequence
$$0 \to U \xrightarrow{f} V \xrightarrow{g} W \to 0,$$
which says exactly that $f$ is injective, $g$ is onto, and $\operatorname{im} f = \ker g$.

## Motivation

The three facts "$f$ is injective", "$g$ is onto" and "$\operatorname{im} f = \ker g$" turn up together again and again in linear algebra.
A short exact sequence packs them into one line.
It says that $V$ contains a copy $f(U)$ of $U$, and that the [[quotient|0BR3FY5Q8M]] $V / f(U)$ is a copy of $W$.
For example, a subspace $U$ of $V$ always gives $0 \to U \to V \to V / U \to 0$.

Longer exact sequences tie together the kernels and images of several maps, and they let you compute one dimension from the others.
For vector spaces the theory is short, because every short exact sequence splits and the dimensions obey one linear relation.
Exact sequences of modules, of groups and of sheaves are the basic language of homological algebra and algebraic topology, and there they need not split.
The vector space case is the model to keep in mind when you meet them.

## Notation

We write $0 \to U \to V \to W \to 0$ for a short exact sequence.
The $0$ at the left end means that $f$ is injective, because exactness at $U$ says $\ker f = \operatorname{im}(0 \to U) = 0$.
The $0$ at the right end means that $g$ is onto, because exactness at $W$ says $\operatorname{im} g = \ker(W \to 0) = W$.
Some books mark injective maps with $\hookrightarrow$ and onto maps with $\twoheadrightarrow$.
A short exact sequence *splits* when there is a linear map $s \colon W \to V$ with $g \circ s = \operatorname{id}_W$.

## Remarks

### A first check of exactness

Take $f \colon \R \to \R^3$, $f(t) = (t, t, t)$, and $g \colon \R^3 \to \R^2$, $g(x, y, z) = (x - y, y - z)$.
The map $f$ is injective, since $f(t) = 0$ forces $t = 0$.
The map $g$ is onto, because $g(a + b, b, 0) = (a, b)$.
In the middle, $g(t, t, t) = (0, 0)$ gives $\operatorname{im} f \subseteq \ker g$, and $g(x, y, z) = 0$ forces $x = y = z$, which gives the reverse inclusion.
So $0 \to \R \to \R^3 \to \R^2 \to 0$ is exact, as [[a short exact sequence with R³ in the middle|EEN9A35R25]] works out in full.

### Sequences that come for free

Every subspace $U \subseteq V$ gives the exact sequence $0 \to U \to V \to V / U \to 0$, with the inclusion and the quotient map.
The kernel of the quotient map is $U$, which is exactly the image of the inclusion.

Every linear map $T \colon V \to W$ gives a four-term exact sequence
$$0 \to \ker T \to V \xrightarrow{T} W \to W / \operatorname{im} T \to 0.$$
The last space is the *cokernel* of $T$, and the sequence is exact at $V$ because the image of $\ker T \to V$ is $\ker T$, and at $W$ because the kernel of $W \to W / \operatorname{im} T$ is $\operatorname{im} T$.

Every [[external direct sum|02WZB422CE]] gives $0 \to U \to U \oplus W \to W \to 0$, with $u \mapsto (u, 0)$ and $(u, w) \mapsto w$.

### What is not exact

The sequence $0 \to \R \to \R^2 \to \R \to 0$ with $f(t) = (t, 0)$ and $g(x, y) = x$ has $f$ injective and $g$ onto.
It fails in the middle: $\operatorname{im} f$ is the $x$-axis, while $\ker g$ is the $y$-axis.

The sequence $0 \to \R^2 \xrightarrow{f} \R^2 \to 0$ with $f(x, y) = (x, 0)$ is exact only if $f$ is both injective and onto.
This $f$ is neither, since $f(0, 1) = 0$ and $(0, 1)$ is not in the image.

### The rules you can use

[[Short exact sequences of vector spaces split|1GYTT98CC5]], so in $0 \to U \to V \to W \to 0$ the middle space is isomorphic to $U \oplus W$.
For finite-dimensional spaces this gives $\dim V = \dim U + \dim W$, which is the [[dimension of a quotient space|0SXDQ6TN00]] in another form.
In a longer exact sequence $0 \to V_0 \to \cdots \to V_n \to 0$ of finite-dimensional spaces, the [[alternating sum of dimensions|EFBRMNWDQM]] is $0$.
Applied to the four-term sequence of $T$, this is the [[rank-nullity theorem|0W4FSW1TVB]] with a cokernel term.
Duals keep exactness: if $0 \to U \to V \to W \to 0$ is exact, then so is $0 \to W^* \to V^* \to U^* \to 0$.

### Watch out

The most common mistake is to check only that $g \circ f = 0$.
That proves $\operatorname{im} f \subseteq \ker g$, which is weaker than exactness: $f = 0$ and $g = 0$ in $0 \to \R \to \R \to \R \to 0$ satisfy $g \circ f = 0$, but $f$ is not injective.
A second mistake is to drop the outer zeros: an exact sequence $U \to V \to W$ says nothing about whether $f$ is injective or $g$ is onto.
A third is to expect splitting outside linear algebra.
The exact sequence $0 \to \Z \xrightarrow{\cdot 2} \Z \to \Z / 2\Z \to 0$ of abelian groups does not split, since $\Z$ has no element of order $2$ but $\Z \oplus \Z / 2\Z$ does.

### History

The exactness axiom is one of the axioms for homology theories in Eilenberg and Steenrod's book *Foundations of Algebraic Topology* of 1952.
Cartan and Eilenberg's book *Homological Algebra* of 1956 built a general theory of modules on exact sequences.

### Try it

First, decide whether $0 \to \R \xrightarrow{f} \R^2 \xrightarrow{g} \R \to 0$ with $f(t) = (t, 2t)$ and $g(x, y) = 2x - y$ is exact.
It is: $f$ is injective, $g(1, 0) = 2 \ne 0$ makes $g$ onto, and $\ker g = \{(x, 2x)\} = \operatorname{im} f$.

Second, an exact sequence $0 \to \R^2 \to V \to \R^5 \to \R^4 \to 0$ is given.
The alternating sum $2 - \dim V + 5 - 4 = 0$ forces $\dim V = 3$.

## Explanations

### L1 human

Picture a line of machines, each taking vectors in and passing vectors on.
The line is exact when, at each machine in the middle, the vectors that it throws away are exactly the ones that the previous machine delivers.
A short exact sequence says that a big space is put together from a small space and a quotient.
For vector spaces the big space is just the two pieces side by side: in the example above, $\R^3$ is a line plus a plane, and $3 = 1 + 2$.

### L2 human

Here is a typical problem: show that $0 \to \R \xrightarrow{f} \R^3 \xrightarrow{g} \R^2 \to 0$, with $f(t) = (t, t, t)$ and $g(x, y, z) = (x - y, y - z)$, is exact, and split it.

1. At $\R$: $f(t) = 0$ forces $t = 0$, so $f$ is injective.
2. At $\R^3$: $g \circ f = 0$ gives one inclusion, and solving $x - y = 0$, $y - z = 0$ gives $\ker g = \R(1, 1, 1) = \operatorname{im} f$.
3. At $\R^2$: $g(a + b, b, 0) = (a, b)$, so $g$ is onto.
4. The map $s(a, b) = (a + b, b, 0)$ is linear and satisfies $g \circ s = \operatorname{id}$, so it splits the sequence.

The dimensions satisfy $1 - 3 + 2 = 0$.
Exactness is used in this way to reduce a question about $V$ to questions about the smaller spaces $U$ and $W$.
Watch out: step 2 needs both inclusions, and $g \circ f = 0$ alone gives only one.

### L3 human

General exact sequences belong to homological algebra, where one works with modules over a ring, sheaves, or objects of an abelian category.
There a short exact sequence need not split, and the failure is measured by the functor $\operatorname{Ext}^1$; functors such as $\operatorname{Hom}$ and $\otimes$ need not keep exactness, and the derived functors measure how far they fail.
Over a field every short exact sequence splits, so every additive functor keeps exactness, and dimension is the only invariant.
The alternating sum formula is the simplest case of the invariance of the [[Euler characteristic|RNDDWDAFJ5]] of a complex under passage to homology.
