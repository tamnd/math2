---
tag: 5T8YDW60RV
kind: proof
name: Proof of the number of k-element subsets by induction
msc: [05A10]
proves: 0BFMR2FQ8B
uses: [05099E1NMJ, 0JZSRWRBZE, 092GEF38YD, 0SNQEF7Z53, 0EE2V3CHFK, 03QC59M99B, 0GV2573FP4, 0YRG241HQQ]
methods: [0ASJVEFA9J]
sources:
  - url: https://proofwiki.org/wiki/Cardinality_of_Set_of_Subsets
    locator: Proof 4
---

## Proof

For a set $X$ and a natural number $k$, let $C(X, k)$ be the set of [[$k$-combinations|0JZSRWRBZE]] of $X$, the subsets with exactly $k$ elements. We argue by induction on $n = |X|$ that $|C(X, k)| = \binom{n}{k}$ for every $k$.

1. Let $n = 0$. Then $X = \varnothing$, and its only subset $\varnothing$ has $0$ elements.
2. So $|C(X, 0)| = 1 = \binom{0}{0}$ and $|C(X, k+1)| = 0 = \binom{0}{k+1}$, by the definition of the [[binomial coefficient|092GEF38YD]].
3. Suppose the claim holds for all sets with $n$ elements. Let $|X| = n + 1$, with a [[bijection|0SNQEF7Z53]] $f : \set{1, \dots, n+1} \to X$.
4. Put $x = f(n+1)$ and $X' = X \setminus \set{x}$. The restriction of $f$ to $\set{1, \dots, n}$ is a bijection onto $X'$, so $|X'| = n$.
5. Only $\varnothing$ has $0$ elements, so $|C(X, 0)| = 1 = \binom{n+1}{0}$.
6. Now fix $k \ge 0$. Split $C(X, k+1)$ into $C_{\mathrm{out}}$, the sets that omit $x$, and $C_{\mathrm{in}}$, the sets that contain $x$. These parts are disjoint.
7. The sets in $C_{\mathrm{out}}$ are exactly the $(k+1)$-element subsets of $X'$. By the induction hypothesis, $|C_{\mathrm{out}}| = \binom{n}{k+1}$.
8. For $S \in C_{\mathrm{in}}$, the set $S \setminus \set{x}$ is a subset of $X'$. By the [[complement principle|03QC59M99B]] in $S$, it has $(k+1) - 1 = k$ elements.
9. For $T \in C(X', k)$, the sets $T$ and $\set{x}$ are disjoint, since $x \notin X'$. By the [[rule of sum|0EE2V3CHFK]], $T \cup \set{x}$ has $k + 1$ elements, so it lies in $C_{\mathrm{in}}$.
10. The maps $S \mapsto S \setminus \set{x}$ and $T \mapsto T \cup \set{x}$ are mutually inverse. So they are bijections between $C_{\mathrm{in}}$ and $C(X', k)$.
11. By the induction hypothesis, $C(X', k)$ has $\binom{n}{k}$ elements. Composing a numbering of it with $T \mapsto T \cup \set{x}$ numbers $C_{\mathrm{in}}$. So $|C_{\mathrm{in}}| = \binom{n}{k}$, as in the [[bijection principle|0GV2573FP4]].
12. By the rule of sum, $|C(X, k+1)| = \binom{n}{k} + \binom{n}{k+1}$.
13. By [[Pascal's rule|0YRG241HQQ]], this equals $\binom{n+1}{k+1}$. Together with step 5, the claim holds for all $k$, and the induction is complete.

## Idea

Fix one element $x$. A subset of size $k+1$ either avoids $x$, or contains $x$ together with $k$ other elements.
These two cases are counted by the smaller set, and they add up exactly as the defining recursion of $\binom{n}{k}$ does.
