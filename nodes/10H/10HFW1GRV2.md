---
tag: 10HFW1GRV2
kind: statement
role: theorem
name: Doob's upcrossing inequality
msc: [60G42]
uses: [EQ055QMACW, HNK1Y62G7V, 0DCT0QZVQ1]
about: [6M852B4RA8]
sources:
  - url: https://en.wikipedia.org/wiki/Doob%27s_martingale_convergence_theorems
---

## Statement

Let $n \ge 1$, let $(X_k)_{0 \le k \le n}$ be a [[submartingale|EQ055QMACW]] with respect to a [[filtration|HNK1Y62G7V]] $(\mathcal{F}_k)_{0 \le k \le n}$, and let $a < b$ be real numbers.
Let $U_n[a, b]$ be the number of upcrossings of $[a, b]$ by $X_0, \dots, X_n$.
This is the largest $m \ge 0$ with times $0 \le s_1 < t_1 < \dots < s_m < t_m \le n$ such that $X_{s_i} \le a$ and $X_{t_i} \ge b$ for each $i$.
Then
$$(b - a)\, E\bigl[U_n[a, b]\bigr] \le E\bigl[(X_n - a)^+\bigr] - E\bigl[(X_0 - a)^+\bigr],$$
where $y^+ = \max(y, 0)$.

## Remarks

The proof uses a betting strategy: buy one unit when the process is at most $a$, and sell when it reaches at least $b$.
With $Y_k = (X_k - a)^+$, which is again a submartingale, each completed upcrossing earns at least $b - a$, so the gain is at least $(b - a) U_n[a, b]$.
The opposite strategy holds exactly when the first one does not.
It is predictable and bounded, so its expected gain on the submartingale $Y$ is non-negative.
The two gains add up to $Y_n - Y_0$.
As a consequence, if $\sup_n E[X_n^+] < \infty$, then the total number of upcrossings of every interval $[a, b]$ is finite almost surely.
This is the key step of [[Doob's martingale convergence theorems|MRXBC4ZNRR]]: a sequence that crosses no rational interval infinitely often has a limit in $[-\infty, \infty]$.

## Explanations

### L1 human

An upcrossing is a trip of the process from below $a$ to above $b$.
The inequality says that a process with an upward drift cannot make many such trips, on average, unless it ends up high.
In other words, a submartingale with controlled size cannot oscillate forever.

### L2 human

The inequality turns a question about convergence into a counting question.
A real sequence fails to converge in $[-\infty, \infty]$ exactly when it crosses some interval with rational endpoints infinitely often.
The upcrossing bound and monotone convergence show this happens with probability zero for $L^1$-bounded submartingales.
For a [[supermartingale|KYW1PV0SX5]] the analogous bound is $(b - a)\, E[U_n[a, b]] \le E[(X_n - a)^-]$, where $y^- = \max(-y, 0)$.
