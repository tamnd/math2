---
tag: 84SZZBACP3
kind: concept
name: Elementary proof
aliases: [elementary-methods, elementary-argument]
msc: ["00A35", "11A41"]
topics: [Z2WNQ1DNTX]
audience: ug2
uses: [0B94TKFQJX, 0EHBY5Y84N, 28T3Z4VEHH, 1XWBY4N0VT]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_proof
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Elementary_proof
    locator: Prime number theorem
  - url: https://en.wikipedia.org/wiki/Elementary_proof
    locator: Friedman's conjecture
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: Philosophy of mathematics
---

## Summary

An elementary proof is a proof that stays inside a short list of basic tools, and the word says nothing about how easy the proof is.
You meet it in sentences such as "Selberg and Erdős gave an elementary proof of the prime number theorem": their proofs are long and hard, but they use no [[complex analysis|28T3Z4VEHH]].

An *elementary proof* is a [[proof|0B94TKFQJX]] that uses only the tools of an agreed basic list.
The list depends on the field.
In number theory the list is fixed by custom: the arithmetic of the integers, the real numbers, real inequalities, real logarithms and limits of real sequences are allowed, and functions of a complex variable are not.
So "elementary" describes the tools of a proof, not its length or its difficulty.

## Motivation

A theorem about whole numbers can have a proof that leaves the whole numbers far behind.
The first proofs of the [[prime number theorem|0EHBY5Y84N]] study the [[Riemann zeta function|1XWBY4N0VT]] as a function of a complex variable.
So mathematicians asked a real question: does the theorem need complex analysis, or only the proof that they knew?
An elementary proof answers such a question, because it shows that the theorem can be reached without the advanced tool.

Elementary proofs matter for other reasons too.
They often bring new methods, as Selberg's formula did for prime number theory.
They can also be formalized in weak logical systems, which lets logicians measure how much a theorem really needs.
The page on [[elegant and deep|STHWD1K9AN]] results returns to this, since a result is called deep when no elementary proof is known.

## Notation

No symbol marks an elementary proof.
Authors write "an elementary proof", "by elementary means", "elementary methods" or "an elementary argument".
The word has two readings that look the same in print.
In the technical reading, "an elementary proof of the prime number theorem" means a proof without complex analysis, and it may run to many pages.
In the everyday reading, "an elementary exercise" or "this follows by elementary manipulations" means that the step is short and routine.
To tell which one an author means, ask whether a hard theorem is named: "an elementary proof of" a famous result is the technical reading, and "elementary" before "exercise", "computation" or "estimate" is the everyday one.

The word also appears in unrelated names, such as elementary function, elementary matrix and elementary embedding, and [[elementary number theory|7XZ94HTPQT]] is a field of study, not a kind of proof.

## Remarks

### Reading the tools of a proof

