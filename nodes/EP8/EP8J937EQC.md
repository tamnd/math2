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

The paradox runs as follows.
The number $10^{100}$ is huge.
If $n$ is huge, then $n - 1$ is huge.
So, by $10^{100}$ steps of modus ponens along [[a sorites series|PDFBXAN9CC]], $0$ is huge.
We give "huge" degrees of truth in [[Łukasiewicz logic|JQ713VVD0G]] and follow the truth along the chain.

Fix $N = 1000$, and let $H(n)$ be the statement "$n$ is huge", with value $h(n) = \min(1, n / N)$ for $n \ge 0$.
Recall that $x \to y = \min(1, 1 - x + y)$ and $x \odot y = \max(0, x + y - 1)$.

1. The first premise is totally true, since $h(10^{100}) = 1$.
2. The instance of the second premise for $n$ has the value below.
   $$v(H(n) \to H(n - 1)) = \min(1, 1 - h(n) + h(n - 1)).$$
3. The function $h$ grows by at most $1/N$ per step, so $h(n) - h(n - 1) \le 1/N$.
   Hence each instance has value at least $1 - 1/N = 0.999$, and the second premise is almost true.
4. Modus ponens is sound in the graded sense: the conclusion is at least as true as the strong conjunction of the premises.
   We compute that conjunction for premises $A$ and $A \to B$ with values $a$ and $b$.
   $$a \odot \min(1, 1 - a + b) = \max(0, \min(a + 1, 1 + b) - 1) = \min(a, b) \le b.$$
5. So no single step of the chain creates falsehood.
6. The conclusion is totally false, since $h(0) = 0$.
7. The truth is lost in small amounts.
   The instances for $n = 1, \dots, N$ each have value exactly $1 - 1/N$, and their strong conjunction is computed below.
   $$\max\left(0, N\left(1 - \tfrac1N\right) - (N - 1)\right) = \max(0, 0) = 0.$$

So the paradox does not show a fault in modus ponens.
The second premise is almost true but not totally true, and the small losses add up to the whole of the truth.

## Remarks

The analysis needs a conjunction that loses truth when it is repeated.
Suppose we used $\min$ in step 4 and asked that $h(n - 1) \ge \min(h(n), 0.999)$ for every $n$.
Starting from $h(10^{100}) = 1$, this gives $h(n) \ge 0.999$ for every $n$, so it would force $0$ to be huge to degree $0.999$.
The Łukasiewicz conjunction avoids this, because $N$ copies of $0.999$ already conjoin to $0$.

The choice $N = 1000$ changes only the size of each loss.
A larger $N$ makes each instance more nearly true, with value $1 - 1/N$, but needs more steps of loss, and the end value is $0$ in every case.
Note also that the first $10^{100} - N$ steps lose nothing, because $h(n) = 1$ for every $n \ge N$.
Hájek and Novák gave a different fuzzy treatment in 2003, with a connective for "it is almost true that".

## Explanations

### L1 human

Take away one grain from a heap, and you still have a heap.
Do it many times, and you have no grains, but the argument says you still have a heap.
Fuzzy logic says that "one grain less is still a heap" is almost true, but not fully true.
Each step loses a tiny bit of truth, perhaps one thousandth.
After a thousand steps the truth is gone.

### L2 human

The method has three steps.
First, give the vague predicate a degree that changes slowly, here by $0.001$ per step.
Second, compute the degree of the conditional premise, which comes out near $1$.
Third, use the rule that the conclusion of modus ponens is at least the strong conjunction of the premises.
Watch out: the conclusion of one step can be true to degree $1$, and still the chain ends at degree $0$.
The loss appears only in the steps where $h$ actually drops.
