---
tag: 1RVF7DWG8C
kind: problem
name: Post's problem
msc: [03D25, 03D28]
uses: [TN9G24VABN, PA4PYQ1PZ0, P5N2ND3VCG]
about: [P5N2ND3VCG, TN9G24VABN]
sources:
  - url: https://en.wikipedia.org/wiki/Turing_degree
history:
  posed_by: "Emil Post"
  first_stated: "1944"
---

## Problem

Is there a [[computably enumerable set|TN9G24VABN]] $A \subseteq \N$ that is not computable and is not [[Turing equivalent|PA4PYQ1PZ0]] to the [[halting problem|Z7TN2B35B0]]?
In terms of [[Turing degrees|P5N2ND3VCG]]: is there a computably enumerable degree $\mathbf{a}$ with $\mathbf{0} < \mathbf{a} < \mathbf{0}'$?

## Remarks

Every computably enumerable set $A$ satisfies $A \le_T \emptyset'$, so the question asks whether the c.e. degrees contain anything besides $\mathbf{0}$ and $\mathbf{0}'$.
Emil Post posed the question in 1944.
The answer is yes.
Friedberg and Muchnik answered it independently, in 1957 and 1956, by constructing two c.e. sets that are not Turing reducible to each other; see the [[Friedberg–Muchnik theorem|RA358M9QCN]].
Their method of construction is the [[priority method|3BZFSC5QZ2]].
Post's own attempt was to find a structural property of c.e. sets, such as being simple, that forces the degree to lie strictly between $\mathbf{0}$ and $\mathbf{0}'$.

## Explanations

### L1 human

Among the sets that a computer can list, the easiest are the ones it can also decide, and the hardest is the set of halting programs.
Post asked whether anything lies in between.
It took more than ten years and a new technique to show that the answer is yes.
