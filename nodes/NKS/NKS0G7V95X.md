---
tag: NKS0G7V95X
kind: proof
name: Proof of Friedberg–Muchnik theorem below C
proves: TA4T65ABCQ
sources:
  - wikipedia: en:61969687@r1369417176
    locator: Friedberg–Muchnik theorem, section Friedberg–Muchnik theorem below C > Proof
    note: adopted
    mention: wikipedia://en/61969687#Q227
    sections: [Proof]
---

## Proof

The requirements are still the same, with the same priority: $R_{0,A}\prec R_{0,B} \prec R_{1,A} \prec R_{1,B} \prec \cdots$.

In the original construction for the Friedberg–Muchnik theorem, if it were true that every time we add a witness via $A_{2n} := A_{2n-1} \cup \{w_{i,A}\}$, we also have $w_{i,A} \geq \min(C_{2n+2} \setminus C_{2n})$, then by the permitting lemma, $A \leq_T C$. Similarly for $B \leq_T C$. However, this is not true in general.

In order to bypass the difficulty, we define 3 types of witnesses, 2 types of injuries, and 1 type of permissive moves, that a requirement can have.

- Type 0 witness: $(w_{i,A, 0}, -, -)$. This tentatively witnesses $w_{i,A, 0} \not\in A$ and $TM_i^B(w_{i,A, 0}) \neq 0$.
- Type 1 witness: $(w_{i,A, 0}, w_{i,A, 1}, -)$. This tentatively witnesses $w_{i,A, 0} \not\in A$ and $TM_i^B(w_{i,A, 0}) \neq 0$, and $w_{i,A, 1} \not\in A$ and $TM_i^B(w_{i,A, 1}) = 0$.
- Type 2 witness: $(-,-,w_{i,A, 2})$. This tentatively witnesses $w_{i,A, 2} \in A$ and $TM_i^B(w_{i,A, 2}) = 0$.
- Type 0 injury: Because a prior requirement has made a permitted move, this requirement's witness has *possibly* been invalidated. The witness updates into a type 0 witness.
- Type 1 injury: Because of a previous update to $B$, or because the computation has finally halted, a type 0 witness has been invalidated, in that $TM_i^{B_{2n}}(w_{i,A, 0}) =0$. The witness updates into a type 1 witness.
- Permitted move: Because $w_{i,A,1} \geq \min(C_{2n+2} \setminus C_{2n})$, the type 1 witness updates into a type 2 witness.

At stage *2n*,

- We check if any type 1 witness is permitted to be moved into a type 2 witness.
  - If so, then let $i$ be the smallest $i$ such that $w_{i,A,1} \geq \min(C_{2n+1} \setminus C_{2n})$, and we perform the update: $$A_{2n+1} := A_{2n} \cup\{w_{i,A,1}\},\; w_{i,A} \leftarrow (-,-, w_{i,A,1})$$ and simultaneously incur type 0 injury on all $w_{i,B}, w_{i+1,B}, \dots$ by updating each to $$w_{j,B} \leftarrow (\min\{ r_{jk} : k \in \mathbb{N}, r_{jk} > \max(w_{j,B}, \phi_i^{B_{2n-1}}(w_{i,A}))\}, -, -)$$
- Otherwise, we check for all type 1 injuries.
  - For each $i\in 0:2n-1$, such that $w_{i,A}$ is a type 0 or type 1 witness,
    - Simulate $TM_i^{B_{2n-1}}(w_{i,A,0})$ for up to $2n-1$ steps.
    - If $TM_i^{B_{2n-1}}(w_{i,A,0})[2n-1] = 0$, then a type 1 injury has occurred. Update the witness to $$w_{i,A} \leftarrow (\min\{ r_{ik} : k \in \mathbb{N}, r_{ik} > w_{i,A,0}\}, w_{i,A,0}, -)$$

Similarly for stage *(2n+1)*.

To show that the construction works, we need to show that each requirement's witness can only change state a finite number of times, by induction on the requirements.

By inductive hypothesis, since $R_{0,A}, R_{0,B}, \dots, R_{n,A}, R_{n,B}$ would only change their witnesses a finite number of times, $R_{n+1,A}$ can only be type-0 injured a finite number of times. Consequently, the only way $R_{n+1,A}$ can change its witness is if it is type-1 injured an infinite number of times. Suppose this is the case, then its witness will eventually settle into an infinite process of being repeatedly type-1 injured, never permitted to move into a type 2 witness.

Suppose this is the case, then let $f(k)$ be $w_{n+1,A,1}$ at stage *2k*. By construction, $f(k)$ is a function that is computable, non-decreasing, and because the witness is injured infinitely many times, $\lim_k f(k) = \infty$. By assumption, this witness will eventually be stuck forever as a type 1 witness, never permitted to move, so

$$f(k) < \min(C_{2k+2} \setminus C_{2k})$$

for all large enough *k*. However, if this is the case, then $C$ is decidable, contradicting the original assumption that $C$ is enumerable but undecidable.
