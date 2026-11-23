---
tag: 8JQHJK94RZ
kind: concept
name: Writing proofs
aliases: [writing-mathematical-proofs, proof-writing]
msc: ["00A35", "97E50"]
topics: [STSM6PR7TX]
audience: ug1
uses: [0B94TKFQJX, S9MHMRAX88]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_proof
    locator: Nature and purpose
  - url: https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style/Mathematics
    locator: Writing style in mathematics
  - book: isbn:9781108439534
    locator: Chapter 3
---

## Summary

A written proof is a message to a reader who has only the page and who wants to check every step.
Writing a proof means turning an argument that you believe into a text that such a reader can check, one sentence at a time.

Here is one argument written twice.
The claim is that the sum of two odd integers is even.
The first version is a string of symbols:

> $m = 2a+1,\ n = 2b+1 \Rightarrow m + n = 2a + 2b + 2 = 2(a + b + 1)$, $\therefore$ even.

Each symbol is correct, but the reader must guess what $m$, $n$, $a$ and $b$ are, where the two equations come from, and which number the word "even" describes.
The second version says all of this in sentences:

> Let $m$ and $n$ be odd integers.
> By the definition of an odd integer, there are integers $a$ and $b$ with $m = 2a + 1$ and $n = 2b + 1$.
> Adding the two equations gives $m + n = 2a + 2b + 2 = 2(a + b + 1)$.
> The number $a + b + 1$ is an integer, so $m + n$ is even.
> $\square$

The second text has the same mathematics and about twice the length, and a reader can check each line without help.

In general, a written [[proof|0B94TKFQJX]] states its claim with every hypothesis, introduces each letter with its type, gives a reason for each step that the reader cannot check at a glance, and uses full sentences with the formulas inside them.
It tells the reader its plan when the argument is long, and it ends with the conclusion in the words of the claim.
All of this is measured against a stated reader: a step that one reader can supply is a gap for another.

## Motivation

A student often finds a correct idea and still loses most of the marks.
The answer on the page is a column of formulas, and it does not say what is assumed, why each line follows, or what the last line shows.
The grader cannot check it, so the grader cannot accept it.
A referee of a research paper is in the same position when the main step is missing.

There is a second reason, and it is more important.
Writing the reasons down is the moment when you find out whether you have them.
A false step can hide inside a line of symbols, but it is hard to hide inside a sentence that says "by the definition of an odd integer".
So good writing does not make a wrong proof right, but it makes the wrong step visible to the writer first.

The later pages of the sub-area take the method apart.
[[Scratch work and the final proof|E97XXFW9MV]] separates the search from the text, [[proof strategies by logical form|872K5XB580]] gives the first and last sentence of each part, and [[the language of proofs|GKMRQCA8CW]] gives the words that carry the logic.

## Notation

A proof has little notation of its own.
Most books start it with the word "Proof." in italics and end it with a mark such as $\square$, $\blacksquare$ or the letters Q.E.D., as the page on [[end of proof marks|ET9J6R9T5C]] explains.
Short forms such as "WLOG" and "iff" are common in lectures and less common in print; the page on [[mathematical abbreviations|4ZNYMYRRY3]] lists them.
Many style guides advise you to write "so", "therefore" and "for all" in words in running text, and to keep $\Rightarrow$, $\therefore$ and $\forall$ for formulas and logic courses.

## Remarks

### The steps of the method

The method is a short routine, and each step answers a question that the reader would ask.

1. State what is proved.
   Write the full [[statement|S9MHMRAX88]], with its [[hypotheses and its conclusion|W48XN2MEM9]].
2. Choose the reader.
   Decide what the reader knows, and so which facts you prove and which facts you quote.
3. Say what you assume and what you will show.
   For a [[direct proof|0NTF6DMVAP]] write "Suppose that ..."; for a [[proof by contradiction|0J0XBKG64S]] write "Suppose, for a contradiction, that ...".
4. Introduce each letter once, with its type.
   Write "Let $n$ be an integer" or "there is an integer $k$ with $n = 2k$".
5. Give a reason for each step that the reader cannot check at a glance.
   The reason is a hypothesis, a definition, an earlier result or a rule of logic.
6. Write sentences.
   A formula is a part of a sentence, and a displayed formula ends with a comma or a full stop.
7. Guide the reader.
   Before a long argument, give its plan: "We prove the two inclusions" or "We split into two cases".
8. End with the conclusion in the words of the statement.
9. Read the text again as the chosen reader, and repair each step that this reader cannot check.

### Why the rules are there

Each rule protects the reader from one kind of guess.
Without the statement, the reader does not know what the last line should be.
Without the types, the reader cannot tell whether $k$ is an integer or a real number, and the definition of "even" needs an integer.
Without reasons, the reader cannot tell a deduction from a hope.

Sentences matter because the small words carry the logic.
"Suppose", "so", "for some" and "for every" say which lines are assumed, which are derived, and how each letter is chosen.
A line of symbols drops these words, and the reader must put them back.
The [[language of proofs|GKMRQCA8CW]] treats these words one by one.

### Three proofs to study

The first is [[a written proof that the product of two odd integers is odd|B48X7ZWD5W]].
It has six sentences, and each one does one job: assume, unpack, compute, name the new integer, conclude.

