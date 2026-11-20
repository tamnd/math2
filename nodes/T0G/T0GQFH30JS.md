---
tag: T0GQFH30JS
kind: proof
name: Proof of the Tarski-Vaught test
proves: 60SA99BER7
msc: ["03C07"]
topics: [2RE7GWWXM5]
audience: ug2
uses: [8WZF9SBP39, 676H7EGTKJ, K7XDVK5854, C9494XYEMN, HYJ10AF6RT]
methods: [12MQ2NJ29A, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_equivalence
    locator: Tarski–Vaught test
  - book: isbn:9780387987606
    locator: Chapter 2
---

## Proof

Let $\mathcal{M}$ be a substructure of $\mathcal{N}$ with domains $M \subseteq N$.
Condition (TV) is condition 2 of the statement: for all $\varphi(\bar x, y)$ and $\bar a$ in $M$, if $\mathcal{N} \models \exists y \, \varphi(\bar a, y)$, then $\mathcal{N} \models \varphi(\bar a, b)$ for some $b \in M$.

First we show that an elementary substructure satisfies (TV).

1. Assume $\mathcal{M} \preceq \mathcal{N}$, and let $\bar a$ in $M$ with $\mathcal{N} \models \exists y \, \varphi(\bar a, y)$.
2. The formula $\exists y \, \varphi(\bar a, y)$ has parameters in $M$, so by the definition of an [[elementary substructure|8WZF9SBP39]] it holds in $\mathcal{M}$.
3. By the [[definition of truth|K7XDVK5854]] for $\exists$, some $b \in M$ has $\mathcal{M} \models \varphi(\bar a, b)$.
4. Again by elementarity, $\mathcal{N} \models \varphi(\bar a, b)$. So (TV) holds.

Now assume (TV).
We show by [[induction on formulas|12MQ2NJ29A]] that for each formula $\psi(\bar x)$ and each tuple $\bar a$ in $M$, $\mathcal{M} \models \psi(\bar a)$ if and only if $\mathcal{N} \models \psi(\bar a)$.

5. Atomic formulas: $\mathcal{M}$ is a [[substructure|676H7EGTKJ]], so its inclusion is an embedding, and [[embeddings preserve quantifier-free formulas|C9494XYEMN]].
6. Negation: let $\psi = \neg \chi$. By the definition of truth and the induction hypothesis for $\chi$, $\mathcal{M} \models \neg\chi(\bar a)$ iff $\mathcal{M} \not\models \chi(\bar a)$ iff $\mathcal{N} \not\models \chi(\bar a)$ iff $\mathcal{N} \models \neg\chi(\bar a)$.
7. Conjunction: let $\psi = \chi_1 \land \chi_2$. Both sides hold iff both conjuncts hold, and the induction hypothesis applies to $\chi_1$ and $\chi_2$.
8. Existential quantifier: let $\psi(\bar x) = \exists y \, \chi(\bar x, y)$. Assume $\mathcal{M} \models \psi(\bar a)$.
9. Then $\mathcal{M} \models \chi(\bar a, b)$ for some $b \in M$, by the definition of truth.
10. By the induction hypothesis for $\chi$ and the tuple $(\bar a, b)$ in $M$, $\mathcal{N} \models \chi(\bar a, b)$, so $\mathcal{N} \models \psi(\bar a)$.
11. Conversely, assume $\mathcal{N} \models \psi(\bar a)$. By (TV), applied to $\chi$, some $b \in M$ has $\mathcal{N} \models \chi(\bar a, b)$.
12. By the induction hypothesis for $\chi$ and $(\bar a, b)$, $\mathcal{M} \models \chi(\bar a, b)$, so $\mathcal{M} \models \psi(\bar a)$.
13. The other connectives and $\forall$ are defined from $\neg$, $\land$ and $\exists$, so the induction covers all formulas.
14. So $\mathcal{M}$ and $\mathcal{N}$ agree on every formula with parameters in $M$, and $\mathcal{M} \preceq \mathcal{N}$.

## Idea

The forward direction moves a witness from $\mathcal{M}$ to $\mathcal{N}$ by elementarity.
The backward direction is an induction on formulas, in which only the step for $\exists$ needs work.
Witnesses found in $\mathcal{M}$ go up for free, and (TV) brings witnesses found in $\mathcal{N}$ down into $M$.
The induction hypothesis must hold for all tuples of $M$ at once, because the step for $\exists$ adds the new element $b$ to the tuple.

## Variants

The same induction, with $h(\bar a)$ in place of $\bar a$, proves the version for an embedding $h \colon \mathcal{M} \to \mathcal{N}$.
When $\mathcal{N}$ has Skolem functions, (TV) reduces to closure of $M$ under these functions, and the proof becomes the statement that a substructure of a Skolemized structure is elementary; see [[Skolem functions and Skolem hulls|NKQY9NB955]].
