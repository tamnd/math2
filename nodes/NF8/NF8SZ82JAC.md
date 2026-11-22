---
tag: NF8SZ82JAC
kind: example
name: Induction along the diagonal is not double induction
msc: ["00A35"]
topics: [EEH2F76CYQ]
audience: ug1
not_instance_of:
  - target: AABX4YPKRR
    note: the steps go from (n, n) to (n + 1, n + 1), so they reach only the pairs on the diagonal and not every pair (m, n)
uses: [AABX4YPKRR, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Induction on more than one counter
---

## Example

Let $P(m, n)$ be the statement $m^2 + n^2 = 2mn$ about natural numbers $m$ and $n$.
Here is an argument for the false claim that $P(m, n)$ holds for all pairs.
Base case: $P(0, 0)$ says $0 = 0$.
Step: if $P(n, n)$ holds, then $P(n + 1, n + 1)$ holds, because both sides equal $2(n + 1)^2$.
"Conclusion": $P(m, n)$ holds for every pair.
We show that this argument is not a [[double induction|AABX4YPKRR]].

1. Let $D(n)$ be the statement $P(n, n)$.
   The base case is $D(0)$, and the step is $D(n) \Rightarrow D(n + 1)$.
2. So the argument is an ordinary [[induction|0ASJVEFA9J]] on $n$ for the statement $D(n)$.
   It proves $P(n, n)$ for every $n$, and nothing else.
3. The pairs that the argument reaches from $(0, 0)$ are $(0, 0), (1, 1), (2, 2), \ldots$, which is the diagonal.
4. A double induction must reach every pair.
   The pair $(1, 0)$ is not on the diagonal, so no step of the argument reaches it.
5. The claim is false at that pair, since $P(1, 0)$ says $1 + 0 = 0$.
6. In fact the difference of the two sides is a square:
   $$m^2 + n^2 - 2mn = (m - n)^2.$$
   So $P(m, n)$ holds exactly when $m = n$, and the argument proved exactly the true part of the claim.

## Remarks

The error is in the conclusion, not in the base case or the step, which are both correct.
A double induction for a claim $P(m, n)$ needs steps that together reach every pair, for example the two steps $(m, n) \to (m + 1, n)$ and $(m, n) \to (m, n + 1)$ from the base $(0, 0)$.
Here no correct step leads from $(0, 0)$ to $(1, 0)$, because $P(0, 0)$ holds and $P(1, 0)$ fails, so no correct double induction can prove this claim.

The same error hides more easily inside true claims.
A proof of $\binom{2n}{n} \le 4^n$ by a step from $n$ to $n + 1$ proves only this diagonal case.
It does not prove the bound $\binom{m + n}{m} \le 2^{m + n}$ for all pairs, even though that bound is also true.

## Explanations

### L1 human

Imagine a staircase on a grid that goes one square right and one square up at each step.
Climbing it, we visit the squares $(0, 0)$, $(1, 1)$, $(2, 2)$ and so on, and no others.
A proof that climbs this staircase proves the claims on those squares only.
The square just right of the start, $(1, 0)$, is never visited.
There the claim "$m$ times $m$ plus $n$ times $n$ equals $2$ times $m$ times $n$" is false, because $1$ is not $0$.

### L2 human

Test the claim on a few pairs to see where the argument fails.
At $(2, 2)$ we get $4 + 4 = 8 = 2 \cdot 2 \cdot 2$, which is true.
At $(2, 1)$ we get $4 + 1 = 5$ on the left and $2 \cdot 2 \cdot 1 = 4$ on the right, which is false.
At $(3, 0)$ we get $9$ on the left and $0$ on the right, which is false.
The difference of the two sides is $(m - n)^2$, and it is $0$ only on the diagonal.
The usual source of this error is a step that changes both variables in the same way.
A good check is to pick one pair off the diagonal and ask which chain of steps of the proof reaches it.
