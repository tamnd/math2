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

Fix $x \in [0, 1]$, and write $f(z) = z * x$.
$f$ is monotone by the axioms of [[a t-norm|BHGCVPAJW0]].

**Step A: left-continuity means preservation of suprema.**
Claim: $f$ is left-continuous iff $f(\sup Z) = \sup f[Z]$ for every non-empty $Z \subseteq [0, 1]$.

1. Assume $f$ preserves suprema, and let $z_n \uparrow z$. Then $\sup_n z_n = z$.
2. So $f(z_n)$ increases with supremum $f(z)$, hence $f(z_n) \to f(z)$.
3. Conversely, assume $f$ is left-continuous, and let $s = \sup Z$.
4. $f(w) \le f(s)$ for $w \in Z$, by monotonicity, so $\sup f[Z] \le f(s)$.
5. If $s \in Z$, then $f(s) \le \sup f[Z]$.
6. If $s \notin Z$, choose $z_n \in Z$ with $z_n \uparrow s$.
7. By left-continuity $f(z_n) \to f(s)$, so $f(s) \le \sup f[Z]$.

**Step B: left-continuity implies a residuum.**

8. Let $Z = \set{z : z * x \le y}$. $Z$ contains $0$, since $0 * x = 0$.
9. Let $r = \sup Z$. By Step A, $r * x = \sup \set{z * x : z \in Z} \le y$.
10. So $r \in Z$, and $r = \max Z$.
11. If $z \le r$, then $z * x \le r * x \le y$, by monotonicity.
12. If $z * x \le y$, then $z \in Z$, so $z \le r$.
13. So $x \Rightarrow_* y := r$ satisfies residuation.

**Step C: a residuum implies left-continuity.**

14. Let $\Rightarrow$ be a residuum, $Z$ non-empty, $s = \sup Z$ and $t = \sup \set{z * x : z \in Z}$.
15. $t \le s * x$, by monotonicity.
16. For $z \in Z$: $z * x \le t$, so $z \le x \Rightarrow t$, by residuation.
17. So $s \le x \Rightarrow t$, and by residuation $s * x \le t$.
18. Hence $s * x = t$, and by Step A, $z \mapsto z * x$ is left-continuous.

**Step D: uniqueness and the formula.**

19. If $\Rightarrow$ and $\Rightarrow'$ are residua, then $z \le x \Rightarrow y$ iff $z * x \le y$ iff $z \le x \Rightarrow' y$.
20. Take $z = x \Rightarrow y$ and $z = x \Rightarrow' y$; then the two values are equal.
21. So the residuum is the $r = \max Z$ of Step B. $\blacksquare$

## Idea

For fixed $x$, the map $z \mapsto z * x$ needs a right adjoint.
A monotone map on $[0, 1]$ has one iff it preserves suprema, and that is left-continuity.

## Variants

The same argument works in any complete lattice, with "preserves all joins" in place of left-continuity.
