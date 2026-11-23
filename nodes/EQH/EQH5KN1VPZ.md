---
tag: EQH5KN1VPZ
kind: proof
name: Proof of the soundness and completeness of propositional resolution
msc: ["03B05", "03B35"]
topics: [JDK63589SA]
audience: ug2
proves: DH1P95R390
uses: [ZDW6N1PGJ7, T3SXVH3ZZC, QN7M1JCGT9, H31CS3HK5P, 4X9126SEMM]
methods: [0ASJVEFA9J, 0WCP0PVET6, 0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Resolution_(logic)
    locator: Resolution in propositional logic
  - url: https://builds.openlogicproject.org/
    locator: Resolution
---

## Proof

Take the unsatisfiable clauses $\{ p, q \}$, $\{ \neg p, q \}$ and $\{ \neg q \}$.
Resolving on $p$ in all possible ways gives $\{ q \}$, and the clauses without $p$ give $\{ \neg q \}$, a smaller unsatisfiable set in one variable fewer.
The completeness proof below repeats this step until no variable is left.

We use the definitions given under [[resolution|ZDW6N1PGJ7]].
A [[clause|T3SXVH3ZZC]] is read as a disjunction, so a truth assignment $v$ satisfies a clause $C$ when $v$ makes at least one literal of $C$ true.

### Part 1, soundness

1. Let $C_1 \cup \{ p \}$ and $C_2 \cup \{ \neg p \}$ be clauses with $p \notin C_1$ and $\neg p \notin C_2$.
   Their resolvent on $p$ is $C = C_1 \cup C_2$.
   Let $v$ satisfy both premises, and we show that $v$ satisfies $C$.
2. Suppose $v(p) = 1$.
   Then $\neg p$ is false under $v$, and since $v$ satisfies $C_2 \cup \{ \neg p \}$, some literal of $C_2$ is true under $v$.
   So $v$ satisfies $C$.
3. Suppose $v(p) = 0$.
   Then $p$ is false under $v$, and since $v$ satisfies $C_1 \cup \{ p \}$, some literal of $C_1$ is true under $v$.
   So $v$ satisfies $C$.
4. Let $C^1, \dots, C^m$ be a resolution derivation from $S$, and let $v$ satisfy every clause of $S$.
   By induction on $i$, $v$ satisfies $C^i$.
   A clause of $S$ is satisfied by the choice of $v$, and a resolvent of two earlier clauses by steps 1 to 3.
5. No assignment satisfies $\square$, because $\square$ has no literal that could be true.
6. So if a derivation from $S$ ends with $\square$, no assignment satisfies all of $S$, by steps 4 and 5.
   This proves refutation soundness.

### Part 2, completeness for a finite set

7. We prove by induction on $n$ that every finite unsatisfiable set $S$ of clauses in which at most $n$ variables occur has a resolution refutation.
8. A clause that contains both $p$ and $\neg p$ for some $p$ is tautological, since every assignment satisfies it.
   Let $S_0$ be $S$ without its tautological clauses.
9. The set $S_0$ is unsatisfiable, because an assignment that satisfies $S_0$ also satisfies the removed clauses.
   A refutation of $S_0$ is a refutation of $S$, since $S_0 \subseteq S$.
   So we may assume that $S$ has no tautological clause.
10. In the base case $n = 0$, the only clause with no variable is $\square$, so $S$ is $\emptyset$ or $\{ \square \}$.
    The empty set is satisfied by every assignment, so $S = \{ \square \}$, and the one-line list $\square$ is a refutation.
11. For the inductive step, let at most $n + 1$ variables occur in $S$, and let $p$ be one of them.
    Let $S^{+}$ be the clauses of $S$ that contain $p$, let $S^{-}$ be those that contain $\neg p$, and let $S^{0}$ be the others.
    By step 9 no clause is in both $S^{+}$ and $S^{-}$.
12. Let $S'$ be $S^{0}$ together with all resolvents on $p$ of a clause of $S^{+}$ with a clause of $S^{-}$.
    Such a resolvent is $C_1 \cup C_2$, where $C_1 \cup \{ p \} \in S^{+}$ with $p \notin C_1$, and $C_2 \cup \{ \neg p \} \in S^{-}$ with $\neg p \notin C_2$.
    By step 9, $\neg p \notin C_1$ and $p \notin C_2$, so the resolvent mentions neither $p$ nor $\neg p$.
13. So at most $n$ variables occur in $S'$, and $S'$ is finite, because $S$ is finite.

### Part 2 continued, the smaller set is unsatisfiable

14. Suppose, for a contradiction, that $v$ satisfies $S'$.
    Let $v_0$ and $v_1$ agree with $v$ except that $v_0(p) = 0$ and $v_1(p) = 1$.
    The clauses of $S'$ do not contain $p$, so $v_0$ and $v_1$ satisfy $S'$ as well.
15. The assignment $v_0$ satisfies every clause of $S^{-}$, because it makes $\neg p$ true.
    It satisfies $S^{0}$, since $S^{0} \subseteq S'$.
    Since $S$ is unsatisfiable, $v_0$ does not satisfy $S$.
16. So some clause $C_1 \cup \{ p \}$ of $S^{+}$, with $p \notin C_1$, is false under $v_0$.
    Then every literal of $C_1$ is false under $v_0$, and so under $v$, since $C_1$ does not mention $p$.
17. In the same way, $v_1$ satisfies $S^{+}$ and $S^{0}$.
    So some clause $C_2 \cup \{ \neg p \}$ of $S^{-}$, with $\neg p \notin C_2$, is false under $v_1$, and every literal of $C_2$ is false under $v$.
18. The resolvent $C_1 \cup C_2$ of these two clauses is in $S'$ by step 12, and it is false under $v$ by steps 16 and 17.
    This contradicts the choice of $v$, so $S'$ is unsatisfiable.

### Part 2 continued, lifting the refutation

19. By the induction hypothesis, $S'$ has a resolution refutation $D^1, \dots, D^k = \square$.
20. We turn this into a refutation of $S$.
    First we write all clauses of $S^{+} \cup S^{-}$, which are clauses of $S$, and then we write $D^1, \dots, D^k$.
21. A line $D^i$ that is a member of $S'$ is in $S^{0} \subseteq S$, or it is a resolvent on $p$ of two clauses of the first part, which are earlier lines.
    A line $D^i$ that the refutation derives from earlier lines keeps its justification.
22. So the new list is a resolution refutation of $S$, and this completes the induction.

### Part 3, completeness for an arbitrary set

23. Let $S$ be an unsatisfiable set of clauses, possibly infinite, and read each clause as the disjunction of its literals.
    By the [[compactness theorem|4X9126SEMM]], some finite subset $S_1 \subseteq S$ is unsatisfiable.
24. Only finitely many variables occur in $S_1$, because $S_1$ is finite and each clause is finite.
    By Part 2, $S_1$ has a resolution refutation.
25. A refutation of $S_1$ is a refutation of $S$, because each clause of $S_1$ is a clause of $S$.

This proves that $S$ is unsatisfiable if and only if $S$ has a resolution refutation.

## Idea

Soundness holds because a resolvent is true whenever both of its premises are true, whatever the value of the variable that is cut.
Completeness removes one variable $p$ at a time.
The clauses without $p$, together with all resolvents on $p$, are satisfiable exactly when the original set is.
After all variables are removed, an unsatisfiable set must contain the empty clause.
The compactness theorem reduces an infinite set to a finite one.

## Variants

A second proof of completeness uses semantic trees.
Order the variables $p_1, p_2, \ldots$ and build the binary tree of partial assignments.
Cut each branch at the first node that falsifies a clause of $S$.
For an unsatisfiable finite $S$ the cut tree is finite.
One resolves the two clauses at sibling leaves to get a clause false at their parent, and works from the leaves to the root.
This proof gives a tree-like refutation, the kind that the DPLL procedure produces.
