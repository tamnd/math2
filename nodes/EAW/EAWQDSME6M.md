---
tag: EAWQDSME6M
kind: example
name: An inquiry-based unit on divisibility
msc: ["97D40", "97E50", "97F60"]
topics: [VHGA6J4NZK]
audience: ug1
instance_of: [WKM6535VHG]
uses: [WKM6535VHG, 0PG2H7WKGG, 0ED72CTBNP]
sources:
  - url: https://en.wikipedia.org/wiki/Moore_method
    locator: The original method
  - url: https://en.wikipedia.org/wiki/Inquiry-based_learning
    locator: Characteristics
---

## Example

A transition-to-proof course spends one week on [[divisibility|0PG2H7WKGG]] in the style of the [[Moore method|WKM6535VHG]].
The teacher gives one definition and five tasks, and the students work in groups of three between meetings.
The definition reads: for integers $a$ and $b$, we say that $a$ divides $b$, written $a \mid b$, if there is an integer $k$ with $b = ak$.
The five tasks, with the proofs a group might present, are these.

1. Prove that $a \mid a$ for every integer $a$.
   The proof is $a = a \cdot 1$.
2. Prove that if $a \mid b$ and $b \mid c$, then $a \mid c$.
   From $b = ak$ and $c = bm$ we get $c = a(km)$.
3. Prove that if $a \mid b$ and $a \mid c$, then $a \mid (b + c)$.
   From $b = ak$ and $c = am$ we get $b + c = a(k + m)$.
4. Prove or disprove the converse of task 3.
   A [[counterexample|0ED72CTBNP]] is $a = 2$, $b = c = 1$: we have $2 \mid (1 + 1)$, but $2 \nmid 1$.
5. Prove that if $a \mid b$, then $a \mid bc$ for every integer $c$.
   From $b = ak$ we get $bc = a(kc)$.

In class, one student from each group presents a task at the board, and the class checks each step against the definition.
The teacher gives no proofs, and the accepted results become tools for the next week's tasks on the greatest common divisor.

Now we check the features of the method.
The list exists, and its order lets each task use only the definition and earlier tasks.
The students produce the proofs.
The students present, and the class checks.
The teacher guides only by the choice and order of tasks.
So the unit is an instance of the method.

## Remarks

The unit differs from Moore's original course in two ways: the students work in groups, and they may read.
Both are typical of modern inquiry-based learning, and neither changes who produces the theory.
Task 4 does the most for the class, because it trains students to test a claim before they try to prove it.
If the teacher phrased it as "prove the converse", the class would hunt for a proof that does not exist, so the form "prove or disprove" is part of a good list.

## Explanations

### L1 human

The teacher tells the class what "$a$ divides $b$" means and gives a short list of statements.
The students prove the statements themselves, in small groups.
One statement is false, and the students must find numbers that show it.
In class, the students show their proofs, and the others check them.

### L2 human

To decide whether a unit follows the Moore method, check four things in order.
First, is there a list in which each task needs only the earlier ones?
Here the tasks use only the definition and, for task 5, nothing beyond it.
Second, do students produce the proofs, and third, do they present while the class checks?
Both hold here.
Fourth, does the teacher stay out of the proofs?
Here the teacher guides only by the list, so all four checks pass.
