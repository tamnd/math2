---
tag: H9KKH3C52K
kind: proof
name: Proof of the algebraic completeness of classical propositional logic
msc: ["03G05", "03B05"]
topics: [QYA4H5Y7VR]
audience: grad
proves: J2GTJ8FKF2
uses: [JVZ8APEV7A, CQM84EW10G, 3MKZST79MK, 15PF73BKY6, 0WG43AC0EV]
methods: [0BB5TPGQ1N, 12MQ2NJ29A, JZQVJ9XT63]
sources:
  - url: https://en.wikipedia.org/wiki/Lindenbaum–Tarski_algebra
    locator: lead section
  - url: https://plato.stanford.edu/entries/logic-algebraic-propositional/
    locator: "5. The algebraic counterparts of classical and intuitionistic logic"
  - book: isbn:9780387905785
---

## Proof

We prove 1 implies 2, 2 implies 3, and 3 implies 1.

**1 implies 2 (soundness).**

1. Let $B$ be a Boolean algebra and $v$ a $B$-valuation with $v(T) \subseteq \set{1}$.
2. Each axiom of L has the value $1$ under $v$, by the computation in steps 49 to 53 of [[the proof of the Lindenbaum-Tarski theorem|TW6DDQ57CW]].
3. Members of $T$ have the value $1$ by step 1.
4. If $v(\alpha) = 1$ and $v(\alpha \to \beta) = 1$, then $\neg 1 \lor v(\beta) = v(\beta) = 1$.
5. By induction on the length of a derivation from $T$, every formula derivable from $T$ has the value $1$.

**2 implies 3.** The algebra $\mathbf{2}$ is a Boolean algebra, so 3 is a special case of 2.

**3 implies 1, by contraposition.**

6. Assume $T \nvdash \varphi$, and let $\mathbf{L}_T$ be the Lindenbaum-Tarski algebra of $T$.
7. By [[the Lindenbaum-Tarski theorem|JVZ8APEV7A]], $\mathbf{L}_T$ is a Boolean algebra and $[\varphi] \ne 1$.
8. So $\neg [\varphi] \ne 0$, since $\neg$ is a bijection with $\neg 1 = 0$.
9. The set $F_0 = \set{b \in \mathbf{L}_T : b \ge \neg[\varphi]}$ is a [[filter|15PF73BKY6]], and it is proper because $0 \notin F_0$.
10. By the [[ultrafilter lemma|3MKZST79MK]], there is an [[ultrafilter|CQM84EW10G]] $U \supseteq F_0$.
11. Define $\chi(b) = 1$ if $b \in U$, and $\chi(b) = 0$ otherwise.
12. For each $b$, exactly one of $b$, $\neg b$ is in $U$, so $\chi(\neg b) = \neg \chi(b)$.
13. If $b, c \in U$, then $b \land c \in U$, because $U$ is a filter.
14. If $b \land c \in U$, then $b, c \in U$, because $U$ is upward closed.
15. So $\chi(b \land c) = \chi(b) \land \chi(c)$, and with step 12, $\chi$ preserves $\lor$ by the De Morgan laws.
16. So $\chi \colon \mathbf{L}_T \to \mathbf{2}$ is a homomorphism of Boolean algebras.
17. Define $v(\psi) = \chi([\psi])$ for each formula $\psi$.
18. By step 46 of the proof of the Lindenbaum-Tarski theorem, $[\psi \to \theta] = \neg[\psi] \lor [\theta]$.
19. So $v$ is a $\mathbf{2}$-valuation, by steps 12, 15 and 18.
20. For $\psi \in T$, $[\psi] = 1$ by part 3 of the theorem, so $v(\psi) = 1$.
21. Also $\neg [\varphi] \in U$, so $[\varphi] \notin U$ by step 12, and $v(\varphi) = 0$.
22. So condition 3 fails, which proves 3 implies 1. $\blacksquare$

## Idea

Soundness is a direct check of the axioms in any Boolean algebra.
For completeness, the Lindenbaum-Tarski algebra is a model in which exactly the consequences of $T$ have the value $1$.
An ultrafilter that contains $\neg[\varphi]$ is a homomorphism to $\mathbf{2}$ that keeps $T$ true and makes $\varphi$ false.

## Variants

1. Kalmár's proof avoids algebras: it builds, for each row of the truth table, a derivation of $\varphi$ or of $\neg \varphi$ from the literals of the row.
2. The proof with maximal consistent sets is the same proof in syntactic form: the ultrafilter $U$ corresponds to the maximal consistent set $\set{\psi : [\psi] \in U}$.
3. For finitely many variables, $\mathbf{L}_T$ is finite, and an atom below $\neg[\varphi]$ gives $U$ without the ultrafilter lemma.
