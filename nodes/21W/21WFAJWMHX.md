---
tag: 21WFAJWMHX
kind: proof
name: Proof of the Jónsson-Tarski representation theorem for modal algebras
msc: ["03G05", "06E25"]
topics: [QYA4H5Y7VR]
audience: research
proves: HC5V2QFFWB
uses: [JCP47TNBSD, S4QJ395PA5, CQM84EW10G, 3MKZST79MK, 15PF73BKY6]
methods: [0NTF6DMVAP, MKHVRNW68H, 0J0XBKG64S, JZQVJ9XT63]
sources:
  - url: https://en.wikipedia.org/wiki/General_frame
    locator: Operations and morphisms on general frames
  - book: isbn:9780521527149
    locator: Chapter 5
---

## Proof

Let $(A, \Diamond)$ be a modal algebra, $\Box b = \neg \Diamond \neg b$, and $R$, $h$ as in [[the statement|HC5V2QFFWB]].

**Part A: basic facts about $\Diamond$ and $\Box$.**

1. If $x \le y$, then $\Diamond y = \Diamond(x \lor y) = \Diamond x \lor \Diamond y$, so $\Diamond x \le \Diamond y$.
2. $\Box 1 = \neg \Diamond 0 = 1$, and $\Box(b \land c) = \neg \Diamond(\neg b \lor \neg c) = \Box b \land \Box c$, by De Morgan.
3. So $\Box$ is monotone, and for each ultrafilter $u$ the set $G_u = \set{b : \Box b \in u}$ is a [[filter|15PF73BKY6]].

**Part B: the two descriptions of $R$ (part 1).**

4. Let $u R v$, and let $\Box b \in u$. Suppose $b \notin v$; then $\neg b \in v$, since $v$ is an [[ultrafilter|CQM84EW10G]].
5. So $\Diamond \neg b \in u$ by the definition of $R$, that is $\neg \Box b \in u$.
6. Then $u$ contains $\Box b$ and $\neg \Box b$, so $0 \in u$, which is false. Hence $b \in v$, and $G_u \subseteq v$.
7. Conversely, let $G_u \subseteq v$, and let $b \in v$. Suppose $\Diamond b \notin u$; then $\neg \Diamond b = \Box \neg b \in u$.
8. So $\neg b \in G_u \subseteq v$, and $v$ contains $b$ and $\neg b$, which is false. Hence $\Diamond b \in u$, and $u R v$.

**Part C: $h$ is a Boolean embedding.**

9. By [[Stone's representation theorem|S4QJ395PA5]], $a \mapsto h(a)$ is an injective homomorphism of Boolean algebras into $\mathcal{P}(\mathrm{Uf}\,A)$.

**Part D: $h(\Diamond a) = \langle R \rangle h(a)$.**

10. Let $u \in \langle R \rangle h(a)$: there is $v$ with $u R v$ and $a \in v$.
11. By the definition of $R$, $\Diamond a \in u$, so $u \in h(\Diamond a)$.
12. Conversely, let $u \in h(\Diamond a)$, so $\Diamond a \in u$.
13. Claim: $a \land b \ne 0$ for every $b \in G_u$.
14. Suppose $a \land b = 0$ with $\Box b \in u$. Then $a \le \neg b$, so $\Diamond a \le \Diamond \neg b = \neg \Box b$ by step 1.
15. So $\Diamond a \land \Box b \le \neg \Box b \land \Box b = 0$.
16. But $\Diamond a, \Box b \in u$, so $0 \in u$, which is false. This proves the claim.
17. By steps 3 and 13, the set $F = \set{x : x \ge a \land b \text{ for some } b \in G_u}$ is a proper filter that contains $a$ and $G_u$.
18. By the [[ultrafilter lemma|3MKZST79MK]], there is an ultrafilter $v \supseteq F$.
19. Then $G_u \subseteq v$, so $u R v$ by part 1; and $a \in v$.
20. So $u \in \langle R \rangle h(a)$.
21. By steps 10 to 20, $h(\Diamond a) = \langle R \rangle h(a)$ for each $a \in A$.

**Conclusion.**

22. By steps 9 and 21, $h$ is an injective homomorphism of modal algebras from $(A, \Diamond)$ into $(A_+)^+$. $\blacksquare$

## Idea

The Boolean part is Stone's representation: elements become sets of ultrafilters.
The relation is chosen so that $\Diamond a \in u$ is necessary for $u$ to see a world containing $a$.
For sufficiency, the set $\set{a} \cup \set{b : \Box b \in u}$ has the finite meet property, because a conflict would put $\Diamond a \land \Box \neg a$ into $u$.
The ultrafilter lemma then gives the world $v$.

## Variants

1. Through the canonical model: for the Lindenbaum-Tarski algebra of a normal logic, Part D is the existence lemma of the canonical model, proved with maximal consistent sets.
2. For a normal operator of arity $n$, one finds the ultrafilters $v_1, \dots, v_n$ one at a time by the same argument; Blackburn, de Rijke and Venema give the details in Chapter 5.
3. For finite $A$, the ultrafilters are the principal filters of the atoms, and step 18 needs no choice principle.
