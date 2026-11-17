---
tag: 40QATE3WJN
kind: example
name: The proof of the Kepler conjecture and its formal verification
aliases: [flyspeck-project]
msc: ["52C17", "00A35"]
topics: [1BTHSHST4M]
audience: research
instance_of: [MC18C7BMFT]
uses: [MC18C7BMFT, AFMBQT06ZV, HF32CBN5MA, VNMXB0J2KA]
sources:
  - url: https://en.wikipedia.org/wiki/Kepler_conjecture
    locator: Hales' proof
  - url: https://en.wikipedia.org/wiki/Kepler_conjecture
    locator: A formal proof
---

## Example

The [[Kepler conjecture|AFMBQT06ZV]] says that no [[packing|HF32CBN5MA]] of equal balls in space has a density greater than $\pi/\sqrt{18} \approx 0.7405$, the density of the usual stacking of oranges.
Johannes Kepler stated it in 1611.
Thomas Hales proved it with a large computation, and the proof was accepted only after a formal verification.
We check that the proof is a [[computer-assisted proof|MC18C7BMFT]], and we follow its acceptance.

1. A human reduction. Hales reduced the problem to a statement about finitely many local configurations of balls. The written argument shows that a packing with a higher density would give a configuration that violates one of a finite set of inequalities.
2. The computer part. From 1992 Hales, with his graduate student Samuel Ferguson, checked these inequalities by computer. The work applied [[linear programming|VNMXB0J2KA]] to more than $5000$ configurations and solved about $100000$ linear programs.
3. The size. When Hales announced the proof in August 1998, it consisted of about $250$ pages of notes and about $3$ gigabytes of programs, data and results.
4. The condition of a computer-assisted proof holds: step 1 is a written proof, and the computations of step 2 are far beyond a check by hand.

## Remarks

The acceptance of the proof went through these stages.

1. The Annals of Mathematics agreed to publish the proof if a panel of twelve referees accepted it.
2. In 2003 the head of the panel, Gábor Fejes Tóth, reported that the referees were "99% certain" of the proof. They could not certify all of the computer calculations.
3. The Annals published Hales's article on the part of the proof without computer work in 2005. The journal Discrete and Computational Geometry published the computational parts, by Hales and Ferguson, in 2006.
4. In January 2003 Hales announced the Flyspeck project. Its aim was a complete formal proof that would remove the remaining doubt.
5. The Flyspeck project announced the completion of the formal proof on 10 August 2014. The proof was checked with the proof assistants HOL Light and Isabelle.
6. The paper on the formal proof, with Hales and many collaborators as authors, was accepted by the journal Forum of Mathematics, Pi in 2017.

The example shows the limit of traditional refereeing.
Twelve expert referees worked for years and still could not reach full certainty, because the proof was too large for them.
The formal proof changed the situation: after it, a reader must trust the kernels of the proof assistants and the formal statement, and not the many programs of 1998.

## Explanations

### L1 human

Grocers stack oranges in layers, each orange in a dip of the layer below, and this fills about $74\%$ of the space.
Kepler guessed in 1611 that no arrangement of equal balls fills more.
Thomas Hales announced a proof in 1998, with the help of a computer that checked thousands of cases.
The referees of the journal worked for years, and in the end they were "99% certain" that the proof was right.
To remove the last doubt, Hales led a team that wrote the whole proof in a form that a proof-checking program could check.
This took more than ten years and was finished in 2014.

### L2 human

We read the stages of the proof as answers to the question "what must a reader trust?".

1. Before 2003, a reader had to trust the written argument, the programs of Hales and Ferguson, and the machines that ran them.
2. After the referee report of 2003, the written argument was checked by experts, but the programs were checked only in part.
3. After the formal proof of 2014, the written argument and the computations were both checked by HOL Light and Isabelle.
4. So a reader now has to trust the small kernels of these proof assistants and the formal statement of the theorem.

The typical use of this pattern is a proof whose size exceeds what referees can check, so that a machine check becomes a part of acceptance.
A trap is to think that the formal proof copies the proof of 1998 line by line.
In 2012 Hales published a blueprint that rewrote the proof in a form suited to formalization, and the formal proof follows the blueprint.
