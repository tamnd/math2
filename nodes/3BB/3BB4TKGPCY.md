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

We shrink a model of an $\exists^* \forall^*$ sentence to its witnesses, and then we sort all prefixes by the two forbidden patterns.
Part 1 of the [[statement|ZF79MZRQ8V]] is proved in full.
Part 4 is derived from parts 1 to 3 and from the undecidability of $[\forall \exists \forall]$ and $[\forall^3 \exists]$, which are cited.

### Part 1: the witnesses form a model

1. Let $\sigma = \exists x_1 \cdots \exists x_m \, \forall y_1 \cdots \forall y_n \, \varphi(\vec{x}, \vec{y})$, with $\varphi$ quantifier-free in a signature $L$ of relation symbols, possibly with equality.
   Let $\mathcal{A} \models \sigma$.
2. By the clause of [[satisfaction|1WTCZB4DVB]] for $\exists$, there are $a_1, \ldots, a_m$ in $\mathcal{A}$ with $\mathcal{A} \models \varphi[\vec{a}, \vec{b}]$ for all $\vec{b}$ in $A^n$.
3. Let $B = \{ a_1, \ldots, a_m \}$ if $m \ge 1$, and let $B = \{ a \}$ for any element $a$ of $A$ if $m = 0$.
   Then $1 \le \lvert B \rvert \le \max(m, 1)$.
4. Let $\mathcal{B}$ be the [[substructure|JS7BWX3HW3]] on $B$, in which each relation symbol $R$ means $R^{\mathcal{A}}$ restricted to $B$.
   This is an $L$-structure, because $L$ has no function or constant symbols that could lead out of $B$.
5. Claim: for every quantifier-free $\psi(z_1, \ldots, z_r)$ and all $c_1, \ldots, c_r \in B$, we have $\mathcal{A} \models \psi[\vec{c}]$ if and only if $\mathcal{B} \models \psi[\vec{c}]$.
6. We prove the claim by [[structural induction|12MQ2NJ29A]] on $\psi$.
   For an atom $R(z_{i_1}, \ldots, z_{i_s})$, the tuple of the $c$'s lies in $B^s$, so it lies in $R^{\mathcal{B}}$ exactly when it lies in $R^{\mathcal{A}}$.
   For an atom $z_i = z_j$, equality means identity in both structures.
   The cases $\neg$ and $\wedge$ follow from the induction hypothesis.
7. Let $\vec{b} \in B^n$.
   Then $\vec{b} \in A^n$, so $\mathcal{A} \models \varphi[\vec{a}, \vec{b}]$ by step 2, and $\mathcal{B} \models \varphi[\vec{a}, \vec{b}]$ by step 5.
8. So $\mathcal{B} \models \forall \vec{y} \, \varphi[\vec{a}, \vec{y}]$, and the witnesses $\vec{a} \in B^m$ give $\mathcal{B} \models \sigma$.
   If $m = 0$, there are no witnesses to choose, and step 7 gives $\mathcal{B} \models \sigma$ at once.

### Part 1: the decision procedure

9. Given a sentence $\sigma$ of the class, compute $N = \max(m, 1)$.
   List all $L$-structures with domain $\{ 1, \ldots, s \}$ for $1 \le s \le N$.
   The list is finite, because a relation symbol of arity $t$ has only the $2^{s^t}$ subsets of $\{ 1, \ldots, s \}^t$ as possible meanings.
10. Evaluate $\sigma$ in each listed structure by trying all values of the variables.
    By steps 1 to 8, together with the fact that every model of size at most $N$ is isomorphic to a listed one, $\sigma$ is satisfiable if and only if some listed structure is a model.

### Part 4: undecidability goes up

11. If $p$ is a subsequence of $p'$, then satisfiability for $[p]$ reduces to satisfiability for $[p']$.
    To a sentence with prefix $p$, add quantifiers over new variables that do not occur in the matrix, at the places where $p'$ has extra letters.
12. The new sentence is equivalent to the old one, because a quantifier over a variable that does not occur has no effect in a nonempty domain.
    Its prefix is $p'$, and the map is computable.
13. Hence if $[\forall \exists \forall]$ and $[\forall^3 \exists]$ are undecidable, then $[p']$ is undecidable whenever $p'$ contains $\forall \exists \forall$ or $\forall^3 \exists$ as a subsequence.

### Part 4: the prefixes that remain

14. Let $p$ be a prefix that does not contain $\forall \exists \forall$ as a subsequence.
    If $p$ has no $\forall$, then $p = \exists^a$, which matches $\exists^* \forall^*$.
15. Otherwise write $p = \exists^a \forall w$, where the displayed $\forall$ is the first $\forall$ of $p$.
    In $w$, no $\forall$ comes after an $\exists$, since that would give $\forall \exists \forall$ together with the first $\forall$.
    So $w = \forall^b \exists^c$, and $p = \exists^a \forall^{b+1} \exists^c$.
16. If $c = 0$, then $p$ matches $\exists^* \forall^*$.
    If $c \ge 1$ and $b + 1 \le 2$, then $p$ matches $\exists^* \forall \exists^*$ or $\exists^* \forall^2 \exists^*$.
17. If $c \ge 1$ and $b + 1 \ge 3$, then $p$ contains $\forall^3 \exists$ as a subsequence.
18. By steps 14 to 17, each prefix either matches one of the three decidable patterns, and its class is decidable by parts 1 to 3, or it contains $\forall \exists \forall$ or $\forall^3 \exists$, and its class is undecidable by step 13.
    This proves part 4.

## Idea

A universal sentence stays true when we pass to a substructure, since it only speaks about the elements that are there.
So in a model of $\exists^* \forall^*$, the elements named by the existential quantifiers already form a model, and the size of a model is bounded by the number of those quantifiers.
For the classification, a prefix that avoids the two forbidden patterns must have the shape $\exists^a \forall^{b} \exists^c$ with $b \le 1$ or $c = 0$, which leaves only the three decidable cases.

## Variants

For Ackermann's class $[\exists^* \forall \exists^*]$, a satisfiable sentence has a model whose size is bounded by a computable function of the sentence.
That proof builds a model from finitely many patterns of existential witnesses, and it is longer.

For the Gödel-Kalmár-Schütte class $[\exists^* \forall^2 \exists^*]$, the proof of the finite model property is a longer combinatorial argument.
It does not extend to equality, since the class with equality is undecidable.

The undecidability of $[\forall \exists \forall]$ codes the domino problem for Wang tiles into the prefix, following Kahr, Moore and Wang.
The undecidability of $[\forall^3 \exists]$ is due to Surányi.
