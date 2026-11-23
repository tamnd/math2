---
tag: 16BRS1GYWY
kind: proof
name: Proof of the finite model property of monadic logic by types
msc: ["03B25", "03C13"]
topics: [E4AVTNWE9E]
audience: ug2
proves: AS0NHQMAKA
uses: [SERN6CRVWW, 983GZBQYT4, 1WTCZB4DVB, 12MQ2NJ29A]
methods: [12MQ2NJ29A, 0ASJVEFA9J, 0WCP0PVET6, 01XM7JEKHY]
sources:
  - url: https://en.wikipedia.org/wiki/Monadic_predicate_calculus
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Ehrenfeucht%E2%80%93Fra%C3%AFss%C3%A9_game
    locator: lead section
---

## Proof

We shrink a model of $\sigma$ to a small substructure that keeps a few elements of each type, and we show that $\sigma$ cannot see the difference.

### Setup

Let $\mathcal{A}$ be a model of $\sigma$.
For a type $\tau \subseteq \{ 1, \ldots, k \}$, let $A_\tau$ be the set of elements of $\mathcal{A}$ whose type is $\tau$, in the sense of the [[monadic predicate calculus|SERN6CRVWW]].
For a subset $B$ of the domain, $\mathcal{B}$ denotes the substructure with domain $B$, so $P_i^{\mathcal{B}} = P_i^{\mathcal{A}} \cap B$.
Each element of $B$ has the same type in $\mathcal{B}$ as in $\mathcal{A}$.

### Part 1: sentences without equality

1. From each nonempty set $A_\tau$ we choose one element $r_\tau$, and we let $B$ be the set of these elements.
   Then $1 \le \abs{B} \le 2^k$, because the domain of $\mathcal{A}$ is nonempty.
2. Let $f$ map each $a$ in $\mathcal{A}$ to $r_\tau$, where $\tau$ is the type of $a$.
   Then $a$ and $f(a)$ have the same type, and $f(b) = b$ for $b \in B$.
3. We show by [[structural induction|12MQ2NJ29A]] on formulas $\varphi(x_1, \ldots, x_n)$ without equality that $\mathcal{A} \models \varphi[a_1, \ldots, a_n]$ if and only if $\mathcal{B} \models \varphi[f(a_1), \ldots, f(a_n)]$, for all $a_1, \ldots, a_n$.
4. Atomic case $P_i(x_j)$.
   By step 2, $a_j \in P_i^{\mathcal{A}}$ if and only if $f(a_j) \in P_i^{\mathcal{B}}$, since they have the same type.
5. The cases $\neg$ and $\wedge$ follow from the induction hypothesis and the clauses of [[satisfaction|1WTCZB4DVB]].
6. Case $\exists y \, \psi$, direction from $\mathcal{A}$ to $\mathcal{B}$.
   If $\mathcal{A} \models \psi[\vec{a}, c]$ for some $c$, then $\mathcal{B} \models \psi[f(\vec{a}), f(c)]$ by the induction hypothesis, and $f(c) \in B$.
7. Case $\exists y \, \psi$, direction from $\mathcal{B}$ to $\mathcal{A}$.
   If $\mathcal{B} \models \psi[f(\vec{a}), d]$ with $d \in B$, then $d = f(d)$ by step 2.
   So the induction hypothesis gives $\mathcal{A} \models \psi[\vec{a}, d]$.
8. For the sentence $\sigma$, step 3 gives $\mathcal{B} \models \sigma$.
   This proves part 1.

### Part 2: sentences with equality

9. If $q = 0$, then $\sigma$ has no quantifiers.
   It has no free variables and there are no constant symbols, so $\sigma$ has no atomic subformulas, and its truth value is the same in all structures.
   A structure with one element is a model.
10. Let $q \ge 1$.
    For each type $\tau$, choose a set $B_\tau \subseteq A_\tau$ with $\abs{B_\tau} = \min(\abs{A_\tau}, q)$.
    Let $B$ be the union of the sets $B_\tau$, so $1 \le \abs{B} \le q \cdot 2^k$.
11. Call a pair of tuples $\vec{a} \in A^n$ and $\vec{b} \in B^n$ matched when, for all $i$ and $j$, $a_i$ and $b_i$ have the same type, and $a_i = a_j$ if and only if $b_i = b_j$.
12. Claim $C(r)$: if $\varphi(x_1, \ldots, x_n)$ has quantifier rank at most $r$, $n + r \le q$, and $\vec{a}$, $\vec{b}$ are matched, then $\mathcal{A} \models \varphi[\vec{a}]$ if and only if $\mathcal{B} \models \varphi[\vec{b}]$.
13. We prove $C(r)$ by [[induction|0ASJVEFA9J]] on $r$, and for fixed $r$ by structural induction on $\varphi$.
14. Atomic case $P_i(x_j)$: $a_j$ and $b_j$ have the same type.
    Atomic case $x_i = x_j$: matched tuples have the same equalities.
    The cases $\neg$ and $\wedge$ follow from the induction hypothesis on $\varphi$.
