---
tag: CS0R0WW2V9
kind: proof
name: Outline of Gödel's original proof of the completeness theorem
msc: ["03B10", "03C07", "01A60"]
topics: [FBWW4J1XWG]
audience: grad
proves: WQ1ZE255SF
uses: [CS82V969DE, 81ZNY1XKYJ, AVD7T7J063, DKFGQTRYZE, 983GZBQYT4, RGNF33GVHX]
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

First, a small case shows the method.
Take the sentence $\forall x \, \exists y \, R(x, y)$, and build a model on the positive integers, with new variables $z_1, z_2, \dots$ as names.
Stage $1$ puts $z_1$ for $x$ and a new $z_2$ for its witness, which gives $R(z_1, z_2)$.
Stage $n$ puts $z_n$ for $x$ and a new $z_{n+1}$ for its witness, which gives $R(z_n, z_{n+1})$.
No finite conjunction $R(z_1, z_2) \land \dots \land R(z_n, z_{n+1})$ is propositionally contradictory, so one truth assignment makes all of them true.
Read $z_i$ as $i$, and let $R$ hold of $(i, i + 1)$: this structure satisfies the sentence.
If instead some stage had been a propositional contradiction, the sentence would have been refutable.
The proof below makes this idea work for every sentence.

This is an outline of the proof in Gödel's thesis of 1929, for the weak form and one sentence.
The language is countable, and at first it has relation symbols only, with no equality, constants or function symbols.
A sentence $\varphi$ is refutable when $\vdash \neg \varphi$.

**Step A: the reductions.**

1. It suffices to show that every sentence is refutable or has a model.
   If $\varphi$ is valid, then $\neg \varphi$ has no model, so $\vdash \neg \neg \varphi$, and then $\vdash \varphi$.
2. If $\vdash \varphi \leftrightarrow \psi$ and $\psi$ is refutable or satisfiable, then so is $\varphi$.
   Satisfiability transfers by the [[soundness theorem|AVD7T7J063]].
3. So we may take $\varphi$ in [[prenex normal form|CS82V969DE]]: a block of quantifiers followed by a quantifier-free matrix.
4. Write $\varphi$ as $(P) \Phi$, with prefix $(P)$ and matrix $\Phi$, and let $F$ be a new unary relation symbol.
   Then $\varphi$ is provably equivalent to $\forall y \, (P) \, \exists z \, (\Phi \land (F(y) \lor \neg F(z)))$, because $\forall y \, \exists z \, (F(y) \lor \neg F(z))$ is valid.
5. So we may assume that the prefix begins with $\forall$ and ends with $\exists$.
   The degree of $\varphi$ is the number of blocks of $\forall$ in its prefix.

**Step B: from degree $k + 1$ to degree $k$.**

6. Let $\varphi = \forall \bar x \, \exists \bar y \, \chi$, where $\chi = \forall \bar u \, \exists \bar v \, (P) \psi$ has degree $k$.
   Let $Q$ be a new relation symbol.
7. Put $\Phi = \forall \bar x' \, \exists \bar y' \, Q(\bar x', \bar y') \land \forall \bar x \, \forall \bar y \, (Q(\bar x, \bar y) \to \chi)$.
   Then $\vdash \Phi \to \varphi$.
8. Prenex operations turn $\Phi$ into a provably equivalent sentence $\Psi$ of degree $k$.
   The conjuncts share no variables, so the blocks $\forall \bar x' \exists \bar y'$ and $\forall \bar x \forall \bar y \forall \bar u \exists \bar v$ merge into one alternation.
9. By the induction hypothesis, $\Psi$ is refutable or satisfiable.
   If $\Psi$ is satisfiable, then so is $\Phi$, and so is $\varphi$ by step 7.
10. If $\Psi$ is refutable, then $\vdash \neg \Phi$.
    In this derivation, replace each $Q(\bar a, \bar b)$ by $\chi$ with $\bar a, \bar b$ in place of $\bar x, \bar y$.
11. Axioms stay axioms and MP stays MP, so this gives a derivation of the negation of $\varphi \land \forall \bar x \, \forall \bar y \, (\chi \to \chi)$.
    Hence $\vdash \neg \varphi$.

