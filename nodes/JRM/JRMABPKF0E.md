---
tag: JRMABPKF0E
kind: example
name: Chaining two implications with a cut
msc: ["03F05"]
topics: [R10RMQCJQX]
audience: ug2
instance_of: [HGVMPZ2DXA]
uses: [PZX9J3VEMT, DAMGTSY6VV]
sources:
  - url: https://en.wikipedia.org/wiki/Cut_rule
    locator: lead section
---

## Example

We derive the sequent $p \to q, p, q \to r \Rightarrow r$ in LK with one cut on $q$, where $p$, $q$ and $r$ are propositional variables.
The plan is to prove the lemma $q$ in one branch, use it in the other, and join the branches by a cut.

1. The sequents $p \Rightarrow p$, $q \Rightarrow q$ and $r \Rightarrow r$ are axioms.
2. The rule ${\to}$L, with left premise $p \Rightarrow p$ and right premise $q \Rightarrow q$, gives $p \to q, p \Rightarrow q$.
   Here the contexts of ${\to}$L are $\Gamma = p$, $\Lambda = q$, and $\Delta$ and $\Pi$ empty.
3. The rule ${\to}$L, with premises $q \Rightarrow q$ and $r \Rightarrow r$, gives $q \to r, q \Rightarrow r$.
4. One exchange on the left gives $q, q \to r \Rightarrow r$, so that $q$ stands at the front of the antecedent.
5. The sequent of step 2 has the form $\Gamma \Rightarrow \Delta, A$ with $\Gamma = p \to q, p$, $\Delta$ empty and $A = q$.
6. The sequent of step 4 has the form $A, \Pi \Rightarrow \Lambda$ with $\Pi = q \to r$ and $\Lambda = r$.
7. The [[cut rule|DAMGTSY6VV]] gives $\Gamma, \Pi \Rightarrow \Delta, \Lambda$.

The last step, written out, is the following.
$$\dfrac{p \to q, p \Rightarrow q \qquad q, q \to r \Rightarrow r}{p \to q, p, q \to r \Rightarrow r}\,\mathrm{Cut}$$
Check: the cut formula $q$ is on the right of the left premise and on the left of the right premise, and the conclusion joins the two contexts in order.

## Remarks

The example shows cut as the use of a lemma: step 2 proves $q$ from $p \to q$ and $p$, and step 4 uses $q$ to get $r$.
The cut formula $q$ happens to occur in the conclusion, inside $p \to q$ and $q \to r$, but the cut rule does not need this.

A cut-free derivation of the same sequent exists, as the [[cut-elimination theorem|AYRZ98Y0NW]] promises.
Take $q \to r, q \Rightarrow r$ from step 3 and exchange it to $q, q \to r \Rightarrow r$.
Then apply ${\to}$L with left premise $p \Rightarrow p$ and right premise $q, q \to r \Rightarrow r$.
The result is $p \to q, p, q \to r \Rightarrow r$ with no cut.
Here the cut-free derivation is no longer than the one with the cut.

Longer chains work the same way.
For $p_1 \to p_2, \dots, p_{n-1} \to p_n, p_1 \Rightarrow p_n$, a derivation in this style uses one cut for each of the $n - 2$ middle variables $p_2, \dots, p_{n-1}$.

## Explanations

### L1 human

If $p$ gives $q$, and $q$ gives $r$, then $p$ gives $r$.
The derivation first proves the middle claim $q$ and then uses it.
The cut rule is exactly this "prove the middle, then use it" step.

### L2 human

The left premise has the cut formula $q$ on the right, and the right premise has it on the left.
So the conclusion collects the antecedents $p \to q, p$ and $q \to r$, and keeps the succedent $r$.
Watch out for step 4: LK works with lists, and the rule expects the cut formula at the front of the right antecedent.
Without the exchange the right premise is $q \to r, q \Rightarrow r$, which does not match the pattern $A, \Pi \Rightarrow \Lambda$.
