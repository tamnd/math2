---
tag: DJWM6VAW72
kind: example
name: Necessitation gives the boxed tautologies in K
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
instance_of: [G989VP2NGP]
uses: [G989VP2NGP, JS8W7PA6JK, 05006AJ7DZ, 0Y0MQYST0M, NGHWZ9Y7ZV]
sources:
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds
---

## Example

We use the [[necessitation rule|G989VP2NGP]], "from $\vdash \varphi$ infer $\vdash \square\varphi$", in the logic $\mathsf{K}$ of [[normal modal logic K|JS8W7PA6JK]].
First we box some tautologies.

1. $\vdash \top$, since $\top = \bot \to \bot$ is a [[tautology|05006AJ7DZ]].
2. $\vdash \square\top$, by necessitation from line 1.
3. $\vdash \square\square\top$, by necessitation from line 2.
4. $\vdash \square(p \to p)$, by necessitation from the tautology $p \to p$.

Then we derive the rule RK for two premises: from $\vdash (\varphi_1 \wedge \varphi_2) \to \psi$ infer $\vdash (\square\varphi_1 \wedge \square\varphi_2) \to \square\psi$.

5. From the premise, $\vdash \varphi_1 \to (\varphi_2 \to \psi)$, by a tautology and [[modus ponens|0Y0MQYST0M]].
6. $\vdash \square(\varphi_1 \to (\varphi_2 \to \psi))$, by necessitation.
7. $\vdash \square\varphi_1 \to \square(\varphi_2 \to \psi)$, by an instance of $\mathrm{K}$ and modus ponens.
8. $\vdash \square(\varphi_2 \to \psi) \to (\square\varphi_2 \to \square\psi)$, an instance of $\mathrm{K}$.
9. $\vdash \square\varphi_1 \to (\square\varphi_2 \to \square\psi)$, by chaining lines 7 and 8.
10. $\vdash (\square\varphi_1 \wedge \square\varphi_2) \to \square\psi$, by propositional logic from line 9.

Check: at a world $w$ of a [[Kripke model|NGHWZ9Y7ZV]], $\top$ is true at every successor of $w$, so $\square\top$ is true at $w$, also when $w$ has no successors.

## Remarks

Necessitation makes theorems $\square\varphi$ only from theorems $\varphi$, and the axiom $\mathrm{K}$ then moves the box across implications.
So every boxed tautology, and every $\square^n\varphi$ with $\varphi$ a theorem, is a theorem of $\mathsf{K}$.
RK for $n$ premises works in the same way, with $n$ uses of $\mathrm{K}$, and for $n = 1$ it is the rule RM.

The theorem $\square\top$ differs from $\lozenge\top$.
The formula $\lozenge\top$ is false at a world without successors, so $\mathsf{K} \nvdash \lozenge\top$.

If we drop necessitation and keep the axiom $\mathrm{K}$, then $\square\top$ is no longer derivable.
To see this, read $\square$ as the constant truth function "false".
Then every axiom is true, modus ponens keeps truth, and $\square\top$ is false.

## Explanations

### L1 human

Necessitation says that whatever logic proves is necessary.
The statement "if it rains, then it rains" is always true, so "necessarily, if it rains then it rains" is a law.
We can apply the rule again, and get "necessarily necessarily" in front of the same statement.
In the picture of worlds, a law is true in every world, so it is true in all worlds that a given world can see.
This holds even for a world that sees nothing.

### L2 human

Two instances of RK show what it can do.
With $\varphi_1 = p$, $\varphi_2 = p \to q$ and $\psi = q$, the premise $(p \wedge (p \to q)) \to q$ is a tautology.
So RK gives $\vdash (\square p \wedge \square(p \to q)) \to \square q$, which is a form of the axiom $\mathrm{K}$.
With $\varphi_1 = p$, $\varphi_2 = \neg p$ and $\psi = \bot$, RK gives $\vdash (\square p \wedge \square\neg p) \to \square\bot$.
The typical use of RK is in derivations of theorems of the form $(\square\alpha \wedge \square\beta) \to \square\gamma$.
Watch out: necessitation applies to theorems only, so $p \to \square p$ is not a theorem; see [[the formula p → □p is not a theorem of K|R2WWD2R5NV]].
