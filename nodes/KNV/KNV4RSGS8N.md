---
tag: KNV4RSGS8N
kind: statement
role: proposition
name: Monotone laws
sources:
  - wikipedia: en:54476844@r1368725040
    locator: Boolean algebra, section Laws > Monotone laws
    note: adopted
    mention: wikipedia://en/54476844#AWON
    sections: [Statement]
inventory: [XP7F9PVNE2]
---

## Statement

Boolean algebra satisfies many of the same laws as ordinary algebra when one matches up ∨ with addition and ∧ with multiplication. In particular the following laws are common to both kinds of algebra:

{|

\|- | Associativity of $\lor$: ||style="width:2em"| ||style="text-align: right"| $x \vee (y \vee z)$ || $= (x \vee y) \vee z$ |- | Associativity of $\land$: || ||style="text-align: right"| $x \wedge (y \wedge z)$ || $= (x \wedge y) \wedge z$ |- | Commutativity of $\lor$: || ||style="text-align: right"| $x \vee y$ || $= y \vee x$ |- | Commutativity of $\land$: || ||style="text-align: right"| $x \wedge y$ || $= y \wedge x$ |- | Distributivity of $\land$ over $\lor$: || ||style="text-align: right"| $x \wedge (y \vee z)$ || $= (x \wedge y) \vee (x \wedge z)$ |- | Identity for $\lor$: || ||style="text-align: right"| $x \vee 0$ || $= x$ |- | Identity for $\land$: || ||style="text-align: right"| $x \wedge 1$||$= x$ |- | Annihilator for $\land$: || ||style="text-align: right"| $x \wedge 0$ || $= 0$ |- |}

The following laws hold in Boolean algebra, but not in ordinary algebra:

{|

\|- Annihilator for $\lor$: || ||style="text-align: right"| $x \vee 1$ || $= 1$ |- |Annihilator for $\lor$: || ||style="text-align: right"| $x \vee 1$ |$= 1$ |- | Idempotence of $\lor$: || ||style="text-align: right"| $x \vee x$ || $= x$ |- | Idempotence of $\land$: || ||style="text-align: right"| $x \wedge x$ || $= x$ |- | Absorption 1: || ||style="text-align: right"| $x \wedge (x \vee y)$ || $= x$ |- | Absorption 2: || ||style="text-align: right"| $x \vee (x \wedge y)$ || $= x$ |- |Distributivity of $\lor$ over $\land$: | |$x \vee (y \wedge z)$ |$=(x \vee y) \wedge (x \vee z)$ |- | Distributivity of $\lor$ over $\land$: | |}

Taking $x = 2$ in the third law above shows that it is not an ordinary algebra law, since $2 \times 2 = 4$. The remaining five laws can be falsified in ordinary algebra by taking all variables to be 1. For example, in absorption law 1, the left hand side would be $1(1 + 1) = 2$, while the right hand side would be 1 (and so on).

All of the laws treated thus far have been for conjunction and disjunction. These operations have the property that changing either argument either leaves the output unchanged, or the output changes in the same way as the input. Equivalently, changing any variable from 0 to 1 never results in the output changing from 1 to 0. And vice versa. Operations with this property are said to be *monotone*. Thus the axioms thus far have all been for monotonic Boolean logic. Nonmonotonicity enters via complement ¬ as follows.
