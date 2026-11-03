---
tag: BSPVYC28BY
kind: definition
name: Register machine
msc: [68Q04, 03D10]
defines: TGDKQY6S1T
uses: [0MWKJ44V5A, 4DQGSSWREK]
sources:
  - url: https://en.wikipedia.org/wiki/Register_machine
---

## Definition

Let $k \ge 1$.
A *register machine* (counter machine) with registers $R_1, \dots, R_k$ is a finite sequence $I_1, \dots, I_m$ of instructions of the following three kinds, where $1 \le i \le k$ and $1 \le j, l \le m$.

1. $\mathrm{INC}(i, j)$: add $1$ to $R_i$ and go to instruction $j$.
2. $\mathrm{DEC}(i, j, l)$: if $R_i = 0$, go to instruction $l$; otherwise subtract $1$ from $R_i$ and go to instruction $j$.
3. $\mathrm{HALT}$: stop.

A configuration is a pair $(p, r)$ of an instruction number $p$ and a vector $r \in \N^k$ of register contents.
Here $\N$ is the set of [[natural numbers|0MWKJ44V5A]].
A run starts at instruction $1$ and performs the instructions in turn until it reaches $\mathrm{HALT}$, if ever.
The machine computes the partial function $f \colon \N^n \rightharpoonup \N$, for $n < k$, that takes $(x_1, \dots, x_n)$ to the final content of $R_1$.
Here the run starts with $R_{i+1} = x_i$ for $i \le n$ and all other registers $0$, and $f(x)$ is undefined when the run does not halt.

## Remarks

Example: the program $I_1 = \mathrm{DEC}(3, 2, 3)$, $I_2 = \mathrm{INC}(1, 1)$, $I_3 = \mathrm{DEC}(2, 4, 5)$, $I_4 = \mathrm{INC}(1, 3)$, $I_5 = \mathrm{HALT}$ computes $f(x_1, x_2) = x_1 + x_2$.
Instructions $1$ and $2$ move the $x_2$ units of $R_3$ into $R_1$.
Then instructions $3$ and $4$ move the $x_1$ units of $R_2$ into $R_1$, and the run halts with $R_1 = x_1 + x_2$.
Non-example: an instruction that sets $R_i$ to $R_i \cdot R_j$ in one step is not allowed, since only the three kinds above exist.
Multiplication must be programmed as repeated addition.
The functions computed by register machines are exactly the [[partial recursive functions|4DQGSSWREK]].
Two registers already suffice for universality, when inputs and outputs are suitably encoded, for example as $2^x$.
Other register machine models allow more instructions, such as copying or indirect addressing.
