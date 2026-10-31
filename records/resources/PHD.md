---
records:
    - id: PHD1KSDSBY
      kind: problem-set
      title: Kvant 1986, no. 1
      date: "1986"
      expressions:
        - key: e1
          kind: edition
          date: "1986"
          structure: PHD1KSDSBY/e1.json
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
          native_id: 1986-1
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: PHDHTCTYSG
      kind: monograph
      title: Proceedings of the Second Japan-USSR Symposium on Probability Theory
      creators:
        - name: G. Maruyama
          role: editor
        - name: Yu. V. Prokhorov
          role: editor
      date: "1973"
      expressions:
        - key: e1
          kind: edition
          date: "1973"
          ids:
            doi: 10.1007/bfb0061476
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1973"
              ids:
                isbn:
                    - "9783540063582"
                    - "9783540469568"
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0061476
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
