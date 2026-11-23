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

We build one circuit for each clause of the refutation, in order, and prove by induction along the refutation that each circuit names a side from which a part of its clause follows.
Write $\pi = (C_1, \dots, C_L)$ with $C_L = \square$, as in the definition of [[resolution|6JSH907W5R]].
If an axiom is a clause of both $A$ and $B$, then all its variables are in $p$, and we treat it as a clause of $A$.

### The parts of a clause and the invariant

For a clause $C$, let $C_A$ be the set of literals of $C$ on the variables of $q$ and $p$, and let $C_B$ be the set of literals of $C$ on the variables of $r$ and $p$.
For part 2 we change one definition: $C_A$ is the set of literals of $C$ on $q$ together with the positive literals of $C$ on $p$.
In both cases $(D \cup E)_A = D_A \cup E_A$ and $(D \cup E)_B = D_B \cup E_B$.

We build circuits $I_1, \dots, I_L$ in the variables $p$ with two properties for each $i$.

- (A) Every assignment $(a, b)$ of $(p, q)$ that satisfies $A$ and has $I_i(a) = 0$ satisfies $(C_i)_A$.
- (B) Every assignment $(a, c)$ of $(p, r)$ that satisfies $B$ and has $I_i(a) = 1$ satisfies $(C_i)_B$.

### Axioms

1. For an axiom of $A$, let $I_i = 0$.
   Property (B) holds because $I_i(a) = 1$ never happens.
   For (A), an assignment that satisfies $A$ satisfies its clause $C_i$, and $(C_i)_A = C_i$ because the literals of $C_i$ are on $p$ and $q$.
   In part 2, $C_i$ has no negative literal on $p$ by hypothesis, so again $(C_i)_A = C_i$.
2. For an axiom of $B$, let $I_i = 1$.
   Property (A) holds because $I_i(a) = 0$ never happens, and (B) holds as in step 1, since $(C_i)_B = C_i$.

### Steps on private variables

Let $C_i = D \cup E$ be the resolvent of $C_j = D \cup \{x\}$ and $C_k = E \cup \{\neg x\}$, with $j, k < i$.

3. If $x$ is in $q$, let $I_i = I_j \vee I_k$.
   For (A), let $(a, b)$ satisfy $A$ with $I_i(a) = 0$.
   Then $I_j(a) = I_k(a) = 0$, so $(a, b)$ satisfies $D_A \cup \{x\}$ and $E_A \cup \{\neg x\}$.
   One of $x$ and $\neg x$ is false under $b$, so $(a, b)$ satisfies $D_A$ or $E_A$, hence $(C_i)_A$.
4. For (B), let $(a, c)$ satisfy $B$ with $I_i(a) = 1$, say $I_j(a) = 1$.
   Since $x$ is in $q$, we have $(C_j)_B = D_B$, and (B) for $j$ gives that $(a, c)$ satisfies $D_B \subseteq (C_i)_B$.
   The case $I_k(a) = 1$ is the same.
5. If $x$ is in $r$, let $I_i = I_j \wedge I_k$.
   This is steps 3 and 4 with $A$ and $B$, $q$ and $r$, and $0$ and $1$ exchanged.
   In part 2 nothing changes, since a literal on $r$ never lies in a part $(C)_A$.

### Steps on shared variables

6. In part 1, if $x$ is in $p$, let $I_i = (x \wedge I_k) \vee (\neg x \wedge I_j)$.
   For (A), let $(a, b)$ satisfy $A$ with $I_i(a) = 0$.
   If $a(x) = 1$, then $I_k(a) = 0$, so $(a, b)$ satisfies $E_A \cup \{\neg x\}$ with $\neg x$ false, hence $E_A$.
   If $a(x) = 0$, then $I_j(a) = 0$, so $(a, b)$ satisfies $D_A \cup \{x\}$ with $x$ false, hence $D_A$.
   Property (B) is proved in the same way.
7. In part 2, let $I_i = I_k \wedge (x \vee I_j)$, which has no NOT gate.
   Here $(C_j)_A = D_A \cup \{x\}$ and $(C_k)_A = E_A$, since $\neg x$ is a negative literal.
   For (A), $I_i(a) = 0$ means that $I_k(a) = 0$, and then $(a, b)$ satisfies $E_A$, or that $a(x) = 0$ and $I_j(a) = 0$, and then it satisfies $D_A$.
8. For (B) in part 2, $I_i(a) = 1$ gives $I_k(a) = 1$, so $(a, c)$ satisfies $E_B \cup \{\neg x\}$.
   If $a(x) = 1$, then $\neg x$ is false and $(a, c)$ satisfies $E_B$.
   If $a(x) = 0$, then $I_j(a) = 1$, so $(a, c)$ also satisfies $D_B \cup \{x\}$ with $x$ false, hence $D_B$.

### The end of the refutation

9. For $C_L = \square$ both parts are empty, and no assignment satisfies an empty clause.
   By (A), no $(a, b)$ with $I(a) = 0$ satisfies $A$, so $I(a) = 0$ implies that $A(a, q)$ is unsatisfiable.
   By (B), $I(a) = 1$ implies that $B(a, r)$ is unsatisfiable.
10. Each clause adds at most $4$ gates: none for an axiom, one for a private pivot, two in step 7, and four in step 6, counting the NOT gate.
   So $I = I_L$ has at most $4L$ gates, and the kind of each step, hence each gate, is read off from $\pi$ in polynomial time.

## Idea

Each clause of the refutation gets a circuit that names a side, $A$ or $B$.
The circuit promises that the clause, cut down to the literals of that side, follows from that side at the given values of $p$.
Private pivots keep the promise with an OR or an AND, and a shared pivot is settled by looking at its value.
At the empty clause, the promise says that the named side is unsatisfiable.

## Variants

One can also substitute $a$ into $\pi$ and follow the refutation of $A(a, q) \wedge B(a, r)$.
Then each clause becomes a subclause that is derivable from one side alone, and the same gates compute which side it is.

Pudlák's proof for [[cutting planes|KKCX2HQP2K]] uses the same induction, with lines in place of clauses and integer bounds in place of the bits $0$ and $1$.
