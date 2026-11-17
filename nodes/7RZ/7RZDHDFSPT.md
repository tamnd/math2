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

Statement: for each [[natural number|0MWKJ44V5A]] $n$, the number $n^3 - n$ is divisible by $3$.
We prove it by [[mathematical induction|0ASJVEFA9J]], and we check that each step is a deduction.

1. Let $P(n)$ be the statement "$3$ divides $n^3 - n$".
2. Base case: $0^3 - 0 = 0 = 3 \cdot 0$, so $P(0)$ holds.
3. Induction step: let $n$ be an arbitrary natural number, and assume $P(n)$. So $n^3 - n = 3m$ for some integer $m$.
4. We expand: $(n + 1)^3 - (n + 1) = n^3 + 3n^2 + 3n + 1 - n - 1 = (n^3 - n) + 3n^2 + 3n$.
5. By step 3, this is $3m + 3n^2 + 3n = 3(m + n^2 + n)$, and $m + n^2 + n$ is an integer. So $P(n + 1)$ holds.
6. Steps 3 to 5 show that $P(n)$ implies $P(n + 1)$ for each natural number $n$.
7. By the principle of mathematical induction, steps 2 and 6 give $P(n)$ for each natural number $n$.

Each step follows from the previous steps, from algebra, or from the principle of induction.
No step generalizes from observed cases.

## Remarks

The example shows that mathematical induction is [[deductive reasoning|5V35SGEN1T]], not inductive reasoning.
Inductive reasoning would look at $0, 0, 6, 24, 60, 120$ for $n = 0$ to $5$, see multiples of $3$, and guess the rule.
That guess is evidence, and it is the usual way to find the statement.
The proof above is different: step 6 covers an arbitrary $n$, so the conclusion is certain.

The two meanings of the word "induction" share an image: both move from the small cases to all cases.
But enumerative induction checks the small cases, while mathematical induction proves a rule that carries each case to the next one.
A direct proof is also possible here: $n^3 - n = (n - 1)n(n + 1)$ is a product of three consecutive integers, and one of them is a multiple of $3$.

## Explanations

### L1 human

The name "proof by induction" can mislead.
It does not mean "we checked many cases and saw a pattern".
It means two things are proved: the first case is true, and each case makes the next case true.
Like a row of dominoes, the first one falls and each one knocks over the next.
Then every case is true, with certainty, and no case was left to chance.

### L2 human

We compare the two kinds of reasoning on the same statement.

1. Inductive reasoning: $n = 2$ gives $6$, $n = 3$ gives $24$, $n = 4$ gives $60$. All are multiples of $3$, so the rule looks true.
2. Mathematical induction: the base case $n = 0$ and the induction step of the example prove the rule for all $n$.
3. The first argument can fail for a rule that looks just as good, as for the prime values of $n^2 + n + 41$.
4. The second argument cannot fail once each step is checked.

The typical use of mathematical induction is a statement about all natural numbers with a simple link between case $n$ and case $n + 1$.
A trap is to assume $P(n + 1)$ in the induction step instead of proving it.
The induction step assumes only $P(n)$.
