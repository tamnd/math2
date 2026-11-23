---
tag: DXG8B0NGHC
kind: example
name: The syllogism Darii in the beta graphs
msc: ["03B10", "03-03"]
topics: [H8QZY0RZXZ]
audience: ug1
instance_of: [D3ZS6WHPM1]
uses: [D3ZS6WHPM1, MZBNX2T6Q6, 086QKPF0A6, 0GHS47PDAQ, 0MSRQHCNN9]
sources:
  - url: https://en.wikipedia.org/wiki/Existential_graph
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Syllogism
    locator: lead section
---

## Example

Darii is the syllogism "all $M$ are $P$, some $S$ is $M$, so some $S$ is $P$".
An instance: every multiple of $4$ is even, some square is a multiple of $4$, so some square is even.
We draw the premises as beta [[existential graphs|D3ZS6WHPM1]] and derive the conclusion with the rules of the system.
In text a cut is a pair of square brackets, and a line of identity between two predicate spots is a hyphen, so $S{-}M$ is one line with $S$ at one end and $M$ at the other.

The premise "some $S$ is $M$" is the graph $S{-}M$ on the sheet, which reads $\exists x\,(S(x) \land M(x))$.
The premise "all $M$ are $P$" is the graph $[\,M{-}[P]\,]$, a line in an outer cut that runs from $M$ into an inner cut to $P$.
Its outermost part lies at depth $1$, so it reads $\neg \exists y\,(M(y) \land \neg P(y))$, that is, $\forall y\,(M(y) \to P(y))$.

1. Iteration lets a line of identity be extended from its area into a cut enclosed by that area, so we extend the line $S{-}M$ into the outer cut of the second premise.
2. The end of the extended line and the line at $M$ now both lie in the area of the outer cut, of depth $1$, which is negative.
   Insertion is allowed in a negative area, so we join the two lines there.
   The graph now reads $\exists x\,(S(x) \land M(x) \land \neg(M(x) \land \neg P(x)))$.
3. Inside the outer cut, the spot $M$ on the joined line is a copy of the spot $M$ on the same line on the sheet, so deiteration erases it.
   The graph now reads $\exists x\,(S(x) \land M(x) \land \neg\neg P(x))$.
4. Between the outer and the inner cut there is now only the line of identity, which passes through both cuts, so the double cut rule removes the two cuts.
   The graph now reads $\exists x\,(S(x) \land M(x) \land P(x))$.
5. The spot $M$ lies on the sheet, an area of even depth, so erasure removes it and keeps the line.
   The result is $S{-}P$, which reads $\exists x\,(S(x) \land P(x))$, "some $S$ is $P$".

Each step keeps truth.
Steps 1 and 2 apply the universal premise to the object $x$ of the existential premise, as in [[predicate logic|086QKPF0A6]].
Step 3 uses that $M(x)$ is already known, step 4 removes a double negation, and step 5 drops a conjunct.

## Remarks

Beta graphs do the work of [[syllogistic|MZBNX2T6Q6]] by sharing the middle term along one line and then erasing it.
Joining the lines in step 2 is where the two premises meet, so it plays the role of the middle term.

The same method derives Barbara, with all lines inside cuts, and every other mood that is valid in the modern reading.
Darapti, "all $M$ are $P$, all $M$ are $S$, so some $S$ is $P$", cannot be derived.
Its premises are true when $M$ is empty and its conclusion can then be false, and the beta rules are sound.
In the graphs, both premises are lines inside cuts, and no line on the sheet carries $M$ for the universal premises to act on.

## Explanations

### L1 human

The fact "some square is a multiple of $4$" is drawn as one line, with "square" at one end and "multiple of $4$" at the other.
The line stands for one object that has both properties, for example the number $16$.
The fact "every multiple of $4$ is even" is drawn inside loops, because it says "there is no multiple of $4$ that is not even".
The proof pulls the line of the object $16$ into the loops, uses the rule there, and gets "$16$ is even".
At the end the line has "square" at one end and "even" at the other: some square is even.

### L2 human

We read the graph after each step for the instance with $S$ the squares, $M$ the multiples of $4$ and $P$ the even numbers.

1. Start: there is a square that is a multiple of $4$, and there is no multiple of $4$ that is not even.
2. After joining: there is a square $x$ that is a multiple of $4$, and it is not true that $x$ is a multiple of $4$ and not even.
3. After deiteration: there is a square $x$ that is a multiple of $4$, and it is not true that $x$ is not even.
4. After the double cut: there is a square $x$ that is a multiple of $4$ and even.
5. After erasure: there is a square that is even.

Joining lines is how a universal statement gets applied to a particular object.
The trap is to join lines in the wrong direction: a line inside a cut may not be pulled out onto the sheet, because that would turn "for all" into "there is".
