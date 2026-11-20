---
tag: DPKJWDD7XN
kind: example
name: Contraction fails in affine logic
msc: ["03F52"]
topics: [98QF5J4W16]
audience: research
not_instance_of:
  - target: V0MZVC2XA9
    note: affine logic does not derive p implies p times p, so it has no contraction for arbitrary formulas
uses: [YREXK6X3RP, V0MZVC2XA9, H408H4WHBA]
sources:
  - url: https://en.wikipedia.org/wiki/Affine_logic
    locator: lead
  - url: https://plato.stanford.edu/entries/logic-linear/
    locator: 2.1 Sequent calculus
    note: Di Cosmo and Miller, Linear Logic, Stanford Encyclopedia of Philosophy, revision of 2023-09-16
---

## Example

For an atom $p$, the sequent $\vdash p^{\perp}, p \otimes p$, that is $p \multimap p \otimes p$, is not derivable in [[affine logic|YREXK6X3RP]].
So affine logic does not have [[contraction|V0MZVC2XA9]] for all formulas.
We give each formula a value in $[0, 1]$ and show that every derivable sequent has values with sum at least $1$.

1. Choose $v(p) \in [0, 1]$ for each atom, and put $v(p^{\perp}) = 1 - v(p)$.
2. Put $v(A \otimes B) = \max(0, v(A) + v(B) - 1)$ and $v(A \mathbin{\wp} B) = \min(1, v(A) + v(B))$.
3. Put $v(A \mathbin{\&} B) = \min(v(A), v(B))$, $v(A \oplus B) = \max(v(A), v(B))$, $v(1) = v(\top) = 1$ and $v(\bot) = v(0) = 0$.
4. Put $v(!A) = 1$ if $v(A) = 1$ and $0$ otherwise, and $v(?A) = 1$ if $v(A) > 0$ and $0$ otherwise.
5. Then $v(A^{\perp}) = 1 - v(A)$ for every formula $A$, by induction on $A$ and the De Morgan laws of linear logic.
6. Call $\vdash \Gamma$ *good* if the sum of $v(C)$ over the formulas $C$ of $\Gamma$, with multiplicity, is at least $1$.
7. The axiom is good, since $v(A^{\perp}) + v(A) = 1$.
   The axioms for $1$ and $\top$ are good, since $v(1) = v(\top) = 1$.
8. Cut keeps goodness: from $s + v(A) \geq 1$ and $t + 1 - v(A) \geq 1$, adding gives $s + t \geq 1$.
9. Weakening adds a value $\geq 0$, and the rules for $\bot$, $\mathbin{\wp}$, $\mathbin{\&}$ and $\oplus$ keep goodness by the definitions in steps 2 and 3.
10. Rule $\otimes$: let $s + a \geq 1$ and $t + b \geq 1$.
    If $a + b \geq 1$, then $s + t + (a + b - 1) \geq 1$.
    Otherwise $s + t \geq 2 - a - b > 1$.
11. Dereliction keeps goodness, since $v(?A) \geq v(A)$; contraction for $?A$ keeps it, since $v(?A)$ is $0$ or $1$.
12. Promotion: if a formula $?C$ in the context has value $1$, the conclusion is good.
    Otherwise all context values are $0$, the premise gives $v(A) \geq 1$, and so $v(!A) = 1$.
13. So every sequent derivable in affine logic is good, by induction on derivations.
14. Take $v(p) = 1/2$.
    Then $v(p^{\perp}) + v(p \otimes p) = 1/2 + \max(0, 0) = 1/2 < 1$.
15. So $\vdash p^{\perp}, p \otimes p$ is not good, and it is not derivable in affine logic.

## Remarks

The sequent $\vdash ?p^{\perp}, p \otimes p$, that is $!p \multimap p \otimes p$, is derivable in affine logic, as in [[linear logic|H408H4WHBA]].
In the valuation above, $v(?p^{\perp}) = 1$ when $v(p) = 1/2$, so it is good, as it must be.
The proof uses cut as one of the rules, so it does not need cut elimination for affine logic.

## Explanations

### L1 human

A value between $0$ and $1$ measures how much of a resource we have.
Two copies of half a resource joined by $\otimes$ have value $0$, so one half cannot yield two halves.

### L2 human

We check step 10 with numbers.

1. Let $\Gamma$ have sum $s = 0.3$ and $a = 0.7$, so $s + a = 1$.
2. Let $\Delta$ have sum $t = 0.6$ and $b = 0.4$, so $t + b = 1$.
3. Then $a + b = 1.1 \geq 1$, and $v(A \otimes B) = 0.1$.
4. The conclusion has sum $0.3 + 0.6 + 0.1 = 1$, so it is good.

The typical use of such a valuation is to prove that a sequent is not derivable without a search for proofs.
A trap: the valuation does not refute weakening, and it cannot, since weakening is a rule of affine logic.
