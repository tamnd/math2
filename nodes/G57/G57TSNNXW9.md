---
tag: G57TSNNXW9
kind: definition
name: Doodson numbers
msc: [86A05]
defines: YZ4RBHA6E7
uses: [Y07010W5HJ]
sources:
  - url: https://en.wikipedia.org/wiki/Theory_of_tides
---

## Definition

Let $\tau$ be mean lunar time, $s$ the mean longitude of the Moon, and $h$ the mean longitude of the Sun.
Let $p$ be the longitude of the lunar perigee, and $p_s$ the longitude of the solar perigee.
Let $N' = -N$, where $N$ is the longitude of the Moon's ascending node.
Let a [[tidal constituent|Y07010W5HJ]] have argument
$$k_1 \tau + k_2 s + k_3 h + k_4 p + k_5 N' + k_6 p_s, \qquad k_1, \dots, k_6 \in \Z,$$
where $0 \le k_1 \le 3$ and $-5 \le k_i \le 4$ for $i = 2, \dots, 6$.
The *Doodson number* of the constituent is the six-digit code
$$k_1\, (k_2 + 5)\, (k_3 + 5) \,.\, (k_4 + 5)\, (k_5 + 5)\, (k_6 + 5).$$

## Remarks

Example: the principal lunar semidiurnal tide $M_2$ has argument $2\tau$, so $(k_1, \dots, k_6) = (2, 0, 0, 0, 0, 0)$ and its Doodson number is $255.555$.
Since solar time is $\tau + s - h$, the solar semidiurnal tide $S_2$ has argument $2\tau + 2s - 2h$ and number $273.555$.
The diurnal tides $K_1$ and $O_1$ have arguments $\tau + s$ and $\tau - s$, and numbers $165.555$ and $145.555$.
The first digit $k_1$ is the species: $0$ long period, $1$ diurnal, $2$ semidiurnal, $3$ terdiurnal.
Non-example: the list $(2, 0, 0, 0, 0, 0)$ written without the shift, as $200.000$, is not the Doodson number of $M_2$.
The shift by $5$ in the last five places is part of the code.
The fortnightly constituent $MS_f$, with argument $2s - 2h$, has number $073.555$.
