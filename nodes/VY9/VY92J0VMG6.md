---
tag: VY92J0VMG6
kind: example
name: The congruence 3x = 1 modulo 7 has a unique solution
msc: ["00A35", "11A07"]
topics: [958EF46EYJ]
audience: ug1
instance_of: [GQHHNV79PA]
uses: [GQHHNV79PA, 0WAY5WX8NY, 051VYKA1EX, 0CEC45PRJN]
sources:
  - url: https://en.wikipedia.org/wiki/Modular_multiplicative_inverse
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Euclid%27s_lemma
    locator: lead section
---

## Example

Statement: among the integers $0, 1, \dots, 6$, exactly one $x$ satisfies $3x \equiv 1 \pmod 7$, namely $x = 5$.
Here $a \equiv b \pmod 7$ means $7 \mid a - b$; see [[congruence modulo n|0WAY5WX8NY]].
We prove existence, and then [[uniqueness|GQHHNV79PA]] in the first form.

1. Existence.
   Compute $3 \cdot 5 = 15 = 2 \cdot 7 + 1$, so $3 \cdot 5 \equiv 1 \pmod 7$.
2. Uniqueness.
   Suppose $x$ and $y$ are in $\{0, 1, \dots, 6\}$ with $3x \equiv 1$ and $3y \equiv 1 \pmod 7$.
3. Subtract the two congruences:
   $$7 \mid 3x - 3y = 3(x - y).$$
4. The number $7$ is prime and does not divide $3$.
   By [[Euclid's lemma|051VYKA1EX]], $7 \mid x - y$.
5. Both $x$ and $y$ lie between $0$ and $6$, so $-6 \le x - y \le 6$.
   The only multiple of $7$ in this range is $0$, so $x = y$.
6. Steps 1 to 5 show that $x = 5$ is a solution and that any two solutions are equal.
   So $5$ is the only solution in $\{0, 1, \dots, 6\}$.

In the language of [[modular inverses|0CEC45PRJN]], $5$ is the inverse of $3$ modulo $7$.

## Remarks

A table confirms the result.
The products $3 \cdot 0, 3 \cdot 1, \dots, 3 \cdot 6$ are
$$0, \; 3, \; 6, \; 9, \; 12, \; 15, \; 18,$$
with remainders $0, 3, 6, 2, 5, 1, 4$ on division by $7$.
The remainder $1$ appears once, at $x = 5$.
The table checks seven cases, while the proof explains why each remainder appears only once, and the same proof works for every prime modulus that does not divide $3$.

Uniqueness can fail when the modulus shares a factor with the coefficient, because then step 4 breaks.
Modulo $6$, the congruence $2x \equiv 0$ has the two solutions $x = 0$ and $x = 3$ in $\{0, \dots, 5\}$.
Existence can fail too: $3x \equiv 1 \pmod 6$ has no solution at all, since $3x - 1$ is never a multiple of $3$, let alone of $6$.

## Explanations

### L1 human

Count in steps of $3$ on a clock with $7$ hours, numbered $0$ to $6$.
Starting at $0$, the hand visits $0, 3, 6, 2, 5, 1, 4$.
It lands on $1$ after exactly $5$ steps, and no other number of steps from $0$ to $6$ lands there.
The proof shows that two different step counts can never land on the same hour.

### L2 human

We use the result to solve $3x \equiv 4 \pmod 7$.

1. Multiply both sides by the inverse $5$:
   $$15x \equiv 20 \pmod 7.$$
2. Since $15 \equiv 1$ and $20 \equiv 6 \pmod 7$, this gives $x \equiv 6 \pmod 7$.
3. Check: $3 \cdot 6 = 18 = 2 \cdot 7 + 4$.
4. Two solutions in $\{0, \dots, 6\}$ are equal by the argument of steps 3 to 5 of the example, so $x = 6$ is the only one.

The typical use: once the inverse of $3$ is known to be unique, you can call it "the" inverse and use it to divide by $3$ modulo $7$.
Watch out: multiplying by $5$ keeps every solution and adds none only because $5$ itself has an inverse modulo $7$, namely $3$.
Multiplying by $7$ would turn every congruence into $0 \equiv 0$.
