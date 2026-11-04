---
tag: R6V9E6MD1F
kind: statement
role: proposition
name: Propositional formula with "feedback"
sources:
  - wikipedia: en:1557634@r1345686870
    locator: Propositional formula, section Propositional formula with "feedback"
    note: adopted
    mention: wikipedia://en/1557634#H5FH
    sections: [Statement]
inventory: [6Q6T99DVAK]
---

## Statement

The notion of a propositional formula appearing as one of its own variables requires a formation rule that allows the assignment of the formula to a variable. In general there is no stipulation (either axiomatic or truth-table systems of objects and relations) that forbids this from happening.

The simplest case occurs when an OR formula becomes one its own inputs e.g. p = q. Begin with (p ∨ s) = q, then let p = q. Observe that q's "definition" depends on itself "q" as well as on "s" and the OR connective; this definition of q is thus impredicative. Either of two conditions can result: oscillation or memory.

It helps to think of the formula as a black box. Without knowledge of what is going on "inside" the formula-"box" from the outside it would appear that the output is no longer a [[function|0EPAT51DXQ]] of the inputs alone. That is, sometimes one looks at q and sees 0 and other times 1. To avoid this problem one has to know the state (condition) of the "hidden" variable p inside the box (i.e. the value of q fed back and assigned to p). When this is known the apparent inconsistency goes away.

To understand \[predict\] the behavior of formulas with feedback requires the more sophisticated analysis of sequential circuits. Propositional formulas with feedback lead, in their simplest form, to state machines; they also lead to memories in the form of Turing tapes and counter-machine counters. From combinations of these elements one can build any sort of bounded computational model (e.g. Turing machines, counter machines, register machines, Macintosh computers, etc.).

In the abstract (ideal) case the simplest oscillating formula is a NOT fed back to itself: ~(~(p=q)) = q. Analysis of an abstract (ideal) propositional formula in a truth-table reveals an inconsistency for both p=1 and p=0 cases: When p=1, q=0, this cannot be because p=q; ditto for when p=0 and q=1.

|  |  | q |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
| p |  | ~ | ( | p | ) | \= q |  |
| 0 |  | 1 |  | 0 |  | 1 | q & p inconsistent |
| 1 |  | 0 |  | 1 |  | 0 | q & p inconsistent |

**Oscillation with delay**: If a delay (ideal or non-ideal) is inserted in the abstract formula between p and q then p will oscillate between 1 and 0: 101010...101... *ad infinitum*. If either of the delay and NOT are not abstract (i.e. not ideal), the type of analysis to be used will be dependent upon the exact nature of the objects that make up the oscillator; such things fall outside mathematics and into engineering.

Analysis requires a delay to be inserted and then the loop cut between the delay and the input "p". The delay must be viewed as a kind of proposition that has "qd" (q-delayed) as output for "q" as input. This new proposition adds another column to the truth table. The inconsistency is now between "qd" and "p" as shown in red; two stable states resulting:

|  |  |  | q |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
| qd | p | ( | ~ | ( | p | ) | \= q |  |
| 0 | 0 |  | 1 |  | 0 |  | 1 | state 1 |
| 0 | 1 |  | 0 |  | 1 |  | 0 | qd & p inconsistent |
| 1 | 0 |  | 1 |  | 0 |  | 1 | qd & p inconsistent |
| 1 | 1 |  | 0 |  | 1 |  | 0 | state 0 |

Without delay, inconsistencies must be eliminated from a truth table analysis. With the notion of "delay", this condition presents itself as a momentary inconsistency between the fed-back output variable q and p = q<sub>delayed</sub>.

A truth table reveals the rows where inconsistencies occur between p = q<sub>delayed</sub> at the input and q at the output. After "breaking" the feed-back, the truth table construction proceeds in the conventional manner. But afterwards, in every row the output q is compared to the now-independent input p and any inconsistencies between p and q are noted (i.e. p=0 together with q=1, or p=1 and q=0); when the "line" is "remade" both are rendered impossible by the Law of contradiction ~(p & ~p)). Rows revealing inconsistencies are either considered transient states or just eliminated as inconsistent and hence "impossible".

About the simplest memory results when the output of an OR feeds back to one of its inputs, in this case output "q" feeds back into "p". Given that the formula is first evaluated (initialized) with p=0 & q=0, it will "flip" once when "set" by s=1. Thereafter, output "q" will sustain "q" in the "flipped" condition (state q=1). This behavior, now time-dependent, is shown by the state diagram to the right of the once-flip.

|  |  |  |  | q |  |  |  |  |
|---|---|---|---|---|---|---|---|---|
| p | s | ( | s | ∨ | p | ) | \= q |  |
| 0 | 0 |  | 0 | 0 | 0 |  | 0 | state 0, s=0 |
| 0 | 1 |  | 1 | 1 | 0 |  |  | q & p inconsistent |
| 1 | 0 |  | 0 | 1 | 1 |  | 1 | state 1 with s = 0 |
| 1 | 1 |  | 1 | 1 | 1 |  | 1 | state 1 with s = 1 |

