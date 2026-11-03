---
tag: RRRHWH9F6Y
kind: definition
name: Common knowledge
msc: [03B42, 91A27]
defines: 7BCMKF2P7X
uses: [08QMKTWF9T]
sources:
  - url: https://en.wikipedia.org/wiki/Common_knowledge_(logic)
---

## Definition

Let $\Omega$ be a set of states and let $I$ be a finite set of agents.
For each agent $i \in I$, let $\mathcal{P}_i$ be a [[partition|08QMKTWF9T]] of $\Omega$, and for $\omega \in \Omega$ let $\mathcal{P}_i(\omega)$ be the block of $\mathcal{P}_i$ that contains $\omega$.
An *event* is a subset $E \subseteq \Omega$.
Agent $i$ *knows* $E$ at $\omega$ if $\mathcal{P}_i(\omega) \subseteq E$; write $K_i(E) = \set{\omega \in \Omega : \mathcal{P}_i(\omega) \subseteq E}$.
The event $E$ is *common knowledge* at $\omega$ if
$$\omega \in K_{i_1} K_{i_2} \cdots K_{i_m}(E)$$
for every $m \ge 1$ and all agents $i_1, \dots, i_m \in I$.

## Remarks

Let the *meet* $\mathcal{M}$ be the finest partition of $\Omega$ that is coarser than every $\mathcal{P}_i$, and let $\mathcal{M}(\omega)$ be its block containing $\omega$.
Then $E$ is common knowledge at $\omega$ if and only if $\mathcal{M}(\omega) \subseteq E$.
For finite $\Omega$, the block $\mathcal{M}(\omega)$ consists of the states reached from $\omega$ by chains of steps.
Each step stays inside one block of some $\mathcal{P}_i$.

Example: let $\Omega = \set{1, 2, 3, 4}$, $\mathcal{P}_1 = \set{\set{1, 2}, \set{3, 4}}$ and $\mathcal{P}_2 = \set{\set{1}, \set{2}, \set{3, 4}}$.
The meet is $\set{\set{1, 2}, \set{3, 4}}$, so $E = \set{1, 2}$ is common knowledge at $\omega = 1$.
Directly: $K_1(E) = E$ and $K_2(E) = E$, so every iterate of the operators $K_i$ applied to $E$ is $E$, which contains $1$.

Non-example: let $\Omega = \set{1, 2, 3}$, $\mathcal{P}_1 = \set{\set{1, 2}, \set{3}}$ and $\mathcal{P}_2 = \set{\set{1}, \set{2, 3}}$, and $E = \set{1, 2}$.
At $\omega = 1$ both agents know $E$, since $K_1(E) = \set{1, 2}$ and $K_2(E) = \set{1}$.
But $K_1 K_2(E) = K_1(\set{1}) = \emptyset$, so agent 1 does not know that agent 2 knows $E$, and $E$ is not common knowledge at $1$.

The event that everyone knows $E$ is $\bigcap_{i \in I} K_i(E)$; it is called *mutual knowledge* and is weaker than common knowledge.
