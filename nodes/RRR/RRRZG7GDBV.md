---
tag: RRRZG7GDBV
kind: example
name: The supremum of 1 - 1/n is 1
msc: ["00A35", "26A03"]
topics: [MEKKHHQTKB]
audience: ug1
instance_of: [S3QADD13E9]
uses: [S3QADD13E9, 0R3H5PANRQ, 0S60DVMVPN, 0A74SX55QP]
sources:
  - url: https://en.wikipedia.org/wiki/Infimum_and_supremum
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Archimedean_property
    locator: lead section
---

## Example

Let $A = \{ 1 - \tfrac{1}{n} : n \ge 1 \text{ an integer} \} = \{ 0, \tfrac12, \tfrac23, \tfrac34, \dots \}$.
The set is non-empty and bounded above by $1$, so it has a [[supremum|0R3H5PANRQ]] $s = \sup A$, its least [[upper bound|0S60DVMVPN]].
We prove $s = 1$ by [[equality by two inequalities|S3QADD13E9]].

1. ($s \le 1$) For each $n \ge 1$, $\tfrac1n > 0$, so $1 - \tfrac1n < 1$, and $1$ is an upper bound of $A$.
2. The supremum is at most every upper bound, so $s \le 1$.
3. ($s \ge 1$) We show that no $c < 1$ is an upper bound.
   Let $c < 1$ and put $\varepsilon = 1 - c > 0$.
4. The [[Archimedean property|0A74SX55QP]] gives an integer $n \ge 1$ with $n > \tfrac1\varepsilon$, so $\tfrac1n < \varepsilon$.
5. Then the element $1 - \tfrac1n$ of $A$ is larger than $c$:
   $$1 - \frac1n > 1 - \varepsilon = c.$$
6. So $c$ is not an upper bound.
   Since $s$ is an upper bound, $s$ is not less than $1$, and $s \ge 1$.
7. Steps 2 and 6 give $s = 1$.

Check: for $c = 0.99$, $\varepsilon = 0.01$, and $n = 101 > 100$ gives the element $1 - \tfrac{1}{101} \approx 0.9901 > 0.99$.

## Remarks

The two halves have different characters.
The half $s \le 1$ is one inequality that holds for every element.
The half $s \ge 1$ needs, for each $c < 1$, a witness in $A$ above $c$, and the witness depends on $c$.

The supremum $1$ is not an element of $A$, since $1 - \tfrac1n = 1$ has no solution, so $A$ has no maximum and you cannot just find the largest element.
Add the point $1$ to the set, and the supremum is still $1$, but now it is a maximum and the half $s \ge 1$ shrinks to the remark that $1$ lies in the set.
The infimum of $A$ is $0$, and here it is attained at $n = 1$, so it is the minimum.

## Explanations

### L1 human

The numbers $0$, $\tfrac12$, $\tfrac23$, $\tfrac34$ and so on climb toward $1$ but never reach it.
No number in the list is $1$ or more, so $1$ is a ceiling for the list.
Any lower ceiling, such as $0.99$, fails, because the list passes it: $1 - \tfrac{1}{101}$ is already above $0.99$.
So $1$ is the lowest ceiling, and that is what "the supremum is $1$" means.

### L2 human

We show $\sup C = 1$ for $C = \{ \tfrac{n}{n + 1} : n \ge 1 \}$.

1. ($\le$) Since $n < n + 1$, each $\tfrac{n}{n + 1} < 1$, so $\sup C \le 1$.
2. ($\ge$) Let $c < 1$.
   We need $n$ with $\tfrac{n}{n + 1} = 1 - \tfrac{1}{n + 1} > c$.
3. That holds when $\tfrac{1}{n + 1} < 1 - c$, that is, when $n + 1 > \tfrac{1}{1 - c}$, and the Archimedean property gives such an $n$.
4. So no $c < 1$ is an upper bound, $\sup C \ge 1$, and $\sup C = 1$.

This is the routine for a supremum of a set given by a formula.
Watch out: proving only that $1$ is an upper bound is not enough, since $2$ and $5$ are upper bounds too, and the half $\ge$ is what singles out $1$.
