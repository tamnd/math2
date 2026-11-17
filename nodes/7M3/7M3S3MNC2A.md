---
tag: 7M3S3MNC2A
kind: example
name: Residue classes modulo 7 written as integers
msc: ["00A35", "11A07"]
topics: [Z2WNQ1DNTX]
audience: ug1
instance_of: [JV68YRB5YZ]
uses: [JV68YRB5YZ, 03VFZ2WETT, 0W95W33CMP, 0WAY5WX8NY]
sources:
  - url: https://en.wikipedia.org/wiki/Abuse_of_notation
    locator: Equivalence classes
---

## Example

In [[integers modulo 7|03VFZ2WETT]], texts write $5 + 4 = 2$ and $3 \cdot 5 = 1$.
The elements of $\mathbb{Z}/7\mathbb{Z}$ are [[equivalence classes|0W95W33CMP]] $[a] = a + 7\mathbb{Z}$, not integers, so the short form is an abuse.
We expand it and check that it is safe.

1. The exact form of $5 + 4 = 2$ is $[5] + [4] = [9] = [2]$, since $9 - 2 = 7$.
2. The exact form of $3 \cdot 5 = 1$ is $[3] \cdot [5] = [15] = [1]$, since $15 - 1 = 14 = 2 \cdot 7$.
3. The result must not depend on the member that names a class. Take $12 \in [5]$ in place of $5$: then $12 + 4 = 16$, and $16 - 2 = 14 = 2 \cdot 7$, so $[16] = [2]$ again.
4. In general, if $a \equiv a'$ and $b \equiv b' \pmod 7$, then $a + b \equiv a' + b'$ and $ab \equiv a'b' \pmod 7$. So addition and multiplication of classes are well defined.
5. So each short form such as $5 + 4 = 2$ has exactly one exact form, and the abuse is safe.

## Remarks

The example shows the most common abuse in number theory: a class is named by one of its members, usually the one in $\{0, 1, \ldots, 6\}$.
The abuse is safe because the operations are well defined, which is the content of step 4.
It also explains the notation $a \equiv b \pmod 7$ of [[congruence modulo n|0WAY5WX8NY]], which states $[a] = [b]$ with integers only.
The abuse fails for operations that are not well defined, such as $[a] \mapsto a$ to $\mathbb{Z}$ or the exponent in $2^{[a]}$, since $2^{0} = 1$ but $2^{7} = 128 = 2$ in $\mathbb{Z}/7\mathbb{Z}$.

## Explanations

### L1 human

On a week clock with $7$ days, the days are numbered $0$ to $6$.
Five days after day $4$ is day $2$ of the next week, so we write $4 + 5 = 2$.
Strictly, "$2$" here means every day number that leaves remainder $2$ after division by $7$.
We still write the plain number $2$ because the answer is the same whichever day number we start from.

### L2 human

We find the inverse of $3$ in $\mathbb{Z}/7\mathbb{Z}$ with the short form and check it with the exact form.

1. Try the members $0$ to $6$: $3 \cdot 5 = 15 = 2 \cdot 7 + 1$, so $3 \cdot 5 = 1$ in $\mathbb{Z}/7\mathbb{Z}$.
2. So $3^{-1} = 5$.
3. In exact form, $[3] \cdot [5] = [15] = [1]$, and the class $[5]$ is the inverse of $[3]$.
4. Another member of $[5]$, such as $-2$, gives $3 \cdot (-2) = -6 = -7 + 1$, so $[-6] = [1]$ again.

The typical use of this abuse is in solving congruences, such as $3x = 4$ in $\mathbb{Z}/7\mathbb{Z}$, with solution $x = 5 \cdot 4 = 20 = 6$.
A trap: in $\mathbb{Z}/6\mathbb{Z}$, the class $3$ has no inverse, since $3 \cdot b$ is $0$ or $3$ for every $b$.
