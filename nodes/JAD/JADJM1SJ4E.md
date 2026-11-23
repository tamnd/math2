---
tag: JADJM1SJ4E
kind: example
name: The contrapositive of an implication is neither its converse nor its inverse
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
not_instance_of:
  - target: 09A3N7ZN5G
    note: the formula not q implies not p swaps and negates both parts, while the converse only swaps them and the inverse only negates them
uses: [09A3N7ZN5G, 04T1CT7212]
sources:
  - url: https://en.wikipedia.org/wiki/Contraposition
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Converse_(logic)
    locator: lead section
---

## Example

"If $n$ is odd, then $4$ does not divide $n$" contains two negations, but it is not the inverse of "if $4$ divides $n$, then $n$ is even".
For an integer $n$, let $p$ be "$4$ divides $n$", and let $q$ be "$n$ is even".
The implication $p \to q$ is true.
Let $S$ be the statement "if $n$ is odd, then $4$ does not divide $n$".
We check that $S$ is neither the [[converse nor the inverse|09A3N7ZN5G]] of $p \to q$.

1. The statement $S$ has the form $\neg q \to \neg p$, because "$n$ is odd" is the negation of "$n$ is even".
2. The converse of $p \to q$ is $q \to p$, with antecedent $q$.
   The antecedent of $S$ is $\neg q$, so $S$ is not the converse.
3. The inverse of $p \to q$ is $\neg p \to \neg q$, with antecedent $\neg p$.
   The antecedent of $S$ is $\neg q$, so $S$ is not the inverse.
4. The truth values confirm this.
   The converse "if $n$ is even, then $4$ divides $n$" is false for $n = 2$.
5. The inverse "if $4$ does not divide $n$, then $n$ is odd" is false for $n = 2$ as well.
6. The statement $S$ is true, because if $4$ divided an odd $n$, then $n$ would be even by $p \to q$.

So $S$ is the [[contrapositive|04T1CT7212]] of $p \to q$, the one related implication that is equivalent to $p \to q$.

## Remarks

### Two operations

The three related implications come from two independent operations: swapping the parts and negating them.
The converse swaps, the inverse negates, and the contrapositive does both.
Both operations together keep the truth value, and one operation alone can change it.

### Watch out

Not every implication with "not" in it is the contrapositive.
To name a related implication, first check whether the antecedent is built from $p$ or from $q$, then check whether the parts are negated.

### Try it

Name the statement "if $n$ is not even, then $4$ does not divide $n$" relative to $p \to q$ above.
Its antecedent is $\neg q$ and its consequent is $\neg p$, so it is the contrapositive, and it is true.

## Explanations

### L1 human

Start from "if a number is a multiple of $4$, then it is even".
Swapping the two parts gives "if a number is even, then it is a multiple of $4$", and $2$ shows that this is false.
Swapping and adding "not" to both parts gives "if a number is not even, then it is not a multiple of $4$", and this is true.
The last sentence is the contrapositive, not the converse.

### L2 human

To name a related implication, compare it with $p \to q$ in two steps.
First find whether the antecedent is built from $p$ or from $q$, and then find whether the parts are negated.
Antecedent from $q$ and no negations gives the converse.
Antecedent from $p$ and negations gives the inverse.
Antecedent from $q$ and negations gives the contrapositive.
