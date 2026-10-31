---
records:
    - id: QHEC1YQ0RR
      kind: problem-set
      title: Kvant 1982, no. 11
      date: "1982"
      expressions:
        - key: e1
          kind: edition
          date: "1982"
          structure: QHEC1YQ0RR/e1.json
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
          native_id: 1982-11
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: QHEZHC9Q37
      kind: edited-volume
      title: "Automorphic Forms, Representations and \U0001D43F-Functions"
      creators:
        - name: A. Borel
          role: editor
        - name: W. Casselman
          role: editor
      date: "1979"
      expressions:
        - key: e1
          kind: edition
          date: "1979"
          ids:
            doi:
                - 10.1090/pspum/033.1
                - 10.1090/pspum/033.2
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "1979"
              ids:
                isbn:
                    - "9780821814352"
                    - "9780821833476"
            - key: m2
              kind: print
              publisher: American Mathematical Society
              date: "1979"
              ids:
                isbn:
                    - "9780821814376"
                    - "9780821833711"
      relations:
        - kind: part_of
          to: EVG9FMRY3R
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/pspum/033.1
          level: work
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/pspum/033.2
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
