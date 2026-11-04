---
tag: 2X3BHXYR6D
kind: statement
role: lemma
name: The β function lemma
sources:
  - wikipedia: en:24708433@r1334325217
    locator: Gödel's β function, section The β function lemma
    note: adopted
    mention: wikipedia://en/24708433#FTPA
    sections: [Statement]
inventory: [B96X42M79C]
---

## Statement

The utility of the *β* function comes from the following result (Gödel 1931, *Hilfssatz* 1, p. 192-193), which is the purpose of the *β* function in Gödel’s incompleteness proof. This result is explained in more detail than in Gödel’s proof in (Mendelson 1997:186) and (Smith 2013:113-118).

***β* function lemma**. For any sequence of natural numbers (*k*<sub>0</sub>, *k*<sub>1</sub>, ..., *k*<sub>*n*</sub>), there are natural numbers *b* and *c* such that, for every natural number *0* ≤ *i* ≤ *n*, *β*(*b*, *c*, *i*) = *k*<sub>*i*</sub>.

As an example, the sequence (2, 0, 2, 1) can be encoded by *b* = 3412752 and *c* = 24, since

$$\begin{array}{lllll} \operatorname{rem}(3412752, (1+(0+1) \times 24)) & = & \operatorname{rem}(3412752, 25) & = & 2, \\ \operatorname{rem}(3412752, (1+(1+1) \times 24)) & = & \operatorname{rem}(3412752, 49) & = & 0, \\ \operatorname{rem}(3412752, (1+(2+1) \times 24)) & = & \operatorname{rem}(3412752, 73) & = & 2, \text{ and} \\ \operatorname{rem}(3412752, (1+(3+1) \times 24)) & = & \operatorname{rem}(3412752, 97) & = & 1. \\ \end{array}$$

The proof of the *β* function lemma makes use of the [[Chinese remainder theorem|0FNN9B4W64]].
