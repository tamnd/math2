---
tag: ~5f72fbfc
kind: proof
name: Outline of Gödel's original proof of the completeness theorem
msc: ["03B10", "03C07", "01A60"]
topics: [FBWW4J1XWG]
audience: grad
proves: WQ1ZE255SF
uses: [CS82V969DE, 81ZNY1XKYJ, ~331f6430, DKFGQTRYZE, 983GZBQYT4, RGNF33GVHX]
methods: [0WCP0PVET6, 0ASJVEFA9J, JZQVJ9XT63]
sources:
  - url: https://en.wikipedia.org/wiki/Original_proof_of_G%C3%B6del%27s_completeness_theorem
    locator: "Proof of theorem 2: first step"
  - url: https://en.wikipedia.org/wiki/Original_proof_of_G%C3%B6del%27s_completeness_theorem
    locator: Reducing the theorem to formulas of degree 1
  - url: https://en.wikipedia.org/wiki/Original_proof_of_G%C3%B6del%27s_completeness_theorem
    locator: Proving the theorem for formulas of degree 1
  - url: https://en.wikipedia.org/wiki/Original_proof_of_G%C3%B6del%27s_completeness_theorem
    locator: Extension to first-order predicate calculus with equality
---

## Proof

This is an outline of the proof in Gödel's thesis of 1929, for the weak form and one sentence.
The language is countable, and at first it has relation symbols only, with no equality, constants or function symbols.
A sentence $\varphi$ is refutable when $\vdash \neg \varphi$.

Step A: the reductions.

1. It suffices to show: every sentence is refutable or has a model. If $\varphi$ is valid, then $\neg \varphi$ has no model, so $\vdash \neg \neg \varphi$, and then $\vdash \varphi$.
2. If $\vdash \varphi \leftrightarrow \psi$, then $\varphi$ is refutable or satisfiable when $\psi$ is. Satisfiability transfers by the [[soundness theorem|~331f6430]].
3. So we may take $\varphi$ in [[prenex normal form|CS82V969DE]]: a block of quantifiers followed by a quantifier-free matrix.
4. Let $F$ be a new unary relation symbol. The sentence $\varphi$ is provably equivalent to $\forall y \, (P) \, \exists z \, (\Phi \land (F(y) \lor \neg F(z)))$, where $(P) \Phi$ is $\varphi$.
5. So we may assume that the prefix begins with $\forall$ and ends with $\exists$. The degree of $\varphi$ is the number of blocks of $\forall$ in its prefix.

Step B: from degree $k + 1$ to degree $k$.

6. Let $\varphi = \forall \bar x \, \exists \bar y \, \chi$, where $\chi = \forall \bar u \, \exists \bar v \, (P) \psi$ has degree $k$. Let $Q$ be a new relation symbol.
7. Put $\Phi = \forall \bar x' \, \exists \bar y' \, Q(\bar x', \bar y') \land \forall \bar x \, \forall \bar y \, (Q(\bar x, \bar y) \to \chi)$. Then $\vdash \Phi \to \varphi$.
8. Prenex operations turn $\Phi$ into a provably equivalent sentence $\Psi$ of degree $k$. The two blocks $\forall \bar x' \exists \bar y'$ and $\forall \bar x \forall \bar y \forall \bar u \exists \bar v$ merge into one alternation.
9. By the induction hypothesis, $\Psi$ is refutable or satisfiable. If $\Psi$ is satisfiable, then so is $\Phi$, and so is $\varphi$ by step 7.
10. If $\Psi$ is refutable, then $\vdash \neg \Phi$. Replace $Q(\bar a, \bar b)$ everywhere in this derivation by $\chi$ with $\bar a, \bar b$ for $\bar x, \bar y$.
11. Axioms stay axioms and MP stays MP, so this gives a derivation of the negation of $\varphi \land \forall \bar x \, \forall \bar y \, (\chi \to \chi)$. Hence $\vdash \neg \varphi$.

