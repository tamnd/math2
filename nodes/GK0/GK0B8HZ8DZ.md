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

Consider the rule R: from $\Gamma \Rightarrow \Delta, A$ and $\Pi \Rightarrow \Lambda, A$ infer $\Gamma, \Pi \Rightarrow \Delta, \Lambda$.
It looks like cut, but the formula $A$ is on the right in both premises.
We show that R derives a false sequent.

1. $p \Rightarrow p$ is an axiom of LK. It has the form $\Gamma \Rightarrow \Delta, A$ with $\Gamma = p$, $\Delta$ empty and $A = p$.
2. From $p \Rightarrow p$, the rule ${\neg}$R gives $\Rightarrow p, \neg p$, and an exchange gives $\Rightarrow \neg p, p$.
3. The sequent of step 2 has the form $\Pi \Rightarrow \Lambda, A$ with $\Pi$ empty, $\Lambda = \neg p$ and $A = p$.
4. The rule R gives $\Gamma, \Pi \Rightarrow \Delta, \Lambda$, which is $p \Rightarrow \neg p$.
5. Let $p$ be true. Then the antecedent $p$ is true and the succedent $\neg p$ is false, so $p \Rightarrow \neg p$ is false.
6. The [[cut rule|DAMGTSY6VV]] requires $A$ in the antecedent of the second premise. The second premise of step 4 has an empty antecedent, so step 4 is not a cut.

## Remarks

The example shows why the cut formula must change sides.
The left premise says "$\Gamma$ gives $\Delta$ or $A$", and only a premise that uses $A$ as an assumption can remove $A$.
The mirror rule, with $A$ on the left in both premises, is also unsound: from $p \Rightarrow p$ and $\neg p, p \Rightarrow$ it gives $\neg p \Rightarrow p$, which is false when $p$ is false.

## Explanations

### L1 human

The lemma rule says: prove $A$, then use $A$.
The false rule says: prove "something or $A$" twice, then drop $A$.
That is not safe, because $A$ may be the only true part of both claims.
For one true statement $p$, the false rule turns "$p$ gives $p$" and "$p$ or not $p$" into "$p$ gives not $p$".

### L2 human

The check is a truth table with one row: $p$ true.
Each premise is true in this row, and the conclusion $p \Rightarrow \neg p$ is false.
So R does not preserve truth, and adding it to LK makes the calculus unsound.
A trap is to check only the shape "two premises, one formula disappears": the side of the formula matters.
