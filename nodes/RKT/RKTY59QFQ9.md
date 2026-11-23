---
tag: RKTY59QFQ9
kind: example
name: Derived laws of standard deontic logic
msc: ["03B45"]
topics: [CQM9SRN8PM]
audience: grad
instance_of: [7B74J6J5JV]
uses: [7B74J6J5JV, JS8W7PA6JK, G989VP2NGP, 0Y0MQYST0M]
sources:
  - url: https://en.wikipedia.org/wiki/Deontic_logic
    locator: Standard deontic logic
---

## Example

We derive five laws in the Hilbert system of [[standard deontic logic|7B74J6J5JV]].
The system has all tautologies, the axioms $\mathrm{K}$: $O(p \to q) \to (Op \to Oq)$ and $\mathrm{D}$: $Op \to \neg O\neg p$, [[modus ponens|0Y0MQYST0M]], uniform substitution and the [[necessitation rule|G989VP2NGP]].

### Laws 1 and 2

Law 1 says that no code of norms requires a thing and its negation: $\vdash \neg(Op \wedge O\neg p)$.

1. The formula $Op \to \neg O\neg p$ is the axiom $\mathrm{D}$, since $Pp$ abbreviates $\neg O\neg p$.
2. The formula $(Op \to \neg O\neg p) \to \neg(Op \wedge O\neg p)$ is a tautology.
   Modus ponens with step 1 gives law 1.

Law 2 splits an obligation of a conjunction: $\vdash O(p \wedge q) \to (Op \wedge Oq)$.

3. The formula $(p \wedge q) \to p$ is a tautology, so necessitation gives $O((p \wedge q) \to p)$.
4. The axiom $\mathrm{K}$ and modus ponens give $O(p \wedge q) \to Op$.
5. In the same way we get $O(p \wedge q) \to Oq$.
   Propositional logic joins steps 4 and 5 into law 2.

### Laws 3 and 4

Law 3 joins two obligations: $\vdash (Op \wedge Oq) \to O(p \wedge q)$.

6. The formula $p \to (q \to (p \wedge q))$ is a tautology, so necessitation gives $O(p \to (q \to (p \wedge q)))$.
7. The axiom $\mathrm{K}$ gives $Op \to O(q \to (p \wedge q))$.
8. The instance of $\mathrm{K}$ for $q$ and $p \wedge q$ is $O(q \to (p \wedge q)) \to (Oq \to O(p \wedge q))$.
9. Chaining steps 7 and 8 gives $Op \to (Oq \to O(p \wedge q))$, which is law 3.

Law 4 says that the impossible is never obligatory: $\vdash \neg O\bot$.

10. The formula $\neg\bot$ is a tautology, so necessitation gives $O\neg\bot$.
11. Substitute $\bot$ for $p$ in $\mathrm{D}$ to get $O\bot \to \neg O\neg\bot$.
12. Steps 10 and 11 give $\neg O\bot$ by propositional logic.

### Law 5

Law 5 combines an obligation with a permission: $\vdash (Op \wedge Pq) \to P(p \wedge q)$.

13. Law 3 with $\neg(p \wedge q)$ in place of $q$ gives $(Op \wedge O\neg(p \wedge q)) \to O(p \wedge \neg(p \wedge q))$.
14. The formula $(p \wedge \neg(p \wedge q)) \to \neg q$ is a tautology.
   Necessitation and $\mathrm{K}$ give $O(p \wedge \neg(p \wedge q)) \to O\neg q$.
15. Steps 13 and 14 give $(Op \wedge O\neg(p \wedge q)) \to O\neg q$.
16. Contraposition in the second conjunct gives $(Op \wedge \neg O\neg q) \to \neg O\neg(p \wedge q)$.
   This is law 5 written with $P$.

## Remarks

Laws 2, 3 and 5 use only $\mathrm{K}$ and necessitation, so they hold in every [[normal modal logic|JS8W7PA6JK]].
Laws 1 and 4 need $\mathrm{D}$.
On a one-world frame with no arrow, $O\bot$ is true, so laws 1 and 4 fail in $\mathsf{K}$.
If we replace $\mathrm{D}$ by $\mathrm{T}$: $Op \to p$, all five laws still hold, but the logic now says that every obligation is met.

Law 5 says that if $p$ is obligatory and $q$ is permitted, then doing both is permitted.
Watch out: two permissions do not combine in the same way.
Take a world with two ideal worlds, one where $p$ holds and one where it fails.
There $Pp$ and $P\neg p$ both hold, but $P(p \wedge \neg p)$ is false, since no world satisfies a contradiction.

## Explanations

### L1 human

These five rules say that a sensible set of duties fits together.
You cannot be required both to do a thing and not to do it.
If you must lock the door and must close the window, then you must do both.
If you must lock the door and may open the window, then you may do both.
Each rule follows step by step from two basic laws.

### L2 human

We check law 5 on a model with three worlds.
Take $W = \{w, u, v\}$ with $R[w] = \{u, v\}$, $R[u] = \{u\}$ and $R[v] = \{v\}$, and let $V(p) = \{u, v\}$ and $V(q) = \{v\}$.
At $w$, $Op$ holds, since $p$ is true at both $u$ and $v$.
At $w$, $Pq$ holds, since $q$ is true at $v$.
At $v$ both $p$ and $q$ are true, so $P(p \wedge q)$ holds at $w$, as law 5 predicts.
The typical use of these laws is to simplify a set of norms before a consistency check.