Step C: degree $1$.

12. Now $\varphi = \forall x_1 \cdots \forall x_k \, \exists y_1 \cdots \exists y_m \, \psi$, with $\psi$ quantifier-free. Let $z_1, z_2, \dots$ be new variables.
13. List all $k$-tuples of positive integers as $a^1, a^2, \dots$, by increasing sum and then in lexicographic order. Then the entries of $a^n$ are at most $(n - 1) m + 1$.
14. Let $B_n$ be $\psi$ with $x_j$ replaced by $z_{a^n_j}$ and $y_i$ replaced by $z_{(n-1)m + 1 + i}$. Let $D_n$ be $\exists z_1 \cdots \exists z_{nm+1} \, (B_1 \land \cdots \land B_n)$.
15. By induction on $n$, $\vdash \varphi \to D_n$. Each $B_n$ uses earlier variables for $\bar x$ and $m$ new variables for $\bar y$.
16. Case 1: some $D_n$ is refutable. Then $\vdash \neg \varphi$ by step 15.
17. Case 2: no $D_n$ is refutable. Suppose $\neg (B_1 \land \cdots \land B_n)$ were a tautology. By [[propositional completeness|81ZNY1XKYJ]] it would be derivable, and its generalization would refute $D_n$.
18. So for each $n$, some truth assignment $v_n$ to the atomic formulas makes $B_1 \land \cdots \land B_n$ true.
19. List all atomic formulas $E_1, E_2, \dots$ in the variables $z_i$. Choose a truth value for $E_1$ that infinitely many $v_n$ give it.
20. Among those $v_n$, choose for $E_2$ a value that infinitely many of them give, and so on. Call the result $v$.
21. Each $B_k$ uses finitely many atoms $E_1, \dots, E_h$. Infinitely many $v_n$ with $n \ge k$ agree with $v$ on them and make $B_k$ true. So $v$ makes every $B_k$ true.
22. Define a [[structure|983GZBQYT4]] $\mathcal{A}$ with universe the positive integers. A relation symbol $R$ holds of $(u_1, \dots, u_r)$ iff $v$ makes $R(z_{u_1}, \dots, z_{u_r})$ true.
23. Under the assignment $z_i \mapsto i$, every $B_n$ is true in $\mathcal{A}$. Every $k$-tuple is some $a^n$, and $B_n$ gives its witnesses. So $\mathcal{A} \models \varphi$.

Step D: equality and sets of sentences.

24. For equality, replace $=$ by a new symbol $E$, and add the axioms that $E$ is an [[equivalence relation|RGNF33GVHX]] and a congruence for each relation symbol.
25. A model of the new sentence gives a model of $\varphi$, by the quotient by $E$. A refutation of the new sentence gives a refutation of $\varphi$.
26. For a countable set of sentences, the same argument works with the $B_n$ of all the sentences, interleaved. This gives the countable compactness theorem.

## Idea

Gödel first brings each sentence to a form $\forall \bar x \, \exists \bar y \, \psi$ by adding new relation symbols.
For such a sentence, the finite approximations $D_n$ say that there are enough elements to give witnesses up to stage $n$.
Either one approximation is propositionally contradictory, and then the sentence is refutable, or all of them can be satisfied.
A compactness argument for truth assignments, in the form of König's lemma, then joins the assignments into one model on the positive integers.

## Variants

- Skolem functions replace the degree reduction in modern texts: the Skolem form of $\varphi$ is satisfiable iff $\varphi$ is. See [[Skolem normal form|GCPQGMJYEV]].
- [[Herbrand's theorem|VZ21F10WRS]] is the same idea in proof-theoretic form: a sentence $\exists \bar y \, \psi$ is valid iff a finite disjunction of its instances is a tautology.
- [[Henkin's proof|~c2ea41cc]] avoids normal forms and works for languages of every cardinality.
