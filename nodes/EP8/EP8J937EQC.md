---
tag: EP8J937EQC
kind: example
name: The sorites paradox in Łukasiewicz logic
msc: ["03B52", "03A05"]
topics: [WZP584JQ06]
audience: grad
instance_of: [8DH4QM6AX8]
uses: [JQ713VVD0G, PDFBXAN9CC]
sources:
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: 10. Fuzzy logic and vagueness
---

## Example

SEP states the paradox as follows.
(1) $10^{100}$ is huge.
(2) If $n$ is huge, then $n - 1$ is huge.
(3) Hence, by $10^{100}$ steps of [[a sorites series|PDFBXAN9CC]], $0$ is huge.

We give "huge" degrees of truth and use [[Łukasiewicz logic|JQ713VVD0G]].
Fix $N = 1000$ and put $h(n) = \min(1, n / N)$ for $n \ge 0$.
Let $H(n)$ be the statement "$n$ is huge", with value $h(n)$.

1. $h(10^{100}) = 1$, so premise (1) is totally true.
2. The instance of (2) for $n$ has value $\min(1, 1 - h(n) + h(n - 1))$.
3. $h(n) - h(n - 1) \le 1 / N$, so each instance has value at least $1 - 1/N = 0.999$.
4. A modus ponens step is sound in SEP's sense if $v(B) \ge v(A) \odot v(A \to B)$.
5. This holds in Łukasiewicz logic: $v(A) \odot v(A \to B) = \max(0, v(A) + \min(1, 1 - v(A) + v(B)) - 1) \le v(B)$.
6. So every step of the chain is sound, but each step may lose up to $1/N$ of truth.
7. $h(0) = 0$, so the conclusion (3) is totally false.
8. The strong conjunction of $N$ instances with value $1 - 1/N$ is $\max(0, 1 - N \cdot \tfrac1N) = 0$.

So the paradox does not show a fault in modus ponens.
The premise (2) is almost true, but not totally true, and the small losses add up.

## Remarks

1. The analysis needs a conjunction that loses truth when repeated, as SEP points out.
   With $\min$ in step 4, soundness of each step would force $h(n) \ge 0.999$ for all $n$.
2. The choice $N = 1000$ is arbitrary; any $N \ge 1$ gives the same picture.
3. SEP mentions a different fuzzy treatment by Hájek and Novák (2003), with a connective for "it is almost true that".

## Explanations

### L1 human

Take away one grain from a heap, and you still have a heap.
Do it many times, and you have no grains, but the argument says you still have a heap.
Fuzzy logic says "one grain less is still a heap" is almost true, but not fully true.
Each step loses a tiny bit of truth, and after many steps the truth is gone.

### L2 human

1. Give the vague predicate a degree that changes slowly.
2. Compute the degree of the conditional premise; it is near $1$.
3. Use the rule that the conclusion has at least the strong conjunction of the premises.

A trap: the conclusion of one step can be true to degree $1$, and still the chain ends at degree $0$.
In the example, $h(n) = 1$ for all $n \ge N$, so the first $10^{100} - N$ steps lose nothing.
