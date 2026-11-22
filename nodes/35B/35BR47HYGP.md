---
tag: 35BR47HYGP
kind: example
name: There is no smallest positive rational number
msc: ["00A35", "11A99"]
topics: [958EF46EYJ]
audience: school
instance_of: [0J0XBKG64S]
uses: [0J0XBKG64S, 0NCJ5WXN6Z]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_by_contradiction
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Rational_number
    locator: lead section
---

## Example

Statement: there is no smallest positive [[rational number|0NCJ5WXN6Z]].
We give a [[proof by contradiction|0J0XBKG64S]].

1. Suppose, for a contradiction, that there is a smallest positive rational number, and call it $r$.
2. Since $r$ is rational, $r = a / b$ with integers $a$ and $b \ne 0$.
3. Put $s = r / 2 = a / (2b)$.
   Then $s$ is rational, because $a$ and $2b$ are integers and $2b \ne 0$.
4. Since $r > 0$, also $s = r / 2 > 0$, so $s$ is a positive rational number.
5. Since $r > 0$, we have $r - s = r / 2 > 0$, so $s < r$.
6. Steps 4 and 5 give a positive rational number smaller than $r$, which contradicts the choice of $r$ as the smallest.
7. So the assumption in step 1 is false, and there is no smallest positive rational number.

Check with a number: if someone proposes $r = \frac{1}{1000}$, the proof answers with $s = \frac{1}{2000}$.

## Remarks

The statement is a negation, "it is not the case that a smallest positive rational exists".
So the proof assumes the positive statement and refutes it, which is the form of proof by contradiction that needs no law of excluded middle.

The proof gives more than it claims.
For each positive rational $r$ it names the smaller one, $r / 2$.
So the universal statement "for every positive rational $r$ there is a positive rational $s < r$" has a [[direct proof|0NTF6DMVAP]] with no contradiction at all, and that direct proof implies the original statement.
Many short proofs by contradiction hide a direct proof of this kind.

A change of the set changes the answer.
The positive integers have a smallest element, $1$, by the [[well-ordering principle|01BX15HSRR]], and the step fails there because $\frac{1}{2}$ is not an integer.
The positive real numbers have no smallest element, by the same proof.
The rationals $r \ge 0$ have the smallest element $0$, and the proof fails because step 5 needs $r > 0$.

## Explanations

### L1 human

Think of the smallest piece of cake that is still more than nothing.
Whatever piece is proposed, cut it in half.
The half is still more than nothing, and it is smaller.
So no piece can be the smallest.
The same holds for fractions: half of a positive fraction is a smaller positive fraction, so $\frac{1}{2000}$ beats $\frac{1}{1000}$.

### L2 human

The same idea shows that the set $S$ of rational numbers $q$ with $0 < q < 1$ has no smallest element.
Suppose $S$ had a smallest element $m$.
Then $m / 2$ is rational, and
$$0 < \frac{m}{2} < m < 1,$$
so $m / 2$ lies in $S$ and is smaller than $m$, which contradicts the choice of $m$.
The typical use is the one shown: a set with no least element needs an infimum in place of a minimum, here $0$, which is not in $S$.
Watch out: the proof must check that $m / 2$ belongs to the set.
For the set of rationals $q$ with $\frac{1}{2} \le q < 1$, the number $\frac{1}{2}$ is the minimum, and halving it leaves the set.