15. Case $\varphi = \exists y \, \psi(\vec{x}, y)$, so $r \ge 1$ and $\psi$ has rank at most $r - 1$.
    The tuples in $\psi$ have length $n + 1$, and $(n + 1) + (r - 1) \le q$, so $C(r - 1)$ applies to $\psi$.

### Part 2, continued: the quantifier step

16. Suppose $\mathcal{A} \models \psi[\vec{a}, c]$.
    If $c = a_i$ for some $i$, let $d = b_i$, and then $(\vec{a}, c)$ and $(\vec{b}, d)$ are matched.
17. Otherwise let $\tau$ be the type of $c$, and let $m$ be the number of distinct $a_i$ of type $\tau$.
    Matching gives exactly $m$ distinct $b_i$ of type $\tau$.
18. Since $c \in A_\tau$ differs from these $m$ elements, $\abs{A_\tau} \ge m + 1$.
    Also $m \le n \le q - r \le q - 1$, so $m + 1 \le q$.
19. So $\abs{B_\tau} = \min(\abs{A_\tau}, q) \ge m + 1$, and some $d \in B_\tau$ differs from all $b_i$.
    Then $(\vec{a}, c)$ and $(\vec{b}, d)$ are matched.
20. In both cases $C(r - 1)$ gives $\mathcal{B} \models \psi[\vec{b}, d]$, so $\mathcal{B} \models \varphi[\vec{b}]$.
21. Conversely, suppose $\mathcal{B} \models \psi[\vec{b}, d]$.
    If $d = b_i$ for some $i$, let $c = a_i$.
22. Otherwise let $\tau$ be the type of $d$, and let $m$ be the number of distinct $b_i$ of type $\tau$.
    Then $\abs{A_\tau} \ge \abs{B_\tau} \ge m + 1$, so some $c \in A_\tau$ differs from all $a_i$.
23. In both cases the tuples are matched, and $C(r - 1)$ gives $\mathcal{A} \models \psi[\vec{a}, c]$, so $\mathcal{A} \models \varphi[\vec{a}]$.
24. Apply $C(q)$ with $n = 0$ to $\sigma$.
    Since $\mathcal{A} \models \sigma$, also $\mathcal{B} \models \sigma$, and $\abs{B} \le q \cdot 2^k$.
    This proves part 2.

### Part 3: decidability

25. For a monadic sentence $\sigma$, let $N = 2^k$ without equality and $N = \max(q, 1) \cdot 2^k$ with equality.
    Both numbers are computable from $\sigma$.
26. Up to isomorphism, there are finitely many $L$-structures with at most $N$ elements.
    Each has domain $\{ 1, \ldots, s \}$ with $s \le N$, and each $P_i$ is one of the $2^s$ subsets.
27. In each such structure, the truth of $\sigma$ is computable, by checking all values of the quantified variables.
28. By parts 1 and 2, $\sigma$ is satisfiable if and only if one of these structures is a model.
    So satisfiability is decidable.
29. $\sigma$ is valid if and only if $\neg \sigma$ is not satisfiable, and $\neg \sigma$ has the same predicates and the same rank.
    So validity is decidable.

## Idea

A monadic formula sees an element only through its type, the set of predicates that contain it.
Without equality, one element of each type behaves like the whole set of elements of that type, so $2^k$ elements suffice.
For example, if $\mathcal{A}$ has a million elements in $P$ and none outside, the one-element structure with $P$ true behaves the same for every sentence in $P$ without equality.
With equality, a formula of rank $q$ can count each type only up to $q$, so $q$ elements of each type suffice.
The matching argument of part 2 is a simple Ehrenfeucht-Fraïssé game.

## Variants

Elimination of quantifiers gives another proof.
Every monadic formula is equivalent to a Boolean combination of formulas of the form $\tau(x)$, $x = y$, and "there are at least $m$ elements of type $\tau$".
The bound on the models follows from this normal form.

In the language of [[Ehrenfeucht-Fraïssé games|2RE7YAZK8R]], steps 16 to 23 describe a winning strategy for the second player in the $q$-round game on $\mathcal{A}$ and $\mathcal{B}$.
