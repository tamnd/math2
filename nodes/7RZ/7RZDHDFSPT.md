---
tag: 7RZDHDFSPT
kind: example
name: A proof by mathematical induction is a deduction
msc: ["00A35", "11A05"]
topics: [N4P3E53HM0]
audience: school
instance_of: [5V35SGEN1T, 0ASJVEFA9J]
uses: [5V35SGEN1T, 0ASJVEFA9J, 0MWKJ44V5A]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Inductive_reasoning
    locator: lead section
---

## Example

Statement: for every [[natural number|0MWKJ44V5A]] $n$, the number $n^3 - n$ is divisible by $3$.
We prove it by [[mathematical induction|0ASJVEFA9J]], and we check that every step is a deduction.

1. Let $P(n)$ be the statement "$3$ divides $n^3 - n$".
2. Base case: $0^3 - 0 = 0 = 3 \cdot 0$, so $P(0)$ holds.
3. Induction step: let $n$ be an arbitrary natural number, and assume $P(n)$.
   Then $n^3 - n = 3m$ for some integer $m$.
4. Expand the next case:
   $$(n + 1)^3 - (n + 1) = n^3 + 3n^2 + 3n + 1 - n - 1 = (n^3 - n) + 3n^2 + 3n.$$
5. By step 3 this equals $3m + 3n^2 + 3n = 3(m + n^2 + n)$, and $m + n^2 + n$ is an integer.
   So $P(n + 1)$ holds.
6. Steps 3 to 5 show that $P(n)$ implies $P(n + 1)$ for every natural number $n$.
7. The principle of mathematical induction, applied to steps 2 and 6, gives $P(n)$ for every natural number $n$.

Each step follows from earlier steps, from algebra, or from the principle of induction.
No step generalizes from observed cases.

Check for $n = 4$: $4^3 - 4 = 60 = 3 \cdot 20$.

## Remarks

Mathematical induction is [[deductive reasoning|5V35SGEN1T]], not inductive reasoning.
Inductive reasoning would compute $n^3 - n$ for $n = 0$ to $5$, get $0, 0, 6, 24, 60, 120$, see multiples of $3$, and guess the rule.
That guess is evidence, and it is the usual way to find the statement.
The proof is different: step 6 covers an arbitrary $n$, so the conclusion is certain.

The two meanings of "induction" share an image, since both move from small cases to all cases.
But enumerative induction checks some small cases, while mathematical induction proves a rule that carries each case to the next.

A direct proof also exists.
Factor the number as a product of three consecutive integers:
$$n^3 - n = (n - 1)\,n\,(n + 1).$$
Among three consecutive integers exactly one is a multiple of $3$, so the product is a multiple of $3$.

Watch out.
In the induction step you may assume only $P(n)$, and you must prove $P(n + 1)$.
Writing "assume $P(n + 1)$" and then checking it against $P(n)$ assumes what was to be shown.

## Explanations

### L1 human

The name "proof by induction" can mislead.
It does not mean "we checked many cases and saw a pattern".
It means that two things are proved: the first case is true, and each case makes the next case true.
Think of a row of dominoes: the first one falls, and each one knocks over the next.
Then every domino falls, with certainty, and no case was left to chance.

### L2 human

Compare the two kinds of reasoning on one statement.
Inductive reasoning says: $n = 2$ gives $6$, $n = 3$ gives $24$, $n = 4$ gives $60$, all multiples of $3$, so the rule looks true.
The same kind of argument looks just as good for the prime values of $n^2 + n + 41$, and there it fails at $n = 40$.
Mathematical induction says: the base case $n = 0$ holds, and the expansion
$$(n + 1)^3 - (n + 1) = (n^3 - n) + 3(n^2 + n)$$
carries divisibility by $3$ from $n$ to $n + 1$.
Once each of those two facts is checked, the argument cannot fail.
The method fits any statement about all natural numbers with a simple link between the case $n$ and the case $n + 1$.
