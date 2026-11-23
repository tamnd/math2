---
tag: BKYX7JYW9J
kind: proof
name: Proof that residua exist exactly for left-continuous t-norms
msc: ["03B52", "06F05"]
topics: [WZP584JQ06]
audience: grad
proves: D1R4D2HEPP
uses: [BHGCVPAJW0]
methods: [0NTF6DMVAP, TFQ1845T84]
sources:
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: 1. Fuzzy connectives based on t-norms
---

## Proof

We fix $x$ and show that the map $z \mapsto z * x$ has a residuum exactly when it preserves suprema, which is left-continuity.

Fix $x \in [0, 1]$, and write $f(z) = z * x$.
The map $f$ is monotone by the axioms of [[a t-norm|BHGCVPAJW0]].
A monotone function of two variables is left-continuous exactly when it is left-continuous in each variable, and by commutativity it is enough to treat the first.

Step A shows that $f$ is left-continuous if and only if $f(\sup Z) = \sup f[Z]$ for every nonempty $Z \subseteq [0, 1]$.

1. Assume $f$ preserves suprema, and let $z_n$ increase to $z$.
   Then $\sup_n z_n = z$, so the increasing sequence $f(z_n)$ has supremum $f(z)$, and hence $f(z_n) \to f(z)$.
2. Conversely, assume $f$ is left-continuous, and let $s = \sup Z$.
   By monotonicity $f(w) \le f(s)$ for every $w \in Z$, so $\sup f[Z] \le f(s)$.
3. If $s \in Z$, then $f(s) \le \sup f[Z]$ directly.
4. If $s \notin Z$, choose $z_n \in Z$ increasing to $s$.
   By left-continuity $f(z_n) \to f(s)$, so again $f(s) \le \sup f[Z]$.

Step B shows that left-continuity gives a residuum.

5. Let $Z = \{ z : z * x \le y \}$.
   The set $Z$ is nonempty, since $0 * x = 0 \le y$.
6. Let $r = \sup Z$.
   By Step A, $r * x = \sup \{ z * x : z \in Z \}$, and every term is at most $y$, so $r * x \le y$.
7. So $r \in Z$, and $r = \max Z$.
8. If $z \le r$, then $z * x \le r * x \le y$ by monotonicity.
   If $z * x \le y$, then $z \in Z$, so $z \le r$.
9. So setting $x \Rightarrow_* y = r$ satisfies residuation.

Step C shows that a residuum gives left-continuity.

10. Let $\Rightarrow$ be a residuum, let $Z$ be nonempty, and put $s = \sup Z$ and $t = \sup \{ z * x : z \in Z \}$.
    By monotonicity $t \le s * x$.
11. For each $z \in Z$ we have $z * x \le t$, so $z \le x \Rightarrow t$ by residuation.
12. So $s \le x \Rightarrow t$, and residuation gives $s * x \le t$.
13. Hence $s * x = t$, and by Step A the map $z \mapsto z * x$ is left-continuous.

Step D shows uniqueness and the formula.

14. Let $\Rightarrow$ and $\Rightarrow'$ be residua.
    Then $z \le x \Rightarrow y$ holds iff $z * x \le y$ holds iff $z \le x \Rightarrow' y$ holds.
15. Taking $z = x \Rightarrow y$ gives $x \Rightarrow y \le x \Rightarrow' y$, and taking $z = x \Rightarrow' y$ gives the reverse.
16. So the residuum is unique, and it equals the $r = \max Z$ of Step B. $\blacksquare$

## Idea

For fixed $x$, the map $z \mapsto z * x$ needs a right adjoint, which is what a residuum is.
A monotone map on $[0, 1]$ has a right adjoint exactly when it preserves suprema, and for a monotone map that is left-continuity.
The drastic t-norm shows the failure: for $x = 0.5$ and $y = 0$ the set $Z$ is $[0, 1)$, whose supremum $1$ is not in $Z$.

## Variants

The same argument works in any complete lattice, with "preserves all joins" in place of left-continuity.
Steps B and C never use that $[0, 1]$ is a chain, only that suprema exist and that $*$ is monotone.
Step A is the only place where the order of the real line enters, through sequences.
