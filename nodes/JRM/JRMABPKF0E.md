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

1. $p \Rightarrow p$ and $q \Rightarrow q$ are axioms.
2. ${\to}$L, with $\Gamma = p$, $\Pi$ and $\Delta$ empty and $\Lambda = q$, gives $p \to q, p \Rightarrow q$.
3. $q \Rightarrow q$ and $r \Rightarrow r$ are axioms, and ${\to}$L gives $q \to r, q \Rightarrow r$.
4. An exchange on the left gives $q, q \to r \Rightarrow r$.
5. The sequent of step 2 has the form $\Gamma \Rightarrow \Delta, A$ with $\Gamma = p \to q, p$, $\Delta$ empty and $A = q$.
6. The sequent of step 4 has the form $A, \Pi \Rightarrow \Lambda$ with $\Pi = q \to r$ and $\Lambda = r$.
7. The [[cut rule|DAMGTSY6VV]] gives $\Gamma, \Pi \Rightarrow \Delta, \Lambda$, which is $p \to q, p, q \to r \Rightarrow r$.

We check that this step is an instance of cut: the cut formula $q$ is on the right of the first premise and on the left of the second premise, and the conclusion joins the two contexts.

## Remarks

The example shows cut as the use of a lemma: step 2 proves $q$, and step 4 uses $q$.
The cut formula $q$ does occur in the conclusion, inside $p \to q$ and $q \to r$, but the cut does not need this.
A cut-free derivation of the same sequent also exists.
Apply ${\to}$L to $q \Rightarrow q$ and $r \Rightarrow r$ to get $q \to r, q \Rightarrow r$, then apply ${\to}$L with $p \Rightarrow p$ to get $p \to q, p, q \to r \Rightarrow r$ after exchanges.
With a longer chain $p_1 \to p_2, \dots, p_{n-1} \to p_n$, the derivation uses $n - 2$ cuts, one for each intermediate variable.

## Explanations

### L1 human

If $p$ gives $q$, and $q$ gives $r$, then $p$ gives $r$.
The derivation proves the middle step $q$ first and then uses it.
The cut rule is exactly this "prove the middle, then use it" step.

### L2 human

The left premise has the cut formula $q$ on the right, and the right premise has it on the left.
So the conclusion takes the antecedents $p \to q, p$ and $q \to r$, and the succedent $r$.
A trap is to forget the exchange in step 4: LK takes the cut formula at the front of the antecedent of the right premise.
