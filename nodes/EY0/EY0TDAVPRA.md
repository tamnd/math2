---
tag: EY0TDAVPRA
kind: example
name: Classical first-order logic proves that every term denotes
msc: ["03B60", "03B10"]
topics: [NJB94B39QK]
audience: ug2
not_instance_of:
  - target: Y0CNMRXHVJ
    note: classical first-order logic proves the existence of the denotation of every term
uses: [Y0CNMRXHVJ, 086QKPF0A6, 33ZNXRFVJJ]
sources:
  - url: https://plato.stanford.edu/entries/logic-free/
    locator: Free Logic (SEP entry), section 1
  - url: https://en.wikipedia.org/wiki/Free_logic
    locator: lead section
---

## Example

In classical [[first-order logic|086QKPF0A6]] with equality, let $t$ be any closed term.

1. $t = t$ is an axiom of equality.
2. By [[existential generalization|33ZNXRFVJJ]], from $A[t/x]$ infer $\exists x\, A$. With $A$ the formula $x = t$, line 1 gives $\exists x\,(x = t)$.
3. So $\vdash \exists x\,(x = t)$ for every closed term $t$.

Read $t$ as "Pegasus": classical logic proves "something is identical with Pegasus", that is, Pegasus exists.
So classical first-order logic is not a [[free logic|Y0CNMRXHVJ]].

## Remarks

In positive free logic, line 1 still holds, but line 2 needs the premise $E!t$; so only $E!t \to \exists x\,(x = t)$ follows.
The step in line 2 is exactly the one that free logics restrict.
The semantic reason is that a classical interpretation must assign each constant an element of the domain.

## Explanations

### L1 human

In classical logic, every name must refer to something real.
So the logic proves "Pegasus exists" from the law "Pegasus is Pegasus".
Free logic exists to block this step.

### L2 human

The proof has two lines: the identity axiom and existential generalization.
In free logic, the second line requires $E!t$.
A trap is to think that the problem is the identity axiom; positive free logic keeps $t = t$ and still blocks the conclusion.
