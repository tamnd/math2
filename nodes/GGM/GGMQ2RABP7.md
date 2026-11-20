---
tag: GGMQ2RABP7
kind: example
name: The logic of paradox has gluts but no gaps
msc: ["03B50", "03B53"]
topics: [NJB94B39QK]
audience: ug2
not_instance_of:
  - target: F5SP7HQFFS
    note: in LP every atom is true or false, and the middle value means both, not neither
uses: [F5SP7HQFFS, W28EY7C3FA, 1GFPEGQ697, WH94DG6D3Q]
sources:
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: Many-Valued Logic (SEP entry), section 2
  - url: https://en.wikipedia.org/wiki/Three-valued_logic
    locator: Kleene and Priest logics
---

## Example

The [[logic of paradox|W28EY7C3FA]] uses the same three tables as strong Kleene logic, with the middle value read as "both true and false".
In the relational reading, a valuation relates each atom to $1$, to $0$, or to both, and never to neither.

1. So every atom is at least true or at least false: there are no gaps.
2. Excluded middle $p \lor \neg p$ is designated in LP under every valuation, as computed in [[the excluded middle example|1GFPEGQ697]].
3. An atom related to both values is a [[truth-value glut|WH94DG6D3Q]].

So LP is a logic of gluts, not of gaps.
It is not a [[partial logic|F5SP7HQFFS]], where atoms may lack a value and excluded middle fails.

## Remarks

The two logics differ only in the designated set and in the reading of the middle value.
So the same valuation $v(p) = \tfrac12$ is a gap in K3 and a glut in LP.
A logic with both gaps and gluts needs four values; first-degree entailment is the standard example.

## Explanations

### L1 human

Partial logic allows "no value"; LP allows "both values".
They use the same tables, but the readings are opposite.
So LP is not partial logic.

### L2 human

Test a logic for gaps by excluded middle.
In LP it always holds, so there are no gaps; in partial logic it can fail.
A trap is to call every three-valued logic "partial"; what matters is whether the third value means "neither".
