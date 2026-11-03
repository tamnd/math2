---
tag: RMJ56ZPA63
kind: concept
name: Linear temporal logic
msc: [03B44, 68Q60, 03B70]
specializes: [C3RZY20ETK]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_temporal_logic
same_as:
  wikidata: Q1536492
  wikipedia: Linear temporal logic
---

## Summary

Linear temporal logic (LTL) is a [[modal logic|C3RZY20ETK]] whose formulas speak about a single infinite sequence of time steps.
Besides the Boolean connectives it has the operators "next" ($X$) and "until" ($U$), and from them "eventually" ($F$) and "always" ($G$).
It is a standard language for properties of reactive systems, such as "every request is eventually granted".
It is a main input language of [[model checking|VNY0VXVZ53]].

## Explanations

### L1 human

Picture time as a line of moments $0, 1, 2, \dots$, and at each moment some basic facts are true.
An LTL formula is a statement about the whole line, read from moment $0$.
"$G\,\mathit{safe}$" says the system is safe at every moment.
"$G(\mathit{req} \to F\,\mathit{grant})$" says that whenever a request happens, a grant happens then or later.
A system satisfies a formula when every possible run of it does.