The second is [[one proof written for two readers|7FW2WDYPVR]].
The claim is that $n^2 - n$ is even for every integer $n$.
For a first-year course the proof treats even and odd $n$ in two cases, and for an expert it is one sentence about consecutive integers.
Both are correct, and each fits its reader.

The third is a proof of a set equality by [[double inclusion|MKHVRNW68H]].
It opens with "We show $A \subseteq B$ and $B \subseteq A$", and from that sentence on the reader knows the shape of the rest.

### What is not a written proof

[[A bare computation|4HSYD7GD6V]] such as the two lines "$(x - 2)(x - 3) < 0$" and "$x \in (2, 3)$" has a true outline, but it states no claim and gives no reason for its main step, which is an argument about signs.
A text that starts "Assume $x > 0$" for the claim "for every real $x$, $x^2 \ge 0$" proves only a part of the claim, because the writer has changed the claim.
A text that writes "$m = 2k$ and $n = 2k$" for two even numbers uses [[one letter for two numbers|FDT6332G8D]], and so it proves the claim only when $m = n$.

### Where authors disagree

The writers of advice agree on the main points: state the claim, know the reader, give reasons, and write sentences.
They differ on details, and you should treat their rules as advice.
Most mathematical texts use "we" even with one author, and they read it as "the writer and the reader together".
Some writers prefer "I" in a paper with one author, because "we" can hide who made a choice.
Some style guides ask for words in place of $\forall$, $\exists$ and $\Rightarrow$ in running text, and others accept the symbols in short formulas.
The knowledge base uses "we", and words in running text.

### Watch out

The most common slip is to reuse a letter.
A student proving that $a \mid b$ and $a \mid c$ imply $a \mid b + c$ writes $b = ak$ and $c = ak$.
With $a = 3$, $b = 6$ and $c = 15$ there is no single $k$, since $6 = 3 \cdot 2$ and $15 = 3 \cdot 5$.
The text has proved only the case $b = c$; the repair is two letters, $b = as$ and $c = at$.

A second slip is to check cases and call it a proof.
Checking $n = 1, 2, 3$ supports a claim about every integer $n$, but it proves nothing about $n = 4$.

### History

[[Euclid's Elements|83WHDAV68J]], written around 300 BC, gives each proposition as a statement followed by a proof that ends by repeating what was to be shown.
Paul Halmos wrote the essay "How to Write Mathematics" in 1970.
Donald Knuth, Tracy Larrabee and Paul Roberts published "Mathematical Writing" in 1989.
Leslie Lamport proposed structured proofs in "How to Write a Proof" in 1995.
Transition courses, with books such as Velleman's "How to Prove It", now teach the writing of proofs together with their logic.

### Try it

Rewrite "$n$ even $\Rightarrow n = 2k \Rightarrow n^2 = 4k^2$ even" as a proof in sentences.
One answer reads as follows.

> Let $n$ be an even integer.
> Then $n = 2k$ for some integer $k$, so $n^2 = 4k^2 = 2(2k^2)$.
> Since $2k^2$ is an integer, $n^2$ is even.

A student proves that $x^2 \ge 0$ for every real $x$ with the text "Let $x = 2$, so $x^2 = 4 \ge 0$"; which rule fails?
The first rule fails: the text proves the claim for one number, not for every real number.

## Explanations

### L1 human

A proof is like a letter to someone who wants to check your claim.
That person cannot ask you what a line means, so the letter must say everything.
First you say what you claim.
Then you give each step and its reason, in sentences, such as "$6 = 2 \times 3$, so $6$ is even".
At the end you say that the claim is shown.
A good test is to give your proof to a friend in your class and ask whether every line can be checked.

### L2 human

We write a proof that if $a$ divides $b$ and $a$ divides $c$, then $a$ divides $b + c$, for integers $a$, $b$ and $c$.
The claim first, with its hypothesis and conclusion:
"Let $a$, $b$ and $c$ be integers with $a \mid b$ and $a \mid c$."
Next we unpack the hypothesis with the definition of [[divisibility|0PG2H7WKGG]], and we use two letters, because the two quotients can differ:
"There are integers $s$ and $t$ with $b = as$ and $c = at$."
Then we compute inside a sentence:
$$b + c = as + at = a(s + t).$$
The last sentence names the type and concludes: "Since $s + t$ is an integer, $a \mid b + c$."

Check: for $a = 3$, $b = 6$ and $c = 15$ we get $s = 2$, $t = 5$ and $b + c = 21 = 3 \cdot 7$.
The same four moves (assume, unpack, compute, conclude) write most of the proofs about parity and divisibility in a first course.

### L3 human

Writing a proof is a translation from a private argument to a public text, and the reader fixes the target language.
At one end of the scale is the formal derivation of [[natural deduction|6KT3BJZ7D1]] or of a proof assistant, where each step is an instance of a rule and a machine checks it, as in [[proof assistants and their design|YM6PRDE88V]].
At the other end is the research paper, whose proofs leave out every step that an expert can supply.
The rules of the method are the common part: an explicit claim, explicit hypotheses, a reason for each step, and a stated end.

The [[structured proofs|H2W8D7BMSW]] of Lamport bring the tree of a formal proof into human writing, and [[level of detail in proofs|VYGBV5D8Y4]] studies where on the scale a given text should sit.
The [[structure of a mathematical paper|XZHACQ74C0]] applies the same ideas to a whole paper, and the study of how students learn to read and write proofs belongs to [[teaching reasoning and proof|VHGA6J4NZK]].
