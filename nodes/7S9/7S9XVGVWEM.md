---
tag: 7S9XVGVWEM
kind: definition
name: Star-free language
msc: [68Q45, 68Q70]
defines: K83HS1C5WG
uses: [RABRP2KG81, 5MFZ4VNY6D]
sources:
  - url: https://en.wikipedia.org/wiki/Star-free_language
---

## Definition

Let $\Sigma$ be an [[alphabet|RABRP2KG81]].
The class of *star-free languages* over $\Sigma$ is the smallest class $\mathcal{S}$ of [[formal languages|5MFZ4VNY6D]] over $\Sigma$ such that:

1. $\emptyset \in \mathcal{S}$, $\set{\varepsilon} \in \mathcal{S}$, and $\set{a} \in \mathcal{S}$ for every $a \in \Sigma$;
2. if $K, L \in \mathcal{S}$, then $K \cup L \in \mathcal{S}$ and $KL = \set{uv : u \in K,\ v \in L} \in \mathcal{S}$;
3. if $L \in \mathcal{S}$, then the complement $\Sigma^* \setminus L \in \mathcal{S}$.

## Remarks

Example: over $\Sigma = \set{a, b}$, the language $(ab)^*$ is star-free, because
$$(ab)^* = \Sigma^* \setminus \left( b \Sigma^* \cup \Sigma^* a \cup \Sigma^* aa \Sigma^* \cup \Sigma^* bb \Sigma^* \right),$$
where $\Sigma^* = \Sigma^* \setminus \emptyset$ is star-free by clauses 1 and 3.
Indeed, take a nonempty word that does not start with $b$, does not end with $a$ and contains neither $aa$ nor $bb$.
It alternates $a$ and $b$, starting with $a$ and ending with $b$.
Non-example: over $\set{a}$, the language $(aa)^*$ is regular but not star-free; it cannot be produced by the clauses, as shown by its syntactic monoid $\Z/2\Z$, which is not aperiodic.
Every star-free language is regular, since the clauses only use operations under which regular languages are closed.
