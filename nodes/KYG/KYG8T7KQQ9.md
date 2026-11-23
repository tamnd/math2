---
tag: KYG8T7KQQ9
kind: example
name: The minimum rule for graded modus ponens is unsound in Łukasiewicz logic
msc: ["03B52"]
topics: [WZP584JQ06]
audience: research
not_instance_of:
  - target: YG62F8YC0P
    note: the rule with the bound min(r, s) is not a sound graded rule over Łukasiewicz semantics
uses: [JQ713VVD0G, BHGCVPAJW0]
sources:
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: 1. Fuzzy connectives based on t-norms; 4. Gödel-Dummett logic
  - book: isbn:9780792352389
---

## Example

Consider the rule: from "$\varphi$ to degree $r$" and "$\varphi \to \psi$ to degree $s$", infer "$\psi$ to degree $\min(r, s)$".
It looks safe, since a chain of reasoning seems as strong as its weakest link.
We show that it is unsound in [[Łukasiewicz semantics|JQ713VVD0G]], so it is not a rule of [[Pavelka logic|YG62F8YC0P]].

1. Take $r = 0.7$ and $s = 0.8$, so the rule claims the degree $\min(0.7, 0.8) = 0.7$ for $\psi$.
2. Put $e(\varphi) = 0.7$ and $e(\psi) = 0.5$.
3. Then $e(\varphi \to \psi) = \min(1, 1 - 0.7 + 0.5) = 0.8$, so both premises hold to their degrees.
4. But $e(\psi) = 0.5 < 0.7$, so the conclusion fails.
5. The sound bound is $0.7 \odot 0.8 = 0.5$, as in [[graded modus ponens|820H41656Q]].

The same rule is sound in Gödel semantics, where $x \Rightarrow_G y$ is $1$ for $x \le y$ and $y$ for $x > y$.
Let $x = e(\varphi) \ge r$ and $x \Rightarrow_G y \ge s$, with $y = e(\psi)$.
If $x \le y$, then $y \ge x \ge r \ge \min(r, s)$.
If $x > y$, then $x \Rightarrow_G y = y$, so $y \ge s \ge \min(r, s)$.

## Remarks

For every left-continuous [[t-norm|BHGCVPAJW0]] $*$ with residuum $\Rightarrow$, the bound $r * s$ is sound.
Monotonicity and residuation give $y \ge x * (x \Rightarrow y) \ge r * s$.
For the Gödel t-norm $r * s = \min(r, s)$, so the Gödel argument above is a special case.

So the right bound depends on the t-norm, and the minimum is the largest of them, since $r * s \le \min(r, s)$ for every t-norm.
For the Łukasiewicz t-norm, steps 2 and 3 show that the bound $r \odot s$ is attained, so no larger bound is sound.
For the product t-norm the bound is $0.7 \cdot 0.8 = 0.56$.
Check that it is attained: with $e(\varphi) = 0.7$ and $e(\psi) = 0.56$, the product implication gives $0.56 / 0.7 = 0.8$.

## Explanations

### L1 human

In Łukasiewicz logic, doubts add up.
A premise that is $0.3$ short of true and a rule that is $0.2$ short give a conclusion that can be $0.5$ short.
Taking only the larger doubt, $0.3$, is too optimistic.

### L2 human

To refute a graded rule, choose $e(\varphi) = r$.
Then choose $e(\psi)$ as small as the premise $\varphi \to \psi$ allows, here $r + s - 1$.
If that value is below the claimed degree, the rule is unsound.
Watch out: the minimum rule is sound in Gödel logic, so its failure depends on the t-norm.
