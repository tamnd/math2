---
tag: FR9JC8MNBJ
kind: proof
name: Proof that Post's connectives are functionally complete
msc: ["03B50", "08A40"]
topics: [WZP584JQ06]
audience: research
proves: 8P3Y6T0RZS
uses: [PHGRJ2D97H, EJ8YJVM9BW]
methods: [01XM7JEKHY, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Many-valued_logic
    locator: Post logics Pm
---

## Proof

We build a disjunctive normal form for $f$ out of tests that detect one value each.
Write $V = \{0, \dots, m - 1\}$, $\neg x = x - 1 \bmod m$ and $x \lor y = \max(x, y)$, as in [[the definition|PHGRJ2D97H]].
All terms below are built from $\neg$, $\lor$ and variables.
Let $S x = \neg^{m-1} x = x + 1 \bmod m$, so that $S^k x = x + k \bmod m$.

### Constants and tests

1. Put $\top(x) = \max(x, Sx, \dots, S^{m-1} x)$.
   The values $x + k \bmod m$ for $0 \le k \le m - 1$ are all of $V$, so $\top(x) = m - 1$.
2. Put $\bot(x) = S(\top(x))$.
   Then $\bot(x) = (m - 1) + 1 \bmod m = 0$.
3. Put $M(x) = \max_{0 \le k \le m - 2} S^k x$.
   The values $S^k x$ with $k \le m - 2$ are all residues except $x - 1 \bmod m$.
4. So $M(x) = m - 1$ when $x - 1 \not\equiv m - 1$, that is when $x \ne 0$, and $M(0) = m - 2$.
5. Put $J_0(x) = S(M(x))$.
   Step 4 gives $J_0(0) = S(m - 2) = m - 1$, and $J_0(x) = S(m - 1) = 0$ for $x \ne 0$.
6. For $a \in V$ put $J_a(x) = J_0(S^{m-a} x)$.
   Since $S^{m-a} x = x - a \bmod m$, the argument is $0$ exactly when $x = a$, so step 5 gives $J_a(a) = m - 1$ and $J_a(x) = 0$ for $x \ne a$.

### Conjunction and scaling

7. For $u, v \in \{0, m - 1\}$ put $u \sqcap v = J_0(\max(J_0 u, J_0 v))$.
8. If $u = v = m - 1$, then $J_0 u = J_0 v = 0$ by step 5, and $J_0(0) = m - 1$.
   So $u \sqcap v = m - 1$.
9. If $u = 0$ or $v = 0$, then the maximum is $m - 1$, and $J_0(m - 1) = 0$ because $m - 1 \ne 0$.
   So $u \sqcap v = 0$, and $\sqcap$ is $\min$ on $\{0, m - 1\}$.
10. For $1 \le c \le m - 1$ and $e \in \{0, m - 1\}$ put $K_c(e) = S(\max(S^c e, J_0 e))$.
11. If $e = m - 1$, then $S^c e = c - 1$ and $J_0 e = 0$.
    The maximum is $c - 1$, because $c \ge 1$, so $K_c(e) = c$.
12. If $e = 0$, then $S^c e = c$ and $J_0 e = m - 1$.
    The maximum is $m - 1$, so $K_c(e) = 0$.

### The normal form

Let $f \colon V^n \to V$ with $n \ge 1$, and let $A = \{a \in V^n : f(a) \ge 1\}$.

13. If $A = \emptyset$, then $f(x_1, \dots, x_n) = \bot(x_1)$ by step 2.
14. Otherwise, for $a \in A$ put $T_a(x) = J_{a_1}(x_1) \sqcap \dots \sqcap J_{a_n}(x_n)$.
    By steps 6 and 9, $T_a(x) = m - 1$ if $x = a$ and $T_a(x) = 0$ otherwise.
15. Put $t(x) = \max_{a \in A} K_{f(a)}(T_a(x))$.
16. Let $x = b \in A$.
    The disjunct for $a = b$ is $K_{f(b)}(m - 1) = f(b)$ by step 11, and every other disjunct is $K_c(0) = 0$ by step 12, so $t(b) = f(b)$.
17. Let $x = b \notin A$.
    Every disjunct is $0$ by step 12, so $t(b) = 0 = f(b)$.

So $t$ is a term in $\neg$ and $\lor$ with $t = f$ on all of $V^n$, and $\{\neg, \lor\}$ is functionally complete.

## Idea

The proof copies the disjunctive normal form of classical logic.
The tests $J_a$ play the part of literals, $\sqcap$ plays the part of conjunction, and $\max$ joins the rows of the table.
The cyclic shift is what makes the tests possible.
A maximum over all shifts but one misses exactly one value, so it detects whether the input sits in one fixed place.
The scaling maps $K_c$ then lower the top value to the output that each row needs.

## Variants

One can first define $\min$ on all of $V$ and then use it in place of $\sqcap$.
The version above needs $\min$ only on the two values $0$ and $m - 1$, which keeps the terms simpler to check.
The same proof works for any set of connectives that defines $S$ and $\max$.
This is how [[Webb's Sheffer function|EPSBDVPKJP]] is shown complete, and [[the three-valued case|FV0ZA5CEH6]] runs the proof for one function.
