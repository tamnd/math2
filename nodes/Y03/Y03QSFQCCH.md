---
tag: Y03QSFQCCH
kind: example
name: Addition of residues modulo n is well defined
msc: ["00A35", "11A07"]
topics: [BP0WAF23HB]
audience: ug1
instance_of: [HNGZEBKVY2]
uses: [HNGZEBKVY2, 03VFZ2WETT, 0TPW25CBN6, 0PG2H7WKGG]
sources:
  - url: https://en.wikipedia.org/wiki/Well-defined_expression
    locator: Operations
  - url: https://en.wikipedia.org/wiki/Modular_arithmetic
    locator: lead section
---

## Example

Let $n \geq 1$ be an integer.
For an integer $a$, let $[a] = \{a + kn : k \in \mathbb{Z}\}$ be its residue class modulo $n$, and let $\mathbb{Z}/n\mathbb{Z}$ be the set of the classes.
These are the [[integers modulo $n$|03VFZ2WETT]].
The proposed addition is
$$[a] + [b] := [a + b].$$
We show that it is [[well defined|HNGZEBKVY2]].

1. The rule uses representatives $a$ and $b$, so we must show that other representatives give the same class.
2. Let $[a] = [a']$ and $[b] = [b']$. By the definition of [[congruence modulo $n$|0TPW25CBN6]], $n \mid a' - a$ and $n \mid b' - b$.
3. By the definition of [[divisibility|0PG2H7WKGG]], there are integers $s$ and $t$ with $a' - a = sn$ and $b' - b = tn$.
4. Then $(a' + b') - (a + b) = (a' - a) + (b' - b) = sn + tn = (s + t)n$.
5. So $n \mid (a' + b') - (a + b)$, and $[a' + b'] = [a + b]$.
6. So the sum class is the same for all choices of representatives, and $+$ is an operation on $\mathbb{Z}/n\mathbb{Z}$.

A numerical check with $n = 5$:

1. Take $[3]$ and $[4]$ with the representatives $3$ and $4$. The sum is $[7] = [2]$, because $7 - 2 = 5$.
2. Take the representatives $8$ and $-1$ of the same classes. The sum is $[7] = [2]$ again.
3. Take the representatives $-2$ and $9$. The sum is $[7] = [2]$ again.

## Remarks

1. The proof uses only that $n\mathbb{Z}$ is closed under addition. The same proof works for each subgroup of an abelian group, and it gives the addition on each quotient of an abelian group.
2. The multiplication $[a] \cdot [b] := [ab]$ is also well defined. The proof is in the L2 explanation of the page [[well-defined|HNGZEBKVY2]].
3. The rule $[a] \mapsto [a]$ from $\mathbb{Z}/n\mathbb{Z}$ to $\mathbb{Z}/m\mathbb{Z}$ is well defined only when $m \mid n$, as the [[reduction modulo a divisor|55FJH3WXE9]] shows.
4. Exponents do not reduce modulo $n$. The rule $[a]^{[k]} := [a^k]$ is not well defined on exponent classes: modulo $5$, $[2]^{[1]}$ would be $[2]$, but the representative $6$ of $[1]$ gives $[2^6] = [64] = [4]$.

## Explanations

### L1 human

Clock arithmetic with $5$ hours adds hours and then forgets full turns of the clock.
The time $3$ and the time $8$ are the same position, because $8$ is $3$ plus one full turn.
If we add $4$ hours to $3$, we reach $7$, which is position $2$.
If we add $4$ hours to $8$, we reach $12$, which is also position $2$.
Adding full turns before the sum never changes where we land, so the clock addition gives one clear answer.

### L2 human

We use the result to compute $[17] + [29]$ modulo $6$ in two ways.

1. Direct: $17 + 29 = 46$, and $46 = 7 \cdot 6 + 4$, so the sum is $[4]$.
2. With small representatives: $17 = 2 \cdot 6 + 5$ and $29 = 4 \cdot 6 + 5$, so $[17] = [5]$ and $[29] = [5]$.
3. Then $[5] + [5] = [10] = [4]$, because $10 = 6 + 4$.
4. The two answers agree, as the well-definedness proof guarantees.

The typical use: reduce each number first, then calculate with small numbers.
A trap is to apply the same idea to exponents, as remark 4 shows.
