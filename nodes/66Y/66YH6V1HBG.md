---
tag: 66YH6V1HBG
kind: proof
name: Proof of feasible interpolation for resolution
msc: ["03F20"]
topics: [CBAF7J051K]
audience: research
proves: YHGCN7BBEP
uses: [6JSH907W5R, 59GJCM8C66, SQXNFGVADX]
methods: [0ASJVEFA9J, 0WCP0PVET6, 01XM7JEKHY]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Feasible interpolation
---

## Proof

Write $\pi = (C_1, \dots, C_L)$, with $C_L = \square$, as in the definition of [[resolution|6JSH907W5R]].
If an axiom is a clause of both $A$ and $B$, then all its variables are in $p$, and we treat it as a clause of $A$.

**Parts of a clause.**
For a clause $C$, let $C_A$ be the set of the literals of $C$ on the variables of $q$ and of $p$.
Let $C_B$ be the set of the literals of $C$ on the variables of $r$ and of $p$.
For part 2 we change one definition: $C_A$ is the set of the literals of $C$ on $q$ together with the positive literals of $C$ on $p$.
In both cases $(D \cup E)_A = D_A \cup E_A$ and $(D \cup E)_B = D_B \cup E_B$.

**Invariant.**
We build circuits $I_1, \dots, I_L$ in the variables $p$, in this order, with the following two properties for each $i$.

- (A) Every assignment $(a, b)$ of $(p, q)$ that satisfies $A$ and has $I_i(a) = 0$ satisfies $(C_i)_A$.
- (B) Every assignment $(a, c)$ of $(p, r)$ that satisfies $B$ and has $I_i(a) = 1$ satisfies $(C_i)_B$.

We then take $I = I_L$.

1. **Axioms of $A$.** Let $I_i = 0$. Property (B) holds, since $I_i(a) = 1$ never happens. For (A), an assignment that satisfies $A$ satisfies its clause $C_i$. The literals of $C_i$ are on $p$ and $q$, so $(C_i)_A = C_i$. In part 2, $C_i$ has no negative literal on $p$ by the hypothesis, so again $(C_i)_A = C_i$.
2. **Axioms of $B$.** Let $I_i = 1$. Property (A) holds, since $I_i(a) = 0$ never happens, and (B) holds as in step 1, since $(C_i)_B = C_i$.
3. **Resolution steps.** Let $C_i = D \cup E$ be the resolvent of $C_j = D \cup \set{x}$ and $C_k = E \cup \set{\neg x}$, where $j, k < i$, and $x \notin D$, $\neg x \notin E$. The next steps treat the cases for the pivot $x$.
4. **Pivot in $q$.** Let $I_i = I_j \vee I_k$. For (A), let $(a, b)$ satisfy $A$ with $I_i(a) = 0$. Then $I_j(a) = I_k(a) = 0$, so $(a, b)$ satisfies $D_A \cup \set{x}$ and $E_A \cup \set{\neg x}$. One of $x$ and $\neg x$ is false under $b$, so $(a, b)$ satisfies $D_A$ or $E_A$, hence $(C_i)_A$.
5. **Pivot in $q$, property (B).** Let $(a, c)$ satisfy $B$ with $I_i(a) = 1$. Then $I_j(a) = 1$ or $I_k(a) = 1$, say $I_j(a) = 1$. Since $x$ is not in $r$ or $p$, $(C_j)_B = D_B$, and (B) for $j$ gives that $(a, c)$ satisfies $D_B \subseteq (C_i)_B$. The case $I_k(a) = 1$ is the same.
6. **Pivot in $r$.** Let $I_i = I_j \wedge I_k$. This is step 4 and step 5 with the roles of $A$ and $B$, of $q$ and $r$, and of $0$ and $1$ exchanged. In part 2 the argument is unchanged, since a literal on $r$ is never in $(C_j)_A$.
7. **Pivot in $p$, part 1.** Let $I_i = (x \wedge I_k) \vee (\neg x \wedge I_j)$. For (A), let $(a, b)$ satisfy $A$ with $I_i(a) = 0$. If $a(x) = 1$, then $I_k(a) = 0$, so $(a, b)$ satisfies $E_A \cup \set{\neg x}$, and $\neg x$ is false, so it satisfies $E_A$. If $a(x) = 0$, then $I_j(a) = 0$, so it satisfies $D_A \cup \set{x}$, and $x$ is false, so it satisfies $D_A$. Property (B) is proved in the same way.
8. **Pivot in $p$, part 2.** Let $I_i = I_k \wedge (x \vee I_j)$, which has no NOT gate. Here $(C_j)_A = D_A \cup \set{x}$ and $(C_k)_A = E_A$, since $\neg x$ is negative. For (A), let $(a, b)$ satisfy $A$ with $I_i(a) = 0$. Either $I_k(a) = 0$, and then $(a, b)$ satisfies $E_A$. Or $a(x) = 0$ and $I_j(a) = 0$, and then it satisfies $D_A \cup \set{x}$ with $x$ false, so it satisfies $D_A$.
9. **Pivot in $p$, part 2, property (B).** Let $(a, c)$ satisfy $B$ with $I_i(a) = 1$. Then $I_k(a) = 1$, so $(a, c)$ satisfies $E_B \cup \set{\neg x}$. If $a(x) = 1$, then $\neg x$ is false, and $(a, c)$ satisfies $E_B$. Otherwise $I_j(a) = 1$, so $(a, c)$ also satisfies $D_B \cup \set{x}$. One of $x$ and $\neg x$ is false, so $(a, c)$ satisfies $D_B \cup E_B$.
10. **The empty clause.** For $C_L = \square$, both parts are empty, and no assignment satisfies an empty clause. By (A), no assignment $(a, b)$ with $I(a) = 0$ satisfies $A$, so $I(a) = 0$ implies that $A(a, q)$ is unsatisfiable. By (B), $I(a) = 1$ implies that $B(a, r)$ is unsatisfiable.
11. **Size and time.** Each clause adds at most $4$ gates: none for an axiom, one for a pivot in $q$ or $r$, two in step 8, and four in step 7, counting the NOT gate. So $I$ has at most $4L$ gates. The type of each step, and so each gate, is read off from $\pi$ in polynomial time.

## Idea

Each clause of the refutation gets a circuit that names a side, $A$ or $B$.
The circuit promises that the clause, cut down to the variables of that side, follows from that side at the given values of $p$.
At the empty clause, the promise says that the named side is unsatisfiable.

## Variants

- **Restricted refutations.** One can also substitute $a$ into $\pi$ and follow the refutation of $A(a, q) \wedge B(a, r)$. With this view, each clause gets a subclause derivable from one side, and the same gates compute which side it is.
- **Cutting planes.** Pudlák's proof for [[cutting planes|KKCX2HQP2K]] uses the same induction, with lines in place of clauses and real numbers in place of the bits $0$ and $1$.
