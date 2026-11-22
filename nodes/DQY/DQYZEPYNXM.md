---
tag: DQYZEPYNXM
kind: example
name: The 1896 proofs of the prime number theorem use complex analysis
msc: ["00A35", "11N05"]
topics: [Z2WNQ1DNTX]
audience: ug2
not_instance_of:
  - target: 84SZZBACP3
    note: the proofs study the zeta function as a function of a complex variable
uses: [0EHBY5Y84N, 1XWBY4N0VT, 0M3YQJ81NB, 28T3Z4VEHH, 84SZZBACP3]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_proof
    locator: Prime number theorem
  - url: https://en.wikipedia.org/wiki/Prime_number_theorem
    locator: lead section
---

## Example

The [[prime number theorem|0EHBY5Y84N]] states that
$$\frac{\pi(x) \log x}{x} \to 1 \quad \text{as } x \to \infty,$$
where $\pi(x)$ is the number of primes up to $x$.
Hadamard and de la Vallée Poussin proved it independently in 1896.
We list the main steps of this kind of proof and find the steps that are not [[elementary|84SZZBACP3]].

1. For real $s > 1$ the [[Riemann zeta function|1XWBY4N0VT]] is the series $\zeta(s) = \sum_{n \ge 1} n^{-s}$.
   This step uses only real series, so it is elementary.
2. The proof takes $s$ complex with $\operatorname{Re} s > 1$, and extends $\zeta$ by [[analytic continuation|0M3YQJ81NB]] to the line $\operatorname{Re} s = 1$, except at $s = 1$.
   This step uses [[complex analysis|28T3Z4VEHH]].
3. The proof shows that $\zeta(1 + i t) \ne 0$ for every real $t \ne 0$.
   A standard modern argument applies the identity
   $$3 + 4 \cos \theta + \cos 2\theta = 2(1 + \cos \theta)^2 \ge 0$$
   to $\log |\zeta|$ at complex points.
4. The proof passes from the zeros of $\zeta$ back to the primes, with a contour integral or a theorem about analytic functions.

Steps 2, 3 and 4 need functions of a complex variable, so the proof is not elementary in the sense of number theory.

Check of the identity in step 3: $2(1 + \cos \theta)^2 = 2 + 4 \cos \theta + 2 \cos^2 \theta$, and $2 \cos^2 \theta = 1 + \cos 2\theta$.

## Remarks

The identity in step 3 is elementary by itself, but the step is not, since it applies the identity to values of $\zeta$ at complex points.
A proof is elementary only if every step is, so one step outside the list is enough.

The analytic proof is not a worse proof.
It is shorter than the elementary proofs, and the analytic method later grew into the main tool of analytic number theory.
In 1949 Selberg and Erdős published elementary proofs of the same theorem, which avoid steps 2 to 4 completely.

## Explanations

### L1 human

The prime number theorem says how quickly the primes thin out.
The first proofs, in 1896, used numbers of the form $a + bi$ with $i^2 = -1$.
They studied a function of such numbers, not only the primes.
So these proofs are not elementary.
Proofs without these numbers came more than fifty years later.

### L2 human

To show that a proof is not elementary, find one step whose tools are outside the allowed list.
The allowed list in number theory is the integers, the real numbers and real inequalities.
Step 2 extends $\zeta(s)$ to complex $s$, and analytic continuation is not on the list.
So the proof is not elementary, even though step 1 is.
This is how the word is used: a single advanced step decides, and the rest of the proof does not change the verdict.
