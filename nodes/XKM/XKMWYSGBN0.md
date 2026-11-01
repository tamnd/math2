---
tag: XKMWYSGBN0
kind: definition
name: Prime end
msc: [30D40, 30C35]
defines: GNWE3XR0ZG
uses: [075C629XTH, 0JJ9J1XZ8G, 0R37DFJKFW]
sources:
  - url: https://en.wikipedia.org/wiki/Prime_end
---

## Definition

Let $\Omega \subset \C$ be a bounded [[simply connected domain|075C629XTH]] with [[boundary|0JJ9J1XZ8G]] $\partial\Omega$.
A *crosscut* of $\Omega$ is a set $C \subset \Omega$ that is homeomorphic to the open interval $(0, 1)$ and whose closure is $C \cup \set{a, b}$ with $a, b \in \partial\Omega$.
Then $\Omega \setminus C$ has exactly two [[connected components|0R37DFJKFW]].

A *null chain* is a sequence $(C_n)_{n \ge 0}$ of crosscuts of $\Omega$ such that:

1. the closures $\overline{C_n}$ and $\overline{C_{n+1}}$ are disjoint for all $n$;
2. for each $n \ge 1$, the crosscut $C_n$ separates $C_0$ from $C_{n+1}$ in $\Omega$;
3. the diameter of $C_n$ tends to $0$.

For a null chain, let $V_n$ be the component of $\Omega \setminus C_n$ that does not contain $C_0$, so $V_1 \supset V_2 \supset \cdots$.
Two null chains $(C_n)$ and $(C'_n)$, with domains $V_n$ and $V'_n$, are *equivalent* if for each $m$ there is an $n$ with $V_n \subseteq V'_m$ and $V'_n \subseteq V_m$.
A *prime end* of $\Omega$ is an equivalence class of null chains.

## Remarks

Example: for the unit disc $\mathbb{D}$ and a point $\zeta$ with $\abs{\zeta} = 1$, the arcs $C_n = \set{z \in \mathbb{D} : \abs{z - \zeta} = 2^{-n}}$ for $n \ge 1$, relabelled from $0$, form a null chain.
Their closures are disjoint, each arc separates the previous one from the next, and their diameters tend to $0$.
Every null chain of $\mathbb{D}$ shrinks to a single boundary point, and the prime ends of $\mathbb{D}$ correspond to the points of the unit circle.
Non-example: in $\mathbb{D}$, the vertical chords $C_n = \set{z \in \mathbb{D} : \operatorname{Re} z = 1/(n+2)}$ satisfy clauses 1 and 2, but their diameters $2\sqrt{1 - (n+2)^{-2}}$ tend to $2$, so clause 3 fails.
The *impression* of a prime end is the intersection of the closures $\overline{V_n}$; it is a nonempty compact connected subset of $\partial\Omega$.
Carathéodory's prime end theorem says that a conformal map of $\mathbb{D}$ onto $\Omega$ induces a bijection from the unit circle onto the set of prime ends of $\Omega$.
