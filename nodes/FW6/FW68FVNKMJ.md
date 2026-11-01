---
tag: FW68FVNKMJ
kind: definition
name: Galois connection between subgroups and subfields
msc: [12F10, 06A15]
defines: R3625YKQC0
uses: [0WQ1A8SHTZ, 02NBKVQFRQ, 0KMJ6919WS]
sources:
  - url: https://en.wikipedia.org/wiki/Galois_connection
---

## Definition

Let $L/K$ be a [[field extension|0WQ1A8SHTZ]], and let $G = \Aut(L/K)$ be the group of field automorphisms of $L$ that fix every element of $K$.
Let $\mathcal{S}$ be the set of subgroups of $G$ and let $\mathcal{F}$ be the set of [[intermediate fields|02NBKVQFRQ]] of $L/K$, both ordered by inclusion.
For $H \in \mathcal{S}$, let $L^H = \set{x \in L : \sigma(x) = x \text{ for all } \sigma \in H}$ be the [[fixed field|0KMJ6919WS]] of $H$.
For $E \in \mathcal{F}$, let $\Aut(L/E) = \set{\sigma \in G : \sigma(x) = x \text{ for all } x \in E}$.
The *Galois connection between subgroups and subfields* of $L/K$ is the pair of maps
$$\mathcal{S} \to \mathcal{F},\ H \mapsto L^H \qquad \text{and} \qquad \mathcal{F} \to \mathcal{S},\ E \mapsto \Aut(L/E).$$
It is an antitone Galois connection: for all $H \in \mathcal{S}$ and $E \in \mathcal{F}$,
$$E \subseteq L^H \iff H \subseteq \Aut(L/E).$$

## Remarks

Both sides of the equivalence say that every element of $H$ fixes every element of $E$, which is the check.
From the equivalence, $H \subseteq \Aut(L/L^H)$ and $E \subseteq L^{\Aut(L/E)}$, and each map reverses inclusions.
Example: for $L = \Q(\sqrt{2}, \sqrt{3})$ over $\Q$, the group $G$ has four elements, and the maps are inverse bijections between its five subgroups and the five intermediate fields.
Non-example of a bijection: for $L = \Q(\sqrt[3]{2})$ over $\Q$, the group $G$ is trivial, because $\sqrt[3]{2}$ is the only cube root of $2$ in the real field $L$.
Then the map $E \mapsto \Aut(L/E)$ sends both $\Q$ and $L$ to the trivial group, so it is not injective.
The maps are inverse bijections when $L/K$ is a finite [[Galois extension|0DS2F7GK05]], by the [[fundamental theorem of Galois theory|0T1Q8D0FW8]].