Take [[Euclid's proof that there are infinitely many primes|VF1QJPSDG5]].
From a finite list $p_1, \dots, p_k$ of primes it forms
$$N = p_1 p_2 \cdots p_k + 1,$$
and a prime factor of $N$ is outside the list, because each $p_i$ leaves remainder $1$.
Check: for the list $2, 3, 5$ we get $N = 31$, which is a new prime.
Every tool here is a product, a remainder or a prime factor, so the proof is elementary in every sense of the word.

Euler proved the same theorem in another way: the series $\sum_p 1/p$ over all primes diverges, so there must be infinitely many terms.
That proof uses infinite series and logarithms.
It is still elementary in the number theorist's sense, since all its tools are real, but it is further from the integers.
So one theorem can have proofs at several levels, and "elementary" is a property of a proof, not of a theorem.

### Elementary is not easy

[[Erdős's proof of Bertrand's postulate|9DEWZDTNCV]] shows that every interval $(n, 2n]$ contains a prime.
It works with the binomial coefficient $\binom{2n}{n}$ and with real inequalities only, and it still needs a careful estimate and a finite check of the cases $n \le 467$.

The elementary proofs of the prime number theorem go further.
They are longer and harder than the analytic proofs, which use the zeta function on the complex plane.
A reader who expects "elementary" to mean "short" will be surprised by them.
[[Mertens' theorems|7J3P1W042Y]] on sums over primes also have elementary proofs, built on [[Legendre's formula|01WPV9PHN7]] for the primes in $n!$.

### Proofs that are not elementary

[[The 1896 proofs of the prime number theorem use complex analysis|DQYZEPYNXM]]: they continue $\zeta(s)$ to complex $s$ and study its zeros there, and that step is outside the list.
Dirichlet's proof of [[Dirichlet's theorem on arithmetic progressions|0GNVN3CA2P]] is not elementary either, because it uses $L$-functions and analysis.
The proof of [[Fermat's last theorem|0Y5X3SDBCZ]] by Wiles uses elliptic curves and modular forms, far outside any basic list.
By contrast the cases $n = 3$ and $n = 4$ of that theorem have elementary proofs.

### Watch out

The first error is to read "elementary" as "easy".
A student who is told to "find an elementary proof" of a hard statement may think that a short trick must exist, but the request only restricts the tools.

The second error is to think that an elementary proof avoids analysis entirely.
In number theory, real logarithms, real integrals and limits are allowed, and only complex analysis is excluded.
Erdős's proof of Bertrand's postulate takes logarithms in its main estimate and is still elementary.

The third error is to confuse the field with the method.
A theorem of analytic number theory, such as the prime number theorem, can have an elementary proof, and a theorem of elementary number theory can have a proof that is not elementary.

### History

Hadamard and de la Vallée Poussin proved the prime number theorem independently in 1896, with complex analysis.
In a lecture of 1921, Hardy said that an elementary proof of the theorem seemed very unlikely, because some theorems lie deep.
In 1949 Atle Selberg and Paul Erdős published elementary proofs of the prime number theorem.
Erdős had given his elementary proof of Bertrand's postulate in 1932.
Harvey Friedman later conjectured that every theorem published in the *Annals of Mathematics* whose statement is arithmetical can be proved in [[elementary function arithmetic|2JD80TE553]].

### Try it

First, is the proof that $\sqrt{2}$ is irrational, by writing $\sqrt{2} = p/q$ in lowest terms and deriving that $p$ and $q$ are both even, an elementary proof?
Yes: it uses only divisibility of integers.

Second, a proof that every polynomial with complex coefficients has a complex root uses Liouville's theorem on bounded entire functions.
Is it elementary in the number theorist's sense?
No: Liouville's theorem is a result of complex analysis, so the proof uses a tool outside the list.

## Explanations

### L1 human

A proof is elementary when it uses only simple tools.
For whole numbers the simple tools are adding, multiplying, dividing and comparing sizes.
A proof that uses complex numbers or advanced calculus is not elementary.
An elementary proof can still be very long and hard.
"Elementary" tells you which tools the proof uses, not how easy it is.

### L2 human

Decide whether a proof is elementary by listing the tools of each step and comparing them with the allowed list.
For Euclid's proof the steps use products, the remainder of a division and the existence of a prime factor, and each of these is on the list.
Check on a longer list: from $2, 3, 5, 7, 11, 13$ we get
$$N = 30030 + 1 = 30031 = 59 \cdot 509,$$
and both prime factors are new.
So the proof is elementary.

Now take the 1896 proofs of the prime number theorem.
One step extends $\zeta(s)$ to complex numbers $s$ with real part $1$ and shows that $\zeta$ has no zero there.
That step is outside the list, so the whole proof is not elementary, even though most of its other steps are.
One step outside the list is enough, and this is how the word is used in practice.

### L3 human

In analytic number theory, the prime number theorem is closely tied to the fact that $\zeta(s)$ has no zeros on the line $\operatorname{Re} s = 1$.
Hardy expected that a statement about the zeros of an analytic function would need the theory of analytic functions.
Selberg's symmetry formula, an asymptotic formula for sums of $\log^2 p$ and of $\log p \log q$ over primes, gave a route that stays inside real analysis.

In logic the distinction becomes precise.
A proof is elementary in Friedman's sense when it can be carried out in elementary function arithmetic, a weak system with exponentiation and induction only for bounded formulas.
The question "how elementary can a proof be?" then becomes a question about which formal system proves the theorem, which is the subject of reverse mathematics and proof theory.
