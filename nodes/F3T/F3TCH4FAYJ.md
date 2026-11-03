---
tag: F3TCH4FAYJ
kind: definition
name: Almost periodic function on a group
msc: ["43A60", "22D05"]
defines: N9WKQ0MSEK
uses: [92700QAB5Y, 0X3WGX95FE, 0R6EWFKRCF]
sources:
  - url: https://en.wikipedia.org/wiki/Almost_periodic_function
---

## Definition

Let $G$ be a [[topological group|92700QAB5Y]].
Let $C_b(G)$ be the Banach space of bounded [[continuous functions|0X3WGX95FE]] $G \to \C$ with the norm $\norm{f}_\infty = \sup_{x \in G} \abs{f(x)}$.
For $f \in C_b(G)$ and $a, b \in G$, let ${}_a f_b$ be the function $x \mapsto f(a x b)$.
A function $f \in C_b(G)$ is *almost periodic* if the set $\set{{}_a f_b : a, b \in G}$ is relatively [[compact|0R6EWFKRCF]] in $C_b(G)$.

## Remarks

It is a theorem that the left translates alone, or the right translates alone, already form a relatively compact set exactly when $f$ is almost periodic.
For an abelian group, left and right translates agree, and the definition is the one of [[almost periodic function|GZBSV8DYGS]].
The almost periodic functions form a closed subalgebra $AP(G)$ of $C_b(G)$ that contains the constants and is closed under complex conjugation.

Example: let $\pi$ be a continuous unitary representation of $G$ on $\C^n$, let $u, v \in \C^n$, and let $f(x) = \ip{\pi(x) u}{v}$.
Then ${}_a f_b(x) = \ip{\pi(x) \pi(b) u}{\pi(a)^{*} v}$.
The vectors $\pi(b) u$ and $\pi(a)^{*} v$ lie in spheres of $\C^n$, which are compact, and the map $(u', v') \mapsto (x \mapsto \ip{\pi(x) u'}{v'})$ is continuous into $C_b(G)$.
So the translates of $f$ lie in a compact set, and $f$ is almost periodic.

Non-example: on $G = \R$, the function $f(x) = \arctan x$ is bounded and continuous but not almost periodic.
The translates $f(x + n)$ converge pointwise to $\pi/2$ as $n \to \infty$, but $\abs{f(-n + n) - \pi/2} = \pi/2$ for all $n$, so no subsequence converges uniformly.

If $G$ is compact, every continuous function on $G$ is almost periodic.
