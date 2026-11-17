---
tag: 1X5X03DYTA
kind: example
name: Modus ponens in the alpha graphs
msc: ["03B05", "03-03"]
topics: [H8QZY0RZXZ]
audience: ug1
instance_of: [D3ZS6WHPM1]
uses: [D3ZS6WHPM1, 0Y0MQYST0M, 09K9MWD2QQ]
sources:
  - url: https://en.wikipedia.org/wiki/Existential_graph
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Modus_ponens
    locator: lead section
---

## Example

In the alpha part of the [[existential graphs|D3ZS6WHPM1]] we write a cut as a pair of square brackets and graphs side by side as a conjunction.
The premises of [[modus ponens|0Y0MQYST0M]] are $P$ and $P \to Q$.
The graph of $P \to Q$ is the scroll $[P \ [Q]]$, which reads $\neg(P \land \neg Q)$.
So we start with the graph
$$P \ [P \ [Q]]$$
on the sheet of assertion, and we derive $Q$.

1. The letter $P$ on the sheet has depth $0$. The cut $[P \ [Q]]$ lies on the sheet, so its inner area, of depth $1$, is nested inside the area of the outer $P$.
2. The inner $P$ is a copy of the outer $P$ in an area nested inside the area of the outer $P$. So it could have been drawn by iteration, and the deiteration rule allows us to erase it. The result is $P \ [[Q]]$.
3. The two cuts around $Q$ have nothing between them. The double cut rule removes them. The result is $P \ Q$.
4. The letter $P$ lies on the sheet, an area of depth $0$, which is even. The erasure rule allows us to erase it. The result is $Q$.
5. We check each step by the translation into [[propositional logic|09K9MWD2QQ]]. Step 2 replaces $P \land \neg(P \land \neg Q)$ by $P \land \neg\neg Q$; both are equivalent, since $P$ is true wherever the conjunction is.
6. Step 3 replaces $P \land \neg\neg Q$ by $P \land Q$, an equivalence. Step 4 replaces $P \land Q$ by $Q$, which $P \land Q$ implies.

So the graph $Q$ follows from the premises, and the derivation is an instance of the rules of the alpha system.

## Remarks

The example shows the three typical steps of an alpha proof: deiteration uses a premise inside a cut, the double cut removes a double negation, and erasure drops what is no longer needed.
The order matters: before step 2, the double cut rule does not apply, because $P$ lies between the two cuts.
Modus tollens works in the same way.
From $[Q]$ and $[P \ [Q]]$, deiteration erases the inner cut $[Q]$, which is a copy of the $[Q]$ on the sheet, and leaves $[Q] \ [P]$.
Erasure of $[Q]$ from the sheet leaves $[P]$, which reads $\neg P$.

## Explanations

### L1 human

We have two facts on our sheet: "$P$" and "if $P$, then $Q$".
In the graph, "if $P$ then $Q$" is a big loop containing $P$ and a small loop around $Q$.
Since $P$ is already on the sheet, the copy of $P$ inside the big loop adds nothing, and we may erase it.
Then $Q$ sits inside two loops with nothing between them, and two loops cancel like a double "not".
Now $P$ and $Q$ are both on the sheet, and we may erase $P$, which leaves $Q$.

### L2 human

We derive the same conclusion from the premises in the other order, to see that position on the sheet does not matter.

1. Start with $[P \ [Q]] \ P$. Side by side placement has no order, so this is the same graph as before.
2. Deiterate the inner $P$, which is a copy of the $P$ on the sheet: $[[Q]] \ P$.
3. Remove the double cut: $Q \ P$.
4. Erase $P$ on the sheet: $Q$.

The typical use of the example is to learn to see a premise inside a cut as removable when a copy stands outside.
The trap is to erase the outer $P$ first: erasure allows this, but then the inner $P$ can no longer be removed, and $Q$ cannot be reached.
