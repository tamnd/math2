---
tag: 1DVJWM421F
kind: example
name: The converse and the inverse of "if 6 divides n, then 3 divides n"
msc: ["03B05", "11A05"]
topics: [PM1AYWABA7]
audience: school
instance_of: [09A3N7ZN5G]
uses: [09A3N7ZN5G, 096PW7Q014, 04T1CT7212]
sources:
  - url: https://en.wikipedia.org/wiki/Converse_(logic)
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.5
---

## Example

Every multiple of $6$ is a multiple of $3$, but $3$ itself is a multiple of $3$ and not of $6$.
For an integer $n$, let $p$ be "$6$ [[divides|096PW7Q014]] $n$", and let $q$ be "$3$ divides $n$".
We check the four related implications of $p \to q$ for every integer $n$.

1. The implication $p \to q$ is true.
   If $n = 6k$ for an integer $k$, then $n = 3(2k)$, so $3$ divides $n$.
2. The [[converse|09A3N7ZN5G]] $q \to p$ reads "if $3$ divides $n$, then $6$ divides $n$".
   It is false: for $n = 3$ the antecedent is true, and $6$ does not divide $3$.
3. The inverse $\neg p \to \neg q$ reads "if $6$ does not divide $n$, then $3$ does not divide $n$".
   It is false: for $n = 3$ the antecedent is true, and $3$ divides $3$.
4. The [[contrapositive|04T1CT7212]] $\neg q \to \neg p$ reads "if $3$ does not divide $n$, then $6$ does not divide $n$".
   It is true by step 1 and the law of the contrapositive.
5. The single value $n = 3$ refutes both the converse and the inverse, as their logical equivalence predicts.

## Remarks

### What the example shows

The pattern is typical: a true implication, a true contrapositive, and a false converse and inverse.
Every counterexample to the converse is divisible by $3$ and not by $6$, that is, an odd multiple of $3$ such as $3$, $9$ or $15$.
If we change $6$ to $3$ in $p$, then all four implications become true, because $p$ and $q$ become the same statement.
If we add the hypothesis "$n$ is even" to the converse, it becomes true, because $2$ and $3$ are coprime, so an even multiple of $3$ is a multiple of $6$.

### Watch out

Testing the converse only on $n = 6$ and $n = 12$ would make it look true.
Test the cases where the new antecedent holds and the old one may fail, here the odd multiples of $3$.

### Try it

Is the converse of "if $4$ divides $n$, then $2$ divides $n$" true?
No: $n = 2$ is divisible by $2$ and not by $4$.

## Explanations

### L1 human

A number that splits into $6$ equal whole parts also splits into $3$ equal whole parts.
The reverse is not true: $3$ splits into $3$ parts of size $1$, but not into $6$ whole parts.
So the sentence is true, and the sentence with the parts exchanged is false.

### L2 human

Test a converse on a list of numbers before you try to prove it.
The converse here is "if $3$ divides $n$, then $6$ divides $n$".
Among the multiples of $3$ up to $15$, which are $3$, $6$, $9$, $12$ and $15$, only $6$ and $12$ are divisible by $6$.
So $n = 3$ is a counterexample, and the converse is false.
A short test like this decides quickly whether a converse is worth trying to prove.
