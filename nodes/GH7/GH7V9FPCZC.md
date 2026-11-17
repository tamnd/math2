---
tag: GH7V9FPCZC
kind: example
name: Composition of functions is not commutative
msc: [08A02]
topics: [BAZT8JJ70S]
audience: school
not_instance_of:
  - target: 099E72KTF8
    note: for f(x) = x + 1 and g(x) = 2x, f(g(0)) = 1, but g(f(0)) = 2
uses: [0THBK9V825, 0EPAT51DXQ, 05RWFKVTJ7]
sources:
  - url: https://en.wikipedia.org/wiki/Function_composition
    locator: Properties
---

## Example

Let $f, g \colon \mathbb{R} \to \mathbb{R}$ be the [[functions|0EPAT51DXQ]] $f(x) = x + 1$ and $g(x) = 2x$.
We show that $f \circ g \neq g \circ f$, so [[composition|0THBK9V825]] on the set of functions $\mathbb{R} \to \mathbb{R}$ is not [[commutative|099E72KTF8]].

1. $(f \circ g)(x) = f(2x) = 2x + 1$.
2. $(g \circ f)(x) = g(x + 1) = 2x + 2$.
3. At $x = 0$, $(f \circ g)(0) = 1$, but $(g \circ f)(0) = 2$.
4. Two functions that differ at one point are different, so $f \circ g \neq g \circ f$.

The same happens for [[permutations|05RWFKVTJ7]] of a finite set.
Let $s$ and $t$ be the permutations of $\{1, 2, 3\}$ that exchange $1$ and $2$, and $2$ and $3$, respectively.
We compose from right to left.

5. $(s \circ t)(1) = s(t(1)) = s(1) = 2$.
6. $(t \circ s)(1) = t(s(1)) = t(2) = 3$.
7. So $s \circ t \neq t \circ s$.

## Remarks

Some pairs of functions commute.
For example, each function commutes with itself and with the identity function, and $x \mapsto x + 1$ commutes with $x \mapsto x + 5$.
But commutativity asks for all pairs, and one bad pair is enough to break it.
On a set $X$ with one element there is only one function $X \to X$, so composition on that set of functions is commutative.
On a set with at least two elements, two different constant functions $c_1$ and $c_2$ give $c_1 \circ c_2 = c_1$ and $c_2 \circ c_1 = c_2$.
Thus composition of functions $X \to X$ is commutative only when $X$ has at most one element.
The example of permutations shows that the [[symmetric group|0515A6D2Y1]] on three points is not abelian.

## Explanations

### L1 human

Take a number, double it, then add $1$.
From $0$ we get $1$.
Now take the number, add $1$, then double it.
From $0$ we get $2$.
The order of the two steps changed the answer.

### L2 human

To show that composition of two given functions does not commute, compute $f \circ g$ and $g \circ f$ and find one point where they differ.
Remember that $f \circ g$ means "first $g$, then $f$".
A trap is to choose two functions that commute by chance, such as two translations $x \mapsto x + a$ and $x \mapsto x + b$.
The typical use of this non-example is to explain why the group axioms do not include commutativity: the most natural groups are groups of maps under composition.
