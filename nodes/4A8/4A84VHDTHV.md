---
tag: 4A84VHDTHV
kind: concept
name: Soundness
msc: [03B05, 03B10, 03F03]
sources:
  - url: https://en.wikipedia.org/wiki/Soundness
same_as:
  wikidata: Q693083
  wikipedia: Soundness
---

## Summary

A proof system is sound when everything it proves is true.
More precisely, whenever $\Gamma \vdash \varphi$ in the system, also $\Gamma \models \varphi$ as a [[logical consequence|1HK0VYWTV7]].
Soundness is the converse of completeness, and the standard proof systems for propositional and first-order logic have both.
A sound system can never prove a false statement from true premises.

## Explanations

### L1 human

A proof system is sound if its rules never lead from true premises to a false conclusion.
For example, modus ponens is a safe rule: if $p$ and "if $p$ then $q$" are true, then $q$ is true.
A rule such as "from $q$ and if $p$ then $q$, infer $p$" is unsafe, because $q$ may be true while $p$ is false.
In philosophy, an argument is also called sound when it is valid and all its premises are true.
