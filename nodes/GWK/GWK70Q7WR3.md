---
tag: GWK70Q7WR3
kind: proof
name: Proof of the Kripke completeness of intuitionistic logic by prime theories
msc: ["03B20"]
topics: [38EQ20GR7M]
audience: grad
proves: 480TCT5CJ9
uses: [5GTQ69W47T, 52XCYMK0WW, 9X08XK5RV2, SC0BSJ3GT6, TVE4F04KME, 6ZZSHAKG5F]
methods: [12MQ2NJ29A, 0NTF6DMVAP, 0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Semantics of intuitionistic logic
  - book: isbn:9781447145578
    locator: Chapter 5
---

## Proof

We assume countably many propositional variables, so the formulas can be listed as $\chi_0, \chi_1, \chi_2, \ldots$.

Part A: soundness.

1. Persistence: if $w \Vdash \varphi$ and $w \leq v$, then $v \Vdash \varphi$. We use induction on $\varphi$. For atoms, $V(p)$ is an up-set. No world forces $\bot$. The cases $\wedge$ and $\vee$ follow from the induction hypothesis.
2. For $\varphi \to \psi$: let $w \Vdash \varphi \to \psi$ and $w \leq v$. Every $u \geq v$ satisfies $u \geq w$ by transitivity. So $u \Vdash \varphi$ implies $u \Vdash \psi$, and $v \Vdash \varphi \to \psi$.
3. Axiom 1, $\varphi \to (\psi \to \varphi)$: let $v \geq w$ force $\varphi$, and $u \geq v$ force $\psi$. By step 1, $u \Vdash \varphi$.
4. Axiom 2: let $v \geq w$ force $\varphi \to (\psi \to \chi)$, let $u \geq v$ force $\varphi \to \psi$, and let $x \geq u$ force $\varphi$.
5. By transitivity $x \geq v$, so $x \Vdash \psi \to \chi$ and $x \Vdash \psi$. Reflexivity of $\leq$ at $x$ gives $x \Vdash \chi$.
6. Axioms 3, 4 and 5 hold by the clauses for $\wedge$ and $\vee$, with persistence for the nested implication in axiom 4.
7. Axiom 6: let $v \geq w$ force $\varphi \to \chi$, let $u \geq v$ force $\psi \to \chi$, and let $x \geq u$ force $\varphi \vee \psi$. In both cases of the disjunction, $x \Vdash \chi$.
8. Axiom 7, $\bot \to \varphi$, holds since no world forces $\bot$.
9. Modus ponens: if $w \Vdash \varphi$ and $w \Vdash \varphi \to \psi$, then $w \Vdash \psi$, by the clause for $\to$ with $v = w$.
10. By induction on the length of a derivation from $\Gamma$, every world that forces $\Gamma$ forces each line. This proves item 1.

Part B: the prime extension lemma.

11. A *theory* is a set $T$ of formulas with $T \vdash_{\mathsf{i}} \chi$ only if $\chi \in T$. A theory is *prime* if $\bot \notin T$, and $\chi \vee \psi \in T$ implies $\chi \in T$ or $\psi \in T$.
12. Let $\Gamma \nvdash_{\mathsf{i}} \varphi$. Put $\Gamma_0 = \Gamma$. Put $\Gamma_{n+1} = \Gamma_n \cup \set{\chi_n}$ if $\Gamma_n \cup \set{\chi_n} \nvdash_{\mathsf{i}} \varphi$, and $\Gamma_{n+1} = \Gamma_n$ otherwise.
13. Let $T = \bigcup_n \Gamma_n$. Each $\Gamma_n \nvdash_{\mathsf{i}} \varphi$, by induction on $n$. A derivation uses finitely many hypotheses, so $T \nvdash_{\mathsf{i}} \varphi$.
14. $T$ is a theory: let $T \vdash_{\mathsf{i}} \chi_n$. Then $\Gamma_n \cup \set{\chi_n}$ derives only what $T$ derives, so it does not derive $\varphi$. Hence $\chi_n \in \Gamma_{n+1} \subseteq T$.
15. $\bot \notin T$, since $\bot \vdash_{\mathsf{i}} \varphi$ by axiom 7.
16. $T$ is prime: suppose $\chi_m \vee \chi_k \in T$ with $\chi_m, \chi_k \notin T$. Then $\Gamma_m \cup \set{\chi_m} \vdash_{\mathsf{i}} \varphi$ and $\Gamma_k \cup \set{\chi_k} \vdash_{\mathsf{i}} \varphi$.
17. By the [[deduction theorem|9X08XK5RV2]], $T \vdash_{\mathsf{i}} \chi_m \to \varphi$ and $T \vdash_{\mathsf{i}} \chi_k \to \varphi$.
18. Axiom 6 and modus ponens give $T \vdash_{\mathsf{i}} \chi_m \vee \chi_k \to \varphi$, and then $T \vdash_{\mathsf{i}} \varphi$. This contradicts step 13.
19. So every $\Gamma$ with $\Gamma \nvdash_{\mathsf{i}} \varphi$ lies in a prime theory $T$ with $\varphi \notin T$. This is the intuitionistic form of [[Lindenbaum's lemma|SC0BSJ3GT6]].

Part C: the canonical model and completeness.

20. Let $W_c$ be the set of prime theories, ordered by inclusion $\subseteq$, and let $V_c(p) = \set{T \in W_c : p \in T}$. This is the [[canonical model|TVE4F04KME]].
21. $W_c$ is nonempty: by soundness $\nvdash_{\mathsf{i}} \bot$, and step 19 with $\Gamma = \emptyset$ gives a prime theory. Inclusion is a partial order, and $V_c(p)$ is an up-set.
22. Truth lemma: $T \Vdash \chi$ if and only if $\chi \in T$, for every prime $T$. We use induction on $\chi$.
23. Atoms hold by the definition of $V_c$, and $\bot$ holds by step 11. For $\wedge$, use axioms 3 and 4 and closure of $T$.
24. For $\chi \vee \psi$: if $\chi \in T$, then $\chi \vee \psi \in T$ by axiom 5. If $\chi \vee \psi \in T$, primeness gives $\chi \in T$ or $\psi \in T$.
25. For $\chi \to \psi$, first let $\chi \to \psi \in T$. If $U \supseteq T$ is prime and $\chi \in U$, then $\psi \in U$ by modus ponens. With the induction hypothesis, $T \Vdash \chi \to \psi$.
26. Now let $\chi \to \psi \notin T$. By the deduction theorem, $T \cup \set{\chi} \nvdash_{\mathsf{i}} \psi$.
27. Step 19 gives a prime $U \supseteq T \cup \set{\chi}$ with $\psi \notin U$. By the induction hypothesis, $U \Vdash \chi$ and $U \nVdash \psi$, so $T \nVdash \chi \to \psi$.
28. Completeness: let $\Gamma \nvdash_{\mathsf{i}} \varphi$. Step 19 gives a prime $T \supseteq \Gamma$ with $\varphi \notin T$. By step 22, $T$ forces $\Gamma$ and not $\varphi$. So $\Gamma \nVdash \varphi$, which proves item 2.

Part D: the finite model property.

29. Let $\mathsf{IPC} \nvdash \varphi$, and let $\Sigma$ be the set of subformulas of $\varphi$, with $n$ elements. By item 2, some world $w$ of some model $\mathfrak{M}$ does not force $\varphi$.
30. For a world $x$, let $\Sigma(x)$ be the set of members of $\Sigma$ forced at $x$. Let $W'$ be the set of the sets $\Sigma(x)$ for $x \geq w$, ordered by inclusion.
31. $W'$ has at most $2^n$ elements, and inclusion is a partial order. Its least element is $\Sigma(w)$, since $x \geq w$ gives $\Sigma(w) \subseteq \Sigma(x)$ by persistence.
32. Put $V'(p) = \set{S \in W' : p \in S}$ for $p \in \Sigma$. This is an up-set of $W'$.
33. Claim: for $\chi \in \Sigma$ and $x \geq w$, $\Sigma(x) \Vdash' \chi$ if and only if $\chi \in \Sigma(x)$. We use induction on $\chi$; the cases of atoms, $\bot$, $\wedge$, $\vee$ are direct.
34. Case $\chi \to \psi$, first with $\chi \to \psi \in \Sigma(x)$. Let $\Sigma(y) \supseteq \Sigma(x)$ with $\Sigma(y) \Vdash' \chi$. Then $\chi \in \Sigma(y)$ and $\chi \to \psi \in \Sigma(y)$, so $y \Vdash \psi$. Hence $\psi \in \Sigma(y)$, and $\Sigma(y) \Vdash' \psi$ by the induction hypothesis.
35. Now let $\chi \to \psi \notin \Sigma(x)$. Some $y \geq x$ forces $\chi$ and not $\psi$. Then $\Sigma(x) \subseteq \Sigma(y)$ by persistence, and the induction hypothesis refutes $\chi \to \psi$ at $\Sigma(x)$.
36. So $\varphi$ fails at the root $\Sigma(w)$ of the finite model $(W', \subseteq, V')$. This is a [[filtration|6ZZSHAKG5F]], and it proves item 3.

## Idea

Soundness is a check of each axiom, with persistence as the one lemma.
For completeness, the worlds are the prime theories, which play the role of maximal consistent sets.
A theory that does not contain $\chi \to \psi$ has a larger prime theory that contains $\chi$ but not $\psi$, and this is the clause for implication.
For the finite model property, worlds with the same subformulas of $\varphi$ are merged.

## Variants

1. For uncountable languages, Zorn's lemma gives a maximal theory among those that do not derive $\varphi$, and this theory is prime.
2. Algebraically, the prime theories are the prime filters of the Lindenbaum algebra, and the truth lemma is the Stone representation of a Heyting algebra; see [[Heyting algebra semantics|JM1XJXWZYH]].
3. A proof search in a cut-free sequent calculus for $\mathsf{IPC}$ gives a finite countermodel directly from a failed search tree.
