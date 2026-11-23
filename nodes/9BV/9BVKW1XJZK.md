---
tag: 9BVKW1XJZK
kind: proof
name: Proof of the size-width relation for resolution
msc: ["03F20", "68Q17"]
topics: [CBAF7J051K]
audience: research
proves: GWDGRPAQSM
uses: [6JSH907W5R, 7RX0Z6S1KZ]
methods: [0ASJVEFA9J, 0WCP0PVET6, HXP9VMXV8S]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Lower bounds
---

## Proof

We split on one literal at a time, and we show that a small refutation lets us pay for each split with at most one unit of width.
For a literal $\ell$, write $F|_{\ell = 1}$ for the restriction that makes $\ell$ true, and $F|_{\ell = 0}$ for the one that makes $\ell$ false.
Both are CNFs with fewer variables than $F$.

### Part 1: the width lemma

**Lemma.** Let $\ell$ be a literal and $k \ge 0$.
If $w(F|_{\ell = 1} \vdash \square) \le k - 1$ and $w(F|_{\ell = 0} \vdash \square) \le k$, then $w(F \vdash \square) \le \max(k, w(F))$.

1. Let $\pi_1$ be a refutation of $F|_{\ell = 1}$ of width at most $k - 1$.
   Each axiom of $\pi_1$ is $C \setminus \{\neg \ell\}$ for some $C \in F$ that does not contain $\ell$.
2. Replace each such axiom by $C$, and add $\neg \ell$ to every clause that depends on an axiom that contained $\neg \ell$.
   The variable of $\ell$ does not occur in $F|_{\ell = 1}$, so it is never a pivot, and each step stays a resolution step.
3. The result is a derivation from $F$ of $\square$ or of $\{\neg \ell\}$, and its width is at most $(k - 1) + 1 = k$.
   If it is $\square$, we are done.
4. Otherwise resolve $\{\neg \ell\}$ with each clause $C \in F$ that contains $\ell$.
   This gives $C \setminus \{\ell\}$, of width at most $w(F)$.
5. The axioms of $F|_{\ell = 0}$ are these clauses $C \setminus \{\ell\}$ and the clauses of $F$ that contain neither $\ell$ nor $\neg \ell$.
   The clauses with $\neg \ell$ are true under $\ell = 0$, so they are not axioms of $F|_{\ell = 0}$.
6. So all axioms of $F|_{\ell = 0}$ are now derived, and we follow a refutation of $F|_{\ell = 0}$ of width at most $k$.
7. The whole refutation of $F$ has width at most $\max(k, w(F))$, and the lemma is proved.

### Part 2: tree-like resolution

8. **Claim.** If $F$ has a tree-like refutation with at most $2^b$ leaves, then $w(F \vdash \square) \le w(F) + b$.
   We prove it by induction on $b$, and for each $b$ by induction on the number of variables.
9. If $b = 0$, the refutation has one leaf, so it is the axiom $\square \in F$, and $w(F \vdash \square) = 0$.
10. Let $b \ge 1$, and suppose $\square \notin F$.
    The last step resolves $\{x\}$ and $\{\neg x\}$ for some variable $x$, since $\square$ is a resolvent only of two complementary unit clauses.
    Let $T_1$ and $T_0$ be the subtrees that derive $\{x\}$ and $\{\neg x\}$.
11. Their leaves add up to at most $2^b$, so one of them has at most $2^{b-1}$ leaves.
    If $T_1$ does, let $\ell = \neg x$; otherwise exchange the roles and let $\ell = x$.
12. Restrict $T_1$ by $\ell = 1$, that is $x = 0$.
    By the [[restriction lemma|7RX0Z6S1KZ]], this gives a tree-like derivation from $F|_{\ell = 1}$ of a subclause of $\{x\}|_{x = 0} = \square$, with at most $2^{b-1}$ leaves.
    By induction on $b$, and since $w(F|_{\ell = 1}) \le w(F)$, we get $w(F|_{\ell = 1} \vdash \square) \le w(F) + b - 1$.
13. Restrict the whole refutation by $\ell = 0$.
    This gives a tree-like refutation of $F|_{\ell = 0}$ with at most $2^b$ leaves, and $F|_{\ell = 0}$ has fewer variables.
    By induction on the number of variables, $w(F|_{\ell = 0} \vdash \square) \le w(F) + b$.
14. The lemma with $k = w(F) + b$ gives $w(F \vdash \square) \le w(F) + b$.

### Part 2, the size bound