**Step C: degree $1$.**

12. Now $\varphi = \forall x_1 \cdots \forall x_k \, \exists y_1 \cdots \exists y_m \, \psi$, with $\psi$ quantifier-free.
    Let $z_1, z_2, \dots$ be new variables.
13. List all $k$-tuples of positive integers as $a^1, a^2, \dots$, by increasing sum and then in lexicographic order.
    Then the entries of $a^n$ are at most $n$, and so at most $(n - 1) m + 1$ when $m \ge 1$.
14. Let $B_n$ be $\psi$ with $x_j$ replaced by $z_{a^n_j}$ and $y_i$ replaced by $z_{(n-1)m + 1 + i}$.
    Let $D_n$ be $\exists z_1 \cdots \exists z_{nm+1} \, (B_1 \land \cdots \land B_n)$.
15. By induction on $n$, $\vdash \varphi \to D_n$.
    Each $B_n$ uses earlier variables for $\bar x$ and $m$ new variables for $\bar y$.
16. Case 1: some $D_n$ is refutable.
    Then $\vdash \neg \varphi$ by step 15.
17. Case 2: no $D_n$ is refutable.
    If $\neg (B_1 \land \cdots \land B_n)$ were a tautology, then by [[propositional completeness|81ZNY1XKYJ]] it would be derivable, and its generalization would refute $D_n$.
18. So for each $n$, some truth assignment $v_n$ to the atomic formulas makes $B_1 \land \cdots \land B_n$ true.
19. List all atomic formulas $E_1, E_2, \dots$ in the variables $z_i$.
    Choose a truth value for $E_1$ that infinitely many $v_n$ give it.
20. Among those $v_n$, choose for $E_2$ a value that infinitely many of them give, and so on.
    Call the result $v$.
21. Each $B_k$ uses finitely many atoms $E_1, \dots, E_h$.
    Infinitely many $v_n$ with $n \ge k$ agree with $v$ on these atoms and make $B_k$ true, so $v$ makes every $B_k$ true.
22. Define a [[structure|983GZBQYT4]] $\mathcal{A}$ with universe the positive integers.
    A relation symbol $R$ holds of $(u_1, \dots, u_r)$ if and only if $v$ makes $R(z_{u_1}, \dots, z_{u_r})$ true.
23. Under the assignment $z_i \mapsto i$, every $B_n$ is true in $\mathcal{A}$.
    Every $k$-tuple is some $a^n$, and $B_n$ gives its witnesses, so $\mathcal{A} \models \varphi$.

**Step D: equality and sets of sentences.**

24. For equality, replace $=$ by a new symbol $E$.
    Add the axioms that $E$ is an [[equivalence relation|RGNF33GVHX]] and a congruence for each relation symbol.
25. A model of the new sentence gives a model of $\varphi$, by the quotient by $E$.
    A refutation of the new sentence gives a refutation of $\varphi$.
26. For a countable set of sentences, the same argument works with the $B_n$ of all the sentences, interleaved.
    This gives the compactness theorem for countable languages.

## Idea

Gödel first brings each sentence to a form $\forall \bar x \, \exists \bar y \, \psi$ by adding new relation symbols.
For such a sentence, the finite approximations $D_n$ say that there are enough elements to give witnesses up to stage $n$.
Either one approximation is propositionally contradictory, and then the sentence is refutable, or all of them can be satisfied.
A compactness argument for truth assignments, in the form of König's lemma, then joins the assignments into one model on the positive integers.

Watch out: the model is built from truth values of atoms, not from a theory, so there is no maximal consistent set and no truth lemma.
The finite stages do the work that Henkin's witness constants do in the later proof.

## Variants

- Modern texts replace the degree reduction by Skolem functions: the Skolem form of $\varphi$ is satisfiable if and only if $\varphi$ is. See [[Skolem normal form|GCPQGMJYEV]].
- [[Herbrand's theorem|VZ21F10WRS]] is the same idea in proof-theoretic form: a sentence $\exists \bar y \, \psi$ is valid if and only if a finite disjunction of its instances is a tautology.
- [[Henkin's proof|3FR16954CY]] avoids normal forms and works for languages of every cardinality.
