---
tag: ~c1ce9ccb
kind: proof
name: Proof that elementarily equivalent finite structures are isomorphic by diagram sentences
msc: ["03C07"]
topics: [AY09KYSW81]
audience: ug2
proves: ~906b905e
uses: [P3B1V182N4, PZMGQMDN25, ~ad0fa7f2, DKFGQTRYZE]
methods: [0NTF6DMVAP]
sources:
  - book: isbn:9780387987606
    locator: Chapter 1
  - url: https://en.wikipedia.org/wiki/Elementary_equivalence
    locator: Elementarily equivalent structures
---

## Proof

Let $M = \set{a_1, \dots, a_n}$ with the $a_i$ distinct, and let $\mathcal{M} \equiv \mathcal{N}$.

1. Let $\varepsilon_n$ be $\exists x_1 \cdots \exists x_n \, (\bigwedge_{i < j} x_i \ne x_j \land \forall y \, \bigvee_{i} y = x_i)$. Then $\mathcal{M} \models \varepsilon_n$, so $\mathcal{N} \models \varepsilon_n$, and $N$ has exactly $n$ elements.
2. Let $L_0 \subseteq L$ be finite, and let $\delta_{L_0}(x_1, \dots, x_n)$ be the conjunction of the following formulas; it is a finite conjunction, since $L_0$ and $n$ are finite.
   - The formula $x_i \ne x_j$ for each $i \ne j$.
   - For each $k$-ary function symbol $f \in L_0$ and indices $i_1, \dots, i_k$, the equation $f(x_{i_1}, \dots, x_{i_k}) = x_j$, where $f^{\mathcal{M}}(a_{i_1}, \dots, a_{i_k}) = a_j$.
   - For each constant symbol $c \in L_0$, the equation $c = x_j$, where $c^{\mathcal{M}} = a_j$.
   - For each $k$-ary relation symbol $R \in L_0$ and indices $i_1, \dots, i_k$, the formula $R(x_{i_1}, \dots, x_{i_k})$ if $\mathcal{M} \models R(a_{i_1}, \dots, a_{i_k})$, and its negation if not.
3. $\mathcal{M} \models \delta_{L_0}(a_1, \dots, a_n)$, so $\mathcal{M} \models \exists \bar{x} \, \delta_{L_0}$, and hence $\mathcal{N} \models \exists \bar{x} \, \delta_{L_0}$. Choose $b_1, \dots, b_n$ in $N$ with $\mathcal{N} \models \delta_{L_0}(\bar{b})$.
4. The $b_i$ are distinct and $N$ has $n$ elements, so $a_i \mapsto b_i$ is a bijection $M \to N$. The conjuncts of $\delta_{L_0}$ say that it respects every symbol of $L_0$. So it is an [[isomorphism|PZMGQMDN25]] of the [[reducts|~ad0fa7f2]] to $L_0$. If $L$ is finite, take $L_0 = L$, and the proof is complete.
5. Let $L$ be infinite. For finite $L_0 \subseteq L$ let $I(L_0)$ be the set of bijections $M \to N$ that are isomorphisms of the reducts to $L_0$. By step 4, $I(L_0)$ is nonempty. It has at most $n!$ elements. If $L_0 \subseteq L_1$, then $I(L_1) \subseteq I(L_0)$.
6. Choose a finite $L_0$ with $\abs{I(L_0)}$ as small as possible. For every finite $L_1$, $I(L_0 \cup L_1) \subseteq I(L_0)$, and minimality gives equality. So $I(L_0) \subseteq I(L_1)$.
7. Take $h \in I(L_0)$. For every symbol $s$ of $L$, step 6 with $L_1 = \set{s}$ shows that $h$ respects $s$. So $h$ is an isomorphism $\mathcal{M} \to \mathcal{N}$.

## Idea

A finite structure in a finite signature can be written down completely in one existential sentence, its diagram sentence.
Elementary equivalence carries this sentence to $\mathcal{N}$, and a witness to it in $\mathcal{N}$ is an isomorphism.
For an infinite signature, there are only finitely many candidate bijections, so one of them works for all finite parts of the signature at once.

## Variants

Step 6 can be replaced by a direct argument: if no bijection is an $L$-isomorphism, each of the finitely many bijections $g_1, \dots, g_m$ fails to respect some symbol $s_i$, and then $I(\set{s_1, \dots, s_m})$ is empty, against step 4.
For many-sorted structures, the sentence $\varepsilon_n$ is replaced by one sentence for each sort.
