---
tag: TMY3M75EK8
kind: definition
name: Iterated function system
msc: [28A80, 37C70]
defines: 75B8VHDGSA
uses: [0BY52JW6NK, 0QN69YA357, 00R0X1WGPX]
sources:
  - url: https://en.wikipedia.org/wiki/Iterated_function_system
---

## Definition

Let $(X, d)$ be a [[complete metric space|0BY52JW6NK]].
An *iterated function system* on $X$ is a finite family $f_1, \ldots, f_N \colon X \to X$, with $N \ge 1$, of [[contractions|0QN69YA357]]: there are constants $r_i < 1$ with $d(f_i(x), f_i(y)) \le r_i \, d(x, y)$ for all $x, y \in X$.
Its *attractor* is a nonempty [[compact|00R0X1WGPX]] set $A \subseteq X$ with
$$A = f_1(A) \cup \cdots \cup f_N(A).$$

## Remarks

Hutchinson's theorem says that the attractor exists and is unique.
The proof applies the [[Banach fixed point theorem|0VK6VEH345]] to the map $K \mapsto \bigcup_i f_i(K)$ on the space of nonempty compact subsets of $X$ with the Hausdorff metric.
This space is complete, and the map is a contraction on it with constant $\max_i r_i$.
So for every nonempty compact $K_0$, the iterates $K_{m+1} = \bigcup_i f_i(K_m)$ converge to $A$.

Example: on $\R$, the maps $f_1(x) = x/2$ and $f_2(x) = x/2 + 1/2$ are contractions with constant $\frac{1}{2}$, and $f_1([0, 1]) \cup f_2([0, 1]) = [0, \frac{1}{2}] \cup [\frac{1}{2}, 1] = [0, 1]$.
So the attractor is $[0, 1]$.
With $f_1(x) = x/3$ and $f_2(x) = x/3 + 2/3$ the attractor is the [[Cantor set|0BXNDZFQME]].

Non-example: the family $g_1(x) = x/3$, $g_2(x) = x + 1$ on $\R$ is not an iterated function system, since $g_2$ is not a contraction.
It has no nonempty compact set $A$ with $A = g_1(A) \cup g_2(A)$: the maximum $a$ of such an $A$ would satisfy $a + 1 \in A$, which is impossible.

Suppose that the maps are similarities with ratios $r_i$ and that the pieces $f_i(A)$ do not overlap too much (the open set condition).
Then the [[Hausdorff dimension|SSNFTHZ6YJ]] of $A$ is the number $s$ with $\sum_i r_i^s = 1$.
