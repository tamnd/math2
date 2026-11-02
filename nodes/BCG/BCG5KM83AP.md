---
tag: BCG5KM83AP
kind: statement
role: theorem
name: Jordan–Hölder theorem for modular lattices
msc: [06C05, 06B05]
uses: [QX7WZ92QAK, 4HHDPZ4BDY, 3AX549FFFM]
about: [QX7WZ92QAK]
sources:
  - url: https://en.wikipedia.org/wiki/Composition_series
---

## Statement

Let $L$ be a [[modular lattice|QX7WZ92QAK]] and let $a \le b$ in $L$.
Write $x \lessdot y$ when $y$ [[covers|4HHDPZ4BDY]] $x$.
For $u \le v$ in $L$, write $[u, v] = \set{z \in L : u \le z \le v}$.
Two such intervals are *transposed* if they have the form $[x \wedge y, x]$ and $[y, x \vee y]$ for some $x, y \in L$, in either order.
Two intervals are *projective* if they are joined by a finite sequence of intervals in which each consecutive pair is transposed.

Let
$$a = x_0 \lessdot x_1 \lessdot \cdots \lessdot x_m = b \quad\text{and}\quad a = y_0 \lessdot y_1 \lessdot \cdots \lessdot y_n = b$$
be two finite [[maximal chains|3AX549FFFM]] from $a$ to $b$.
Then $m = n$, and there is a permutation $\sigma$ of $\set{1, \dots, m}$ such that $[x_{i-1}, x_i]$ is projective to $[y_{\sigma(i)-1}, y_{\sigma(i)}]$ for each $i$.

## Remarks

The proof is by induction on $m$.
If $x_1 = y_1$, apply induction to the interval $[x_1, b]$.
Otherwise $x_1$ and $y_1$ both cover $a = x_1 \wedge y_1$, and modularity makes the transposed intervals $[y_1, x_1 \vee y_1]$ and $[a, x_1]$ isomorphic, so $x_1 \vee y_1$ covers both $x_1$ and $y_1$.
Choosing a maximal chain from $x_1 \vee y_1$ to $b$ and applying induction in $[x_1, b]$ and in $[y_1, b]$ gives the result.

Example: the lattice of submodules of a module $M$ is modular.
For submodules $X$ and $Y$, the transposed intervals give the isomorphism $X / (X \cap Y) \cong (X + Y) / Y$, so projective intervals of length one give isomorphic simple quotients.
So the theorem yields the [[Jordan–Hölder theorem for modules|M1ABX18FC4]]: two [[composition series|0XV2A49X6Q]] of a module have the same length and isomorphic factors up to order.

Without modularity the equal-length conclusion can fail.
In the [[pentagon lattice N5|DHC8TZXGYS]], the maximal chains $0 < a < c < 1$ and $0 < b < 1$ have lengths $3$ and $2$.

## Explanations

### L1 human

In a modular lattice, any two ways of climbing from $a$ to $b$ by smallest possible steps use the same number of steps.
Moreover, the steps of one climb match the steps of the other, up to order, in a precise sense.
This is the lattice form of the familiar fact that composition series of a module have the same length and the same factors.

### L2 human

The theorem shows that modular lattices satisfy the [[Jordan–Dedekind chain condition|RW7YC3HG0S]] on every interval of finite length, so such intervals have a well-defined length.
For submodule lattices it recovers the Jordan–Hölder theorem for modules, with projectivity of intervals giving isomorphism of factors.
The [[Jordan–Hölder theorem|0E088ZP533]] for groups is a close relative, with subnormal series in place of chains of submodules.
The same equal-length conclusion holds in [[semimodular lattices|C1NET23GG0]], which is why matroids and geometric lattices have a rank function.
