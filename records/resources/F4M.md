---
records:
    - id: F4M16ZGJ1M
      kind: edited-volume
      title: African Americans in Mathematics II
      creators:
        - name: Nathaniel Dean
          role: editor
        - name: Cassandra M. McZeal
          role: editor
        - name: Pamela J. Williams
          role: editor
      date: "1999"
      expressions:
        - key: e1
          kind: edition
          date: "1999"
          ids:
            doi: 10.1090/conm/252
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "1999"
              ids:
                isbn:
                    - "9780821811955"
                    - "9780821855881"
                    - "9780821878422"
      relations:
        - kind: part_of
          to: VAEN3CBGT1
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/conm/252
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: F4M67ZVBF2
      kind: preprint
      title: An Enhanced Higher Green's Function on the Modular Curve
      creators:
        - name: Nina Sakharova
          role: author
      date: "2026-10-12"
      subjects:
        - system: arxiv
          code: math.NT
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-12"
          ids:
            arxiv: "2610.17258"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.17258"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
    - id: F4MMYF8DPB
      kind: problem-set
      title: Kvant 1982, no. 3
      date: "1982"
      expressions:
        - key: e1
          kind: edition
          date: "1982"
          structure: F4MMYF8DPB/e1.json
      relations:
        - kind: part_of
          to: W84MAFPC23
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: kvant
          snapshot: blake3:9ef7ec326c8e38c2cc1957ddca07480f15b4e9ef49d8059191fc4a1c78c7cd39
          native_id: 1982-3
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
