---
tag: XYPJ07PT5G
kind: definition
name: Almost periodic function
msc: [43A60, 42A75]
defines: GZBSV8DYGS
uses: [92700QAB5Y, 0X3WGX95FE, 0R6EWFKRCF]
sources:
  - url: https://en.wikipedia.org/wiki/Almost_periodic_function
---

## Definition

Let $G$ be an abelian [[topological group|92700QAB5Y]], written additively.
Let $C_b(G)$ be the space of bounded [[continuous functions|0X3WGX95FE]] $G \to \C$ with the norm $\norm{f}_\infty = \sup_{x \in G} \abs{f(x)}$.
For $f \in C_b(G)$ and $a \in G$, let $f_a(x) = f(x + a)$ be the translate of $f$ by $a$.
A function $f \in C_b(G)$ is *almost periodic* if the set of its translates $\set{f_a : a \in G}$ is relatively [[compact|0R6EWFKRCF]] in $C_b(G)$.
This means that its closure in the norm $\norm{\cdot}_\infty$ is compact.

## Remarks

Equivalently, every sequence of translates $f_{a_1}, f_{a_2}, \dots$ has a subsequence that converges uniformly on $G$.
This is Bochner's form of the definition.
For $G = \R$ it is equivalent to Bohr's definition through relatively dense sets of almost periods, see [[Bohr almost periodic function|ED69H4C3PK]].
For a locally compact abelian group $G$, the almost periodic functions are exactly the functions $F \circ b$, where $b \colon G \to bG$ is the [[Bohr compactification|G852FHZ3W1]] and $F$ is continuous on $bG$.

Example: on $\R$, let $f(x) = \cos x + \cos(\sqrt{2} x)$.
The translates of $\cos$ are $\cos(x + a) = \cos a \cos x - \sin a \sin x$, the image of the circle $\set{(\cos a, \sin a)}$ under a continuous map into $C_b(\R)$, so they form a compact set.
The same holds for $\cos(\sqrt{2} x)$, and the translates of $f$ lie in the sum of these two compact sets, which is compact.
So $f$ is almost periodic.

Non-example: $f(x) = \arctan x$ on $\R$ is bounded and continuous, but not almost periodic.
The translates $f_n$, $n = 1, 2, \dots$, converge pointwise to the constant $\pi/2$.
A uniformly convergent subsequence would have the same limit, but $\abs{f_n(-n) - \pi/2} = \pi/2$ for every $n$.