The next simplest case is the "set-reset" flip-flop shown below the once-flip. Given that r=0 & s=0 and q=0 at the outset, it is "set" (s=1) in a manner similar to the once-flip. It however has a provision to "reset" q=0 when "r"=1. And additional complication occurs if both set=1 and reset=1. In this formula, the set=1 *forces* the output q=1 so when and if (s=0 & r=1) the flip-flop will be reset. Or, if (s=1 & r=0) the flip-flop will be set. In the abstract (ideal) instance in which s=1 ⇒ s=0 & r=1 ⇒ r=0 simultaneously, the formula q will be indeterminate (undecidable). Due to delays in "real" OR, AND and NOT the result will be unknown at the outset but thereafter predicable.

|  |  |  |  |  | q |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| p | s | r | ( | s | ∨ | ( | p | & | ~ | ( | r | ) | ) | ) | \= q |  |
| 0 | 0 | 0 |  | 0 | 0 |  | 0 | 0 | 1 |  | 0 |  |  |  | 0 | state 0 with ( s=0 & r=0 ) |
| 0 | 0 | 1 |  | 0 | 0 |  | 0 | 0 | 0 |  | 1 |  |  |  | 0 | state 0 with ( s=0 & r=1 ) |
| 0 | 1 | 0 |  | 1 | 1 |  | 0 | 0 | 1 |  | 0 |  |  |  |  | q & p inconsistent |
| 0 | 1 | 1 |  | 1 | 1 |  | 0 | 0 | 0 |  | 1 |  |  |  |  | q & p inconsistent |
| 1 | 0 | 0 |  | 0 | 1 |  | 1 | 1 | 1 |  | 0 |  |  |  | 1 | state 1 with ( s=0 & r=0 ) |
| 1 | 0 | 1 |  | 0 | 0 |  | 1 | 0 | 0 |  | 1 |  |  |  |  | q & p inconsistent |
| 1 | 1 | 0 |  | 1 | 1 |  | 1 | 1 | 1 |  | 0 |  |  |  | 1 | state 1 with ( s=1 & r=0 ) |
| 1 | 1 | 1 |  | 1 | 1 |  | 1 | 0 | 0 |  | 1 |  |  |  | 1 | state 1 with s & r simultaneously 1 |

The formula known as "clocked flip-flop" memory ("c" is the "clock" and "d" is the "data") is given below. It works as follows: When c = 0 the data d (either 0 or 1) cannot "get through" to affect output q. When c = 1 the data d "gets through" and output q "follows" d's value. When c goes from 1 to 0 the last value of the data remains "trapped" at output "q". As long as c=0, d can change value without causing q to change.

- Examples
  1. ( ( c & d ) ∨ ( **p** & ( ~( c & ~( d ) ) ) ) = **q**, but now let p = q:
  1. ( ( c & d ) ∨ ( **q** & ( ~( c & ~( d ) ) ) ) = **q**

The state diagram is similar in shape to the flip-flop's state diagram, but with different labelling on the transitions.

|  |  |  |  |  |  |  | s |  |  | q |  |  | w | v |  |  |  | r | u |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| row | q | d | c | ( | ( | c | & | d | ) | ∨ | ( | q | & | ~ | ( | ( | c | & | ~ | ( | d | ) | ) | ) | ) | ) | \=q | Description |
| 0 | 0 | 0 | 0 |  |  | 0 | 0 | 0 |  | 0 |  | 0 | 0 | 1 |  |  | 0 | 0 | 1 |  | 0 |  |  |  |  |  | 0 | state 0 with ( s=0 & r=0 ), 0 is trapped |
| 1 | 0 | 0 | 1 |  |  | 1 | 0 | 0 |  | 0 |  | 0 | 0 | 0 |  |  | 1 | 1 | 1 |  | 0 |  |  |  |  |  | 0 | state 0 with ( d=0 & c=1 ): q=0 is following d=0 |
| 2 | 0 | 1 | 0 |  |  | 0 | 0 | 1 |  | 0 |  | 0 | 0 | 1 |  |  | 0 | 0 | 0 |  | 1 |  |  |  |  |  | 0 | state 0 with ( d=1 & r=0 ), 0 is trapped |
| 3 | 0 | 1 | 1 |  |  | 1 | 1 | 1 |  | 1 |  | 0 | 0 | 1 |  |  | 1 | 0 | 0 |  | 1 |  |  |  |  |  |  | q & p inconsistent |
| 4 | 1 | 0 | 0 |  |  | 0 | 0 | 0 |  | 1 |  | 1 | 1 | 1 |  |  | 0 | 0 | 1 |  | 0 |  |  |  |  |  | 1 | state 1 with (d =0 & c=0 ), 1 is trapped |
| 5 | 1 | 0 | 1 |  |  | 1 | 0 | 0 |  | 0 |  | 1 | 0 | 0 |  |  | 1 | 1 | 1 |  | 0 |  |  |  |  |  |  | q & p inconsistent |
| 6 | 1 | 1 | 0 |  |  | 0 | 0 | 1 |  | 1 |  | 1 | 1 | 1 |  |  | 0 | 0 | 0 |  | 1 |  |  |  |  |  | 1 | state 1 with (d =1 & c=0 ), 1 is trapped |
| 7 | 1 | 1 | 1 |  |  | 1 | 1 | 1 |  | 1 |  | 1 | 1 | 1 |  |  | 1 | 0 | 0 |  | 1 |  |  |  |  |  | 1 | state 1 with ( d=1 & c=1 ): q=1 is following d=1 |
