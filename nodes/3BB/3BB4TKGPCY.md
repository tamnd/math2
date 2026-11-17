---
tag: 3BB4TKGPCY
kind: proof
name: Proof of the decidability of the Bernays-Schönfinkel-Ramsey class and reduction of the classification
msc: ["03B25", "03B10"]
topics: [E4AVTNWE9E]
audience: research
proves: ZF79MZRQ8V
uses: [CS82V969DE, JS7BWX3HW3, 983GZBQYT4, 1WTCZB4DVB, 12MQ2NJ29A]
methods: [01XM7JEKHY, 12MQ2NJ29A, 0WCP0PVET6, DX2H7AD66G]
sources:
  - url: https://en.wikipedia.org/wiki/Bernays%E2%80%93Sch%C3%B6nfinkel_class
    locator: lead section
---

## Proof

This page proves part 1 of the statement completely.
It then proves that part 4 follows from parts 1 to 3 and from the undecidability of $[\forall \exists \forall]$ and $[\forall^3 \exists]$, which are cited.

Part 1: the Bernays-Schönfinkel-Ramsey class.

1. Let $\sigma = \exists x_1 \cdots \exists x_m \, \forall y_1 \cdots \forall y_n \, \varphi(\vec{x}, \vec{y})$, with $\varphi$ quantifier-free in a signature of relation symbols, possibly with equality. Let $\mathcal{A} \models \sigma$.
2. By the clause of [[satisfaction|1WTCZB4DVB]] for $\exists$, there are $a_1, \ldots, a_m$ in $\mathcal{A}$ with $\mathcal{A} \models \varphi[\vec{a}, \vec{b}]$ for all $\vec{b}$ in $\mathcal{A}^n$.
3. Let $B = \set{a_1, \ldots, a_m}$ if $m \ge 1$, and let $B = \set{a}$ for any element $a$ if $m = 0$. Then $1 \le \abs{B} \le \max(m, 1)$.
4. Let $\mathcal{B}$ be the [[substructure|JS7BWX3HW3]] on $B$: each relation symbol $R$ is interpreted by $R^{\mathcal{A}}$ restricted to $B$. This is an $L$-structure because $L$ has no function or constant symbols.
5. Claim: for every quantifier-free $\psi(z_1, \ldots, z_r)$ and $c_1, \ldots, c_r \in B$, $\mathcal{A} \models \psi[\vec{c}]$ if and only if $\mathcal{B} \models \psi[\vec{c}]$.
6. Proof of the claim, by [[structural induction|12MQ2NJ29A]]. For $R(z_{i_1}, \ldots, z_{i_s})$, the tuple of the $c$'s lies in $B^s$, so it lies in $R^{\mathcal{B}}$ exactly when it lies in $R^{\mathcal{A}}$. For $z_i = z_j$, equality has the same meaning in both structures. The cases $\neg$ and $\wedge$ follow from the induction hypothesis.
7. Let $\vec{b} \in B^n$. Then $\vec{b} \in \mathcal{A}^n$, so $\mathcal{A} \models \varphi[\vec{a}, \vec{b}]$ by step 2. By step 5, $\mathcal{B} \models \varphi[\vec{a}, \vec{b}]$.
8. So $\mathcal{B} \models \forall \vec{y} \, \varphi[\vec{a}, \vec{y}]$, and with the witnesses $\vec{a} \in B^m$, $\mathcal{B} \models \sigma$. If $m = 0$, there are no witnesses to choose, and step 7 gives $\mathcal{B} \models \sigma$ directly.
9. Decidability. For a sentence $\sigma$ of the class, compute $N = \max(m, 1)$. List all structures with domain $\set{1, \ldots, s}$ for $s \le N$; there are finitely many, since each relation symbol of arity $t$ is one of the $2^{s^t}$ subsets of $\set{1, \ldots, s}^t$.
10. Evaluate $\sigma$ in each listed structure, by checking all values of the variables. By steps 1 to 8, $\sigma$ is satisfiable if and only if one of these structures is a model.

Part 4: the classification follows from the five cited or proved facts.

11. If $p$ is a subsequence of $p'$, then $[p]$ reduces to $[p']$. Insert in a sentence with prefix $p$ dummy quantifiers on new variables that do not occur in the matrix.
12. The new sentence is equivalent to the old one, because a quantifier over a variable that does not occur has no effect in a nonempty domain. Its prefix is $p'$, and the map is computable.
13. So if $[\forall \exists \forall]$ or $[\forall^3 \exists]$ is undecidable, then $[p']$ is undecidable whenever $p'$ contains $\forall \exists \forall$ or $\forall^3 \exists$ as a subsequence.
14. Let $p$ be a prefix that does not contain $\forall \exists \forall$ as a subsequence. If $p$ has no $\forall$, then $p = \exists^a$, which matches $\exists^* \forall^*$.
15. Otherwise write $p = \exists^a \forall w$, where the displayed $\forall$ is the first one. In $w$, no $\forall$ comes after an $\exists$, because that would give $\forall \exists \forall$. So $w = \forall^b \exists^c$, and $p = \exists^a \forall^{b+1} \exists^c$.
16. If $c = 0$, then $p$ matches $\exists^* \forall^*$. If $c \ge 1$ and $b + 1 \le 2$, then $p$ matches $\exists^* \forall \exists^*$ or $\exists^* \forall^2 \exists^*$.
17. If $c \ge 1$ and $b + 1 \ge 3$, then $p$ contains $\forall^3 \exists$ as a subsequence.
18. By steps 14 to 17, each prefix either matches one of the three decidable patterns, and is decidable by parts 1 to 3, or contains $\forall \exists \forall$ or $\forall^3 \exists$, and is undecidable by step 13. This proves part 4.

## Idea

For a sentence of the form $\exists^* \forall^*$, the universal part is preserved when we pass to a substructure, so the witnesses of the existential part already form a model.
This bounds the size of a model by the number of existential quantifiers.
For the classification, a prefix that avoids the two forbidden patterns has the shape $\exists^a \forall^{b} \exists^c$, which leaves only the three decidable cases.

## Variants

- Ackermann's class $[\exists^* \forall \exists^*]$: a satisfiable sentence has a model whose size is bounded by a computable function of the sentence. The proof builds a model from a finite set of patterns of the existential witnesses, and is longer.
- The Gödel-Kalmár-Schütte class $[\exists^* \forall^2 \exists^*]$: the proof of the finite model property is a longer combinatorial argument. It does not extend to equality, since the class with equality is undecidable.
- The undecidability of $[\forall \exists \forall]$ codes the domino problem of Wang tiles into the prefix, following Kahr, Moore and Wang. The undecidability of $[\forall^3 \exists]$ is due to Surányi.
