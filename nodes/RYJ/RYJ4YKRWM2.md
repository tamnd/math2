---
tag: RYJ4YKRWM2
kind: example
name: Divisibility by 3 is characterized by the digit sum
msc: ["03B05", "11A63"]
topics: [PM1AYWABA7]
audience: school
instance_of: [09BJQQB3VS]
uses: [09BJQQB3VS, 0R9D4CEJEB, 7ATVYQDHEX, 096PW7Q014]
sources:
  - url: https://en.wikipedia.org/wiki/Divisibility_rule
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Necessity_and_sufficiency
    locator: lead section
---

## Example

Let $n$ be a natural number with decimal digits $d_k d_{k-1} \dots d_0$, so that $n = \sum_{i=0}^{k} d_i 10^i$, and let $s = d_0 + d_1 + \dots + d_k$ be its [[digit sum|7ATVYQDHEX]].
The property is "$3$ [[divides|096PW7Q014]] $n$", and the condition is "$3$ divides $s$".
We check that the condition is [[necessary and sufficient|09BJQQB3VS]] for the property.

1. We have $10 \equiv 1 \pmod 3$, because $10 = 3 \cdot 3 + 1$.
2. So $10^i \equiv 1^i = 1 \pmod 3$ for each $i \ge 0$, because congruences can be raised to powers.
3. So $n = \sum d_i 10^i \equiv \sum d_i = s \pmod 3$, because congruences can be multiplied and added.
4. Sufficiency: if $3 \mid s$, then $s \equiv 0 \pmod 3$, and step 3 gives $n \equiv 0 \pmod 3$, so $3 \mid n$.
5. Necessity: if $3 \mid n$, then $n \equiv 0 \pmod 3$, and step 3 gives $s \equiv 0 \pmod 3$, so $3 \mid s$.
6. By steps 4 and 5, $3 \mid n$ if and only if $3 \mid s$. This is the [[rule of divisibility by 3|0R9D4CEJEB]].

Two checks with numbers: $7341$ has digit sum $15$, and $7341 = 3 \cdot 2447$; $2026$ has digit sum $10$, and $2026 = 3 \cdot 675 + 1$.

## Remarks

The example shows a characterization theorem: a property and an easier condition that is equivalent to it.
Both directions are used in practice: sufficiency to show that $3$ divides a number, and necessity to show that it does not.
If we replace $3$ by $9$, the same proof works, because $10 \equiv 1 \pmod 9$.
If we replace $3$ by $7$, the condition is neither necessary nor sufficient: $14$ is divisible by $7$ with digit sum $5$, and $16$ has digit sum $7$ but is not divisible by $7$.
The proof fails for $7$ at step 1, because $10 \equiv 3 \pmod 7$.

## Explanations

### L1 human

To test whether a number divides by $3$, add its digits.
If the sum divides by $3$, the number does, and if the sum does not, the number does not.
For $123$, the sum is $1 + 2 + 3 = 6$, which divides by $3$, and indeed $123 = 3 \cdot 41$.
For $124$, the sum is $7$, so $124$ does not divide by $3$.

### L2 human

We decide whether $3$ divides $987654$.

1. The digit sum is $9 + 8 + 7 + 6 + 5 + 4 = 39$.
2. The digit sum of $39$ is $12$, and $3 \mid 12$.
3. By sufficiency, applied twice, $3 \mid 39$ and then $3 \mid 987654$.

The typical use is a fast test, and the rule can be applied again to the digit sum.
A trap is to use the same test for $6$: the number $15$ has digit sum $6$, but $6 \nmid 15$, so the digit sum alone does not characterize divisibility by $6$.
