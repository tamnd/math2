---
tag: 5WQDFMR91G
kind: example
name: A proof system with the rule of affirming the consequent is unsound
msc: ["03B05"]
topics: [H8QZY0RZXZ]
audience: ug2
not_instance_of:
  - target: 4A84VHDTHV
    note: "The rule 'from psi and phi -> psi infer phi' does not keep truth, so the system derives p from {p -> q, q} and even derives every formula."
uses: [4A84VHDTHV, HZCFTQDRA5, J7KFCFQRBT, 0Y0MQYST0M]
sources:
  - url: https://en.wikipedia.org/wiki/Soundness
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Affirming_the_consequent
    locator: lead section
---

## Example

Let $\mathsf{H}$ be the [[Hilbert system of the soundness theorem|HZCFTQDRA5]], with the schemas A1, A2, A3 and modus ponens.
Let $\mathsf{H}^{\mathrm{AC}}$ be $\mathsf{H}$ with one more rule, the rule of [[affirming the consequent|J7KFCFQRBT]]: from $\psi$ and $\varphi \to \psi$, infer $\varphi$.
We show that $\mathsf{H}^{\mathrm{AC}}$ is not [[sound|4A84VHDTHV]] for truth tables, in the strong and in the weak sense.

1. Let $\Gamma = \{ p \to q, \; q \}$.
   The list $p \to q$, $q$, $p$ is a derivation from $\Gamma$.
   The first two lines are members of $\Gamma$, and the third line uses the new rule on lines 2 and 1.
2. The valuation $p = \mathsf{F}$, $q = \mathsf{T}$ gives $v(p \to q) = \mathsf{T}$ and $v(q) = \mathsf{T}$, but $v(p) = \mathsf{F}$.
3. So $\Gamma \vdash p$ but $\Gamma \not\models p$, and strong soundness fails.
4. Now let $\varphi$ be any formula, and let $\alpha$ be the A1 instance $p_1 \to (p_1 \to p_1)$.
5. Line 1 is $\alpha$, an instance of A1.
   Line 2 is $\alpha \to (\varphi \to \alpha)$, an instance of A1 with $\alpha$ for the first letter and $\varphi$ for the second.
6. Line 3 is $\varphi \to \alpha$, by [[modus ponens|0Y0MQYST0M]] from lines 1 and 2.
7. Line 4 is $\varphi$, by the new rule from line 1, with $\psi = \alpha$, and line 3.
8. So every formula is a theorem of $\mathsf{H}^{\mathrm{AC}}$, including $p_1$, which is not a tautology.
   Weak soundness fails, and the system is not even Post consistent.

## Remarks

The failure is local: the rule itself does not keep truth, as step 2 shows with one valuation.
The system $\mathsf{H}$ without the rule is sound, so the extra rule alone causes the failure.
Step 8 shows more than unsoundness: with a theorem $\alpha$ and A1, the bad rule proves every formula.
The rule of denying the antecedent, "from $\lnot\varphi$ and $\varphi \to \psi$, infer $\lnot\psi$", is unsound for the same reason.
The valuation $\varphi = \mathsf{F}$, $\psi = \mathsf{T}$ makes both premises true and the conclusion false.

## Explanations

### L1 human

The rule "if it rains, the street is wet; the street is wet; so it rains" looks like modus ponens, but it runs backwards.
The street can be wet because a pipe broke, while there is no rain.
A proof system with this backwards rule can reach false conclusions from true facts.
Worse, it can prove any statement at all.

### L2 human

We use the bad rule on true facts about numbers.

1. "If $6 = 4$, then $6$ is even" is true, because its second part is true.
2. "$6$ is even" is true.
3. The bad rule, with $\psi$ = "$6$ is even" and $\varphi$ = "$6 = 4$", concludes "$6 = 4$", which is false.

The typical use of this example is as a test case: any new rule must be checked against every valuation before it joins a proof system.
A trap is to check the rule only in cases where the conclusion happens to be true.
For example "if $4 = 4$, then $4$ is even" and "$4$ is even" give the true conclusion "$4 = 4$", which proves nothing about the rule.
