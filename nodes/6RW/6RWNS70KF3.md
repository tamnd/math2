---
tag: 6RWNS70KF3
kind: example
name: Implications between unrelated statements
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
instance_of: [0NMG7W7Q11]
uses: [0NMG7W7Q11, 0ZNX6DQ3EJ]
sources:
  - url: https://en.wikipedia.org/wiki/Paradoxes_of_material_implication
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Material_conditional
    locator: lead section
---

## Example

We compute the truth values of four [[material implications|0NMG7W7Q11]] whose antecedent and consequent have no link of meaning.

| implication | antecedent | consequent | value |
|---|---|---|---|
| if $2 + 2 = 4$, then $7$ is prime | T | T | T |
| if $2 + 2 = 4$, then $9$ is prime | T | F | F |
| if $10$ is prime, then $3 < 4$ | F | T | T |
| if $2 + 2 = 5$, then $9$ is prime | F | F | T |

1. The number $7$ is prime, because its only positive divisors are $1$ and $7$.
   So the first line falls in the row TT of the [[truth table|0ZNX6DQ3EJ]], and the value is T.
2. The number $9$ is not prime, because $9 = 3 \cdot 3$.
   So the second line falls in the row TF, and the value is F.
3. The number $10$ is not prime, because $10 = 2 \cdot 5$.
   So the third line falls in the row FT, and the value is T.
4. The fourth line has two false parts, so it falls in the row FF, and the value is T.

Three of the implications are true and one is false.
The subject matter of the parts plays no role: only their truth values count.

## Remarks

### Why they sound strange

The true lines sound strange in English, because no reasoning leads from the antecedent to the consequent.
They are instances of the [[paradoxes of material implication|3T7ZJFC9QF]].
A true consequent makes the implication true, as in the first and third lines.
A false antecedent makes it true, as in the third and fourth lines.
Replace the consequent of the first line by any true statement, and it stays true.
Replace the antecedent of the fourth line by any false statement, and it stays true.

### Implications in theorems

In mathematics such implications rarely appear alone.
A theorem usually has a variable and a hidden "for every", as in "for every integer $n$, if $4$ divides $n$, then $n$ is even".
The link between antecedent and consequent then comes from the quantifier: the implication must hold at every $n$, and that needs a reason.
[[Conditional statements|FA6YZGR2SS]] treats this reading of mathematical English.

## Explanations

### L1 human

In logic, "if $A$, then $B$" is false only when $A$ is true and $B$ is false.
The sentence "if $2 + 2 = 4$, then $7$ is prime" has a true first part and a true second part.
So it is true, although adding $2$ and $2$ says nothing about the number $7$.
Logic checks only whether the promise is broken, not whether the two parts are about the same thing.

### L2 human

Decide the truth value of "if $\sqrt{2}$ is rational, then every triangle has four sides".

1. The antecedent "$\sqrt{2}$ is rational" is false, by the classical proof that $\sqrt{2}$ is irrational.
2. The consequent "every triangle has four sides" is false.
3. The row FF of the truth table gives T, so the implication is true.

Proofs by contradiction use this fact: once a false statement is derived, every implication from it is true, so any conclusion follows.
This is the principle of [[explosion|TTKZGJEEK7]].
Watch out: a true implication with a false antecedent gives no information about the consequent.
From step 3 we learn nothing about triangles.