15. Let $D = w(F \vdash \square) - w(F)$.
    If $D \le 0$, the bound $S_T \ge 2^D$ is trivial, so let $D \ge 1$.
16. Let a tree-like refutation have $L$ leaves.
    If $L \le 2^{D-1}$, the claim gives $w(F \vdash \square) \le w(F) + D - 1$, which is false.
    So $L \ge 2^{D-1} + 1$.
17. A tree in which every inner node has two children has $2L - 1$ nodes.
    So the refutation has at least $2^D + 1$ clauses, and $S_T(F \vdash \square) \ge 2^D$.
    This proves part 1.

### Part 3: general resolution

18. Fix $n$, the number of variables of $F$, and a real number $d$ with $0 < d < 2n$.
    Call a clause *fat* if its width is greater than $d$, and let $a = 1/(1 - d/(2n)) > 1$.
19. **Claim.** Let $G$ be an unsatisfiable CNF with at most $n$ variables.
    If $G$ has a refutation with fewer than $a^b$ fat clauses, then $w(G \vdash \square) \le w(G) + d + b$.
    We prove it by induction on $b$, and for each $b$ by induction on the number of variables of $G$.
20. If the refutation has no fat clause, its width is at most $d$, and the claim holds.
    This covers $b = 0$.
21. Otherwise let $f \ge 1$ be the number of fat clauses.
    There are at most $2n$ literals, and each fat clause has more than $d$ of them.
    By averaging, some literal $\ell$ occurs in at least $f d/(2n)$ fat clauses.
22. Restrict by $\ell = 1$, so the fat clauses that contain $\ell$ become true and disappear.
    By the restriction lemma, every clause of the new refutation of $G|_{\ell = 1}$ comes from one clause of the old one and is no wider.
    So the new refutation has at most $f (1 - d/(2n)) = f/a < a^{b-1}$ fat clauses.
    By induction on $b$, $w(G|_{\ell = 1} \vdash \square) \le w(G) + d + b - 1$.
23. Restrict by $\ell = 0$.
    The new refutation of $G|_{\ell = 0}$ has at most $f < a^b$ fat clauses, and $G|_{\ell = 0}$ has fewer variables.
    By induction on the number of variables, $w(G|_{\ell = 0} \vdash \square) \le w(G) + d + b$.
    The induction has a base, since an unsatisfiable CNF without variables contains $\square$.
24. The lemma with $k = w(G) + d + b$ gives $w(G \vdash \square) \le w(G) + d + b$.

### Part 3, the choice of parameters

25. Let $S = S(F \vdash \square)$.
    If $S = 1$, then $\square \in F$, and part 2 holds.
26. Let $S \ge 2$ and $d = \sqrt{2n \ln S}$.
    If $d \ge 2n$, the right side of part 2 is at least $2d \ge 4n$.
    A refutation read off a full DPLL search tree has width at most $n$, so $w(F \vdash \square) \le n$, and part 2 holds.
27. Otherwise $\ln a = -\ln(1 - d/(2n)) \ge d/(2n)$.
    Let $b$ be the least integer with $a^b > S$.
    Then $b \le \ln S/\ln a + 1 \le 2n \ln S/d + 1 = d + 1$.
28. A least refutation has at most $S < a^b$ fat clauses.
    The claim gives $w(F \vdash \square) \le w(F) + 2d + 1 = w(F) + 1 + 2\sqrt{2n \ln S}$.
29. If $w(F \vdash \square) \ge w(F) + 1$, we subtract $w(F) + 1$, square, and divide by $8n$.
    This gives $\ln S \ge (w(F \vdash \square) - w(F) - 1)^2/(8n)$, and part 2 is proved.

$\blacksquare$

## Idea

The width lemma says that one restriction may cost one unit of width, and the other restriction may cost nothing extra.
In a tree, one of the two subtrees is small, and it pays for the extra unit, so the width grows by one each time the tree size halves.
In a dag, a literal that occurs in many fat clauses plays the role of the small subtree: setting it true removes a fixed fraction of the fat clauses.
Students often slip at the order of the two restrictions.
The branch that costs a unit of width must be the one where the measure drops, the small subtree or the branch that kills fat clauses.
The other branch only loses a variable, and the induction on variables handles it.

## Variants

The proof gives the general bound with $n$ replaced by the number of variables that occur in the refutation, since only those literals are counted in step 21.
The same argument, with degree in place of width and a restriction of one variable at a time, proves the size-degree relation of Impagliazzo, Pudlák and Sgall for the [[polynomial calculus|ZERBQSTZB5]].
