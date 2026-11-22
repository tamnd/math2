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

A short argument in lecture shorthand uses three [[mathematical abbreviations|4ZNYMYRRY3]].
It has four sentences:

- "Let $x, y \in \mathbb{R}$ `s.t.` $x + y = 2$."
- "`WLOG` $x \leq y$."
- "Then $x \leq 1 \leq y$."
- "Also $x = y$ `iff` $x = 1$."

We expand each abbreviation and check each sentence.

1. `s.t.` means "such that".
   The first sentence fixes two [[real numbers|08J2M1JYAG]] $x$ and $y$ whose sum is $2$.
2. `WLOG` means "without loss of generality", and it claims that the case $y \leq x$ follows from the case $x \leq y$.
   Swapping $x$ and $y$ leaves the hypothesis $x + y = 2$ unchanged.
   It also leaves the claims unchanged once they are written as "$\min(x, y) \leq 1 \leq \max(x, y)$" and "$x = y$ exactly when both equal $1$".
   So the swap turns the case $y \leq x$ into the case $x \leq y$, and the assumption loses no case.
3. From $x \leq y$, add $x$ to both sides:
   $$2x \leq x + y = 2, \qquad \text{so } x \leq 1.$$
4. From $x \leq y$, add $y$ to both sides:
   $$2 = x + y \leq 2y, \qquad \text{so } 1 \leq y.$$
   Steps 3 and 4 prove the third sentence.
5. `iff` means "if and only if", so the fourth sentence is a [[biconditional|0S6GMNJ62Y]], and we prove both directions.
6. If $x = y$, then $2x = x + y = 2$, so $x = 1$.
7. If $x = 1$, then $y = 2 - x = 1$, so $x = y$.

Each sentence is true once the abbreviations are expanded.
Check: $x = 0.5$ and $y = 1.5$ give $0.5 \leq 1 \leq 1.5$, and $x \neq y$ with $x \neq 1$.

## Remarks

Each of the three short forms carries logic.
`s.t.` introduces a condition, `WLOG` claims a symmetry, and `iff` claims two implications.
The step that needs the most care is the `WLOG`, because it is the only one that hides an argument.

Change the hypothesis to $x + 2y = 2$, and the swap no longer preserves it.
Then `WLOG` $x \leq y$ is not justified.
For example, $x = 4$ and $y = -1$ satisfy $x + 2y = 4 - 2 = 2$ with $y < x$, and here $x > 1$, so the case that `WLOG` threw away really behaves differently.

## Explanations

### L1 human

Short forms such as `s.t.` and `iff` save space, but each one stands for a full phrase.
Here two numbers add up to $2$, for example $0.5$ and $1.5$.
The smaller one is at most $1$ and the larger one is at least $1$: $0.5 \leq 1 \leq 1.5$.
The two numbers are equal only when both are $1$.

### L2 human

To test a `WLOG`, write the hypothesis and the claim as statements about the pair $(x, y)$.
Apply the swap $(x, y) \mapsto (y, x)$ to both.
If both stay the same, one order of the two variables is enough, and the `WLOG` is justified.
For $x + y = 2$ the swap gives $y + x = 2$, the same equation, so the test passes.
Watch out: the claim must be symmetric as well as the hypothesis.
The claim "$x \leq 1$" on its own is not symmetric, and it fails for $x = 1.5$, $y = 0.5$, which satisfy the hypothesis.
So the claim has to be stated as "$\min(x, y) \leq 1$" before the `WLOG` can be used.
