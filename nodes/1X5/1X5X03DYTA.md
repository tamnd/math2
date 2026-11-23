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

In the alpha [[existential graphs|D3ZS6WHPM1]] we write a cut as a pair of square brackets, and graphs side by side assert a conjunction.
The premises of [[modus ponens|0Y0MQYST0M]] are $P$ and $P \to Q$, and the graph of $P \to Q$ is the scroll $[P \ [Q]]$, which reads $\neg(P \land \neg Q)$.
So we start with the graph
$$P \ [P \ [Q]]$$
on the sheet of assertion, and we derive $Q$.

1. The outer $P$ lies on the sheet, at depth $0$, and the cut $[P \ [Q]]$ lies on the sheet too, so the area inside the cut, of depth $1$, is enclosed by the area of the outer $P$.
2. The inner $P$ is a copy of the outer $P$ in an enclosed area, so it could have been drawn by iteration, and deiteration erases it.
   The result is $P \ [[Q]]$.
3. The two cuts around $Q$ have nothing between them, so the double cut rule removes them.
   The result is $P \ Q$.
4. The letter $P$ lies on the sheet, an area of even depth, so erasure removes it.
   The result is $Q$.
5. We check the steps in [[propositional logic|09K9MWD2QQ]].
   Step 2 replaces $P \land \neg(P \land \neg Q)$ by $P \land \neg\neg Q$, an equivalence, since $P$ is true wherever either conjunction is.
6. Step 3 replaces $P \land \neg\neg Q$ by $P \land Q$, an equivalence, and step 4 replaces $P \land Q$ by $Q$, which it implies.

So $Q$ follows from the premises by the rules of the alpha system.

## Remarks

The three steps are typical of alpha proofs: deiteration uses a premise inside a cut, the double cut removes a double negation, and erasure drops what is no longer needed.
The order matters, because before step 2 the double cut rule does not apply: $P$ lies between the two cuts.

Modus tollens works the same way.
From $[Q]$ and $[P \ [Q]]$, deiteration erases the inner $[Q]$, a copy of the $[Q]$ on the sheet, and leaves $[Q] \ [P]$.
Erasing $[Q]$ from the sheet leaves $[P]$, which reads $\neg P$.

## Explanations

### L1 human

We have two facts on our sheet: "$P$" and "if $P$, then $Q$".
In the graph, "if $P$ then $Q$" is a big loop containing $P$ and a small loop around $Q$.
Since $P$ is already on the sheet, the copy of $P$ inside the big loop adds nothing, and we may erase it.
Then $Q$ sits inside two loops with nothing between them, and two loops cancel like a double "not".
Now $P$ and $Q$ are both on the sheet, and we may erase $P$, which leaves $Q$.

### L2 human

We derive the same conclusion with the premises in the other order, to see that position on the sheet does not matter.

1. Start with $[P \ [Q]] \ P$, the same graph as before, since side by side placement has no order.
2. Deiterate the inner $P$, a copy of the $P$ on the sheet: $[[Q]] \ P$.
3. Remove the double cut: $Q \ P$.
4. Erase $P$ on the sheet: $Q$.

A premise inside a cut can be removed whenever a copy of it stands outside.
The trap is to erase the outer $P$ first: erasure allows it, but then the inner $P$ can no longer be removed, and $Q$ is out of reach.
