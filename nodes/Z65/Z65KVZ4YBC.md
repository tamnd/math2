---
tag: Z65KVZ4YBC
kind: proof
name: Proof that ultrahomogeneity is omega-categoricity with quantifier elimination
msc: ["03C15", "03C35"]
topics: [ZS8X8KS54R]
audience: grad
proves: ZRWJZK78MD
uses: [H8VM37SSAX, CZFGSN4JNE, 7FDDXV3JK7, A22K1X8GKD, 1513J40TKA, MCZRXR3SVB, 6F2DB4HTJR, 9V71Q3SD1G]
methods: [0NTF6DMVAP, 6F2DB4HTJR, TFQ1845T84]
sources:
  - url: https://en.wikipedia.org/wiki/Fraïssé_limit
    locator: ω-categoricity and quantifier elimination
  - book: isbn:9780521587136
---

## Proof

Let $L$ be finite relational, $M$ countably infinite, and $T = \operatorname{Th}(M)$.
In a relational signature every subset of $M$ is a substructure.
We prove both directions of the [[biconditional|TFQ1845T84]].

### Quantifier-free types

1. Fix $n$. There are finitely many [[atomic formulas|MCZRXR3SVB]] in $x_1, \dots, x_n$, since $L$ is finite and relational.
2. A quantifier-free type $q$ of an $n$-tuple is a choice of truth value for each of them.
3. Let $\chi_q(\bar x)$ be the conjunction of the atomic formulas true in $q$ and the negations of the others.
4. If $\bar a, \bar b$ both satisfy $\chi_q$, then $a_i \mapsto b_i$ is a well-defined isomorphism between the substructures $\set{\bar a}$ and $\set{\bar b}$. Equality is atomic, so the map is well defined.

### Forward direction

5. Assume $M$ is [[ultrahomogeneous|H8VM37SSAX]], and let $\varphi(\bar x)$ be any formula.
6. Let $\bar a$ and $\bar b$ satisfy the same $\chi_q$. Step 4 gives an isomorphism between them. It extends to an automorphism $\sigma$ with $\sigma(\bar a) = \bar b$.
7. Automorphisms preserve all formulas, so $M \models \varphi(\bar a)$ if and only if $M \models \varphi(\bar b)$.
8. Let $S$ be the set of $q$ realized by some tuple in $\varphi(M)$. Then $M \models \forall \bar x\, (\varphi \leftrightarrow \bigvee_{q \in S} \chi_q)$.
9. This sentence lies in $T$, so $T$ has [[quantifier elimination|7FDDXV3JK7]].
10. Each complete $n$-[[type|9V71Q3SD1G]] of $T$ is then fixed by its quantifier-free part, so $T$ has finitely many $n$-types.
11. $T$ is complete with infinite models, so the [[Ryll-Nardzewski theorem|1513J40TKA]] gives $\aleph_0$-categoricity.

### Converse direction

12. Assume $T$ has quantifier elimination. We first show the extension property.
13. Let $A \subseteq B$ be finite structures in the age of $M$, with $A = \set{\bar a}$ and $B = \set{\bar a, \bar b}$. Let $f \colon A \to M$ be an embedding.
14. Fix an embedding $h \colon B \to M$. Let $\theta(\bar x, \bar y)$ be $\chi_q$ for the quantifier-free type $q$ of $(\bar a, \bar b)$ in $B$.
15. Then $M \models \exists \bar y\, \theta(h \bar a, \bar y)$.
16. The tuples $h \bar a$ and $f \bar a$ have the same quantifier-free type, so by quantifier elimination they have the same type.
17. So $M \models \exists \bar y\, \theta(f \bar a, \bar y)$. A witness $\bar c$ gives an embedding $g$ extending $f$, with $g(\bar b) = \bar c$.
18. Now let $p \colon A \to A'$ be an isomorphism of finite substructures. Enumerate $M = \set{m_0, m_1, \dots}$.
19. Build finite partial isomorphisms $p = p_0 \subseteq p_1 \subseteq \cdots$ by the [[back-and-forth method|6F2DB4HTJR]].
20. At step $2k + 1$, put $m_k$ into the domain, using the extension property for $p_{2k}$.
21. At step $2k + 2$, put $m_k$ into the range, using the extension property for $p_{2k+1}^{-1}$.
22. The union $\sigma = \bigcup_k p_k$ is a bijection $M \to M$ that preserves all relations, so it is an automorphism extending $p$.

## Idea

Ultrahomogeneity says orbits on tuples equal quantifier-free types.
There are finitely many such types, so every definable set is a finite union of them.
Conversely, quantifier elimination lets a one-point extension found over one copy of $A$ be moved to any other copy, and back-and-forth does the rest.

## Variants

The converse never used $\aleph_0$-categoricity, so for countably infinite $M$ in a finite relational signature, quantifier elimination alone is equivalent to ultrahomogeneity.
A second route to the converse uses that a countable model of an $\aleph_0$-categorical theory is homogeneous for elementary maps; quantifier elimination makes every isomorphism of finite substructures elementary.
