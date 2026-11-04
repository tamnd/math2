---
tag: 7G0MN4Q4DJ
kind: statement
role: proposition
name: Minimizing pairwise inequality
sources:
  - wikipedia: en:68407499@r1360707387
    locator: Mathematics of apportionment, section Minimizing pairwise inequality
    note: adopted
    mention: wikipedia://en/68407499#CGTJ
    sections: [Statement]
inventory: [M4JDZRH6BB]
---

## Statement

One way to evaluate apportionment methods is by whether they minimize the amount of *inequality* between pairs of agents. Clearly, inequality should take into account the different entitlements: if $a_i/t_i = a_j / t_j$ then the agents are treated "equally" (w.r.t. their entitlements); otherwise, if $a_i/t_i > a_j / t_j$ then agent $i$ is favored, and if $a_i/t_i < a_j / t_j$ then agent $j$ is favored. However, since there are 16 ways to rearrange the equality $a_i/t_i = a_j / t_j$, there are correspondingly many ways by which inequality can be defined.

- $|a_i/t_i - a_j / t_j|$. Webster's method is the unique apportionment method in which, for each pair of agents $i$ and $j$, this difference is minimized (that is, moving a seat from $i$ to $j$ or vice versa would not make the difference smaller).
- $a_i - (t_i/t_j)a_j$ for $a_i/t_i \geq a_j/t_j$ This leads to Adams's method.
- $a_i(t_j/t_i) - a_j$ for $a_i/t_i \geq a_j/t_j$. This leads to Jefferson's method.
- $|t_i/a_i - t_j /a_j|$. This leads to Dean's method.
- $\left|\frac{a_i/t_i}{a_j/t_j} - 1\right|$. This leads to the Huntington-Hill method.

This analysis was done by Huntington in the 1920s. Some of the possibilities do not lead to a stable solution. For example, if we define inequality as $|a_i/a_j - t_i/t_j|$, then there are instances in which, for any allocation, moving a seat from one agent to another might decrease their pairwise inequality. There is an example with 3 states with populations (737,534,329) and 16 seats.
