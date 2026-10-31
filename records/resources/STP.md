---
records:
    - id: STP52H4T26
      kind: monograph
      title: 'Cryptography: An Introduction'
      creators:
        - name: V. Yaschenko
          role: editor
      date: "2002-11-21"
      expressions:
        - key: e1
          kind: edition
          date: "2002-11-21"
          ids:
            doi: 10.1090/stml/018
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2002-11-21"
              ids:
                isbn:
                    - "9781470421328"
                    - "9780821848500"
                    - "9780821829868"
      relations:
        - kind: part_of
          to: 6RX4VMGQKK
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/stml/018
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: STPNP83RJS
      kind: preprint
      title: On the Cardinality of the Smith Set Under Impartial Culture with Many Alternatives
      creators:
        - name: Zachary Berchenko
          role: author
        - name: Kaizhao Liu
          role: author
      date: "2026-10-01"
      subjects:
        - system: arxiv
          code: econ.TH
        - system: arxiv
          code: math.CO
        - system: arxiv
          code: math.PR
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-01"
          ids:
            arxiv: "2610.03814"
      scope:
        value: out
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.03814"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to out
---
