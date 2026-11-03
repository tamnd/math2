---
tag: MTXTWTXYD2
kind: definition
name: Weakly almost periodic function
msc: ["43A60", "46A03"]
defines: KFPM82FQ8J
uses: [92700QAB5Y, 0X3WGX95FE, P6KHVSTPZV, 06GZ956657, 2MTN8CQWME]
sources:
  - url: https://en.wikipedia.org/wiki/Almost_periodic_function
---

## Definition

Let $G$ be a [[topological group|92700QAB5Y]].
Let $C_b(G)$ be the [[Banach space|06GZ956657]] of bounded [[continuous functions|0X3WGX95FE]] $G \to \C$ with the uniform norm.
For $f \in C_b(G)$ and $a \in G$, let $(L_a f)(x) = f(a x)$.
A function $f \in C_b(G)$ is *weakly almost periodic* if the set $\set{L_a f : a \in G}$ is relatively compact in the [[weak topology|P6KHVSTPZV]] of $C_b(G)$.

## Remarks

Using right translates instead of left translates gives the same class of functions.
Grothendieck's double limit criterion gives an equivalent form.
The function $f$ is weakly almost periodic if and only if, for all sequences $(x_n)$ and $(y_m)$ in $G$,
$$\lim_{n} \lim_{m} f(x_n y_m) = \lim_{m} \lim_{n} f(x_n y_m)$$
whenever both iterated limits exist.
Every [[almost periodic function|N9WKQ0MSEK]] is weakly almost periodic, since norm-compact sets are weakly compact.

Example: on $G = \Z$, let $f = \mathbf{1}_{\set{0}}$.
Its translates are the functions $\mathbf{1}_{\set{k}}$, which lie in the closed subspace $c_0(\Z)$.
Every bounded linear functional on $c_0(\Z)$ is $h \mapsto \sum_n h(n) c_n$ for some $(c_n)$ with $\sum \abs{c_n} < \infty$, so $\mathbf{1}_{\set{k}} \to 0$ weakly as $\abs{k} \to \infty$.
Hence every sequence of translates has a weakly convergent subsequence, with limit a translate or $0$, and by the [[Eberlein–Šmulian theorem|2MTN8CQWME]] $f$ is weakly almost periodic.

Non-example: on $G = \Z$, let $f = \mathbf{1}_{\set{0, 1, 2, \ldots}}$.
Take $x_n = n$ and $y_m = -m$.
Then $\lim_m f(n - m) = 0$ for each $n$, while $\lim_n f(n - m) = 1$ for each $m$.
The iterated limits are $0$ and $1$, so $f$ is not weakly almost periodic.

On a locally compact group, every continuous function vanishing at infinity and every coefficient $x \mapsto \ip{\pi(x) u}{v}$ of a unitary representation is weakly almost periodic.
