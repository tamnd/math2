---
tag: K35RJ9YHC0
kind: example
name: A sentence with the abbreviations s.t., wlog and iff
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: school
instance_of: [4ZNYMYRRY3]
uses: [4ZNYMYRRY3, 08J2M1JYAG, 0S6GMNJ62Y]
sources:
  - url: https://en.wikipedia.org/wiki/List_of_mathematical_abbreviations
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Without_loss_of_generality
    locator: lead section
---

## Example

We read a short argument that uses three [[mathematical abbreviations|4ZNYMYRRY3]].
The argument has four sentences.

- "Let $x, y \in \mathbb{R}$ `s.t.` $x + y = 2$."
- "`WLOG` $x \leq y$."
- "Then $x \leq 1 \leq y$."
- "Also $x = y$ `iff` $x = 1$."

We expand each abbreviation and check each sentence.

1. `s.t.` means "such that". The first sentence fixes two [[real numbers|08J2M1JYAG]] $x$ and $y$ whose sum is $2$.
2. `WLOG` means "without loss of generality". The hypothesis $x + y = 2$ does not change when we swap $x$ and $y$, and the conclusions "$\min(x, y) \leq 1 \leq \max(x, y)$" and "$x = y$ exactly when both are $1$" do not change either. So the case $y \leq x$ follows from the case $x \leq y$ by swapping the names, and the assumption $x \leq y$ loses no case.
3. From $x \leq y$ we get $2x \leq x + y = 2$, so $x \leq 1$.
4. From $x \leq y$ we get $2 = x + y \leq 2y$, so $1 \leq y$. Steps 3 and 4 prove the third sentence.
5. `iff` means "if and only if", so the fourth sentence is a [[biconditional|0S6GMNJ62Y]]. We prove both directions.
6. If $x = y$, then $2x = x + y = 2$, so $x = 1$.
7. If $x = 1$, then $y = 2 - x = 1$, so $x = y$.

So each sentence is true after the abbreviations are expanded.

## Remarks

The example shows that each abbreviation carries logic.
The word `s.t.` introduces a condition, `WLOG` claims a symmetry, and `iff` claims two implications.
If we change the hypothesis to $x + 2y = 2$, then the swap of $x$ and $y$ changes the hypothesis, and `WLOG` $x \leq y$ is no longer justified.
For example, $x = 4$ and $y = -1$ satisfy $x + 2y = 2$ with $y < x$, and here $x > 1$.

## Explanations

### L1 human

Short forms such as `s.t.` and `iff` save space, but each one stands for a full phrase.
Here two numbers add up to $2$, for example $0.5$ and $1.5$.
The smaller number is at most $1$ and the larger is at least $1$: here $0.5 \leq 1 \leq 1.5$.
The two numbers are equal only when both are $1$.

### L2 human

The abbreviation `WLOG` is the step that needs the most care.

1. Write the hypothesis and the claim as a statement about the pair $(x, y)$.
2. Apply the swap $(x, y) \mapsto (y, x)$ to the hypothesis and to the claim.
3. If both stay the same, then one order of $x$ and $y$ is enough, and `WLOG` is justified.

The typical use is to order two variables, or to choose the sign of one variable, before a computation.
A trap: the claim must also be symmetric, not only the hypothesis.
The claim "$x \leq 1$" alone is not symmetric, and it is false for $x = 1.5$, $y = 0.5$, although these numbers satisfy the hypothesis.
