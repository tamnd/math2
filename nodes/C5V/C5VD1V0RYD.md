---
tag: C5VD1V0RYD
kind: definition
name: Random-access machine
msc: [68Q04, 68Q25]
defines: 2PQKV1KX24
uses: [TGDKQY6S1T, 0MWKJ44V5A]
sources:
  - url: https://en.wikipedia.org/wiki/Random-access_machine
---

## Definition

A *random-access machine* has registers $r_0, r_1, r_2, \dots$, indexed by the [[natural numbers|0MWKJ44V5A]], each holding a natural number.
A program is a finite sequence $I_1, \dots, I_m$ of instructions of the following kinds, where $i, j, k, c \in \N$ and $1 \le l \le m$.

1. $r_i \leftarrow c$, which loads a constant.
2. $r_i \leftarrow r_j + r_k$ and $r_i \leftarrow r_j \mathbin{\dot-} r_k$, where $a \mathbin{\dot-} b = \max(a - b, 0)$.
3. $r_i \leftarrow r_{r_j}$ and $r_{r_i} \leftarrow r_j$, the indirect load and store.
4. $\mathrm{JZ}(i, l)$, which goes to instruction $l$ if $r_i = 0$.
5. $\mathrm{HALT}$.

Every instruction other than a taken jump or $\mathrm{HALT}$ is followed by the next one in the list.
A run starts at $I_1$ with the input in finitely many registers and all other registers $0$.
When the run halts, the output is read from a fixed register.
In the *unit cost* measure each instruction costs $1$.
In the *logarithmic cost* measure an instruction costs the total number of bits of the addresses and values it uses.

## Remarks

Example: the program $I_1 = r_3 \leftarrow r_{r_1}$, $I_2 = \mathrm{HALT}$ copies into $r_3$ the content of the register whose number is stored in $r_1$.
With $r_1 = 100$ it reads $r_{100}$ in one step.
A [[register machine|TGDKQY6S1T]] program names only finitely many registers, so it cannot read a register whose number is computed during the run.
Non-example: a program with the instruction $r_i \leftarrow r_j \cdot r_k$ is not a program of this machine.
Adding unit-cost multiplication changes the model, since repeated squaring then builds numbers with exponentially many bits in polynomially many steps.
Many variants are in use, for example with an accumulator or with integer registers; they have the same computing power.
