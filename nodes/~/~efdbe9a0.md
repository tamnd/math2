---
tag: ~efdbe9a0
kind: example
name: The minimum rule for graded modus ponens is unsound in Łukasiewicz logic
msc: ["03B52"]
topics: [WZP584JQ06]
audience: research
not_instance_of:
  - target: ~4b515603
    note: the rule with the bound min(r, s) is not a sound graded rule over Łukasiewicz semantics
uses: [~3e406741, ~a4e21349]
sources:
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: 1. Fuzzy connectives based on t-norms; 4. Gödel-Dummett logic
  - book: isbn:9780792352389
---

## Example

Consider the rule: from "$\varphi$ to degree $r$" and "$\varphi \to \psi$ to degree $s$", infer "$\psi$ to degree $\min(r, s)$".
We show that it is unsound in [[Łukasiewicz semantics|~3e406741]], so it is not a rule of [[Pavelka logic|~4b515603]].

1. Take $r = 0.7$ and $s = 0.8$, so the rule claims the degree $\min(0.7, 0.8) = 0.7$ for $\psi$.
2. Put $e(\varphi) = 0.7$ and $e(\psi) = 0.5$.
3. Then $e(\varphi \to \psi) = \min(1, 1 - 0.7 + 0.5) = 0.8$, so both premises hold to their degrees.
4. But $e(\psi) = 0.5 < 0.7$, so the conclusion fails.
5. The sound bound is $0.7 \odot 0.8 = 0.5$; see [[graded modus ponens|~a20c89aa]].

The same rule is sound in Gödel semantics:

6. Let $x = e(\varphi) \ge r$ and $x \Rightarrow_G y \ge s$, with $y = e(\psi)$.
7. If $x \le y$, then $y \ge x \ge r \ge \min(r, s)$.
8. If $x > y$, then $x \Rightarrow_G y = y$, so $y \ge s \ge \min(r, s)$.

## Remarks

1. For every left-continuous [[t-norm|~a4e21349]] $*$ with residuum $\Rightarrow$, the bound $r * s$ is sound.
   Monotonicity and residuation give $y \ge x * (x \Rightarrow y) \ge r * s$.
2. For the minimum, $r * s = \min(r, s)$, so steps 6 to 8 are the case $* = \min$ of remark 1.
3. For the Łukasiewicz t-norm, steps 2 and 3 show that the bound $r \odot s$ is attained, so no larger bound is sound.

## Explanations

### L1 human

With Łukasiewicz logic, doubts add up.
A premise that is $0.3$ short of true and a rule that is $0.2$ short give a conclusion that can be $0.5$ short.
Taking the smaller doubt, $0.3$, is too optimistic.

### L2 human

1. To refute a graded rule, choose $e(\varphi) = r$.
2. Choose $e(\psi)$ as small as the premise $\varphi \to \psi$ permits.

A trap: the minimum rule is sound for Gödel logic, so its failure depends on the t-norm.
