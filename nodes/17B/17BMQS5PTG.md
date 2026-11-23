---
tag: 17BMQS5PTG
kind: example
name: The computer-assisted proof of the four color theorem
aliases: [appel-haken-proof, the-computer-assisted-proof-of-the-four-colour-theorem]
msc: ["05C15", "00A35"]
topics: [1BTHSHST4M]
audience: research
instance_of: [MC18C7BMFT]
uses: [MC18C7BMFT, 0M406JC8J1, JGRCNPKNGG, 029JQEK15B]
sources:
  - url: https://en.wikipedia.org/wiki/Four_color_theorem
    locator: History
  - url: https://en.wikipedia.org/wiki/Four_color_theorem
    locator: Summary of proof ideas
  - url: https://en.wikipedia.org/wiki/Computer-assisted_proof
    locator: Theorems proved with the help of computer programs
---

## Example

The [[four color theorem|0M406JC8J1]] says that the vertices of every finite loopless [[planar graph|029JQEK15B]] can be colored with four colors so that adjacent vertices get different colors.
Kenneth Appel and Wolfgang Haken announced a proof in 1976, and they published it in 1977 in the *Illinois Journal of Mathematics*, in two parts.
We check that the proof is a [[computer-assisted proof|MC18C7BMFT]], and then we follow how mathematicians came to accept it.

1. The first written reduction. The proof studies a [[minimal counterexample|JGRCNPKNGG]], a planar graph that needs five colors and has as few vertices as possible. A written argument, called discharging, shows that such a graph must contain at least one configuration from a fixed finite list. A list with this property is called an unavoidable set.
2. The second written reduction. A configuration is called reducible when it cannot occur in a minimal counterexample. The reason is that a four-coloring of the smaller graph without the configuration would extend to the whole graph.
3. The computer part. A program showed that each configuration of the unavoidable set is reducible. The set had more than a thousand configurations, and the checks took over a thousand hours of computer time.
4. The conclusion. By step 1 a minimal counterexample must contain a configuration from the list, and by step 3 it cannot contain one. So no counterexample exists.
5. Steps 1 and 2 are written proofs, and step 3 is a computation that no person could repeat by hand, so the proof is computer-assisted.

## Remarks

Acceptance took two decades and came in stages.
At first many mathematicians doubted a proof that no person could read in full, and the doubt was about the method as much as about this proof.

The written part had errors too.
In 1981 Ulrich Schmidt checked part of the discharging argument in his master's thesis and found an error in it.
Appel and Haken corrected this error, and others that readers had found, in their 1989 book *Every Planar Map is Four Colorable*.

Neil Robertson, Daniel Sanders, Paul Seymour and Robin Thomas announced a new proof in 1996 and published it in 1997.
It follows the same plan with an unavoidable set of $633$ configurations and with its own programs.
In 2005 Georges Gonthier, with Benjamin Werner, checked a proof in the Coq proof assistant.
After that check, a reader must trust only the small kernel of Coq and the formal statement of the theorem.

So a computer-assisted proof is accepted the way other proofs are: other people check it, over time, by independent means.
The example also shows that the written part of such a proof can fail, and that the program is not the only source of doubt.
Alfred Kempe's incorrect proof of 1879 belongs to the history of the same theorem, and [[famous incorrect proofs|1CV4HTA6C8]] tells it.

## Explanations

### L1 human

The four color theorem says that four colors are enough for any map, if neighboring countries must get different colors.
Appel and Haken proved it in 1976.
They showed that every map, however large, contains one of more than a thousand small patterns.
Then a computer showed that none of these patterns can appear in a smallest map that needs five colors.
No person could check the computer's work by hand, so many mathematicians felt uneasy.
Over the next thirty years others found and fixed small errors, wrote a new and simpler proof, and finally had the whole proof checked by a proof-checking program.

### L2 human

We follow the logic of the proof as a [[proof by contradiction|0J0XBKG64S]].

1. Assume that some planar graph needs five colors.
2. Among all such graphs, choose one with the fewest vertices, and call it $G$.
3. By the unavoidability theorem, $G$ contains a configuration $C$ from the list.
4. The program has checked that $C$ is reducible. We delete or contract part of $C$ and get a smaller planar graph $G'$, which has a four-coloring by the choice of $G$.
5. Reducibility means that this four-coloring of $G'$ can be changed and extended to all of $G$. So $G$ has a four-coloring, which contradicts step 1.

The smallest case of step 5 shows the idea.
If $G$ had a vertex $v$ with at most three neighbors, we would delete $v$, four-color the rest, and give $v$ a color that its at most three neighbors do not use.
So a vertex of degree at most $3$ is a reducible configuration, and the program handles hundreds of larger ones in the same spirit.

The typical use of this pattern is a theorem whose minimal counterexample is forced to contain one of many small structures.
Watch out for the idea that the computer proved the theorem alone.
Steps 2, 3 and 5 rest on written arguments, and the error that Schmidt found was in the written part behind step 3.
