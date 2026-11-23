---
tag: Y8EQM4QS3D
kind: proof
name: Proof of the residua of the basic t-norms
msc: ["03B52"]
topics: [WZP584JQ06]
audience: grad
proves: 7R2JBNNMT5
uses: [BHGCVPAJW0]
methods: [0WCP0PVET6, TFQ1845T84]
sources:
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: 1. Fuzzy connectives based on t-norms
---

## Proof

For each t-norm $*$ and candidate $r(x, y)$, we prove that $z * x \le y$ holds exactly when $z \le r(x, y)$, for all $x, y, z \in [0, 1]$.
This is the residuation law of [[the definition|BHGCVPAJW0]], and a residuum is unique, so $r$ is the residuum.

Łukasiewicz, with $r(x, y) = \min(1, 1 - x + y)$:

1. Since $y \ge 0$, the inequality $\max(0, z + x - 1) \le y$ holds exactly when $z + x - 1 \le y$, that is, when $z \le 1 - x + y$.
2. Since $z \le 1$ always holds, $z \le 1 - x + y$ holds exactly when $z \le \min(1, 1 - x + y)$.

Gödel, with $r(x, y) = 1$ if $x \le y$ and $r(x, y) = y$ otherwise:

3. Let $x \le y$.
   Then $\min(z, x) \le x \le y$ for every $z$, and $z \le 1$ for every $z$, so both sides hold for all $z$.
4. Let $x > y$.
   If $z \le y$, then $\min(z, x) \le z \le y$.
5. If $z > y$, then $\min(z, x) > y$, because both $z > y$ and $x > y$.
   So for $x > y$, $\min(z, x) \le y$ holds exactly when $z \le y$.

Product, with $r(x, y) = 1$ if $x \le y$ and $r(x, y) = y / x$ otherwise:

6. Let $x \le y$.
   Then $z x \le x \le y$ for every $z \in [0, 1]$, so both sides hold for all $z$.
7. Let $x > y$.
   Then $x > 0$, and dividing by the positive number $x$ shows that $z x \le y$ holds exactly when $z \le y / x$.
8. Here $0 \le y / x < 1$, so the value $y / x$ lies in $[0, 1]$.

Negations, with $y = 0$:

9. For Łukasiewicz, $x \Rightarrow 0 = \min(1, 1 - x) = 1 - x$.
10. For Gödel and product, $x \le 0$ holds only for $x = 0$, so $0 \Rightarrow 0 = 1$.
11. For $x > 0$, Gödel gives $0$ and product gives $0 / x = 0$.

This proves the three residua and the three negations.
$\blacksquare$

## Idea

A residuum is the largest $z$ that, combined with $x$, stays at most $y$.
So the proof solves the inequality $z * x \le y$ for $z$, the way one solves a linear inequality in school.
For Łukasiewicz the solution is a subtraction, for the product it is a division, and for the minimum the answer is $y$ itself.
The case $x \le y$ is the same for all three: every $z$ works, so the answer is $1$.

## Variants

One can first prove, for every left-continuous t-norm, that the residuum is $\max \{ z : z * x \le y \}$, as in [[the left-continuity statement|D1R4D2HEPP]].
Then each residuum is the computation of a maximum, and steps 1 to 8 become the computation of that maximum.
That route needs the general theorem first, while the direct proof above uses only the definition.
