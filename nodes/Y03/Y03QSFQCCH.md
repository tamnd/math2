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

Let $n \ge 1$ be an integer.
For an integer $a$, let $[a] = \{ a + kn : k \in \mathbb{Z} \}$ be its residue class modulo $n$, and let $\mathbb{Z}/n\mathbb{Z}$ be the set of these classes, the [[integers modulo $n$|03VFZ2WETT]].
The proposed addition is
$$[a] + [b] := [a + b].$$
We show that it is [[well defined|HNGZEBKVY2]].

1. The rule uses representatives $a$ and $b$, so we must show that other representatives give the same class.
2. Let $[a] = [a']$ and $[b] = [b']$.
   By the definition of [[congruence modulo $n$|0TPW25CBN6]], $n \mid a' - a$ and $n \mid b' - b$.
3. By the definition of [[divisibility|0PG2H7WKGG]], there are integers $s$ and $t$ with $a' - a = sn$ and $b' - b = tn$.
4. Subtract the two sums:
   $$(a' + b') - (a + b) = (a' - a) + (b' - b) = sn + tn = (s + t) n.$$
5. So $n \mid (a' + b') - (a + b)$, and $[a' + b'] = [a + b]$.
6. The sum class is the same for every choice of representatives, so $+$ is an operation on $\mathbb{Z}/n\mathbb{Z}$.

Check with $n = 5$ and the classes $[3]$ and $[4]$.
The representatives $3$ and $4$, then $8$ and $-1$, then $-2$ and $9$, give the sums
$$7, \qquad 7, \qquad 7,$$
and $[7] = [2]$ because $7 - 2 = 5$.
The pair $13$ and $4$ gives $17$, and $17 - 2 = 15$, so the sum is again $[2]$.

## Remarks

The proof uses only that the multiples of $n$ are closed under addition.
So the same argument works for every subgroup of an abelian group, and it gives the addition on every quotient of an abelian group.

Multiplication $[a] \cdot [b] := [ab]$ is well defined as well, and the L2 explanation of [[well-defined|HNGZEBKVY2]] proves it.
The rule $[a]_n \mapsto [a]_m$ from $\mathbb{Z}/n\mathbb{Z}$ to $\mathbb{Z}/m\mathbb{Z}$ is well defined only when $m \mid n$, as [[the reduction from $\mathbb{Z}/6\mathbb{Z}$ to $\mathbb{Z}/3\mathbb{Z}$|55FJH3WXE9]] shows.

Exponents do not reduce modulo $n$.
The rule $[a]^{[k]} := [a^k]$ is not well defined on exponent classes modulo $5$:
$$[2]^{[1]} = [2^1] = [2], \qquad [2]^{[6]} = [2^6] = [64] = [4],$$
although $[1] = [6]$ modulo $5$.

## Explanations

### L1 human

Clock arithmetic with $5$ hours adds hours and then forgets full turns of the clock.
The times $3$ and $8$ are the same position, because $8$ is $3$ plus one full turn.
If we add $4$ hours to $3$, we reach $7$, which is position $2$.
If we add $4$ hours to $8$, we reach $12$, which is also position $2$.
Extra full turns never change where we land, so clock addition gives one clear answer.

### L2 human

We use the result to compute $[17] + [29]$ modulo $6$ in two ways.
Directly, $17 + 29 = 46 = 7 \cdot 6 + 4$, so the sum is $[4]$.
With small representatives, $17 = 2 \cdot 6 + 5$ and $29 = 4 \cdot 6 + 5$, so $[17] = [5]$ and $[29] = [5]$, and
$$[5] + [5] = [10] = [4].$$
The two answers agree, as the well-definedness proof guarantees.
This is the everyday use of the result: reduce each number first, and then calculate with small numbers.
Watch out: the same shortcut is wrong for exponents, as the remark above shows.
