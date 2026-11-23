---
tag: GK0B8HZ8DZ
kind: example
name: A cut with the formula on the same side is unsound
msc: ["03F05"]
topics: [R10RMQCJQX]
audience: ug2
not_instance_of:
  - target: HGVMPZ2DXA
    note: the shared formula occurs in the succedent of both premises, while the cut rule needs it in the succedent of one premise and in the antecedent of the other
uses: [PZX9J3VEMT, DAMGTSY6VV]
sources:
  - url: https://en.wikipedia.org/wiki/Cut_rule
    locator: lead section
---

## Example

Consider the rule R that looks like cut but keeps the shared formula $A$ on the right in both premises.
$$\dfrac{\Gamma \Rightarrow \Delta, A \qquad \Pi \Rightarrow \Lambda, A}{\Gamma, \Pi \Rightarrow \Delta, \Lambda}\,\mathrm{R}$$
We show that R derives a false sequent from two derivable ones.

1. The axiom $p \Rightarrow p$ has the form $\Gamma \Rightarrow \Delta, A$ with $\Gamma = p$, $\Delta$ empty and $A = p$.
2. From $p \Rightarrow p$, the rule ${\neg}$R gives $\Rightarrow p, \neg p$, and an exchange gives $\Rightarrow \neg p, p$.
3. The sequent of step 2 has the form $\Pi \Rightarrow \Lambda, A$ with $\Pi$ empty, $\Lambda = \neg p$ and $A = p$.
4. The rule R gives $\Gamma, \Pi \Rightarrow \Delta, \Lambda$, which is $p \Rightarrow \neg p$.
5. Let $p$ be true.
   Then the antecedent $p$ is true and the succedent $\neg p$ is false, so the sequent $p \Rightarrow \neg p$ is false.
6. The [[cut rule|DAMGTSY6VV]] needs $A$ in the antecedent of the right premise.
   The right premise of step 4 has an empty antecedent, so step 4 is not a cut.

## Remarks

The example shows why the cut formula must change sides.
The left premise says "from $\Gamma$, some formula of $\Delta$ or $A$ holds".
Only a premise that takes $A$ as an assumption can discharge $A$, so only such a premise may make it disappear.
In the case above $A = p$ is the only true formula in both succedents, and R throws exactly that formula away.

The mirror rule, with $A$ on the left in both premises, fails in the same way.
It infers $\Gamma, \Pi \Rightarrow \Delta, \Lambda$ from $A, \Gamma \Rightarrow \Delta$ and $A, \Pi \Rightarrow \Lambda$.
With $A = p$, the premises $p \Rightarrow p$ and $p, \neg p \Rightarrow$ give $\neg p \Rightarrow p$.
That sequent is false when $p$ is false.
Both bad rules have the shape "two premises, one shared formula drops out", so the shape alone does not make a rule a cut.

## Explanations

### L1 human

The lemma rule says: prove $A$, then use $A$.
The false rule says: prove "something or $A$" twice, then forget $A$.
That is not safe, because $A$ may be the only true part of both claims.
With one true statement $p$, the false rule turns "from $p$ we get $p$" and "$\neg p$ or $p$" into "from $p$ we get $\neg p$".

### L2 human

The check is one row of a truth table, the row where $p$ is true.
In that row both premises $p \Rightarrow p$ and $\Rightarrow \neg p, p$ are true, and the conclusion $p \Rightarrow \neg p$ is false.
So R does not preserve truth, and LK with R added would be unsound.
Watch out: checking that "a formula disappears" is not enough to recognize a cut, because the side on which it stands decides soundness.
